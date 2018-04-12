import pytest

from django.urls import reverse

from find_a_supplier.tests import factories
from find_a_supplier import models


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
    factories.IndustryLandingPageFactory()

    url = reverse(
        'lookup-by-page-type',
        kwargs={'page_type': 'find_a_supplier.IndustryLandingPage'}
    )

    response = admin_client.get(url)

    assert response.status_code == 200
    assert len(response.json()['industries']) == 1


@pytest.mark.django_db
def test_industry_exposes_article_summaries(admin_client, untranslated_page):
    models.IndustryPageArticleSummary.objects.create(
        industry_name='industry name',
        title='title',
        body='body',
        page=untranslated_page
    )

    url = reverse('api:pages:detail', kwargs={'pk': untranslated_page.pk})

    response = admin_client.get(url)

    assert response.status_code == 200
    assert len(response.json()['article_summaries']) == 1
