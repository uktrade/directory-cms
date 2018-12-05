from core.cache import AbstractDatabaseCacheSubscriber

from export_readiness import models


class TermsAndConditionsPageSubscriber(AbstractDatabaseCacheSubscriber):
    model = models.TermsAndConditionsPage
    subscriptions = []


class PrivacyAndCookiesPageSubscriber(AbstractDatabaseCacheSubscriber):
    model = models.PrivacyAndCookiesPage
    subscriptions = []


class GetFinancePageSubscriber(AbstractDatabaseCacheSubscriber):
    model = models.GetFinancePage
    subscriptions = []


class PerformanceDashboardPageSubscriber(AbstractDatabaseCacheSubscriber):
    model = models.PerformanceDashboardPage
    subscriptions = []


class PerformanceDashboardNotesPageSubscriber(AbstractDatabaseCacheSubscriber):
    model = models.PerformanceDashboardNotesPage
    subscriptions = []


class TopicLandingPageSubscriber(AbstractDatabaseCacheSubscriber):
    model = models.TopicLandingPage
    subscriptions = []


class ArticleListingPageSubscriber(AbstractDatabaseCacheSubscriber):
    model = models.ArticleListingPage
    subscriptions = [
        models.ArticlePage,
        models.Tag,
    ]


class ArticlePageSubscriber(AbstractDatabaseCacheSubscriber):
    model = models.ArticlePage
    subscriptions = [
        models.Tag,
    ]


class HomePageSubscriber(AbstractDatabaseCacheSubscriber):
    model = models.HomePage
    subscriptions = [
        models.ArticleListingPage,
        models.TopicLandingPage,
        models.ArticleListingPage,
        models.ArticlePage,
    ]


class InternationalLandingPageSubscriber(AbstractDatabaseCacheSubscriber):
    model = models.InternationalLandingPage
    subscriptions = []


class EUExitInternationalFormPageSubscriber(AbstractDatabaseCacheSubscriber):
    model = models.EUExitInternationalFormPage
    subscriptions = []


class EUExitDomesticFormPageSubscriber(AbstractDatabaseCacheSubscriber):
    model = models.EUExitDomesticFormPage
    subscriptions = []


class EUExitFormSuccessPageSubscriber(AbstractDatabaseCacheSubscriber):
    model = models.EUExitFormSuccessPage
    subscriptions = []


class CampaignPageSubscriber(AbstractDatabaseCacheSubscriber):
    model = models.CampaignPage
    subscriptions = []


class ContactSuccessPageSubscriber(AbstractDatabaseCacheSubscriber):
    model = models.ContactSuccessPage
    subscriptions = []


class ContactUsGuidancePageSubscriber(AbstractDatabaseCacheSubscriber):
    model = models.ContactUsGuidancePage
    subscriptions = []
