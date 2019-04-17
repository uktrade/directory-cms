from functools import partial
import hashlib
from urllib.parse import urlencode

from directory_constants.constants import choices
from django.core.exceptions import ValidationError
from modeltranslation import settings as modeltranslation_settings
from modeltranslation.translator import translator
from modeltranslation.utils import build_localized_fieldname
from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel
from wagtail.contrib.settings.models import BaseSetting, register_setting
from wagtail.core.models import Page, PageBase

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
from django.utils import translation

from core import constants, forms
from core.helpers import get_page_full_url
from core.wagtail_fields import FormHelpTextField, FormLabelField


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


@register_setting
class RoutingSettings(BaseSetting):
    root_path_prefix = models.CharField(
        blank=True,
        max_length=100,
        help_text=(
            "When determining URLs for a page in this site, the page's "
            "'url_path' is prepended with this value to create a URL that "
            "will be recognised by the relevant front-end app."
        ),
    )
    include_port_in_urls = models.BooleanField(
        default=True,
        verbose_name="include port in page URLs",
        help_text=(
            "This allows us to add dummy port values to Wagtail Site "
            "objects, to get around the unique hostname/port "
            "restrictions. If unchecked, the port won't be included "
            "in page URLs, and so becomes inconsequential."
        ),
    )

    panels = [
        MultiFieldPanel(
            heading="Routing configuration",
            children=[
                FieldPanel('root_path_prefix'),
                FieldPanel('include_port_in_urls'),
            ],
        )
    ]


class BasePage(Page):
    service_name = models.CharField(
        max_length=100,
        choices=choices.CMS_APP_CHOICES,
        db_index=True,
        null=True,
    )
    uses_tree_based_routing = models.BooleanField(
        default=False,
        verbose_name="tree-based routing enabled",
        help_text=(
            "Allow this page's URL to be determined by its slug, and "
            "the slugs of its ancestors in the page tree."
        ),
    )

    class Meta:
        abstract = True

    # URL fixes for legacy pages:
    # overrides the url path before the page slug is appended
    view_path = ''
    # overrides the entire url path including any custom slug the page has
    full_path_override = ''
    # if True when generating the url this page's slug will be ignored
    folder_page = False
    # overrides page.slug when generating the url
    slug_override = ''

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
        url = self.full_url
        querystring = {}
        if is_draft:
            querystring['draft_token'] = self.get_draft_token()
        if language_code != settings.LANGUAGE_CODE:
            querystring['lang'] = language_code
        if querystring:
            url += '?' + urlencode(querystring)
        return url

    @property
    def full_path(self):
        """Return the full path of a page, ignoring the root_page and
        the app page. Used by the lookup-by-url view in prototype mode
        """
        if self.full_path_override:
            return self.full_path_override

        path_components = []

        if not self.view_path:
            # starts from 2 to remove root page and app page
            path_components = [
                page.specific.slug_override or page.specific.slug
                for page in self.get_ancestors()[2:]
                if not page.specific.folder_page]

        # need to also take into account the view_path if it's set
        else:
            path_components.insert(0, self.view_path.replace('/', ''))

        path_components.append(self.slug_override or self.slug)

        return '/{path}/'.format(path='/'.join(path_components))

    @property
    def full_url(self):
        domain = dict(constants.APP_URLS)[self.service_name_value]
        return get_page_full_url(domain, self.full_path)

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
        return set(translated_languages)

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

    @classmethod
    def can_exist_under(cls, parent):
        if not parent.specific_class:
            return []
        return super().can_exist_under(parent)


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
    parent_page_types = ['wagtailcore.Page']

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


class FormPageMetaClass(PageBase):
    """Metaclass that adds <field_name>_label and <field_name>_help_text to a
    Page when given a list of form_field_names.
    """
    def __new__(mcls, name, bases, attrs):
        form_field_names = attrs['form_field_names']
        for field_name in form_field_names:
            attrs[field_name + '_help_text'] = FormHelpTextField()
            attrs[field_name + '_label'] = FormLabelField()

        form_panels = [
            MultiFieldPanel(
                heading=name.replace('_', ' '),
                children=[
                    FieldPanel(name + '_label'),
                    FieldPanel(name + '_help_text'),
                ]
            ) for name in form_field_names
        ]
        attrs['content_panels'] = (
            attrs['content_panels_before_form'] +
            form_panels +
            attrs['content_panels_after_form']
        )

        return super().__new__(mcls, name, bases, attrs)
