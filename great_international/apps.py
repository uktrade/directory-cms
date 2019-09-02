from django.apps import AppConfig


class GreatInternationalConfig(AppConfig):
    name = 'great_international'

    def ready(self):
        from great_international import cache
        cache.InternationalSectorPageSubscriber.subscribe()
        cache.InternationalSubSectorPageSubscriber.subscribe()
        cache.InternationalHomePageSubscriber.subscribe()
        cache.InternationalArticlePageSubscriber.subscribe()
        cache.InternationalCampaignPageSubscriber.subscribe()
        cache.InternationalArticleListingPageSubscriber.subscribe()
        cache.InternationalTopicLandingPageSubscriber.subscribe()
        cache.InternationalCuratedTopicLandingPageSubscriber.subscribe()
        cache.InternationalGuideLandingPageSubscriber.subscribe()
        cache.InternationalEUExitFormPageSubscriber.subscribe()
        cache.InternationalEUExitFormSuccessPageSubscriber.subscribe()
        cache.InternationalCapitalInvestLandingPageSubscriber.subscribe()
        cache.CapitalInvestOpportunityPageSubscriber.subscribe()
        cache.CapitalInvestOpportunityListingPageSubscriber.subscribe()
        cache.InvestInternationalHomePageSubscriber.subscribe()
        cache.InvestHighPotentialOpportunityDetailPageSubscriber.subscribe()
        cache.InvestHighPotentialOpportunityFormPageSubscriber.subscribe()
        cache.InvestHighPotentialOpportunityFormSuccessPageSubscriber.subscribe()  # noqa
        cache.InvestRegionLandingPageSubscriber.subscribe()
        cache.InvestRegionPageSubscriber.subscribe()
        cache.InternationalTradeHomePageSubscriber.subscribe()
        cache.InternationalTradeIndustryContactPageSubscriber.subscribe()
        cache.AboutDitLandingPageSubscriber.subscribe()
        cache.AboutDitServicesPageSubscriber.subscribe()
        cache.AboutUkLandingPageSubscriber.subscribe()
        cache.AboutUkRegionListingPageSubscriber.subscribe()
        cache.AboutUkRegionPageSubscriber.subscribe()
        cache.AboutUkWhyChooseTheUkPageSubscriber.subscribe()
        cache.CapitalInvestContactFormPageSubscriber.subscribe()
        cache.CapitalInvestContactFormSuccessPageSubscriber.subscribe()
