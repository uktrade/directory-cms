from django.apps import AppConfig


class GreatInternationalConfig(AppConfig):
    name = 'great_international'

    def ready(self):
        from great_international import cache
        cache.HomePageSubscriber.subscribe()
