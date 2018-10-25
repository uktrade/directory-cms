from core.cache import AbstractDatabaseCacheSubscriber

from components import models


class BannerComponentSubscriber(AbstractDatabaseCacheSubscriber):
    model = models.BannerComponent
    subscriptions = []
