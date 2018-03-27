import pytest

from django.urls import reverse

from find_a_supplier.tests import factories


@pytest.mark.django_db
def test_landing_page_exposes_industries(admin_client):
    factories.IndustryPageFactory()
    factories.LandingPageFactory()

    url = reverse(
        'lookup-by-page-type',
        kwargs={'page_type': 'find_a_supplier.LandingPage'}
    )

    response = admin_client.get(url)

    assert response.status_code == 200
    assert len(response.json()['industries']) == 1


@pytest.mark.django_db
def test_industry_landing_page_exposes_industries(admin_client):
    factories.IndustryPageFactory()
    factories.IndustryLandingPagePageFactory()

    url = reverse(
        'lookup-by-page-type',
        kwargs={'page_type': 'find_a_supplier.IndustryLandingPage'}
    )

    response = admin_client.get(url)

    assert response.status_code == 200
    assert len(response.json()['industries']) == 1
