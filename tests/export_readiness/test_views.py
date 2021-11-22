import pytest
from rest_framework.reverse import reverse

from tests.export_readiness import factories
from core import cache


@pytest.mark.django_db
def test_performance_dashboard_notes(admin_client, root_page):
    page = factories.PerformanceDashboardNotesPageFactory(
        live=True,
        parent=root_page
    )
    cache.rebuild_all_cache()

    url = reverse('api:api:pages:detail', kwargs={'pk': page.pk})

    response = admin_client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_topic_landing_page_view(admin_client, root_page):
    topic_landing_page = factories.TopicLandingPageFactory.create(
        parent=root_page,
        live=True
    )
    article_listing_page = factories.ArticleListingPageFactory.create(
        parent=topic_landing_page,
        live=True
    )
    factories.ArticlePageFactory.create(
        parent=article_listing_page,
        live=True
    )
    factories.ArticlePageFactory.create(
        parent=article_listing_page,
        live=True
    )
    cache.rebuild_all_cache()

    url = reverse('api:api:pages:detail', kwargs={'pk': topic_landing_page.pk})
    response = admin_client.get(url)
    assert response.status_code == 200
    assert 'child_pages' in response.json()


@pytest.mark.django_db
def test_article_listing_page_view(admin_client, root_page):
    article_listing_page = factories.ArticleListingPageFactory.create(
        parent=root_page,
        live=True
    )
    factories.ArticlePageFactory.create(
        parent=article_listing_page,
        live=True
    )
    factories.ArticlePageFactory.create(
        parent=article_listing_page,
        live=True
    )
    cache.rebuild_all_cache()

    url = reverse(
        'api:api:pages:detail', kwargs={'pk': article_listing_page.pk}
    )
    response = admin_client.get(url)
    assert response.status_code == 200
    assert 'articles' in response.json()
    assert 'meta' in response.json()['articles'][0]


@pytest.mark.django_db
def test_article_page_view(admin_client, root_page):
    topic_landing_page = factories.TopicLandingPageFactory.create(
        parent=root_page,
        live=True
    )
    article_listing_page = factories.ArticleListingPageFactory.create(
        parent=topic_landing_page,
        live=True
    )
    tag = factories.TagFactory()
    tag2 = factories.TagFactory()
    article = factories.ArticlePageFactory.create(
        parent=article_listing_page,
        live=True,
    )
    article.tags = [tag, tag2]
    article.save()

    cache.rebuild_all_cache()

    url = reverse('api:api:pages:detail', kwargs={'pk': article.pk})
    response = admin_client.get(url)
    assert response.status_code == 200
    assert 'tags' in response.json()
    assert 'name' in response.json()['tags'][0]


@pytest.mark.django_db
def test_domestic_homepage(admin_client, root_page):
    home_page = factories.HomePageFactory.create(
        parent=root_page,
        hero_cta_url='/foo/bar'
    )
    cache.rebuild_all_cache()

    url = reverse('api:api:pages:detail', kwargs={'pk': home_page.pk})
    response = admin_client.get(url)
    assert response.json()['hero_cta_url'] == '/foo/bar'
    assert response.status_code == 200


@pytest.mark.django_db
def test_regions_list_view(client):

    url = reverse('api:regions-list-view')

    response = client.get(url)
    assert response.status_code == 200
