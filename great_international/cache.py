from core.cache import AbstractDatabaseCacheSubscriber

from great_international import models


class InternationalHomePageSubscriber(AbstractDatabaseCacheSubscriber):
    model = models.InternationalHomePage
    subscriptions = [
        models.InternationalArticlePage,
        models.InternationalMarketingPages
    ]


class InternationalMarketingPagesSubscriber(AbstractDatabaseCacheSubscriber):
    model = models.InternationalMarketingPages
    subscriptions = [
        models.InternationalArticlePage,
        models.InternationalCampaignPage
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
    model = models.InternationalArticleListingPage
    subscriptions = [
        models.InternationalArticlePage
    ]
