from functools import partial

from modeltranslation.translator import translator
from modeltranslation.utils import build_localized_fieldname
from wagtail.core.models import Page

from django.core.exceptions import ValidationError
from django.db import transaction
from django.utils import translation

from core import constants
from django.conf import settings


class ServiceNameUniqueSlugMixin:

    @staticmethod
    def _slug_is_available(slug, parent, page=None):
        from core import filters  # circular dependencies
        queryset = filters.ServiceNameFilter().filter_service_name(
            queryset=Page.objects.filter(slug=slug).exclude(pk=page.pk),
            name=None,
            value=page.service_name,
        )
        return not queryset.exists()

    @transaction.atomic
    def save(self, *args, **kwargs):
        self.service_name = self.service_name_value
        if not self._slug_is_available(
            slug=self.slug,
            parent=self.get_parent(),
            page=self
        ):
            raise ValidationError({'slug': 'This slug is already in use'})
        return super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        """
        NOTE: This override should probably be removed

        We need to override delete to use the Page's parent one.

        Using the Page one would cause the original _slug_is_available method
        to be called and that is not considering services
        """
        super(Page, self).delete(*args, **kwargs)


class ModeltranslationPageMixin:

    @classmethod
    def get_translatable_fields(cls):
        return list(translator.get_options_for_model(cls).fields.keys())

    @classmethod
    def get_translatable_string_fields(cls):
        text_fields = ['TextField', 'CharField']
        return [
            name for name in cls.get_translatable_fields()
            if cls._meta.get_field(name).get_internal_type() in text_fields
        ]

    @classmethod
    def get_required_translatable_fields(cls):
        fields = [
            cls._meta.get_field(name) for name in cls.get_translatable_fields()
        ]
        return [
            field.name for field in fields
            if not field.blank and field.model is cls
        ]

    @property
    def translated_languages(self):
        fields = self.get_required_translatable_fields()
        if not fields:
            return [settings.LANGUAGE_CODE]
        language_codes = translation.trans_real.get_languages()
        # If new mandatory fields are added to a page model which has existing
        # instances on wagtail admin, the code below returns an empty list
        # because not all the mandatory fields are populated with English
        # content. An empty list means that the UI client will return a 404
        # because it can't find English, although the page is valid and still
        # published in CMS. I'm forcing en-gb in the list to avoid this issue.
        # This is diffucult to test both programmatically and manually and it's
        # a corner case so I'm leaving the next line effectively untested.
        # A manual test would have the following steps:
        # 1) Add a page model
        # 2) Create an instance of the above page model in wagtail
        # 3) Add at least one new mandatory field to the model
        # 4) Migrate CMS
        # 5) Open the page on the UI client without adding the new content
        translated_languages = ['en-gb']
        for language_code in language_codes:
            builder = partial(build_localized_fieldname, lang=language_code)
            if all(getattr(self, builder(field_name=name)) for name in fields):
                translated_languages.append(language_code)
                # cast to a set to remove double en-gb if any
        return list(set(translated_languages))

    @property
    def language_names(self):
        if len(self.translated_languages) > 1:
            names = [
                label for code, label, _ in settings.LANGUAGES_DETAILS
                if code in self.translated_languages
                and code != settings.LANGUAGE_CODE
            ]
            return 'Translated to {}'.format(', '.join(names))
        return ''

    def get_localized_urls(self):
        # localized urls are used to tell google of alternative urls for
        # available languages, so there should be no need to expose the draft
        # url
        return [
            (language_code, self.get_url(language_code=language_code))
            for language_code in self.translated_languages
        ]


class ServiceHomepageMixin:
    full_path = '/'

    @property
    def full_url(self):
        return dict(constants.APP_URLS)[self.service_name_value]
