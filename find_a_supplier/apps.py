from django.apps import AppConfig


class FindASupplierConfig(AppConfig):
    name = 'find_a_supplier'

    def ready(self):
        from find_a_supplier import cache
        cache.IndustryPageSubscriber.subscribe()
        cache.IndustryLandingPageSubscriber.subscribe()
        cache.IndustryArticlePageSubscriber.subscribe()
        cache.LandingPageSubscriber.subscribe()
        cache.IndustryContactPageSubscriber.subscribe()
