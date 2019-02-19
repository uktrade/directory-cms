from directory_constants.constants import cms
from rest_framework.reverse import reverse

from great_international.tests import factories


def test_international_homepage(admin_client, root_page):
    home_page = factories.InternationalHomePageFactory.create(
        parent=root_page
    )
    # news
    marketing_folder = factories.InternationalMarketingPagesFactory(
        slug=cms.GREAT_INTERNATIONAL_MARKETING_PAGES_SLUG,
        live=True
    )
    for _ in range(5):
        factories.InternationalArticlePageFactory.create(
            parent=marketing_folder
        )
    factories.InternationalArticlePageFactory.create(
        parent=root_page
    )

    url = reverse('api:api:pages:detail', kwargs={'pk': home_page.pk})
    response = admin_client.get(url)
    assert response.status_code == 200
    assert 'articles' in response.json()
    assert len(response.json()['articles']) == 3


def test_international_homepage_no_news(admin_client, root_page):

    home_page = factories.InternationalHomePageFactory.create(
        parent=root_page
    )

    url = reverse('api:api:pages:detail', kwargs={'pk': home_page.pk})
    response = admin_client.get(url)
    assert response.status_code == 200
    assert 'articles' in response.json()
    assert len(response.json()['articles']) == 0


def test_international_campaign_page(admin_client, root_page):

    campaign_page = factories.InternationalCampaignPageFactory(
        parent=root_page
    )
    url = reverse('api:api:pages:detail', kwargs={'pk': campaign_page.pk})
    response = admin_client.get(url)
    assert response.status_code == 200


def test_international_article_listing_page_view(admin_client, root_page):
    article_listing_page = factories.InternationalArticleListingPageFactory.create(  # NOQA
        parent=root_page,
        live=True
    )
    factories.InternationalArticlePageFactory.create(
        parent=article_listing_page,
        live=True
    )
    factories.InternationalArticlePageFactory.create(
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


def test_international_topic_landing_page_view(admin_client, root_page):
    topic_landing_page = factories.InternationalTopicLandingPageFactory.create(
        parent=root_page,
        live=True
    )
    article_listing_page = factories.InternationalArticleListingPageFactory.create(  # NOQA
        parent=topic_landing_page,
        live=True
    )
    factories.InternationalArticlePageFactory.create(
        parent=article_listing_page,
        live=True
    )
    factories.InternationalArticlePageFactory.create(
        parent=article_listing_page,
        live=True
    )

    url = reverse('api:api:pages:detail', kwargs={'pk': topic_landing_page.pk})
    response = admin_client.get(url)
    assert response.status_code == 200
    assert 'child_pages' in response.json()
