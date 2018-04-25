from wagtail.wagtailadmin.edit_handlers import FieldPanel, MultiFieldPanel
from wagtail.api import APIField
from wagtail.wagtailcore.fields import RichTextField
from wagtailmarkdown.edit_handlers import MarkdownPanel
from wagtailmarkdown.fields import MarkdownField

from django.db import models

from core import constants
from core.fields import APIRichTextField, APIMetaField
from core.models import BaseApp, BasePage, ExclusivePageMixin
from core.panels import SearchEngineOptimisationPanel


class ExportReadinessApp(ExclusivePageMixin, BaseApp):
    view_app = constants.EXPORT_READINESS


class TermsAndConditionsPage(ExclusivePageMixin, BasePage):

    view_app = constants.EXPORT_READINESS
    view_path = 'terms-and-conditions/'
    slug_identity = 'terms-and-conditions'

    body = MarkdownField(blank=False)

    content_panels = [
        MultiFieldPanel(
            heading='Terms and conditions',
            children=[
                MarkdownPanel('body'),
            ]
        ),
        SearchEngineOptimisationPanel(),
    ]

    settings_panels = [
        FieldPanel('title_en_gb'),
    ]

    api_fields = [
        APIField('seo_title'),
        APIField('search_description'),
        APIRichTextField('body'),
        APIMetaField('meta'),
    ]


class PrivacyAndCookiesPage(ExclusivePageMixin, BasePage):

    view_app = constants.EXPORT_READINESS
    view_path = 'privacy-and-cookies/'

    body = MarkdownField(blank=False)

    content_panels = [
        MultiFieldPanel(
            heading='Privacy and cookies',
            children=[
                MarkdownPanel('body'),
            ]
        ),
        SearchEngineOptimisationPanel(),
    ]

    settings_panels = [
        FieldPanel('title_en_gb'),
    ]

    api_fields = [
        APIField('seo_title'),
        APIField('search_description'),
        APIRichTextField('body'),
        APIMetaField('meta'),
    ]
