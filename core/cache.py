import abc
import hashlib
from urllib.parse import urlencode

from rest_framework.renderers import JSONRenderer
from wagtail.core.signals import page_published, page_unpublished
from wagtail.core.models import Page

from django.conf import settings
from django.core.cache import cache
from django.db.models.signals import post_save
from django.urls import reverse
from django.utils import translation
from django.utils.http import quote_etag

from core.serializer_mapping import MODELS_SERIALIZERS_MAPPING
from conf.celery import app


def generate_etag(instance):
    serializer_class = MODELS_SERIALIZERS_MAPPING[instance.__class__]
    serializer = serializer_class(instance=instance)
    json_data = JSONRenderer().render(serializer.data)
    return quote_etag(hashlib.md5(json_data).hexdigest())


class PageCache:
    cache = cache

    @staticmethod
    def build_key(slug, service_name, language_code):
        url = reverse('api:lookup-by-slug', kwargs={'slug': slug})
        params = {'service_name': service_name}
        if language_code:
            params['lang'] = language_code
        # using the page slug as a redis hash tag ensures the keys related to
        # the same page in the same node, preventing delete_many from failing
        # because the keys could be stored across different nodes
        node_prefix = f'{{slug}}'
        return node_prefix + url + '?' + urlencode(params)

    @classmethod
    def set(cls, slug, service_name, contents, language_code=None):
        key = cls.build_key(
            slug=slug, service_name=service_name, language_code=language_code
        )
        cls.cache.set(key, contents, timeout=settings.API_CACHE_EXPIRE_SECONDS)

    @classmethod
    def get(cls, slug, service_name, language_code=None):
        key = cls.build_key(
            slug=slug, service_name=service_name, language_code=language_code
        )
        return cls.cache.get(key)

    @classmethod
    def delete(cls, slug, service_name, language_codes):
        keys = [
            cls.build_key(
                slug=slug,
                service_name=service_name,
                language_code=None,
            )
        ]
        for language_code in language_codes:
            keys.append(cls.build_key(
                slug=slug,
                service_name=service_name,
                language_code=language_code,
            ))
        cls.cache.delete_many(keys)


class CachePopulator:

    @classmethod
    def populate_async(cls, instance):
        PageCache.delete(
            slug=instance.slug,
            service_name=instance.service_name,
            language_codes=instance.translated_languages,
        )
        cls.populate.delay(instance.pk)

    @staticmethod
    @app.task
    def populate(instance_pk):
        instance = Page.objects.get(pk=instance_pk).specific
        serializer_class = MODELS_SERIALIZERS_MAPPING[instance.__class__]
        for language_code in instance.translated_languages:
            with translation.override(language_code):
                serializer = serializer_class(instance=instance)
                PageCache.set(
                    slug=instance.slug,
                    language_code=language_code,
                    service_name=instance.service_name,
                    contents={
                        **serializer.data, 'etag': generate_etag(instance)
                    }
                )


class AbstractDatabaseCacheSubscriber(abc.ABC):

    @property
    @abc.abstractmethod
    def model(self):
        return

    @property
    @abc.abstractmethod
    def subscriptions(self):
        return []

    @classmethod
    def subscribe(cls):
        page_published.connect(
            receiver=cls.populate,
            sender=cls.model,
            dispatch_uid=cls.model.__name__,
        )
        page_unpublished.connect(
            receiver=cls.delete,
            sender=cls.model,
            dispatch_uid=cls.model.__name__,
        )
        for model in cls.subscriptions:
            post_save.connect(
                receiver=cls.populate_many,
                sender=model,
                dispatch_uid=f'{cls.model.__name__}-{model.__name__}',
            )
            page_unpublished.connect(
                receiver=cls.populate_many,
                sender=model,
                dispatch_uid=f'{cls.model.__name__}-{model.__name__}',
            )

    @classmethod
    def populate(cls, sender, instance, *args, **kwargs):
        CachePopulator.populate_async(instance)

    @classmethod
    def delete(cls, sender, instance, *args, **kwargs):
        PageCache.delete(
            slug=instance.slug,
            service_name=instance.service_name,
            language_codes=instance.translated_languages,
        )

    @classmethod
    def populate_many(cls, sender, instance, *args, **kwargs):
        for related_instance in cls.model.objects.filter(live=True):
            CachePopulator.populate_async(related_instance)
