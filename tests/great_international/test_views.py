from directory_constants import cms

from rest_framework.reverse import reverse

from tests.great_international import factories


def test_international_sector_page(admin_client, international_root_page):
    sector_page = factories.InternationalSectorPageFactory.create(
        parent=international_root_page
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
    subsections = response.json()['section_two_subsections']
    assert list(subsections[0].keys()) == ['icon', 'heading', 'body']
    featured_links = response.json()['featured_links'][0]
    assert list(featured_links.keys()) == ['image', 'heading']


def test_international_campaign_page(admin_client, international_root_page):

    campaign_page = factories.InternationalCampaignPageFactory(
        parent=international_root_page
    )
    url = reverse('api:api:pages:detail', kwargs={'pk': campaign_page.pk})
    response = admin_client.get(url)
    assert response.status_code == 200


def test_international_article_listing_page_view(admin_client, international_root_page):
    article_listing_page = factories.InternationalArticleListingPageFactory.create(  # NOQA
        parent=international_root_page,
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


def test_international_topic_landing_page_view(admin_client, international_root_page):
    topic_landing_page = factories.InternationalTopicLandingPageFactory.create(
        parent=international_root_page,
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


def test_international_topic_landing_page_view_sectors_alphabetical_order(
        admin_client, international_root_page):
    landing_page = factories.InternationalTopicLandingPageFactory.create(
        parent=international_root_page
    )
    sector_page1 = factories.InternationalSectorPageFactory.create(
        parent=landing_page,
        live=True,
        heading='acme'
    )
    sector_page2 = factories.InternationalSectorPageFactory.create(
        parent=landing_page,
        live=True,
        heading='foo'
    )
    url = reverse('api:api:pages:detail', kwargs={'pk': landing_page.pk})
    response = admin_client.get(url)
    assert response.status_code == 200
    assert [page['id'] for page in response.json()['child_pages']] == [
        sector_page1.pk, sector_page2.pk
    ]


def test_article_listingpage_with_localised_content(admin_client, international_root_page):
    article_listing_page = factories.InternationalArticleListingPageFactory.create(  # NOQA
        parent=international_root_page,
        live=True,
        slug='setup-uk'
    )
    factories.InternationalArticlePageFactory.create(
        parent=article_listing_page,
        live=True
    )
    region_page = factories.InternationalRegionPageFactory(
        parent=international_root_page,
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
        'api:lookup-by-slug',
        kwargs={'slug': article_listing_page.slug}
    )

    response = admin_client.get(
        url,
        {'region': 'germany', 'service_name': cms.GREAT_INTERNATIONAL}
    )
    assert response.status_code == 200
    assert 'localised_child_pages' in response.json()
    expected_localised_article = response.json(
        )['localised_child_pages'][0]['id']
    assert expected_localised_article == localised_article.pk


def test_article_listingpage_without_localised_content(
        admin_client, international_root_page
):
    article_listing_page = factories.InternationalArticleListingPageFactory.create( # NOQA
        parent=international_root_page,
        live=True,
        slug='setup-uk'
    )
    factories.InternationalArticlePageFactory.create(
        parent=article_listing_page,
        live=True
    )
    region_page = factories.InternationalRegionPageFactory(
        parent=international_root_page,
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
        'api:lookup-by-slug',
        kwargs={'slug': article_listing_page.slug}
    )

    response = admin_client.get(
        url,
        {'region': 'bar', 'service_name': cms.GREAT_INTERNATIONAL}
    )
    assert response.status_code == 200
    assert 'localised_child_pages' in response.json()
    assert response.json()['localised_child_pages'] == []


def test_client_not_passing_region(admin_client, international_root_page):
    article_listing_page = factories.InternationalArticleListingPageFactory.create(  # NOQA
        parent=international_root_page,
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


def test_invest_home_page(document, admin_client, international_root_page):
    page = factories.InvestInternationalHomePageFactory(live=True, parent=international_root_page)

    factories.InvestHighPotentialOpportunityDetailPageFactory(
        title='Featured',
        live=True,
        pdf_document=document,
        featured=True,
        parent=international_root_page,
    )

    factories.InvestHighPotentialOpportunityDetailPageFactory(
        title='Not Featured',
        live=True,
        pdf_document=document,
        featured=False,
        parent=international_root_page,
    )

    url = reverse(
        'api:lookup-by-slug',
        kwargs={'slug': page.slug}
    )

    response = admin_client.get(url, {'service_name': cms.GREAT_INTERNATIONAL})
    assert response.status_code == 200
    high_potential_ops = response.json()['high_potential_opportunities']
    assert len(high_potential_ops) == 1
    assert high_potential_ops[0]['title'] == 'Featured'


def test_invest_region_page(admin_client, international_root_page):
    page = factories.InvestRegionPageFactory(
        live=True, featured=True, parent=international_root_page
    )
    factories.InvestRegionPageFactory(live=True, parent=page)

    url = reverse('api:api:pages:detail', kwargs={'pk': page.pk})

    response = admin_client.get(url)
    assert response.status_code == 200


def test_invest_region_landing_page(admin_client, international_root_page):
    page = factories.InvestRegionLandingPageFactory(
        live=True, parent=international_root_page
    )
    factories.InvestRegionPageFactory(live=True, parent=page)

    url = reverse('api:api:pages:detail', kwargs={'pk': page.pk})

    response = admin_client.get(url)
    assert response.status_code == 200
    assert len(response.json()['regions']) == 1


def test_high_potential_opportunity_api(document, admin_client, international_root_page):
    factories.InvestHighPotentialOpportunityDetailPageFactory(
        parent=international_root_page,
        live=True,
        pdf_document=document,
    )
    page = factories.InvestHighPotentialOpportunityDetailPageFactory(
        parent=international_root_page,
        live=True,
        pdf_document=document,
        slug='some-nice-slug',
    )

    url = reverse(
        'api:lookup-by-slug',
        kwargs={'slug': page.slug}
    )

    response = admin_client.get(url, {'service_name': cms.GREAT_INTERNATIONAL})

    assert response.status_code == 200
    parsed = response.json()
    assert 'other_opportunities' in parsed
    assert 'other_opportunities' not in parsed['other_opportunities'][0]


def test_international_trade_home_page_exposes_industries(
        admin_client,
        international_root_page
):
    industry = factories.InternationalSectorPageFactory(parent=international_root_page,
                                                        live=True)
    factories.InternationalSectorPageFactory(parent=international_root_page, live=False)
    homepage = factories.InternationalTradeHomePageFactory(
        live=True, parent=international_root_page
    )
    url = reverse('api:api:pages:detail', kwargs={'pk': homepage.pk})
    response = admin_client.get(url)

    assert response.status_code == 200
    assert len(response.json()['industries']) == 1
    assert response.json()['industries'][0]['meta']['pk'] == industry.pk


def test_sector_page_exposes_articles_child_sub_pages(admin_client, international_root_page):
    sector_page = factories.InternationalSectorPageFactory(parent=international_root_page, slug='sector-one')
    article_page = factories.InternationalArticlePageFactory(parent=sector_page)
    article_page2 = factories.InternationalArticlePageFactory(parent=sector_page)
    url = reverse('api:api:pages:detail', kwargs={'pk': sector_page.pk})
    response = admin_client.get(url)

    assert response.status_code == 200
    assert len(response.json()['child_sub_articles']) == 2
