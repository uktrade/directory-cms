from django.apps import AppConfig


class GreatInternationalConfig(AppConfig):
    name = 'great_international'

    def ready(self):
        from core.cache import DatabaseCacheSubscriber, RegionAwareDatabaseCacheSubscriber
        from great_international import cache

        for subscriber in cache.subscribers:
            subscriber.subscribe()