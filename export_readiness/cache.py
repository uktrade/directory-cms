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
    subscriptions = [
        models.ArticlePage,
        models.ArticleListingPage,
        models.SuperregionPage,
        models.CountryGuidePage,
    ]


class ArticleListingPageSubscriber(AbstractDatabaseCacheSubscriber):
    model = models.ArticleListingPage
    subscriptions = [
        models.TopicLandingPage,
        models.CountryGuidePage,
        models.ArticlePage,
        models.Tag,
    ]


class ArticlePageSubscriber(AbstractDatabaseCacheSubscriber):
    model = models.ArticlePage
    subscriptions = [
        models.ArticlePage,
        models.TopicLandingPage,
        models.SuperregionPage,
        models.CountryGuidePage,
        models.CampaignPage,
        models.ArticleListingPage,
        models.Tag,
    ]


class MarketingArticlePageSubscriber(AbstractDatabaseCacheSubscriber):
    model = models.MarketingArticlePage
    subscriptions = [
        models.ArticlePage,
        models.Tag,
    ]


class HomePageSubscriber(AbstractDatabaseCacheSubscriber):
    model = models.HomePage
    subscriptions = [
        models.ArticleListingPage,
        models.TopicLandingPage,
        models.ArticlePage,
    ]


class HomePageOldSubscriber(AbstractDatabaseCacheSubscriber):
    model = models.HomePageOld
    subscriptions = [
        models.ArticleListingPage,
        models.TopicLandingPage,
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
    subscriptions = [
        models.ArticlePage,
    ]


class ContactSuccessPageSubscriber(AbstractDatabaseCacheSubscriber):
    model = models.ContactSuccessPage
    subscriptions = []


class ContactUsGuidancePageSubscriber(AbstractDatabaseCacheSubscriber):
    model = models.ContactUsGuidancePage
    subscriptions = []


class SuperregionPageSubscriber(AbstractDatabaseCacheSubscriber):
    model = models.SuperregionPage
    subscriptions = [
        models.TopicLandingPage,
        models.ArticleListingPage,
        models.CountryGuidePage,
    ]


class CountryGuidePageSubscriber(AbstractDatabaseCacheSubscriber):
    model = models.CountryGuidePage
    subscriptions = [
        models.ArticlePage,
        models.TopicLandingPage,
        models.ArticleListingPage,
        models.CampaignPage,
    ]
