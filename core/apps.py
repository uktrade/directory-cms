from django.apps import AppConfig
from django.db.models.signals import post_save


class CoreConfig(AppConfig):
    name = 'core'

    def ready(self):
        from core import models, signals
        from core.cache import PageIDCache, DatabaseCacheSubscriber

        post_save.connect(
            receiver=signals.create_image_hash,
            sender='wagtailimages.Image'
        )
        post_save.connect(
            receiver=signals.create_document_hash,
            sender='wagtaildocs.Document'
        )
        PageIDCache.subscribe()
        DatabaseCacheSubscriber.subscribe()
        models.BasePage.fix_base_form_class_monkeypatch()
