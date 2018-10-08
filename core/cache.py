import abc

from django.core.cache import cache
from wagtail.core.signals import page_published, page_unpublished
from django.urls import reverse

import requests

from django.test import Client
from django.utils import translation


class PageCache:
    cache = cache

    @staticmethod
    def build_key(slug, service_name, language_code):
        key = reverse('lookup-by-slug', kwargs={'slug': slug})
        if language_code or service_name:
            key += '?'
        if language_code:
            key += f'lang={language_code}&'
        if service_name:
            key += f'service_name={service_name}&'
        return key

    @classmethod
    def set(cls, slug, service_name, contents, language_code=None):
        key = cls.build_key(
            slug=slug, service_name=service_name, language_code=language_code
        )
        cls.cache.set(key, contents)

    @classmethod
    def get(cls, slug, service_name, language_code=None):
        key = cls.build_key(
            slug=slug, service_name=service_name, language_code=language_code
        )
        return cls.cache.get(key)

    @classmethod
    def delete(cls, instance):
        keys = [
            cls.build_key(
                slug=instance.slug,
                service_name=instance.service_name,
                language_code=None,
            )
        ]
        for language_code in instance.translated_languages:
            keys.append(cls.build_key(
                slug=instance.slug,
                service_name=instance.service_name,
                language_code=language_code,
            ))
        cls.cache.delete_many(keys)


class CachePopulator:
    # drafts will not be cached. This is as per design
    client = Client()

    @classmethod
    def populate(cls, page_cache, instance):
        page_cache.delete(instance)
        url = reverse('lookup-by-slug', kwargs={'slug': instance.slug})
        for language_code in instance.translated_languages:
            with translation.override(language_code):
                cls.client.get(url, {'service_name': instance.service_name})


class CacheDatabaseSubscriber(abc.ABC):
    cache_populator = CachePopulator
    page_cache = PageCache

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
            page_published.connect(
                receiver=cls.populate_many,
                sender=model,
                dispatch_uid=f'{cls.model.__name__}-{model.__name__}',
            )
            page_unpublished.connect(
                receiver=cls.delete_many,
                sender=model,
                dispatch_uid=f'{cls.model.__name__}-{model.__name__}',
            )

    @classmethod
    def populate(cls, sender, instance, *args, **kwargs):
        cls.cache_populator.populate(
            page_cache=cls.page_cache, instance=instance
        )

    @classmethod
    def delete(cls, sender, instance, *args, **kwargs):
        cls.cache_populator.page_cache.delete(instance)

    @classmethod
    def populate_many(cls, sender, instance, *args, **kwargs):
        for instance in cls.model.objects.all():
            cls.populate(
                page_cache=cls.page_cache, instance=instance
            )

    @classmethod
    def delete_many(cls, sender, instance, *args, **kwargs):
        for instance in cls.model.objects.all():
            cls.page_cache.delete(instance)
