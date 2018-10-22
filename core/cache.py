import abc
from urllib.parse import urlencode
import logging

from wagtail.core.signals import page_unpublished
from sigauth.helpers import RequestSigner

from django.conf import settings
from django.core.cache import cache
from django.db.models.signals import post_save
from django.test import Client
from django.urls import reverse


logger = logging.getLogger(__name__)


PREPOPULATE_ERROR = 'Unable to populate the page cache'


class PageCache:
    cache = cache

    @staticmethod
    def build_key(slug, service_name, language_code):
        url = reverse('lookup-by-slug', kwargs={'slug': slug})
        params = {'service_name': service_name}
        if language_code:
            params['lang'] = language_code
        return url + '?' + urlencode(params)

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
    # drafts will not be cached. This is as per design
    client = Client()

    @classmethod
    def populate(cls, page_cache, instance):
        request_signer = RequestSigner(
            secret=settings.SIGNATURE_SECRET, sender_id='cache-populator'
        )
        url = reverse('lookup-by-slug', kwargs={'slug': instance.slug})

        page_cache.delete(
            slug=instance.slug,
            service_name=instance.service_name,
            language_codes=instance.translated_languages,
        )
        for language_code in instance.translated_languages:
            params = {
                'service_name': instance.service_name,
                'lang': language_code
            }
            signature_headers = request_signer.get_signature_headers(
                url=url + '?' + urlencode(params),
                body=None,
                method='GET',
                content_type='',
            )
            response = cls.client.get(
                url,
                params,
                HTTP_X_SIGNATURE=signature_headers[request_signer.header_name],
                CONTENT_TYPE='',
            )
            if not response.status_code == 200:
                logger.error(
                    PREPOPULATE_ERROR,
                    extra={'url': url, 'status_code': response.status_code},
                )


class AbstractDatabaseCacheSubscriber(abc.ABC):
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
        post_save.connect(
            receiver=cls.populate_if_live,
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
                receiver=cls.populate_many_if_live,
                sender=model,
                dispatch_uid=f'{cls.model.__name__}-{model.__name__}',
            )
            page_unpublished.connect(
                receiver=cls.populate_many_if_live,
                sender=model,
                dispatch_uid=f'{cls.model.__name__}-{model.__name__}',
            )

    @classmethod
    def populate_if_live(cls, sender, instance, *args, **kwargs):
        if instance.live:
            cls.cache_populator.populate(
                page_cache=cls.page_cache, instance=instance
            )

    @classmethod
    def delete(cls, sender, instance, *args, **kwargs):
        cls.page_cache.delete(
            slug=instance.slug,
            service_name=instance.service_name,
            language_codes=instance.translated_languages,
        )

    @classmethod
    def populate_many_if_live(cls, sender, instance, *args, **kwargs):
        for related_instance in cls.model.objects.filter(live=True):
            cls.cache_populator.populate(
                page_cache=cls.page_cache, instance=related_instance
            )


def is_registered_for_cache(model):
    models = [
        subscriber.model
        for subscriber in AbstractDatabaseCacheSubscriber.__subclasses__()
    ]
    return model in models
