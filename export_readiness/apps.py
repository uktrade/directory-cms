from django.apps import AppConfig


class ExportReadinessConfig(AppConfig):
    name = 'export_readiness'

    def ready(self):
        from export_readiness import cache
        cache.TermsAndConditionsPageSubscriber.subscribe()
        cache.PrivacyAndCookiesPageSubscriber.subscribe()
        cache.GetFinancePageSubscriber.subscribe()
        cache.PerformanceDashboardPageSubscriber.subscribe()
        cache.PerformanceDashboardNotesPageSubscriber.subscribe()
        cache.TopicLandingPageSubscriber.subscribe()
        cache.ArticleListingPageSubscriber.subscribe()
        cache.ArticlePageSubscriber.subscribe()
        cache.HomePageSubscriber.subscribe()
        cache.InternationalLandingPageSubscriber.subscribe()
        cache.EUExitInternationalFormPageSubscriber.subscribe()
        cache.EUExitDomesticFormPageSubscriber.subscribe()
        cache.EUExitFormSuccessPageSubscriber.subscribe()
        cache.CampaignPageSubscriber.subscribe()
        cache.ContactSuccessPageSubscriber.subscribe()
        cache.ContactUsGuidancePageSubscriber.subscribe()
