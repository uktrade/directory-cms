from django.apps import AppConfig


class ComponentsConfig(AppConfig):
    name = 'components'

    def ready(self):
        from components import cache
        cache.BannerComponentSubscriber.subscribe()
