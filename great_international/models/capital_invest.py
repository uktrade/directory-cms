from django.db import models

from wagtail.admin.edit_handlers import (
    FieldPanel, MultiFieldPanel, PageChooserPanel
)
from wagtail.documents.edit_handlers import DocumentChooserPanel
from wagtail.images.edit_handlers import ImageChooserPanel

from core.models import WagtailAdminExclusivePageMixin
from core.model_fields import MarkdownField

from great_international.models.base import BaseInternationalPage
import great_international.panels.capital_invest as panels
from directory_constants import slugs


class RegionCardField(models.Model):
    region_card_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        on_delete=models.SET_NULL,
        related_name='+',
        blank=True
    )
    region_card_title = models.CharField(max_length=255, blank=True)
    region_card_summary = MarkdownField(blank=True)

    panels = [
        MultiFieldPanel([
            ImageChooserPanel('region_card_image'),
            FieldPanel('region_card_title'),
            FieldPanel('region_card_summary'),
        ]),
    ]

    class Meta:
        abstract = True


class HomesInEnglandCardField(models.Model):
    homes_in_england_card_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        on_delete=models.SET_NULL,
        related_name='+',
        blank=True
    )
    homes_in_england_card_title = models.CharField(max_length=255, blank=True)
    homes_in_england_card_pdf_document = models.ForeignKey(
        'wagtaildocs.Document',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    panels = [
        MultiFieldPanel([
            ImageChooserPanel('homes_in_england_card_image'),
            FieldPanel('homes_in_england_card_title'),
            DocumentChooserPanel('homes_in_england_card_pdf_document'),
        ]),
    ]

    class Meta:
        abstract = True


class RelatedRegion(models.Model):
    related_region = models.ForeignKey(
        'great_international.AboutUkRegionPage',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    panels = [
        PageChooserPanel(
            'related_region',
            ['great_international.AboutUkRegionPage']
        ),
    ]

    class Meta:
        abstract = True


class CapitalInvestContactFormPage(
    panels.CapitalInvestContactFormPagePanels, WagtailAdminExclusivePageMixin, BaseInternationalPage
):
    parent_page_types = [
        'great_international.InvestmentAtlasLandingPage'
    ]
    slug_identity = slugs.CONTACT_FORM_SLUG

    breadcrumbs_label = models.CharField(max_length=255, blank=True)
    heading = models.CharField(max_length=255)
    intro = MarkdownField(blank=True)
    comment = models.TextField(
        max_length=255,
        default="To provide you with the best help, we may forward your message to "
                "appropriate Capital Investment team colleagues in British embassies, "
                "high commissions and consulates located internationally. "
    )
    cta_text = models.CharField(max_length=255)

    @classmethod
    def allowed_subpage_models(cls):
        return [
            CapitalInvestContactFormSuccessPage
        ]


class CapitalInvestContactFormSuccessPage(
    panels.CapitalInvestContactFormSuccessPagePanels, WagtailAdminExclusivePageMixin, BaseInternationalPage
):
    parent_page_types = [
        'great_international.CapitalInvestContactFormPage',
        'great_international.InvestmentAtlasLandingPage'
    ]
    slug_identity = slugs.FORM_SUCCESS_SLUG

    message_box_heading = models.CharField(max_length=255)
    message_box_description = MarkdownField(blank=True)
    what_happens_next_description = MarkdownField(blank=True)
