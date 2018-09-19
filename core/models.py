from functools import partial, reduce
import hashlib
from urllib.parse import urljoin, urlencode

from directory_constants.constants import choices
from django.core.exceptions import ValidationError
from modeltranslation import settings as modeltranslation_settings
from modeltranslation.translator import translator
from modeltranslation.utils import build_localized_fieldname
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.core.models import Page

from django.core import signing
from django.conf import settings
from django.contrib.contenttypes.fields import (
    GenericForeignKey, GenericRelation
)
from django.contrib.contenttypes.models import ContentType
from django.contrib.postgres.fields import ArrayField
from django.db import models
from django.db import transaction
from django.forms import MultipleChoiceField
from django.shortcuts import redirect
from django.template.loader import render_to_string
from django.utils import translation
from django.utils.text import mark_safe
from core import constants, forms


class Breadcrumb(models.Model):
    service_name = models.CharField(
        max_length=50,
        choices=choices.CMS_APP_CHOICES,
        null=True,
        db_index=True
    )
    label = models.CharField(max_length=50)
    slug = models.SlugField()

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    page = GenericForeignKey('content_type', 'object_id')


class ChoiceArrayField(ArrayField):

    def formfield(self, **kwargs):
        defaults = {
            'form_class': MultipleChoiceField,
            'choices': self.base_field.choices,
        }
        defaults.update(kwargs)
        return super(ArrayField, self).formfield(**defaults)


class BasePage(Page):
    service_name = models.CharField(
        max_length=100,
        choices=choices.CMS_APP_CHOICES,
        db_index=True,
        null=True,
    )

    class Meta:
        abstract = True

    subpage_types = []
    base_form_class = forms.WagtailAdminPageForm
    content_panels = []
    promote_panels = []
    read_only_fields = []

    def __init__(self, *args, **kwargs):
        self.signer = signing.Signer()
        #  workaround modeltranslation patching Page.clean in an unpythonic way
        #  goo.gl/yYD4pw
        self.clean = lambda: None
        super().__init__(*args, **kwargs)

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
        """We need to override delete to use the Page's parent one.

        Using the Page one would cause the original _slug_is_available method
        to be called and that is not considering services
        """
        super(Page, self).delete(*args, **kwargs)

    @staticmethod
    def _slug_is_available(slug, parent, page=None):
        from core import filters  # circular dependencies
        queryset = filters.ServiceNameFilter().filter_service_name(
            queryset=Page.objects.filter(slug=slug).exclude(pk=page.pk),
            name=None,
            value=page.service_name,
        )
        is_unique_in_service = (queryset.count() == 0)
        return is_unique_in_service

    def get_draft_token(self):
        return self.signer.sign(self.pk)

    def is_draft_token_valid(self, draft_token):
        try:
            value = self.signer.unsign(draft_token)
        except signing.BadSignature:
            return False
        else:
            return str(self.pk) == str(value)

    def get_url_path_parts(self):
        return [self.view_path, self.slug + '/']

    def get_url(self, is_draft=False, language_code=settings.LANGUAGE_CODE):
        domain = dict(constants.APP_URLS)[self.service_name_value]
        url_path_parts = self.get_url_path_parts()
        url = reduce(urljoin, [domain] + url_path_parts)
        querystring = {}
        if is_draft:
            querystring['draft_token'] = self.get_draft_token()
        if language_code != settings.LANGUAGE_CODE:
            querystring['lang'] = language_code
        if querystring:
            url += '?' + urlencode(querystring)
        return urlencode

    @property
    def full_path(self):
        """Return the full path of a page, ignoring the root_page and
        the app page. Used by the lookup-by-url view in prototype mode
        """
        # starts from 2 to remove root page and app page
        path_components = [page.slug for page in self.get_ancestors()[2:]]
        path_components.append(self.slug)
        return '{path}/'.format(path='/'.join(path_components))

    @property
    def url(self):
        return self.get_url()

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
            return []
        language_codes = translation.trans_real.get_languages()
        translated_languages = []
        for language_code in language_codes:
            builder = partial(build_localized_fieldname, lang=language_code)
            if all(getattr(self, builder(name)) for name in fields):
                translated_languages.append(language_code)
        return translated_languages

    def get_admin_display_title(self):
        translated_languages = self.translated_languages
        language_names = [
            label for code, label, _ in settings.LANGUAGES_DETAILS
            if code in translated_languages
            and code != settings.LANGUAGE_CODE
        ]
        display_title = render_to_string('core/admin_display_title.html', {
            'language_names': language_names,
            'cms_page_title': super().get_admin_display_title(),
        })
        return mark_safe(display_title)


class AbstractObjectHash(models.Model):
    class Meta:
        abstract = True

    content_hash = models.CharField(max_length=1000)

    @staticmethod
    def generate_content_hash(field_file):
        filehash = hashlib.md5()
        field_file.open()
        filehash.update(field_file.read())
        field_file.close()
        return filehash.hexdigest()


class DocumentHash(AbstractObjectHash):
    document = models.ForeignKey(
        'wagtaildocs.Document',
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name='+'
    )


class ImageHash(AbstractObjectHash):
    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name='+'
    )


class ExclusivePageMixin:
    read_only_fields = ['slug']
    base_form_class = forms.WagtailAdminPageExclusivePageForm

    @classmethod
    def can_create_at(cls, parent):
        return super().can_create_at(parent) and not cls.objects.exists()

    def save(self, *args, **kwargs):
        if not self.pk and hasattr(self, 'slug_identity'):
            self.slug = self.slug_identity
        super().save(*args, **kwargs)

    def get_url_path_parts(self, *args, **kwargs):
        return [self.view_path]


class BreadcrumbMixin(models.Model):
    """Optimization for retrieving breadcrumbs that a service will display
    on a global navigation menu e.g., home > industry > contact us. Reduces SQL
    calls from >12 to 1 in APIBreadcrumbsSerializer compared with filtering
    Page and calling `specific()` and then retrieving the breadcrumbs labels.
    """

    class Meta:
        abstract = True

    breadcrumb = GenericRelation(Breadcrumb)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        defaults = {
            'service_name': self.service_name_value,
            'slug': self.slug,
        }
        if 'breadcrumb_label' in self.get_translatable_fields():
            for lang in modeltranslation_settings.AVAILABLE_LANGUAGES:
                localizer = partial(build_localized_fieldname, lang=lang)
                field_name = localizer('breadcrumbs_label')
                defaults[localizer('label')] = getattr(self, field_name, '')
        else:
            defaults['label'] = self.breadcrumbs_label
        self.breadcrumb.update_or_create(defaults=defaults)


class ServiceMixin(models.Model):
    service_name_value = None
    base_form_class = forms.BaseAppAdminPageForm
    view_path = ''

    class Meta:
        abstract = True

    @classmethod
    def allowed_subpage_models(cls):
        allowed_name = cls.service_name_value
        return [
            model for model in Page.allowed_subpage_models()
            if getattr(model, 'service_name_value', None) == allowed_name
        ]

    settings_panels = [
        FieldPanel('title_en_gb')
    ]
    content_panels = []
    promote_panels = []
