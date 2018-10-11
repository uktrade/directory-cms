from unittest import mock

import pytest
from wagtail.core.models import Page

from core import cache, models


@pytest.fixture(autouse=True)
def clear_djano_cache():
    cache.cache.clear()


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
    assert key == '/api/pages/lookup-by-slug' + expected


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
    cache.CachePopulator.populate(
        page_cache=cache.PageCache,
        instance=translated_page,
    )
    for language_code in translated_page.translated_languages:
        assert cache.PageCache.get(
            slug=translated_page.slug,
            service_name=translated_page.service_name,
            language_code=language_code
        )


@mock.patch('core.cache.post_save.connect')
@mock.patch('core.cache.page_unpublished.connect')
def test_subscriber_subscribe_to_publish(
    mock_page_unpublished, mock_post_save
):

    class TestSubscriber(cache.AbstractDatabaseCacheSubscriber):
        model = Page
        subscriptions = [
            models.Breadcrumb
        ]

    TestSubscriber.subscribe()

    assert mock_post_save.call_count == 2
    assert mock_page_unpublished.call_count == 2
    assert mock_post_save.call_args_list == [
        mock.call(
            dispatch_uid='Page',
            receiver=TestSubscriber.populate_if_live,
            sender=Page,
        ),
        mock.call(
            dispatch_uid='Page-Breadcrumb',
            receiver=TestSubscriber.populate_many_if_live,
            sender=models.Breadcrumb,
        )
    ]
    assert mock_page_unpublished.call_args_list == [
        mock.call(
            dispatch_uid='Page',
            receiver=TestSubscriber.delete,
            sender=Page
        ),
        mock.call(
            dispatch_uid='Page-Breadcrumb',
            receiver=TestSubscriber.delete_many,
            sender=models.Breadcrumb,
        )
    ]


@mock.patch(
    'core.cache.AbstractDatabaseCacheSubscriber.cache_populator.populate'
)
def test_subscriber_populate(mock_populate):
    class TestSubscriber(cache.AbstractDatabaseCacheSubscriber):
        model = Page
        subscriptions = [
            models.Breadcrumb
        ]

    instance = mock.Mock()
    TestSubscriber.populate_if_live(sender=None, instance=instance)

    assert mock_populate.call_count == 1
    assert mock_populate.call_args == mock.call(
        page_cache=TestSubscriber.page_cache,
        instance=instance
    )


@mock.patch(
    'core.cache.AbstractDatabaseCacheSubscriber.page_cache.delete'
)
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
@mock.patch(
    'core.cache.AbstractDatabaseCacheSubscriber.cache_populator.populate'
)
def test_subscriber_populate_many(mock_populate, translated_page):
    class TestSubscriber(cache.AbstractDatabaseCacheSubscriber):
        model = translated_page.__class__
        subscriptions = [
            models.Breadcrumb
        ]

    TestSubscriber.populate_many_if_live(sender=None, instance=translated_page)

    assert mock_populate.call_count == 1
    assert mock_populate.call_args == mock.call(
        page_cache=TestSubscriber.page_cache,
        instance=translated_page
    )


@pytest.mark.django_db
@mock.patch(
    'core.cache.AbstractDatabaseCacheSubscriber.page_cache.delete'
)
def test_subscriber_delete_many(mock_delete, translated_page):
    class TestSubscriber(cache.AbstractDatabaseCacheSubscriber):
        model = translated_page.__class__
        subscriptions = [
            models.Breadcrumb
        ]

    TestSubscriber.delete_many(sender=None, instance=translated_page)

    assert mock_delete.call_count == 1
    assert mock_delete.call_args == mock.call(
        slug=translated_page.slug,
        service_name=translated_page.service_name,
        language_codes=translated_page.translated_languages,
    )
