from functools import partial, reduce
import hashlib
from urllib.parse import urljoin, urlencode

from modeltranslation.translator import translator
from modeltranslation.utils import build_localized_fieldname
from wagtail.wagtailcore.models import Page

from django.core import signing
from django.conf import settings
from django.db import models
from django.shortcuts import redirect
from django.utils import translation

from core import constants


class BasePage(Page):

    class Meta:
        abstract = True

    subpage_types = []

    def __init__(self, *args, **kwargs):
        self.signer = signing.Signer()
        super().__init__(*args, **kwargs)

    def get_draft_token(self):
        return self.signer.sign(self.pk)

    def is_draft_token_valid(self, draft_token):
        try:
            value = self.signer.unsign(draft_token)
        except signing.BadSignature:
            return False
        else:
            return str(self.pk) == str(value)

    def get_url_path_parts(self, language_code):
        slug_fieldname = build_localized_fieldname('slug', lang=language_code)
        slug = getattr(self, slug_fieldname) or self.slug_en_gb
        return [self.view_path, str(self.pk) + '/', slug + '/']

    def get_url(self, is_draft=False, language_code=settings.LANGUAGE_CODE):
        domain = dict(constants.APP_URLS)[self.view_app]
        url_path_parts = self.get_url_path_parts(language_code=language_code)
        url = reduce(urljoin, [domain] + url_path_parts)
        querystring = {}
        if is_draft:
            querystring['draft_token'] = self.get_draft_token()
        if language_code != settings.LANGUAGE_CODE:
            querystring['lang'] = language_code
        if querystring:
            url += '?' + urlencode(querystring)
        return url

    def get_localized_urls(self):
        # localized urls are used to tell google of alternative urls for
        # available languages, so there should be no need to expose the draft
        # url
        return [
            (language_code, self.get_url(language_code=language_code))
            for language_code in self.translated_languages
        ]

    def serve(self, request, *args, **kwargs):
        return redirect(self.get_url())

    def get_latest_nested_revision_as_page(self):
        revision = self.get_latest_revision_as_page()
        foreign_key_names = [
            field.name for field in revision._meta.get_fields()
            if isinstance(field, models.ForeignKey)
        ]
        for name in foreign_key_names:
            field = getattr(revision, name)
            if hasattr(field, 'get_latest_revision_as_page'):
                setattr(revision, name, field.get_latest_revision_as_page())
        return revision

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
        names = cls.get_translatable_fields()
        return [name for name in names if not cls._meta.get_field(name).blank]

    @property
    def translated_languages(self):
        fields = self.get_required_translatable_fields()
        language_codes = translation.trans_real.get_languages()
        translated_languages = []
        for language_code in language_codes:
            builder = partial(build_localized_fieldname, lang=language_code)
            if all(getattr(self, builder(name)) for name in fields):
                translated_languages.append(language_code)
        return translated_languages


class ImageHash(models.Model):

    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name='+'
    )
    content_hash = models.CharField(
        max_length=1000
    )

    @staticmethod
    def generate_content_hash(file):
        filehash = hashlib.md5()
        filehash.update(file.read())
        return filehash.hexdigest()


class ExcludeivePageMixin:
    @classmethod
    def can_create_at(cls, parent):
        return super().can_create_at(parent) and not cls.objects.exists()
