from rest_framework.reverse import reverse

from great_international.tests import factories


def test_international_sector_page(admin_client, root_page):
    sector_page = factories.InternationalSectorPageFactory.create(
        parent=root_page
    )
    url = reverse('api:api:pages:detail', kwargs={'pk': sector_page.pk})
    response = admin_client.get(url)
    assert response.status_code == 200


def test_international_homepage(admin_client, root_page):
    home_page = factories.InternationalHomePageFactory.create(
        parent=root_page
    )
    url = reverse('api:api:pages:detail', kwargs={'pk': home_page.pk})
    response = admin_client.get(url)
    assert response.status_code == 200


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
    article = factories.InternationalArticlePageFactory.create(
        parent=article_listing_page,
        live=True
    )
    campaign = factories.InternationalCampaignPageFactory.create(
        parent=article_listing_page,
        live=True
    )

    url = reverse(
        'api:api:pages:detail', kwargs={'pk': article_listing_page.pk}
    )
    response = admin_client.get(url)
    assert response.status_code == 200
    assert 'child_pages' in response.json()
    assert sorted(
        [page['id'] for page in response.json()['child_pages']],
        reverse=True
    ) == [campaign.pk, article.pk]
    assert 'meta' in response.json()['child_pages'][0]


def test_international_topic_landing_page_view(admin_client, root_page):
    topic_landing_page = factories.InternationalTopicLandingPageFactory.create(
        parent=root_page,
        live=True
    )
    campaign_page = factories.InternationalCampaignPageFactory(
        parent=topic_landing_page,
        live=True
    )
    article_listing_page = factories.InternationalArticleListingPageFactory.create(  # NOQA
        parent=topic_landing_page,
        live=True
    )

    url = reverse('api:api:pages:detail', kwargs={'pk': topic_landing_page.pk})
    response = admin_client.get(url)
    assert response.status_code == 200
    assert 'child_pages' in response.json()
    assert sorted(
        [page['id'] for page in response.json()['child_pages']],
        reverse=True
    ) == [article_listing_page.pk, campaign_page.pk]


def test_article_listingpage_with_localised_content(admin_client, root_page):
    article_listing_page = factories.InternationalArticleListingPageFactory.create(  # NOQA
        parent=root_page,
        live=True,
        slug='setup-uk'
    )
    factories.InternationalArticlePageFactory.create(
        parent=article_listing_page,
        live=True
    )
    region_page = factories.InternationalRegionPageFactory(
        parent=root_page,
        live=True,
        slug='germany'
    )
    regional_folder_page = factories.InternationalLocalisedFolderPageFactory(
        parent=region_page,
        live=True,
        slug='setup-uk'
    )
    localised_article = factories.InternationalArticlePageFactory.create(
        parent=regional_folder_page,
        live=True
    )

    url = reverse(
        'api:api:pages:detail',
        kwargs={'pk': article_listing_page.pk}
    )
    response = admin_client.get(url, {'region': 'germany'})
    assert response.status_code == 200
    assert 'localised_child_pages' in response.json()
    expected_localised_article = response.json(
        )['localised_child_pages'][0]['id']
    assert expected_localised_article == localised_article.pk


def test_article_listingpage_without_localised_content(
        admin_client, root_page
):
    article_listing_page = factories.InternationalArticleListingPageFactory.create( # NOQA
        parent=root_page,
        live=True,
        slug='setup-uk'
    )
    factories.InternationalArticlePageFactory.create(
        parent=article_listing_page,
        live=True
    )
    region_page = factories.InternationalRegionPageFactory(
        parent=root_page,
        live=True,
        slug='germany'
    )
    regional_folder_page = factories.InternationalLocalisedFolderPageFactory(
        parent=region_page,
        live=True,
        slug='news'  # different branch from setup uk
    )
    factories.InternationalArticlePageFactory.create(
        parent=regional_folder_page,
        live=True
    )

    url = reverse(
        'api:api:pages:detail',
        kwargs={'pk': article_listing_page.pk}
    )
    response = admin_client.get(url, {'region': 'bar'})
    assert response.status_code == 200
    assert 'localised_child_pages' in response.json()
    assert response.json()['localised_child_pages'] == []


def test_client_not_passing_region(admin_client, root_page):
    article_listing_page = factories.InternationalArticleListingPageFactory.create(  # NOQA
        parent=root_page,
        live=True
    )

    url = reverse(
        'api:api:pages:detail',
        kwargs={'pk': article_listing_page.pk}
    )
    response = admin_client.get(url)
    assert response.status_code == 200
    assert 'localised_child_pages' in response.json()
    assert response.json()['localised_child_pages'] == []
