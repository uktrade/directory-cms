import pytest
from directory_constants import cms
from rest_framework.reverse import reverse
from wagtail.documents.models import Document
from django.core.files.base import ContentFile
from django.utils.six import b
from . import factories
from find_a_supplier.tests.factories import IndustryPageFactory


@pytest.fixture
def page(root_page):
    return IndustryPageFactory(
        parent=root_page,
        slug='the-slug'
    )


@pytest.mark.django_db
def test_invest_home_page(admin_client):
    page = factories.InvestHomePageFactory(live=True)
    factories.SetupGuidePageFactory(live=True)
    factories.SetupGuidePageFactory(live=False)
    factories.SectorPageFactory(live=True, featured=True)
    factories.SectorPageFactory(live=True, featured=False)

    fake_file = ContentFile(b('A boring example document'))
    fake_file.name = 'test.pdf'
    pdf = Document.objects.create(title="Test document", file=fake_file)

    factories.HighPotentialOpportunityDetailPageFactory(
        title="Featured",
        live=True,
        pdf_document=pdf,
        featured=True
    )

    factories.HighPotentialOpportunityDetailPageFactory(
        title="Not Featured",
        live=True,
        pdf_document=pdf,
        featured=False
    )

    url = reverse(
        'api:lookup-by-slug',
        kwargs={'slug': page.slug}
    )

    response = admin_client.get(url, {'service_name': cms.INVEST})
    assert response.status_code == 200
    meta = response.json()['meta']
    assert meta['url'] == 'http://invest.trade.great:8011'
    assert meta['slug'] == 'home-page'
    assert len(response.json()['guides']) == 1
    assert len(response.json()['sectors']) == 1
    high_potential_ops = response.json()['high_potential_opportunities']
    assert len(high_potential_ops) == 1
    assert high_potential_ops[0]['title'] == "Featured"


@pytest.mark.django_db
def test_invest_info_page(admin_client, root_page):
    page = factories.InfoPageFactory(live=True, parent=root_page)

    url = reverse('api:api:pages:detail', kwargs={'pk': page.pk})

    response = admin_client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_invest_sector_page(admin_client, root_page):
    page = factories.SectorPageFactory(
        live=True, featured=True, parent=root_page
    )
    factories.SectorPageFactory(live=True, parent=page)
    factories.SectorPageFactory(
        live=True,
        parent=factories.SectorPageFactory()
    )

    url = reverse('api:api:pages:detail', kwargs={'pk': page.pk})

    response = admin_client.get(url)
    assert response.status_code == 200
    assert len(response.json()['children_sectors']) == 1


@pytest.mark.django_db
def test_invest_sector_landing_page(admin_client, root_page):
    page = factories.SectorLandingPageFactory(
        live=True, parent=root_page
    )
    factories.SectorPageFactory(live=True, parent=page)

    url = reverse('api:api:pages:detail', kwargs={'pk': page.pk})

    response = admin_client.get(url)
    assert response.status_code == 200
    assert len(response.json()['children_sectors']) == 1


@pytest.mark.django_db
def test_invest_region_landing_page(admin_client, root_page):
    page = factories.RegionLandingPageFactory(
        live=True, parent=root_page
    )
    factories.SectorPageFactory(live=True, parent=page)

    url = reverse('api:api:pages:detail', kwargs={'pk': page.pk})

    response = admin_client.get(url)
    assert response.status_code == 200
    assert len(response.json()['children_sectors']) == 1


@pytest.mark.django_db
def test_invest_setup_guide_page(admin_client, root_page):
    page = factories.SetupGuidePageFactory(
        live=True, parent=root_page
    )
    factories.SetupGuidePageFactory(live=True, parent=page)
    factories.SetupGuidePageFactory(
        live=True,
        parent=factories.SetupGuidePageFactory()
    )

    url = reverse('api:api:pages:detail', kwargs={'pk': page.pk})

    response = admin_client.get(url)
    assert response.status_code == 200
    assert len(response.json()['children_setup_guides']) == 1


@pytest.mark.django_db
def test_invest_setup_guide_landing_page(admin_client, root_page):
    page = factories.SetupGuideLandingPageFactory(
        live=True, parent=root_page
    )
    factories.SetupGuidePageFactory(live=True, parent=page)

    url = reverse('api:api:pages:detail', kwargs={'pk': page.pk})

    response = admin_client.get(url)
    assert response.status_code == 200
    assert len(response.json()['children_setup_guides']) == 1


@pytest.mark.django_db
def test_high_potential_opportunity_api(page, admin_client, root_page):
    pdf_document = Document.objects.create(
        title='document.pdf',
        file=page.introduction_column_two_icon.file  # not really pdf
    )

    factories.HighPotentialOpportunityDetailPageFactory(
        parent=root_page,
        live=True,
        pdf_document=pdf_document,
    )
    page = factories.HighPotentialOpportunityDetailPageFactory(
        parent=root_page,
        live=True,
        pdf_document=pdf_document,
        slug='some-nice-slug',
    )

    url = reverse(
        'api:lookup-by-slug',
        kwargs={'slug': page.slug}
    )

    response = admin_client.get(url, {'service_name': cms.INVEST})

    assert response.status_code == 200
    parsed = response.json()
    assert 'other_opportunities' in parsed
    assert 'other_opportunities' not in parsed['other_opportunities'][0]
