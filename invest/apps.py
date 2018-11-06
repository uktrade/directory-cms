from django.apps import AppConfig


class InvestConfig(AppConfig):
    name = 'invest'

    def ready(self):
        from invest import cache
        cache.SectorLandingPageSubscriber.subscribe()
        cache.RegionLandingPageSubscriber.subscribe()
        cache.SectorPageSubscriber.subscribe()
        cache.SetupGuideLandingPageSubscriber.subscribe()
        cache.SetupGuidePageSubscriber.subscribe()
        cache.InvestHomePageSubscriber.subscribe()
        cache.InfoPageSubscriber.subscribe()
        cache.HighPotentialOpportunityFormPageSubscriber.subscribe()
        cache.HighPotentialOpportunityDetailPageSubscriber.subscribe()
        cache.HighPotentialOpportunityFormSuccessPageSubscriber.subscribe()
