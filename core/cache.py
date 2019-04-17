import abc
import hashlib

from rest_framework.renderers import JSONRenderer
from wagtail.core.signals import page_published, page_unpublished
from wagtail.core.models import Page

from django.conf import settings
from django.core.cache import cache
from django.db.models.signals import post_delete, post_save
from django.utils import translation
from django.utils.http import quote_etag

from core.serializer_mapping import MODELS_SERIALIZERS_MAPPING
from conf.celery import app


class PageCache:
    cache = cache

    @staticmethod
    def build_key(page_id, **variation_kwargs):
        # no matter the order of 'variation_kwargs', the same key/val
        # combinations should result in the same key
        variation_kwargs_sorted = sorted(
            item for item in variation_kwargs.items()
            if item[1]
        )
        # improve reliability of delete_many() by creating a redis hashtag,
        # from `page_id` - ensure keys related to the same page are stored
        # in the same node in a clustered environment
        hashtag_val = f'serialized-page-{page_id}'
        return '{{%s}}%s' % (hashtag_val, variation_kwargs_sorted)

    @classmethod
    def set(cls, page_id, data, **variation_kwargs):
        data['etag'] = cls.generate_etag(data)
        key = cls.build_key(page_id=page_id, **variation_kwargs)
        cls.cache.set(key, data, timeout=settings.API_CACHE_EXPIRE_SECONDS)

    @classmethod
    def get(cls, page_id, **variation_kwargs):
        key = cls.build_key(page_id=page_id, **variation_kwargs)
        return cls.cache.get(key)

    @classmethod
    def delete(cls, page_id, **variation_kwargs):
        key = cls.build_key(page_id=page_id, **variation_kwargs)
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
        cls.delete(instance)
        cls.populate.delay(instance.pk)

    @classmethod
    def populate_sync(cls, instance):
        serializer_class = MODELS_SERIALIZERS_MAPPING[instance.__class__]
        with PageCache.transaction() as page_cache:
            for language_code in instance.translated_languages:
                with translation.override(language_code):
                    serializer = serializer_class(instance=instance)
                    page_cache.set(
                        page_id=instance.id,
                        data=serializer.data,
                        lang=language_code,
                    )

    @classmethod
    def delete(cls, instance):
        with PageCache.transaction() as page_cache:
            for language_code in instance.translated_languages:
                page_cache.delete(
                    page_id=instance.id,
                    lang=language_code,
                )


class AbstractDatabaseCacheSubscriber(abc.ABC):

    cache_populator = CachePopulator

    def __init__(self):
        raise SystemError('This class cannot be instantiated.')

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
        cls.cache_populator.delete(instance)

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
        cls.delete(instance)
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
                            page_id=instance.id,
                            data=serializer.data,
                            lang=language_code,
                            region=region,
                        )


    @classmethod
    def delete(cls, instance):
        with PageCache.transaction() as page_cache:
            for language_code in instance.translated_languages:
                for region in cls.regions:
                    page_cache.delete(
                        page_id=instance.id,
                        lang=language_code,
                        region=region,
                    )


class PageIDCache:
    """
    Helps to efficiently map page slugs and url_path values to their
    respective page ids. Automatic repopulation on page data change
    means the cache is almost always hot. But, population itself is
    really quite efficient, due to only needing two values from the
    Page table to create lookup values.
    """
    cache = cache
    cache_key = 'page-ids'
    by_path_map_key = 'by-slug'
    by_slug_map_key = 'by-url_path'

    @staticmethod
    def build_slug_lookup_key(service_name_root_path, slug):
        return f'{service_name_root_path}:{slug}'

    @classmethod
    def get_population_queryset(cls):
        return Page.objects.values('id', 'slug', 'url_path')

    @classmethod
    def populate(cls, *args, **kwargs):
        ids_by_path = {}
        ids_by_slug = {}

        for page in cls.get_population_queryset():
            # url_path lookup keys are simple
            ids_by_path[page['url_path']] = page['id']
            # slug lookup keys must include the service name root path,
            # which is always the first portion of url_path (after
            # the first forward slash)
            slug_lookup_key = cls.build_slug_lookup_key(
                service_name_root_path=page['url_path'].split('/')[1],
                slug=page['slug'],
            )
            ids_by_slug[slug_lookup_key] = page['id']

        page_ids = {
            cls.by_path_map_key: ids_by_path,
            cls.by_slug_map_key: ids_by_slug,
        }
        cls.cache.set(cls.cache_key, page_ids, timeout=settings.API_CACHE_EXPIRE_SECONDS) # noqa
        return page_ids

    @classmethod
    def clear(cls, *args, **kwargs):
        return cls.cache.delete(cls.cache_key)

    @classmethod
    def get(cls, populate_if_cold=False):
        result = cls.cache.get(cls.cache_key)
        if result is not None:
            return result
        if populate_if_cold:
            return cls.populate()

    @classmethod
    def get_mapping(cls, map_key):
        return cls.populate(populate_if_cold=True)[map_key]

    @classmethod
    def get_for_slug(cls, service_name_root_path, slug):
        lookup_key = cls.build_slug_lookup_key(service_name_root_path, slug)
        return cls.get_mapping(cls.by_slug_map_key).get(lookup_key)

    @classmethod
    def get_for_path(cls, path):
        return cls.get_mapping(cls.by_path_map_key).get(path)

    @classmethod
    def subscribe_to_signals(cls):
        post_save.connect(receiver=cls.populate, sender=Page)
        post_delete.connect(receiver=cls.populate, sender=Page)
