import hashlib
import itertools
from urllib.parse import urlencode

from directory_constants import cms, slugs
from rest_framework.renderers import JSONRenderer
from wagtail.signals import page_published, page_unpublished
from wagtail.models import Page, Site

from django.conf import settings
from django.core.cache import cache
from django.db.models.signals import post_delete, post_migrate, post_save
from django.utils import translation
from django.utils.http import quote_etag

from core.serializer_mapping import MODELS_SERIALIZERS_MAPPING
from conf.celery import app


ROOT_PATHS_TO_SERVICE_NAMES = {
    slugs.GREAT_HOME: cms.EXPORT_READINESS,
    slugs.GREAT_HOME_INTERNATIONAL: cms.GREAT_INTERNATIONAL,
    'components-app': cms.COMPONENTS,
}

SERVICE_NAMES_TO_ROOT_PATHS = {value: key for key, value in ROOT_PATHS_TO_SERVICE_NAMES.items()}


class PageCache:
    cache = cache

    @staticmethod
    def build_key(page_id, **variation_kwargs):
        """
        Return a string from the supplied arguments that is suitable for use
        as a cache key.
        """
        variation_kwargs_sorted = sorted(
            item for item in variation_kwargs.items()
            if item[1]
        )

        return 'serialized-page-{page_id}:{varation_kwargs_encoded}'.format(
            page_id=page_id,
            varation_kwargs_encoded=urlencode(variation_kwargs_sorted)
        )

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
        if instance.__class__ in MODELS_SERIALIZERS_MAPPING and instance.__class__ is not Page:
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
                    if instance.has_unpublished_changes:
                        draft_instance = instance.get_latest_nested_revision_as_page()
                        draft_serializer = serializer_class(
                            instance=draft_instance,
                            context={'is_draft': True}
                        )
                        page_cache.set(
                            page_id=instance.id,
                            data=draft_serializer.data,
                            lang=language_code,
                            draft_version=True
                        )

    @classmethod
    def delete(cls, instance):
        with PageCache.transaction() as page_cache:
            for language_code in instance.translated_languages:
                page_cache.delete(
                    page_id=instance.id,
                    lang=language_code,
                )
                page_cache.delete(
                    page_id=instance.id,
                    lang=language_code,
                    draft_version=True
                )


class PageIDCache:
    """
    Helps to efficiently map page slugs and path values to their respective
    page ids.

    Population happens on request. Invalidation happens automatically when
    page or site data changes, but those actions do not trigger
    repopulation.

    Population is efficient due to only needing to query the database for
    vanilla `Page` objects with a small subset of fields. Site data almost
    always comes from a cache, and content type data (if needed) is typically
    cached also.
    """
    cache = cache
    cache_key = 'page-ids'
    by_path_map_key = 'by-path'
    by_slug_map_key = 'by-slug'

    @staticmethod
    def build_slug_lookup_key(service_name, slug):
        return f'{service_name}:{slug}'

    @staticmethod
    def build_path_lookup_key(site_id, path):
        path = path.strip('/')
        if not path.endswith('/'):
            path = f'{path}/'
        if not path.startswith('/'):
            path = f'/{path}'
        return f'{site_id}:{path}'

    @staticmethod
    def get_service_name_for_page(page):
        try:
            # This works for all pages in practice, because pages always
            # live below an 'app' root page, and so always have a predictable
            # segment at the start of their url_path
            root_path = page.url_path.split('/')[1]
            return ROOT_PATHS_TO_SERVICE_NAMES[root_path]
        except KeyError:
            # In tests, pages are often added as direct children of the root
            # page node, so the above won't work. Instead, we fetch the model
            # for the page from its content type, and get the value from there
            return getattr(page.specific_class, 'service_name_value', None)

    @classmethod
    def get_population_queryset(cls):
        return Page.objects.only('id', 'slug', 'url_path', 'content_type_id')

    @classmethod
    def populate(cls, *args, **kwargs):
        ids_by_path = {}
        ids_by_slug = {}

        # This value should be cached by Wagtail
        site_root_paths = Site.get_site_root_paths()
        for page in cls.get_population_queryset():
            # Path lookup keys must include the site id and url_path, minus
            # the site root path, which Page.get_url_parts() can give us

            # setting this prevents repeat cache lookups
            page._wagtail_cached_site_root_paths = site_root_paths
            url_parts = page.get_url_parts()
            if url_parts:
                key = cls.build_path_lookup_key(url_parts[0], url_parts[2])
                ids_by_path[key] = page.id

            # Slug lookup keys must include the service name, as well as the
            # slug, which we need to work out
            service_name = cls.get_service_name_for_page(page)
            if service_name:
                key = cls.build_slug_lookup_key(service_name, page.slug)
                ids_by_slug[key] = page.id

        page_ids = {
            cls.by_path_map_key: ids_by_path,
            cls.by_slug_map_key: ids_by_slug,
        }
        cls.cache.set(cls.cache_key, page_ids, timeout=settings.API_CACHE_EXPIRE_SECONDS)
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
    def get_for_slug(cls, slug, service_name):
        key = cls.build_slug_lookup_key(service_name, slug)
        return cls.get_mapping(cls.by_slug_map_key).get(key)

    @classmethod
    def get_for_path(cls, path, site_id):
        key = cls.build_path_lookup_key(site_id, path)
        return cls.get_mapping(cls.by_path_map_key).get(key)

    @classmethod
    def subscribe(cls):
        post_save.connect(receiver=cls.clear, sender=Page)
        post_delete.connect(receiver=cls.clear, sender=Page)
        post_save.connect(receiver=cls.clear, sender=Site)
        post_delete.connect(receiver=cls.clear, sender=Site)
        post_migrate.connect(receiver=cls.clear)


class MarketPagesCache:
    cache = cache

    @staticmethod
    def build_key(region, industry):
        return f'countryguide_{region}{industry}'

    @classmethod
    def set(cls, data, region=None, industry=None,):
        key = cls.build_key(region=region, industry=industry)
        cls.cache.set(key, data, timeout=settings.API_CACHE_EXPIRE_SECONDS)

    @classmethod
    def get_many(cls, industries=[None], countries=[None]):
        keys = [cls.build_key(*args) for args in itertools.product(countries, industries)]
        pages = {}
        # making the values returned distinct
        for records in cls.cache.get_many(keys).values():
            for record in records:
                pages[record['id']] = record

        return list(pages.values())

    @classmethod
    def transaction(cls):
        class Transaction(cls):
            cache = TransactionalCache()

            def __enter__(self):
                return self

            def __exit__(self, *args):
                self.cache.commit()

        return Transaction()


class DatabaseCacheSubscriber:

    cache_populator = CachePopulator
    model_classes = MODELS_SERIALIZERS_MAPPING.keys()

    @classmethod
    def subscribe(cls):
        for model_class in cls.model_classes:
            page_published.connect(
                receiver=cls.populate,
                sender=model_class,
                dispatch_uid=model_class.__name__,
            )
            page_unpublished.connect(
                receiver=cls.delete,
                sender=model_class,
                dispatch_uid=model_class.__name__,
            )

    @classmethod
    def populate(cls, sender, instance, *args, **kwargs):
        cls.cache_populator.populate_async(instance)

    @classmethod
    def delete(cls, sender, instance, *args, **kwargs):
        cls.cache_populator.delete(instance)


@app.task
def rebuild_all_cache():
    for page in Page.objects.live().specific():
        CachePopulator.populate_async(page)

