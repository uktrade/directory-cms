from directory_constants.constants import cms
from django.core.files.base import ContentFile

from rest_framework.reverse import reverse
from six import b
from wagtail.documents.models import Document

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
    subsections = response.json()['section_two_subsections']
    assert list(subsections[0].keys()) == ['icon', 'heading', 'body']
    featured_links = response.json()['featured_links'][0]
    assert list(featured_links.keys()) == ['image', 'heading']


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


def test_international_topic_landing_page_view_sectors_alphabetical_order(
        admin_client, root_page):
    landing_page = factories.InternationalTopicLandingPageFactory.create(
        parent=root_page
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


def test_invest_home_page(admin_client, root_page):
    page = factories.InvestInternationalHomePageFactory(live=True)
    sector_one = factories.InternationalSectorPageFactory(
        live=True, parent=page
    )
    sector_two = factories.InternationalSectorPageFactory(
        live=True, parent=page
    )

    fake_file = ContentFile(b('A boring example document'))
    fake_file.name = 'test.pdf'
    pdf = Document.objects.create(title='Test document', file=fake_file)

    factories.InvestHighPotentialOpportunityDetailPageFactory(
        title='Featured',
        live=True,
        pdf_document=pdf,
        featured=True,
        parent=sector_one,
    )

    factories.InvestHighPotentialOpportunityDetailPageFactory(
        title='Not Featured',
        live=True,
        pdf_document=pdf,
        featured=False,
        parent=sector_two,
    )

    url = reverse(
        'api:lookup-by-slug',
        kwargs={'slug': page.slug}
    )

    response = admin_client.get(url, {'service_name': cms.GREAT_INTERNATIONAL})
    assert response.status_code == 200
    meta = response.json()['meta']
    assert meta['url'] == 'http://invest.trade.great:8011/'
    assert meta['slug'] == 'home-page'
    assert len(response.json()['sectors']) == 1
    high_potential_ops = response.json()['high_potential_opportunities']
    assert len(high_potential_ops) == 1
    assert high_potential_ops[0]['title'] == 'Featured'


def test_high_potential_opportunity_api(page, admin_client, root_page):
    pdf_document = Document.objects.create(
        title='document.pdf',
        file=page.introduction_column_two_icon.file  # not really pdf
    )

    factories.InvestHighPotentialOpportunityDetailPageFactory(
        parent=root_page,
        live=True,
        pdf_document=pdf_document,
    )
    page = factories.InvestHighPotentialOpportunityDetailPageFactory(
        parent=root_page,
        live=True,
        pdf_document=pdf_document,
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
