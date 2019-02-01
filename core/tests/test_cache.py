from unittest import mock

import pytest
from wagtail.core.models import Page, get_page_models

from core import cache, models

import components.models
import find_a_supplier.models
import invest.models
import export_readiness


@pytest.mark.parametrize('slug,service_name,language_code,expected', (
    (
        'some-slug',
        'FIND_A_SUPPLIER',
        None,
        '/some-slug/?service_name=FIND_A_SUPPLIER'
    ),
    (
        'some-other-slug',
        'FIND_A_SUPPLIER',
        'en-gb',
        '/some-other-slug/?service_name=FIND_A_SUPPLIER&lang=en-gb'
    ),
    (
        'and-another-slug',
        'EXPORT_READINESS',
        'fr',
        '/and-another-slug/?service_name=EXPORT_READINESS&lang=fr'
    ),
))
def test_page_cache_build_keys(slug, service_name, language_code, expected):
    key = cache.PageCache.build_key(
        slug=slug, service_name=service_name, language_code=language_code
    )
    assert key == f'{{slug}}/api/pages/lookup-by-slug' + expected


def test_page_cache_get_set_delete():
    slug = 'some-slug'
    service_name = 'FIND_A_SUPPLIER'
    language_code = 'en-gb'

    # given the cache contains no content
    assert cache.PageCache.get(
        slug=slug,
        service_name=service_name,
        language_code=language_code
    ) is None

    contents = expected = {'field': 'value'}
    # when the page is populated
    cache.PageCache.set(
        slug=slug,
        service_name=service_name,
        contents=contents,
        language_code=language_code
    )

    # then the content is present
    assert cache.PageCache.get(
        slug=slug,
        service_name=service_name,
        language_code=language_code
    ) == expected

    # when the existing content is deleted
    cache.PageCache.delete(
        slug=slug,
        service_name=service_name,
        language_codes=[language_code]
    )

    # then the content is removed from the cache
    assert cache.PageCache.get(
        slug=slug,
        service_name=service_name,
        language_code=language_code
    ) is None


@pytest.mark.django_db
def test_cache_populator(translated_page):
    # translated_page is a IndustryPage, which is registered for caching in
    # find_a_supplier.cache
    cache.CachePopulator.populate(translated_page.pk)
    for language_code in translated_page.translated_languages:
        assert cache.PageCache.get(
            slug=translated_page.slug,
            service_name=translated_page.service_name,
            language_code=language_code
        )


@mock.patch('wagtail.core.signals.page_published.connect')
@mock.patch('core.cache.post_save.connect')
@mock.patch('core.cache.page_unpublished.connect')
def test_subscriber_subscribe_to_publish(
    mock_page_unpublished, mock_post_save, mock_page_published
):

    class TestSubscriber(cache.AbstractDatabaseCacheSubscriber):
        model = Page
        subscriptions = [
            models.Breadcrumb
        ]

    TestSubscriber.subscribe()

    assert mock_page_published.call_count == 1
    assert mock_page_published.call_args == mock.call(
        dispatch_uid='Page',
        receiver=TestSubscriber.populate,
        sender=Page,
    )
    assert mock_post_save.call_count == 1
    assert mock_page_unpublished.call_count == 2
    assert mock_post_save.call_args == mock.call(
        dispatch_uid='Page-Breadcrumb',
        receiver=TestSubscriber.populate_many,
        sender=models.Breadcrumb,
    )
    assert mock_page_unpublished.call_args_list == [
        mock.call(
            dispatch_uid='Page',
            receiver=TestSubscriber.delete,
            sender=Page
        ),
        mock.call(
            dispatch_uid='Page-Breadcrumb',
            receiver=TestSubscriber.populate_many,
            sender=models.Breadcrumb,
        )
    ]


@pytest.mark.django_db
@mock.patch('core.cache.CachePopulator.populate.delay')
def test_subscriber_populate(mock_populate, translated_page):
    class TestSubscriber(cache.AbstractDatabaseCacheSubscriber):
        model = Page
        subscriptions = [
            models.Breadcrumb
        ]

    TestSubscriber.populate(sender=None, instance=translated_page)

    assert mock_populate.call_count == 1
    assert mock_populate.call_args == mock.call(translated_page.pk)


@mock.patch('core.cache.PageCache.delete')
def test_subscriber_delete(mock_delete):
    class TestSubscriber(cache.AbstractDatabaseCacheSubscriber):
        model = Page
        subscriptions = [
            models.Breadcrumb
        ]

    instance = mock.Mock(
        slug='some-slug', service_name='thing', translated_languages=['en-gb']
    )
    TestSubscriber.delete(sender=None, instance=instance)

    assert mock_delete.call_count == 1
    assert mock_delete.call_args == mock.call(
        slug='some-slug',
        service_name='thing',
        language_codes=['en-gb'],
    )


@pytest.mark.django_db
@mock.patch('core.cache.CachePopulator.populate.delay')
def test_subscriber_populate_many(mock_populate, translated_page):
    class TestSubscriber(cache.AbstractDatabaseCacheSubscriber):
        model = translated_page.__class__
        subscriptions = [
            models.Breadcrumb
        ]

    TestSubscriber.populate_many(sender=None, instance=translated_page)

    assert mock_populate.call_count == 1
    assert mock_populate.call_args == mock.call(translated_page.pk)


def test_all_models_cached():
    exclude = {
        # apps
        export_readiness.models.ExportReadinessApp,
        components.models.ComponentsApp,
        find_a_supplier.models.FindASupplierApp,
        invest.models.InvestApp,
        # "folders"
        export_readiness.models.MarketingPages,
        export_readiness.models.SitePolicyPages,
        export_readiness.models.ContactUsGuidancePages,
        export_readiness.models.ContactSuccessPages,
        export_readiness.models.EUExitFormPages,
        export_readiness.models.AllContactPagesPage,
        # Page is added by TestSubscriber in other tests.
        Page,
    }
    all_models = {
        model for model in get_page_models()
        if model not in exclude
    }
    cached_models = {
        item.model
        for item in cache.AbstractDatabaseCacheSubscriber.__subclasses__()
        if item.model not in exclude
    }

    assert all_models == cached_models


@mock.patch('django.core.cache.cache.set')
@mock.patch('django.core.cache.cache.set_many')
def test_transactional_cache(mock_set_many, mock_set, settings):
    with cache.PageCache.transaction() as page_cache:
        page_cache.set(
            slug='s1',
            language_code='en-gb',
            service_name='INVEST',
            contents={'key': 'value-one'}
        )
        page_cache.set(
            slug='s2',
            language_code='fr',
            service_name='INVEST',
            contents={'key': 'value-two'}
        )
        page_cache.set(
            slug='s3',
            language_code='de',
            service_name='INVEST',
            contents={'key': 'value-three'}
        )

    assert mock_set.call_count == 0
    assert mock_set_many.call_count == 1
    assert mock_set_many.call_args == mock.call({
        '{slug}/api/pages/lookup-by-slug/s1/?service_name=INVEST&lang=en-gb': {
            'key': 'value-one'
        },
        '{slug}/api/pages/lookup-by-slug/s2/?service_name=INVEST&lang=fr': {
            'key': 'value-two'
        },
        '{slug}/api/pages/lookup-by-slug/s3/?service_name=INVEST&lang=de': {
            'key': 'value-three'}
        }, timeout=settings.API_CACHE_EXPIRE_SECONDS
    )
