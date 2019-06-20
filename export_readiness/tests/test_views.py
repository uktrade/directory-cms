import pytest
from rest_framework.reverse import reverse
from directory_constants import slugs

from conf import settings
from export_readiness.tests import factories
from directory_constants import urls


def test_performance_dashboard(admin_client, root_page):
    page = factories.PerformanceDashboardPageFactory(
        live=True,
        parent=root_page,
        product_link=urls.SERVICES_GREAT_DOMESTIC
    )

    url = reverse('api:api:pages:detail', kwargs={'pk': page.pk})

    response = admin_client.get(url)
    assert response.status_code == 200
    assert response.json()['page_type'] == 'PerformanceDashboardPage'


def test_performance_dashboard_notes(admin_client, root_page):
    page = factories.PerformanceDashboardNotesPageFactory(
        live=True,
        parent=root_page
    )

    url = reverse('api:api:pages:detail', kwargs={'pk': page.pk})

    response = admin_client.get(url)
    assert response.status_code == 200


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

    url = reverse('api:api:pages:detail', kwargs={'pk': topic_landing_page.pk})
    response = admin_client.get(url)
    assert response.status_code == 200
    assert 'child_pages' in response.json()


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

    url = reverse(
        'api:api:pages:detail', kwargs={'pk': article_listing_page.pk}
    )
    response = admin_client.get(url)
    assert response.status_code == 200
    assert 'articles' in response.json()
    assert 'meta' in response.json()['articles'][0]


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

    url = reverse('api:api:pages:detail', kwargs={'pk': article.pk})
    response = admin_client.get(url)
    assert response.status_code == 200
    assert 'tags' in response.json()
    assert 'name' in response.json()['tags'][0]
    assert 'slug' in response.json()['tags'][0]


def test_homepage(admin_client, root_page):

    home_page = factories.HomePageFactory.create(
        parent=root_page
    )

    # news
    article_listing_page = factories.ArticleListingPageFactory(
        slug=settings.EU_EXIT_NEWS_LISTING_PAGE_SLUG
    )
    for _ in range(5):
        factories.ArticlePageFactory.create(
            parent=article_listing_page
        )
    factories.ArticlePageFactory.create(
        parent=root_page
    )

    # guidance
    topic_landing_page = factories.TopicLandingPageFactory(
        slug=slugs.GREAT_ADVICE
    )
    for _ in range(5):
        factories.ArticleListingPageFactory.create(
            parent=topic_landing_page
        )

    url = reverse('api:api:pages:detail', kwargs={'pk': home_page.pk})
    response = admin_client.get(url)
    assert response.status_code == 200
    assert 'articles' in response.json()
    assert 'advice' in response.json()
    assert len(response.json()['advice']) == 5
    assert len(response.json()['articles']) == 5


def test_homepage_no_news(admin_client, root_page):

    home_page = factories.HomePageFactory.create(
        parent=root_page
    )

    url = reverse('api:api:pages:detail', kwargs={'pk': home_page.pk})
    response = admin_client.get(url)
    assert response.status_code == 200
    assert 'articles' in response.json()
    assert len(response.json()['articles']) == 0


def test_homepage_no_advice(admin_client, root_page):

    home_page = factories.HomePageFactory.create(
        parent=root_page
    )

    url = reverse('api:api:pages:detail', kwargs={'pk': home_page.pk})
    response = admin_client.get(url)
    assert response.status_code == 200
    assert 'advice' in response.json()
    assert len(response.json()['advice']) == 0


def test_international_landing_age(admin_client, root_page):

    page = factories.InternationaLandingPageFactory.create(
        parent=root_page
    )
    url = reverse('api:api:pages:detail', kwargs={'pk': page.pk})
    response = admin_client.get(url)
    assert response.status_code == 200
    assert 'articles_count' in response.json()


@pytest.mark.django_db
def test_lookup_by_tag_slug(admin_client, root_page):
    tag = factories.TagFactory(name='foo')
    article1 = factories.ArticlePageFactory(parent=root_page,)
    article1.tags = [tag]
    article1.save()
    article2 = factories.ArticlePageFactory(parent=root_page)
    article2.tags = [tag]
    article2.save()
    factories.ArticlePageFactory(parent=root_page)
    url = reverse('api:lookup-by-tag-list', kwargs={'slug': tag.slug})
    response = admin_client.get(url)

    assert response.status_code == 200
    assert response.json()['name'] == tag.name
    assert response.json()['slug'] == tag.slug
    assert len(response.json()['articles']) == 2


@pytest.mark.django_db
def test_country_page_view(admin_client, root_page):
    page = factories.CountryGuidePageFactory(
        parent=root_page,
        live=True
    )
    url = reverse('api:api:pages:detail', kwargs={'pk': page.pk})
    response = admin_client.get(url)
    assert response.status_code == 200
    assert 'accordions' in response.json()
    assert 'statistics' in response.json()
    assert 'fact_sheet' in response.json()
    assert 'intro_ctas' in response.json()
    assert 'subsections' in response.json()['accordions'][0]
    assert 'statistics' in response.json()['accordions'][0]
    assert 'case_study' in response.json()['accordions'][0]


@pytest.mark.django_db
def test_topic_landing_page_view_country_guides_alph_order(
        admin_client,
        root_page):
    topic_landing_page = factories.TopicLandingPageFactory.create(
        parent=root_page,
        live=True
    )
    country_guide_page1 = factories.CountryGuidePageFactory.create(
        parent=topic_landing_page,
        live=True,
        heading='acme'
    )
    country_guide_page2 = factories.CountryGuidePageFactory.create(
        parent=topic_landing_page,
        live=True,
        heading='foo'
    )

    url = reverse('api:api:pages:detail', kwargs={'pk': topic_landing_page.pk})
    response = admin_client.get(url)
    assert response.status_code == 200
    assert [page['id'] for page in response.json()['child_pages']] == [
        country_guide_page1.pk, country_guide_page2.pk
    ]
