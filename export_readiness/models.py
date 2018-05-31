from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel
from wagtail.api import APIField
from wagtailmarkdown.edit_handlers import MarkdownPanel

from core import constants
from core.fields import APIMarkdownToHTMLField, APIMetaField, MarkdownField
from core.models import BaseApp, BasePage, ExclusivePageMixin
from core.panels import SearchEngineOptimisationPanel


class ExportReadinessApp(BaseApp):
    view_app = constants.EXPORT_READINESS
    slug_identity = 'export-readiness-app'

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
        FieldPanel('slug_en_gb'),
    ]

    api_fields = [
        APIField('seo_title'),
        APIField('search_description'),
        APIMarkdownToHTMLField('body'),
        APIMetaField('meta'),
    ]


class PrivacyAndCookiesPage(ExclusivePageMixin, BasePage):

    view_app = constants.EXPORT_READINESS
    view_path = 'privacy-and-cookies/'
    slug_identity = 'privacy-and-cookies'

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
        FieldPanel('slug_en_gb'),
    ]

    promote_panels = []

    api_fields = [
        APIField('seo_title'),
        APIField('search_description'),
        APIMarkdownToHTMLField('body'),
        APIMetaField('meta'),
    ]
