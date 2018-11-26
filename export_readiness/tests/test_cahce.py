from unittest import mock

from core.cache import is_registered_for_cache
from export_readiness import models


def test_cache_registration():
    for model in [
        models.TermsAndConditionsPage,
        models.PrivacyAndCookiesPage,
        models.GetFinancePage,
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
        models.CampaignPage,
    ]:
        assert is_registered_for_cache(model)


def test_cache_not_registred():
    assert not is_registered_for_cache(mock.Mock)
