from functools import partial
import hashlib
import mimetypes
from urllib.parse import urlencode, urljoin

from directory_constants import choices

from modeltranslation import settings as modeltranslation_settings
from modeltranslation.utils import build_localized_fieldname
from modeltranslation.translator import translator
from wagtail.admin.panels import FieldPanel, MultiFieldPanel
from wagtail.contrib.settings.models import BaseSiteSetting, register_setting
from wagtail.models import Page, PageBase, Site

from django.core import signing
from django.conf import settings
from django.contrib.contenttypes.fields import (
    GenericForeignKey, GenericRelation
)
from django.contrib.contenttypes.models import ContentType
from django.db import models, transaction
from django.shortcuts import redirect
from django.utils import translation

from core import constants, forms
from core.helpers import get_page_full_url
from core.wagtail_fields import FormHelpTextField, FormLabelField
from wagtailmedia.models import Media
from django.utils.translation import ugettext_lazy as _
from django.urls import reverse


class GreatMedia(Media):

    transcript = models.TextField(
        verbose_name=_('Transcript'), blank=True, null=True  # left null because was an existing field
    )

    subtitles_en = models.TextField(
        verbose_name=_('English subtitles'),
        null=True,
        blank=True,
        help_text='English-language subtitles for this video, in VTT format',
    )

    admin_form_fields = Media.admin_form_fields + (
        'transcript',
        'subtitles_en',
    )

    @property
    def sources(self):
        return [
            {
                'src': self.url,
                'type': mimetypes.guess_type(self.filename)[0] or 'application/octet-stream',
                'transcript': self.transcript,
            }
        ]

    @property
    def subtitles(self):
        output = []
        # TO COME: support for more than just English
        if self.subtitles_en:
            output.append(
                {
                    'srclang': 'en',
                    'label': 'English',
                    'url': reverse('subtitles-serve', args=[self.id, 'en']),
                    'default': False,
                },
            )
        return output


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


@register_setting
class RoutingSettings(BaseSiteSetting):
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
    slug_override = None

    subpage_types = []
    content_panels = []
    promote_panels = []
    read_only_fields = []

    _base_form_class = forms.WagtailAdminPageForm

    def __init__(self, *args, **kwargs):
        self.signer = signing.Signer()
        #  workaround modeltranslation patching Page.clean in an unpythonic way
        #  goo.gl/yYD4pw
        self.clean = lambda: None
        super().__init__(*args, **kwargs)

    @classmethod
    def get_subclasses(cls):
        for subclass in cls.__subclasses__():
            yield from subclass.get_subclasses()
            yield subclass

    @classmethod
    def fix_base_form_class_monkeypatch(cls):
        # workaround modeltranslation patching Page.base_form_class in an unpythonic way
        for model in cls.get_subclasses():
            base_form_class = getattr(model, '_base_form_class')
            setattr(model, 'base_form_class', base_form_class)

    @transaction.atomic
    def save(self, *args, **kwargs):
        self.service_name = self.service_name_value
        return super().save(*args, **kwargs)

    def get_draft_token(self):
        return self.signer.sign(self.pk)

    def is_draft_token_valid(self, draft_token):
        try:
            value = self.signer.unsign(draft_token)
        except signing.BadSignature:
            return False
        else:
            return str(self.pk) == str(value)

    def get_non_prefixed_url(self, site=None):
        """
        Returns the page's url_path value with the url_path of the
        site's root page removed from the start, and starting with
        a forward slash. e.g. "/international/some-some-page".
        Used by get_tree_based_url() and for generating `old_path`
        values when creating redirects for this page
        """
        site = site or self.get_site()
        return self.url_path[len(site.root_page.url_path):]

    def get_site(self):
        """
        Overrides Page.get_site() in order to fetch ``RoutingSettings``
        in the same query (for tree-based-routing). Will also create a
        ``RoutingSettings`` for the site if they haven't been created yet.
        """
        url_parts = self.get_url_parts()

        if url_parts is None:
            # page is not routable
            return

        site_id, root_url, page_path = url_parts

        site = Site.objects.select_related('routingsettings').get(id=site_id)

        # Ensure the site has routingsettings before returning
        try:
            # if select_related() above was successful, great!
            site.routingsettings
        except RoutingSettings.DoesNotExist:
            # RoutingSettings need creating
            site.routingsettings = RoutingSettings.objects.create(site=site)
        return site

    def get_tree_based_url(self, include_site_url=False):
        """
        Returns the URL for this page based on it's position in the tree,
        and the RoutingSettings options for the `Site` the page belongs to.
        Wagtail multisite must be set up in order for this to work.
        """
        site = self.get_site()
        routing_settings = site.routingsettings
        page_path = self.get_non_prefixed_url(site)

        # prefix path with prefix from routing settings
        prefix = routing_settings.root_path_prefix.rstrip('/')
        if prefix:
            page_path = prefix + '/' + page_path

        if include_site_url:
            if not routing_settings.include_port_in_urls:
                # prevent the port being included in site.root_url
                site.port = 80
            return urljoin(site.root_url, page_path)

        return page_path

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
    def ancestors_in_app(self):
        """
            Used by `full_path` and `get_tree_based_breadcrumbs`
            in BasePageSerializer.
            Starts at 2 to exclude the root page and the app page.
            Ignores 'folder' pages.
        """
        ancestors = self.get_ancestors()[2:]

        return [
            page for page in ancestors
            if page.specific_class and not page.specific_class.folder_page
        ]

    @property
    def full_path(self):
        """Return the full path of a page, ignoring the root_page and
        the app page.
        """
        if self.uses_tree_based_routing:
            return self.get_tree_based_url(include_site_url=False)

        # continue with existing behaviour
        if self.full_path_override:
            return self.full_path_override

        path_components = []

        if not self.view_path:
            path_components = [
                page.specific_class.slug_override or page.slug
                for page in self.ancestors_in_app
            ]

        # need to also take into account the view_path if it's set
        else:
            path_components.insert(0, self.view_path.strip('/'))

        path_components.append(
            self.slug_override if self.slug_override is not None else self.slug
        )

        return '/{path}/'.format(path='/'.join(path_components))

    @property
    def full_url(self):
        if self.uses_tree_based_routing:
            return self.get_tree_based_url(include_site_url=True)

        # continue with existing behaviour
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
                # cast to a set to remove double en-gb if any
        return list(set(translated_languages))

    @property
    def language_names(self):
        if len(self.translated_languages) > 1:
            names = [
                label for code, label, _ in settings.LANGUAGES_DETAILS
                if code in self.translated_languages and code != settings.LANGUAGE_CODE
            ]
            return 'Translated to {}'.format(', '.join(names))
        return ''

    @classmethod
    def can_exist_under(cls, parent):
        """
        Overrides Page.can_exist_under() so that pages cannot be created or
        moved below a parent page whos specific page class has been removed.
        """
        if not parent.specific_class:
            return False
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


class WagtailAdminExclusivePageMixin:
    """
    Limits creation of pages in Wagtail's admin UI to only one
    instance of a specific type. If the class also has a `slug_identity`
    attribute set, that will be used as default slug in the page
    creation UI.
    """

    _base_form_class = forms.WagtailAdminPageExclusivePageForm

    @classmethod
    def can_create_at(cls, parent):
        return super().can_create_at(parent) and not cls.objects.exists()


class ExclusivePageMixin(WagtailAdminExclusivePageMixin):
    """
    A more restrictive version of `WagtailAdminExclusivePageMixin` that
    prevents anything other than the `slug_identity` class attribute
    value being used as the `slug` when creating new pages.
    """
    read_only_fields = ['slug']

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
    _base_form_class = forms.BaseAppAdminPageForm
    view_path = ''
    parent_page_types = ['wagtailcore.Page']

    class Meta:
        abstract = True

    @classmethod
    def allowed_subpage_models(cls):
        allowed_name = getattr(cls, 'service_name_value', None)
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
            attrs['content_panels_before_form'] + form_panels + attrs['content_panels_after_form']
        )

        return super().__new__(mcls, name, bases, attrs)
