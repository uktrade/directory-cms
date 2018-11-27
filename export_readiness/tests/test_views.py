from rest_framework.reverse import reverse

from conf import settings
from . import factories


def test_performance_dashboard(admin_client, root_page):
    page = factories.PerformanceDashboardPageFactory(
        live=True,
        parent=root_page
    )

    url = reverse('api:api:pages:detail', kwargs={'pk': page.pk})

    response = admin_client.get(url)
    assert response.status_code == 200


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
    assert 'article_listing' in response.json()


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
    topic_landing_page = factories.TopicLandingPageFactory(slug='guidance')
    for _ in range(5):
        factories.ArticleListingPageFactory.create(
            parent=topic_landing_page
        )

    url = reverse('api:api:pages:detail', kwargs={'pk': home_page.pk})
    response = admin_client.get(url)
    assert response.status_code == 200
    assert 'articles' in response.json()
    assert 'guidance' in response.json()
    assert len(response.json()['guidance']) == 5
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


def test_homepage_no_guidance(admin_client, root_page):

    home_page = factories.HomePageFactory.create(
        parent=root_page
    )

    url = reverse('api:api:pages:detail', kwargs={'pk': home_page.pk})
    response = admin_client.get(url)
    assert response.status_code == 200
    assert 'guidance' in response.json()
    assert len(response.json()['guidance']) == 0


def test_international_landing_age(admin_client, root_page):

    page = factories.InternationaLandingPageFactory.create(
        parent=root_page
    )
    url = reverse('api:api:pages:detail', kwargs={'pk': page.pk})
    response = admin_client.get(url)
    assert response.status_code == 200
    assert 'articles_count' in response.json()
