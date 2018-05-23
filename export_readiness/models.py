from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel
from wagtail.api import APIField
from wagtailmarkdown.edit_handlers import MarkdownPanel
from wagtail.images.edit_handlers import ImageChooserPanel

from django.db import models

from core import constants
from core.fields import (
    APIMarkdownToHTMLField, APIMetaField, MarkdownField, APIImageField)
from core.models import BaseApp, BasePage, ExclusivePageMixin
from core.panels import SearchEngineOptimisationPanel


class ExportReadinessApp(ExclusivePageMixin, BaseApp):
    slug_identity = 'export-readiness-app'
    view_path = ''
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


class GetFinancePage(ExclusivePageMixin, BasePage):

    view_app = constants.EXPORT_READINESS
    view_path = 'get-finance/'
    slug_identity = 'get-finance'

    banner_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    ukef_logo = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    breadcrumbs_label = models.CharField(max_length=50)
    banner_content = MarkdownField()
    section_one_content = MarkdownField()
    section_two_content = MarkdownField()
    video_embed = models.CharField(max_length=500)
    section_three_content = MarkdownField()
    call_to_action_text = models.CharField(max_length=255)
    call_to_action_url = models.CharField(max_length=500)

    content_panels = [
        FieldPanel('breadcrumbs_label'),
        MultiFieldPanel(
            heading='Banner',
            children=[
                FieldPanel('banner_content'),
                ImageChooserPanel('banner_image'),
            ]
        ),
        MultiFieldPanel(
            heading='Section 1',
            children=[
                ImageChooserPanel('ukef_logo'),
                MarkdownPanel('section_one_content'),
                FieldPanel('call_to_action_text'),
                FieldPanel('call_to_action_url'),
            ]
        ),
        MultiFieldPanel(
            heading='Section 2',
            children=[
                MarkdownPanel('section_two_content'),
                FieldPanel('video_embed'),
            ]
        ),
        MultiFieldPanel(
            heading='Section 3',
            children=[
                MarkdownPanel('section_three_content'),
            ]
        ),
        SearchEngineOptimisationPanel(),
    ]

    settings_panels = [
        FieldPanel('title_en_gb'),
        FieldPanel('slug_en_gb'),
    ]

    api_fields = [
        APIField('breadcrumbs_label'),
        APIMarkdownToHTMLField('banner_content'),
        APIImageField('banner_image'),
        APIMarkdownToHTMLField('section_one_content'),
        APIMarkdownToHTMLField('section_two_content'),
        APIImageField('ukef_logo'),
        APIField('video_embed'),
        APIMarkdownToHTMLField('section_three_content'),
        APIField('call_to_action_text'),
        APIField('call_to_action_url'),
        APIField('seo_title'),
        APIField('search_description'),
        APIMetaField('meta'),
    ]
