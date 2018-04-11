from wagtail.wagtailadmin.edit_handlers import FieldPanel, MultiFieldPanel
from wagtail.api import APIField
from wagtail.wagtailcore.fields import RichTextField

from django.db import models

from core import constants
from core.fields import APIRichTextField, APIMetaField
from core.helpers import make_translated_interface
from core.models import BaseApp, BasePage, ExclusivePageMixin
from core.panels import SearchEngineOptimisationPanel


class ExportReadinessApp(ExclusivePageMixin, BaseApp):
    view_app = constants.EXPORT_READINESS


class TermsAndConditionsPage(ExclusivePageMixin, BasePage):

    view_app = constants.EXPORT_READINESS
    view_path = 'terms-and-conditions/'

    terms_title = models.CharField(max_length=50)
    body = RichTextField(blank=False)

    content_panels = [
        MultiFieldPanel(
            heading='Terms and conditions',
            children=[
                FieldPanel('terms_title'),
                FieldPanel('body'),
            ]
        ),
        SearchEngineOptimisationPanel(),
    ]

    settings_panels = [
        FieldPanel('title_en_gb'),
    ]

    edit_handler = make_translated_interface(
        content_panels=content_panels,
        settings_panels=settings_panels,
    )

    api_fields = [
        APIField('seo_title'),
        APIField('search_description'),
        APIField('terms_title'),
        APIRichTextField('body'),
        APIMetaField('meta'),
    ]
