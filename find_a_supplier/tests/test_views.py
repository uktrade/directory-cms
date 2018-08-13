import pytest

from django.urls import reverse

from find_a_supplier.tests import factories
from find_a_supplier import models


@pytest.mark.django_db
def test_landing_page_exposes_industries(admin_client, root_page):
    industry = factories.IndustryPageFactory(live=True, show_on_homepage=True)
    factories.IndustryPageFactory(live=False)
    factories.IndustryPageFactory(show_on_homepage=True, live=False)
    factories.IndustryPageFactory()
    landing_page = factories.LandingPageFactory(live=True, parent=root_page)

    url = reverse('api:pages:detail', kwargs={'pk': landing_page.pk})

    response = admin_client.get(url)

    assert response.status_code == 200
    assert len(response.json()['industries']) == 1
    assert response.json()['industries'][0]['meta']['pk'] == industry.pk


@pytest.mark.django_db
def test_industry_landing_page_exposes_industries(admin_client, root_page):
    industry = factories.IndustryPageFactory(live=True)
    factories.IndustryPageFactory(live=False)
    landing_page = factories.IndustryLandingPageFactory(
        live=True,
        parent=root_page
    )

    url = reverse('api:pages:detail', kwargs={'pk': landing_page.pk})

    response = admin_client.get(url)

    assert response.status_code == 200
    assert len(response.json()['industries']) == 1
    assert response.json()['industries'][0]['meta']['pk'] == industry.pk


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
