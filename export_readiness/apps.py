from django.apps import AppConfig


class GreatDomesticConfig(AppConfig):
    name = 'export_readiness'

    def ready(self):
        from export_readiness import cache

        for subscriber in cache.subscribers:
            subscriber.subscribe()
