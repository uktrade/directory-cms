from directory_constants.constants import cms

import pytest

from django.urls import reverse
from django.utils import translation

from core.cache import is_registered_for_cache, PageCache
from core.helpers import CachedResponse
from export_readiness import models
from export_readiness.tests import factories


def test_cache_registration():
    for model in [
        models.TermsAndConditionsPage,
        models.PrivacyAndCookiesPage,
        models.DeprecatedGetFinancePage,
        models.NewGetFinancePage,
        models.PerformanceDashboardPage,
        models.PerformanceDashboardNotesPage,
        models.TopicLandingPage,
        models.ArticleListingPage,
        models.ArticlePage,
        models.HomePage,
        models.InternationalLandingPage,
        models.EUExitInternationalFormPage,
        models.EUExitDomesticFormPage,
        models.EUExitFormSuccessPage,
    ]:
        assert not is_registered_for_cache(model)


@pytest.mark.django_db
def test_unregistered_page_not_cached(admin_client):
    service_name = cms.EXPORT_READINESS
    # given there exists a page that is unregistered for cache
    page = factories.InternationaLandingPageFactory.create(live=True)

    # when the industry page is retrieveds
    url = reverse('lookup-by-slug', kwargs={'slug': page.slug})
    response_one = admin_client.get(url, {'service_name': service_name})

    # then the page is not retrieved from the cache
    assert not isinstance(response_one, CachedResponse)

    # and the page has not been cached by the view
    assert PageCache.get(
        slug=page.slug,
        service_name=service_name,
        language_code=translation.get_language()
    ) is None

    # and subsequent requests are not handled by the cache
    response_two = admin_client.get(url, {'service_name': service_name})
    assert not isinstance(response_two, CachedResponse)
