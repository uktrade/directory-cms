from django.urls import reverse

import pytest

from find_a_supplier import models
from find_a_supplier.tests import factories

from core.helpers import CachedResponse
from core.cache import is_registered_for_cache


@pytest.mark.django_db
def test_unpublished_not_cached(admin_client):
    # given there exists an industry page
    contact_page = factories.IndustryContactPageFactory.create(live=False)

    # when the industry page is retrieveds
    url = reverse('lookup-by-slug', kwargs={'slug': contact_page.slug})
    response = admin_client.get(url, {'service_name': 'FIND_A_SUPPLIER'})

    # then the page is retrieved from the cache
    assert isinstance(response, CachedResponse) is False


@pytest.mark.django_db
def test_cache_retrieval(admin_client):
    # given there exists an industry page
    contact_page = factories.IndustryContactPageFactory.create(live=True)

    # when the industry page is retrieveds
    url = reverse('lookup-by-slug', kwargs={'slug': contact_page.slug})
    response = admin_client.get(url, {'service_name': 'FIND_A_SUPPLIER'})

    # then the page is retrieved from the cache
    assert isinstance(response, CachedResponse)


@pytest.mark.django_db
def test_cache_retrieval_external_change(admin_client):
    service_name = 'FIND_A_SUPPLIER'
    # given there is an unpublished industry page
    factories.IndustryPageFactory.create(live=False)
    # and a live industry page
    industry_page = factories.IndustryPageFactory.create(
        introduction_text_en_gb='first value'
    )

    # and an external page that the page is subscribed to is created
    contact_page = factories.IndustryContactPageFactory.create()

    # when the industry page is retrieved
    url = reverse('lookup-by-slug', kwargs={'slug': contact_page.slug})
    first_response = admin_client.get(url, {'service_name': service_name})

    # then the page is retrieved from the cache
    assert isinstance(first_response, CachedResponse)

    # and contains the external page contents
    industries = first_response.json()['industry_options']
    assert len(industries) == 1
    assert industries[0]['meta']['pk'] == industry_page.pk
    assert industries[0]['introduction_text'] == 'first value'

    # when I update the external page
    industry_page.introduction_text = 'updated value'
    industry_page.save()

    # when the industry page is retrieved
    second_response = admin_client.get(url, {'service_name': service_name})

    # then the page is retrieved from the cache
    assert isinstance(second_response, CachedResponse)

    # and contains the external page updated contents
    industries = second_response.json()['industry_options']
    assert len(industries) == 1
    assert industries[0]['meta']['pk'] == industry_page.pk
    assert industries[0]['introduction_text'] == 'updated value'


@pytest.mark.django_db
def test_cache_unpublish(admin_client):
    # given there exists an industry page
    contact_page = factories.IndustryContactPageFactory.create(live=True)

    # when the industry page is retrieved
    url = reverse('lookup-by-slug', kwargs={'slug': contact_page.slug})
    response = admin_client.get(url, {'service_name': 'FIND_A_SUPPLIER'})

    # then the page is retrieved from the cache
    assert isinstance(response, CachedResponse)

    # when the page is unpublished
    contact_page.unpublish()
    contact_page.live = False
    contact_page.save()

    # when the industry page is retrieved
    response = admin_client.get(url, {'service_name': 'FIND_A_SUPPLIER'})

    # then the page is not retrieved from the cache
    assert isinstance(response, CachedResponse) is False
    assert response.status_code == 404


def test_cache_registration():
    for model in [
        models.IndustryPage,
        models.IndustryLandingPage,
        models.IndustryArticlePage,
        models.LandingPage,
        models.IndustryContactPage,
    ]:
        assert is_registered_for_cache(model)
