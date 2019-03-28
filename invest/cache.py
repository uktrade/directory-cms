from core.cache import AbstractDatabaseCacheSubscriber

from invest import models


class SectorLandingPageSubscriber(AbstractDatabaseCacheSubscriber):
    model = models.SectorLandingPage
    subscriptions = [
        models.SectorPage,
    ]


class RegionLandingPageSubscriber(AbstractDatabaseCacheSubscriber):
    model = models.RegionLandingPage
    subscriptions = [
        models.SectorPage,
    ]


class SectorPageSubscriber(AbstractDatabaseCacheSubscriber):
    model = models.SectorPage
    subscriptions = [
        # not a typo: each sector page contains a list of other sector pages
        models.SectorPage,
    ]


class SetupGuideLandingPageSubscriber(AbstractDatabaseCacheSubscriber):
    model = models.SetupGuideLandingPage
    subscriptions = [
        models.SetupGuidePage,
    ]


class SetupGuidePageSubscriber(AbstractDatabaseCacheSubscriber):
    model = models.SetupGuidePage
    subscriptions = [
        # not a typo: each guide page contains a list of other guide pages
        models.SetupGuidePage,
    ]


class InvestHomePageSubscriber(AbstractDatabaseCacheSubscriber):
    model = models.InvestHomePage
    subscriptions = [
        models.SectorPage,
        models.SetupGuidePage,
        models.HighPotentialOpportunityDetailPage
    ]


class InfoPageSubscriber(AbstractDatabaseCacheSubscriber):
    model = models.InfoPage
    subscriptions = []


class HighPotentialOpportunityFormPageSubscriber(
    AbstractDatabaseCacheSubscriber
):
    model = models.HighPotentialOpportunityFormPage
    subscriptions = [
        models.HighPotentialOpportunityDetailPage,
    ]


class HighPotentialOpportunityDetailPageSubscriber(
    AbstractDatabaseCacheSubscriber
):
    model = models.HighPotentialOpportunityDetailPage
    subscriptions = [
        models.HighPotentialOpportunityDetailPage,
    ]


class HighPotentialOpportunityFormSuccessPageSubscriber(
    AbstractDatabaseCacheSubscriber
):
    model = models.HighPotentialOpportunityFormSuccessPage
    subscriptions = [
        models.HighPotentialOpportunityDetailPage,
    ]
