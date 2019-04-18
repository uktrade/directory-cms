import pytest

from wagtail.core.models import Site

from core import cache
from export_readiness.tests.factories import (
    ExportReadinessAppFactory, TopicLandingPageFactory,
    ArticleListingPageFactory, ArticlePageFactory,
)


@pytest.mark.django_db
def test_page_id_cache_population(root_page, django_assert_num_queries):
    domestic_root_page = ExportReadinessAppFactory(parent=root_page)
    topic_page = TopicLandingPageFactory(
        parent=domestic_root_page, slug='topic')
    article_list_page = ArticleListingPageFactory(
        parent=topic_page, slug='list')
    article_page = ArticlePageFactory(
        parent=article_list_page, slug='article')

    Site.objects.all().delete()
    site = Site.objects.create(
        site_name='Great Domestic',
        hostname='domestic.trade.great',
        root_page=domestic_root_page,
    )

    # Trigger population of site root paths cache
    Site.get_site_root_paths()

    # Prefetch content type for this page
    root_page.specific_class

    # With the two potential queries above out of the way,
    # population should only use as single datatbase query
    with django_assert_num_queries(1):
        result = cache.PageIDCache.populate()

    # Check result looks as expected
    assert result == {
        'by-path': {
            f'{site.id}:/': domestic_root_page.id,
            f'{site.id}:/topic/': topic_page.id,
            f'{site.id}:/topic/list/': article_list_page.id,
            f'{site.id}:/topic/list/article/': article_page.id
        },
        'by-slug': {
            'EXPORT_READINESS:export-readiness-app': domestic_root_page.id,
            'EXPORT_READINESS:topic': topic_page.id,
            'EXPORT_READINESS:list': article_list_page.id,
            'EXPORT_READINESS:article': article_page.id,
        },
    }

@pytest.mark.django_db
def test_page_id_cache_get_populate_delete():

    # the cache should be empty
    assert cache.PageIDCache.get() is None

    # when the page is populated
    result = cache.PageIDCache.populate()

    # then get returns something useful
    assert cache.PageIDCache.get() == result

    # when the cache is cleared
    cache.PageIDCache.clear()

    # then the cache is empty again
    assert cache.PageIDCache.get() is None

    # but we can use populate_if_cold to trigger population
    new_result = cache.PageIDCache.get(populate_if_cold=True)

    # and the result should look very much like what we had before
    assert new_result == result

    # let's clear it again
    cache.PageIDCache.clear()
