from core.cache import (
    AbstractDatabaseCacheSubscriber, RegionAwareCachePopulator
)

from great_international import models


class InternationalSectorPageSubscriber(AbstractDatabaseCacheSubscriber):
    model = models.InternationalSectorPage
    subscriptions = [
        models.InternationalArticlePage,
        models.InternationalCampaignPage
    ]


class InternationalHomePageSubscriber(AbstractDatabaseCacheSubscriber):
    model = models.InternationalHomePage
    subscriptions = [
        models.InternationalArticlePage,
    ]


class InternationalArticlePageSubscriber(AbstractDatabaseCacheSubscriber):
    model = models.InternationalArticlePage
    subscriptions = []


class InternationalCampaignPageSubscriber(AbstractDatabaseCacheSubscriber):
    model = models.InternationalCampaignPage
    subscriptions = []


class InternationalArticleListingPageSubscriber(
    AbstractDatabaseCacheSubscriber
):
    cache_populator = RegionAwareCachePopulator
    model = models.InternationalArticleListingPage
    subscriptions = [
        models.InternationalArticlePage,
        models.InternationalCampaignPage
    ]


class InternationalTopicLandingPageSubscriber(AbstractDatabaseCacheSubscriber):
    model = models.InternationalTopicLandingPage
    subscriptions = [
        models.InternationalArticlePage,
        models.InternationalArticleListingPage,
        models.InternationalSectorPage,
        models.InternationalCampaignPage
    ]


class InternationalCuratedTopicLandingPageSubscriber(
    AbstractDatabaseCacheSubscriber
):
    model = models.InternationalCuratedTopicLandingPage
    subscriptions = []


class InternationalGuideLandingPageSubscriber(AbstractDatabaseCacheSubscriber):
    model = models.InternationalGuideLandingPage
    subscriptions = [models.InternationalArticlePage]


class InternationalEUExitFormPageSubscriber(
    AbstractDatabaseCacheSubscriber
):
    model = models.InternationalEUExitFormPage
    subscriptions = []


class InternationalEUExitFormSuccessPageSubscriber(
    AbstractDatabaseCacheSubscriber
):
    model = models.InternationalEUExitFormSuccessPage
    subscriptions = []


class InternationalCapitalInvestLandingPageSubscriber(
                                        AbstractDatabaseCacheSubscriber):
    model = models.InternationalCapitalInvestLandingPage
    subscriptions = [models.CapitalInvestRegionPage]


class CapitalInvestRegionPageSubscriber(AbstractDatabaseCacheSubscriber):
    model = models.CapitalInvestRegionPage
    subscriptions = [
        models.CapitalInvestRegionalSectorPage,
        models.InternationalCapitalInvestLandingPage
    ]


class CapitalInvestRegionalSectorPageSubscriber(AbstractDatabaseCacheSubscriber):
    model = models.CapitalInvestRegionalSectorPage
    subscriptions = [
        models.CapitalInvestOpportunityPage,
        models.CapitalInvestRegionPage
    ]


class CapitalInvestOpportunityPageSubscriber(AbstractDatabaseCacheSubscriber):
    model = models.CapitalInvestOpportunityPage
    subscriptions = [
        models.CapitalInvestOpportunityPage,
        models.CapitalInvestRegionalSectorPage,
        models.CapitalInvestRegionPage,
    ]
