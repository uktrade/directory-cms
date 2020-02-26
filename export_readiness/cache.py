from core.cache import AbstractDatabaseCacheSubscriber

from export_readiness import models, snippets


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
    ]


class ArticleListingPageSubscriber(AbstractDatabaseCacheSubscriber):
    model = models.ArticleListingPage
    subscriptions = [
        snippets.Tag,
    ]


class ArticlePageSubscriber(AbstractDatabaseCacheSubscriber):
    model = models.ArticlePage
    subscriptions = [
        models.SuperregionPage,
        snippets.Tag,
    ]


class MarketingArticlePageSubscriber(AbstractDatabaseCacheSubscriber):
    model = models.MarketingArticlePage
    subscriptions = [
        models.ArticlePage,
        snippets.Tag,
    ]


class HomePageSubscriber(AbstractDatabaseCacheSubscriber):
    model = models.HomePage
    subscriptions = [
        models.ArticleListingPage,
        models.TopicLandingPage,
        models.ArticlePage,
    ]


class EUExitDomesticFormPageSubscriber(AbstractDatabaseCacheSubscriber):
    model = models.EUExitDomesticFormPage
    subscriptions = []


class EUExitFormSuccessPageSubscriber(AbstractDatabaseCacheSubscriber):
    model = models.EUExitFormSuccessPage
    subscriptions = []


class CampaignPageSubscriber(AbstractDatabaseCacheSubscriber):
    model = models.CampaignPage
    subscriptions = [
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
        models.ArticleListingPage,
        models.CountryGuidePage,
    ]


class CountryGuidePageSubscriber(AbstractDatabaseCacheSubscriber):
    model = models.CountryGuidePage
    subscriptions = [
        models.CampaignPage,
        snippets.IndustryTag
    ]


class SellingOnlineOverseasHomePageSubscriber(AbstractDatabaseCacheSubscriber):
    model = models.SellingOnlineOverseasHomePage
    subscriptions = [
        models.ArticlePage,
    ]
