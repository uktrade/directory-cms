from unittest.mock import call

import factory
import pytest
from unittest import mock

from wagtail.models import Page
from wagtail.signals import page_published

from core import cache

from tests.great_international.factories import InternationalArticlePageFactory

pytestmark = pytest.mark.django_db


@pytest.mark.parametrize('page_id,language_code,region,expected', (
    (
        1,
        None,
        None,
        'serialized-page-1:'
    ),
    (
        2,
        'en-gb',
        None,
        'serialized-page-2:lang=en-gb'
    ),
    (
        3,
        'en-gb',
        'eu',
        'serialized-page-3:lang=en-gb&region=eu'
    ),
))
def test_page_cache_build_keys(page_id, language_code, region, expected):
    key = cache.PageCache.build_key(
        page_id=page_id,
        lang=language_code,
        region=region,
    )
    assert key == expected


@pytest.mark.parametrize('test_kwargs', (
    # reversed
    {
        'another_thing': 'ABC',
        'something_else': '123',
        'lang': 'en-gb',
        'region': 'eu',

    },
    # randomised
    {
        'something_else': '123',
        'another_thing': 'ABC',
        'region': 'eu',
        'lang': 'en-gb',
    },
))
def test_page_cache_build_key_ignored_variation_kwarg_order(test_kwargs):
    original_kwargs = {
        'lang': 'en-gb',
        'region': 'eu',
        'something_else': '123',
        'another_thing': 'ABC',
    }
    original_key = cache.PageCache.build_key(1, **original_kwargs)

    test_key = cache.PageCache.build_key(1, **test_kwargs)

    assert original_key == test_key


def test_page_cache_get_set_delete():
    page_id = 1
    language_code = 'en-gb'

    # given the cache contains no content
    assert cache.PageCache.get(
        page_id=page_id,
        lang=language_code,
    ) is None

    data = expected = {'field': 'value'}
    # when the page is populated
    cache.PageCache.set(
        page_id=page_id,
        lang=language_code,
        data=data,
    )

    # then the content is present
    assert cache.PageCache.get(
        page_id=page_id,
        lang=language_code,
    ) == expected

    # when the existing content is deleted
    cache.PageCache.delete(
        page_id=page_id,
        lang=language_code,
    )

    # then the content is removed from the cache
    assert cache.PageCache.get(
        page_id=page_id,
        lang=language_code,
    ) is None


@pytest.mark.django_db
def test_cache_populator(translated_page):
    cache.CachePopulator.populate(translated_page.pk)
    for language_code in translated_page.translated_languages:
        assert cache.PageCache.get(
            page_id=translated_page.id,
            lang=language_code,
        )


@mock.patch('wagtail.signals.page_published.connect')
@mock.patch('core.cache.page_unpublished.connect')
def test_subscriber_subscribe_to_publish(mock_page_unpublished, mock_page_published):

    class TestSubscriber(cache.DatabaseCacheSubscriber):
        model_classes = [Page]

    TestSubscriber.subscribe()

    assert mock_page_published.call_count == 1
    assert mock_page_published.call_args == mock.call(
        dispatch_uid='Page',
        receiver=TestSubscriber.populate,
        sender=Page,
    )
    assert mock_page_unpublished.call_count == 1
    assert mock_page_unpublished.call_args == mock.call(
        dispatch_uid='Page',
        receiver=TestSubscriber.delete,
        sender=Page
    )


@pytest.mark.django_db
@mock.patch('core.cache.CachePopulator.populate.delay')
def test_subscriber_populate(mock_populate, translated_page):
    class TestSubscriber(cache.DatabaseCacheSubscriber):
        model_classes = [Page]

    TestSubscriber.populate(sender=None, instance=translated_page)

    assert mock_populate.call_count == 1
    assert mock_populate.call_args == mock.call(translated_page.pk)


@mock.patch('core.cache.PageCache.delete')
def test_subscriber_delete(mock_delete):
    class TestSubscriber(cache.DatabaseCacheSubscriber):
        model_classes = [Page]

    instance = mock.Mock(
        id=2, slug='some-slug', service_name='thing',
        translated_languages=['en-gb']
    )
    TestSubscriber.delete(sender=None, instance=instance)

    assert mock_delete.call_count == 2
    assert mock_delete.call_args_list == [
        mock.call(
            page_id=2,
            lang='en-gb',
        ),
        mock.call(
            page_id=2,
            lang='en-gb',
            draft_version=True,
        )
    ]


@mock.patch('django.core.cache.cache.set')
@mock.patch('django.core.cache.cache.set_many')
def test_transactional_cache_set(mock_set_many, mock_set, settings):
    with cache.PageCache.transaction() as page_cache:
        page_cache.set(
            page_id=1,
            data={'key': 'value-one'},
        )
        page_cache.set(
            page_id=2,
            data={'key': 'value-two'},
        )
        page_cache.set(
            page_id=3,
            data={'key': 'value-three'},
        )

    assert mock_set.call_count == 0
    assert mock_set_many.call_count == 1
    assert mock_set_many.call_args == mock.call(
        {
            'serialized-page-1:': {
                'key': 'value-one',
                'etag': '"67216138eb3d94858a5014cfcd83688f"',
            },
            'serialized-page-2:': {
                'key': 'value-two',
                'etag': '"4bb0f72aae58a2f70bc87ee99161a585"',
            },
            'serialized-page-3:': {
                'key': 'value-three',
                'etag': '"92b996db2b999fb74640d7d88aa5124c"',
            },
        },
        timeout=settings.API_CACHE_EXPIRE_SECONDS
    )


@mock.patch('django.core.cache.cache.delete')
@mock.patch('django.core.cache.cache.delete_many')
def test_transactional_cache_delete(mock_delete_many, mock_delete):
    with cache.PageCache.transaction() as page_cache:
        page_cache.delete(page_id=1)
        page_cache.delete(page_id=2)
        page_cache.delete(page_id=3)

    assert mock_delete.call_count == 0
    assert mock_delete_many.call_count == 1
    assert mock_delete_many.call_args == mock.call([
        'serialized-page-1:',
        'serialized-page-2:',
        'serialized-page-3:',
    ])


@pytest.mark.django_db
@factory.django.mute_signals(page_published)
@mock.patch('core.cache.CachePopulator')
def test_rebuild_all_cache_task(mock_cache_populator):
    article1 = InternationalArticlePageFactory(live=True)
    article2 = InternationalArticlePageFactory(live=True)
    InternationalArticlePageFactory(live=False)
    cache.rebuild_all_cache()
    assert mock_cache_populator.populate_async.call_count == 5  # contains home page
    assert mock_cache_populator.populate_async.call_args_list[-2] == call(article1)
    assert mock_cache_populator.populate_async.call_args_list[-1] == call(article2)
