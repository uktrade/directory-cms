from core.cache import DatabaseCacheSubscriber

from export_readiness import models, snippets


subscribers = [
    DatabaseCacheSubscriber([
        models.TermsAndConditionsPage
        models.PrivacyAndCookiesPage
        models.GetFinancePage
        models.PerformanceDashboardPage
        models.PerformanceDashboardNotesPage
        models.TopicLandingPage
        models.ArticleListingPage
        models.ArticlePage
        models.MarketingArticlePage
        models.HomePage
        models.EUExitDomesticFormPage
        models.EUExitFormSuccessPage
        models.CampaignPage
        models.ContactSuccessPage
        models.ContactUsGuidancePage
        models.SuperregionPage
        models.CountryGuidePage
        models.SellingOnlineOverseasHomePage
    ])
]