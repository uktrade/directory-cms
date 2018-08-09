from django.apps import AppConfig
from django.db.models.signals import post_save


class CoreConfig(AppConfig):
    name = 'core'

    def ready(self):
        from core import models, signals
        post_save.connect(
            receiver=signals.create_image_hash,
            sender='wagtailimages.Image'
        )

        for model_class in models.BasePage.__subclasses__():
            post_save.connect(
                receiver=signals.create_historic_slug,
                sender=model_class
            )
