from core.cache import is_registered_for_cache
from export_readiness import models


def test_cache_registration():
    for model in [
        models.TermsAndConditionsPage,
        models.PrivacyAndCookiesPage,
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
        assert is_registered_for_cache(model)


def test_cache_not_registred():
    for model in [
        models.DeprecatedGetFinancePage,
    ]:
        assert not is_registered_for_cache(model)
