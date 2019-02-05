from core.cache import AbstractDatabaseCacheSubscriber

from great_international import models


class HomePageSubscriber(AbstractDatabaseCacheSubscriber):
    model = models.InternationalHomePage
    subscriptions = [
        models.InternationalArticlePage,
        models.InternationalMarketingPages
    ]


class MarketingPagesSubscriber(AbstractDatabaseCacheSubscriber):
    model = models.InternationalMarketingPages
    subscriptions = [
        models.InternationalArticlePage,
    ]


class ArticlePageSubscriber(AbstractDatabaseCacheSubscriber):
    model = models.InternationalArticlePage
    subscriptions = []
