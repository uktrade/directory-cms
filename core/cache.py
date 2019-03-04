import abc
import hashlib
from urllib.parse import urlencode

from rest_framework.renderers import JSONRenderer
from w3lib.url import canonicalize_url
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


class PageCache:
    cache = cache

    @staticmethod
    def build_key(slug, params):
        url = reverse('api:lookup-by-slug', kwargs={'slug': slug})
        params = {key: value for key, value in params.items() if value}
        # using the page slug as a redis hash tag ensures the keys related to
        # the same page in the same node, preventing delete_many from failing
        # because the keys could be stored across different nodes
        return f'{{slug}}' + canonicalize_url(url + '?' + urlencode(params))

    @classmethod
    def set(cls, slug, params, data):
        data['etag'] = cls.generate_etag(data)
        key = cls.build_key(slug=slug, params=params)
        cls.cache.set(key, data, timeout=settings.API_CACHE_EXPIRE_SECONDS)

    @classmethod
    def get(cls, slug, params):
        key = cls.build_key(slug=slug, params=params)
        return cls.cache.get(key)

    @classmethod
    def delete(cls, slug, params):
        key = cls.build_key(slug=slug, params=params)
        cls.cache.delete(key)

    @staticmethod
    def generate_etag(data):
        json_data = JSONRenderer().render(data)
        return quote_etag(hashlib.md5(json_data).hexdigest())

    @classmethod
    def transaction(cls):
        class Transaction(cls):
            cache = TransactionalCache()

            def __enter__(self):
                return self

            def __exit__(self, *args):
                self.cache.commit()

        return Transaction()


class TransactionalCache:
    """
    Like `django.core.cache.cache`, but it buffers operations to be
    committed in a single transaction.
    """

    cache = cache

    def __init__(self, *args, **kwargs):
        self.transaction_set = {}
        self.transaction_delete = []
        super().__init__(*args, **kwargs)

    def set(self, key, data, timeout):
        self.transaction_set[key] = data

    def delete(self, key):
        self.transaction_delete.append(key)

    def commit(self):
        self.cache.delete_many(self.transaction_delete)
        self.cache.set_many(
            self.transaction_set, timeout=settings.API_CACHE_EXPIRE_SECONDS
        )


class CachePopulator:

    @staticmethod
    @app.task
    def populate(instance_pk):
        instance = Page.objects.get(pk=instance_pk).specific
        CachePopulator.populate_sync(instance)

    @classmethod
    def populate_async(cls, instance):
        with PageCache.transaction() as page_cache:
            for language_code in instance.translated_languages:
                page_cache.delete(
                    slug=instance.slug,
                    params={
                        'service_name': instance.service_name,
                        'lang': language_code
                    }
                )
        cls.populate.delay(instance.pk)

    @classmethod
    def populate_sync(cls, instance):
        serializer_class = MODELS_SERIALIZERS_MAPPING[instance.__class__]
        with PageCache.transaction() as page_cache:
            for language_code in instance.translated_languages:
                with translation.override(language_code):
                    serializer = serializer_class(instance=instance)
                    page_cache.set(
                        slug=instance.slug,
                        params={
                            'lang': language_code,
                            'service_name': instance.service_name,
                        },
                        data=serializer.data,
                    )


class AbstractDatabaseCacheSubscriber(abc.ABC):

    cache_populator = CachePopulator

    @property
    @abc.abstractmethod
    def model(self):
        return  # pragma: no cover

    @property
    @abc.abstractmethod
    def subscriptions(self):
        return []  # pragma: no cover

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
        cls.cache_populator.populate_async(instance)

    @classmethod
    def delete(cls, sender, instance, *args, **kwargs):
        with PageCache.transaction() as page_cache:
            for lang in instance.translated_languages:
                page_cache.delete(
                    slug=instance.slug,
                    params={
                        'lang': lang,
                        'service_name': instance.service_name,
                    }
                )

    @classmethod
    def populate_many(cls, sender, instance, *args, **kwargs):
        for related_instance in cls.model.objects.filter(live=True):
            cls.cache_populator.populate_async(related_instance)


class RegionAwareCachePopulator(CachePopulator):
    regions = ['eu', 'not-eu']

    @staticmethod
    @app.task(name='region-aware-populate')
    def populate(instance_pk):
        instance = Page.objects.get(pk=instance_pk).specific
        RegionAwareCachePopulator.populate_sync(instance)

    @classmethod
    def populate_async(cls, instance):
        with PageCache.transaction() as page_cache:
            for language_code in instance.translated_languages:
                for region in cls.regions:
                    page_cache.delete(
                        slug=instance.slug,
                        params={
                            'service_name': instance.service_name,
                            'lang': language_code,
                            'region': region,
                        }
                    )
        cls.populate.delay(instance.pk)

    @classmethod
    def populate_sync(cls, instance):
        serializer_class = MODELS_SERIALIZERS_MAPPING[instance.__class__]
        with PageCache.transaction() as page_cache:
            for language_code in instance.translated_languages:
                with translation.override(language_code):
                    for region in cls.regions:
                        serializer = serializer_class(
                            instance=instance,
                            context={'region': region}
                        )
                        page_cache.set(
                            slug=instance.slug,
                            params={
                                'lang': language_code,
                                'service_name': instance.service_name,
                                'region': region,
                            },
                            data=serializer.data,
                        )
