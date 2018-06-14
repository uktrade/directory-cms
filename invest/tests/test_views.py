import pytest
from rest_framework.reverse import reverse

from . import factories


@pytest.mark.django_db
def test_invest_home_page(admin_client):
    page = factories.InvestHomePageFactory(live=True)
    factories.SetupGuidePageFactory(live=True)
    factories.SetupGuidePageFactory(live=False)
    factories.SectorPageFactory(live=True, featured=True)
    factories.SectorPageFactory(live=True, featured=False)

    url = reverse(
        'lookup-by-slug',
        kwargs={'slug': page.slug}
    )

    response = admin_client.get(url)
    assert response.status_code == 200
    meta = response.json()['meta']
    assert meta['url'] == 'http://invest.trade.great:8011'
    assert meta['slug'] == 'invest-home-page'
    assert len(response.json()['guides']) == 1
    assert len(response.json()['sectors']) == 1


@pytest.mark.django_db
def test_invest_info_page(admin_client, root_page):
    page = factories.InfoPageFactory(live=True, parent=root_page)

    url = reverse('api:pages:detail', kwargs={'pk': page.pk})

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

    url = reverse('api:pages:detail', kwargs={'pk': page.pk})

    response = admin_client.get(url)
    assert response.status_code == 200
    assert len(response.json()['children_sectors']) == 1


@pytest.mark.django_db
def test_invest_sector_landing_page(admin_client, root_page):
    page = factories.SectorLandingPageFactory(
        live=True, parent=root_page
    )
    factories.SectorPageFactory(live=True, parent=page)

    url = reverse('api:pages:detail', kwargs={'pk': page.pk})

    response = admin_client.get(url)
    assert response.status_code == 200
    assert len(response.json()['children_sectors']) == 1


@pytest.mark.django_db
def test_invest_region_landing_page(admin_client, root_page):
    page = factories.RegionLandingPageFactory(
        live=True, parent=root_page
    )
    factories.SectorPageFactory(live=True, parent=page)

    url = reverse('api:pages:detail', kwargs={'pk': page.pk})

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

    url = reverse('api:pages:detail', kwargs={'pk': page.pk})

    response = admin_client.get(url)
    assert response.status_code == 200
    assert len(response.json()['children_setup_guides']) == 1


@pytest.mark.django_db
def test_invest_setup_guide_landing_page(admin_client, root_page):
    page = factories.SetupGuideLandingPageFactory(
        live=True, parent=root_page
    )
    factories.SetupGuidePageFactory(live=True, parent=page)

    url = reverse('api:pages:detail', kwargs={'pk': page.pk})

    response = admin_client.get(url)
    assert response.status_code == 200
    assert len(response.json()['children_setup_guides']) == 1
