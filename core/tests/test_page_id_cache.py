import pytest

from wagtail.core.models import Site

from core.cache import PageIDCache
from export_readiness.tests.factories import (
    HomePageFactory, TopicLandingPageFactory,
    ArticleListingPageFactory, ArticlePageFactory,
)


@pytest.mark.django_db
def test_population_and_value_getting(root_page, django_assert_num_queries):
    domestic_homepage = HomePageFactory(parent=root_page)
    topic_page = TopicLandingPageFactory(
        parent=domestic_homepage, slug='topic')
    article_list_page = ArticleListingPageFactory(
        parent=topic_page, slug='list')
    article_page = ArticlePageFactory(
        parent=article_list_page, slug='article')

    Site.objects.all().delete()
    site = Site.objects.create(
        site_name='Great Domestic',
        hostname='domestic.trade.great',
        root_page=domestic_homepage,
    )

    # Trigger population of site root paths cache
    Site.get_site_root_paths()

    # Prefetch content type for this page
    root_page.specific_class

    # With the two potential queries above out of the way,
    # population should only use as single datatbase query
    with django_assert_num_queries(1):
        result = PageIDCache.populate()

    # Check result looks as expected
    assert result == {
        'by-path': {
            f'{site.id}:/': domestic_homepage.id,
            f'{site.id}:/topic/': topic_page.id,
            f'{site.id}:/topic/list/': article_list_page.id,
            f'{site.id}:/topic/list/article/': article_page.id
        },
        'by-slug': {
            'EXPORT_READINESS:export-readiness-app': domestic_homepage.id,
            'EXPORT_READINESS:topic': topic_page.id,
            'EXPORT_READINESS:list': article_list_page.id,
            'EXPORT_READINESS:article': article_page.id,
        },
    }

    # Check get_for_path()
    result_1 = PageIDCache.get_for_path('/', site.id)
    assert result_1 == domestic_homepage.id
    result_2 = PageIDCache.get_for_path('/topic/list/article/', site.id)
    assert result_2 == article_page.id

    # Check invalid get_for_path()
    assert PageIDCache.get_for_path('123', 99) is None

    # Check get_for_slug()
    result_1 = PageIDCache.get_for_slug('topic', 'EXPORT_READINESS')
    assert result_1 == topic_page.id
    result_2 = PageIDCache.get_for_slug('article', 'EXPORT_READINESS')
    assert result_2 == article_page.id

    # Check invalid get_for_slug()
    assert PageIDCache.get_for_slug('abc', 'IMPORT_NOT_READINESS') is None


@pytest.mark.django_db
def test_get_populate_and_delete():

    # the cache should be empty
    assert PageIDCache.get() is None

    # when the page is populated
    result = PageIDCache.populate()

    # then get returns something useful
    assert PageIDCache.get() == result

    # when the cache is cleared
    PageIDCache.clear()

    # then the cache is empty again
    assert PageIDCache.get() is None

    # but we can use populate_if_cold to trigger population
    new_result = PageIDCache.get(populate_if_cold=True)

    # and the result should look very much like what we had before
    assert new_result == result

    # let's clear it again
    PageIDCache.clear()
