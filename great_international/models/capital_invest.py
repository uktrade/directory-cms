from django.db import models
from modelcluster.fields import ParentalKey

from wagtail.core.models import Orderable

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


class CapitalInvestRegionCardFieldsSummary(Orderable, RegionCardField):
    page = ParentalKey(
        'great_international.InternationalCapitalInvestLandingPage',
        on_delete=models.CASCADE,
        related_name='added_region_card_fields',
        blank=True,
        null=True,
    )


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


class CapitalInvestHomesInEnglandCardFieldsSummary(
    Orderable, HomesInEnglandCardField
):
    page = ParentalKey(
        'great_international.InternationalCapitalInvestLandingPage',
        on_delete=models.CASCADE,
        related_name='added_homes_in_england_card_fields',
        blank=True,
        null=True,
    )


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


class CapitalInvestRelatedRegions(Orderable, RelatedRegion):
    page = ParentalKey(
        'great_international.InternationalCapitalInvestLandingPage',
        on_delete=models.CASCADE,
        related_name='added_regions',
        blank=True,
        null=True,
    )


class InternationalCapitalInvestLandingPage(
    panels.InternationalCapitalInvestLandingPagePanels, WagtailAdminExclusivePageMixin, BaseInternationalPage
):
    slug_identity = 'capital-invest'

    parent_page_types = ['great_international.InternationalHomePage']
    subpage_types = [
        'great_international.CapitalInvestContactFormPage',
        'great_international.InternationalGuideLandingPage',
        'great_international.AboutDitServicesPage'
    ]

    breadcrumbs_label = models.CharField(max_length=255, blank=True)
    hero_title = models.CharField(max_length=255)
    hero_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        on_delete=models.SET_NULL,
        related_name='+', blank=True
    )
    hero_subheading = models.CharField(
        max_length=255,
        blank=True,
        help_text="Please use if you'd like to "
                  "add to the title on a second line"
    )
    hero_subtitle = models.CharField(max_length=255, blank=True)
    hero_cta_text = models.CharField(max_length=255, blank=True)
    hero_cta_link = models.CharField(max_length=255, blank=True)

    featured_description = models.TextField(max_length=255, blank=True)

    reason_to_invest_section_title = models.CharField(
        max_length=255,
        blank=True
    )
    reason_to_invest_section_intro = models.CharField(
        max_length=255,
        blank=True
    )
    reason_to_invest_section_content = MarkdownField(blank=True)
    reason_to_invest_section_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        on_delete=models.SET_NULL,
        related_name='+',
        blank=True
    )

    region_ops_section_title = models.CharField(
        max_length=255,
        verbose_name="Region opportunities section title",
        blank=True
    )
    region_ops_section_intro = models.CharField(
        max_length=255,
        blank=True,
        verbose_name="Region opportunities section intro"
    )
    region_card_one_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        on_delete=models.SET_NULL,
        related_name='+',
        blank=True
    )
    banner_information = MarkdownField(blank=True)

    energy_sector_title = models.CharField(max_length=255, blank=True)
    energy_sector_content = MarkdownField(blank=True)
    energy_sector_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        on_delete=models.SET_NULL,
        related_name='+', blank=True
    )
    energy_sector_cta_text = models.CharField(max_length=255, blank=True)
    energy_sector_pdf_document = models.ForeignKey(
        'wagtaildocs.Document',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    homes_in_england_section_title = models.CharField(
        max_length=255, blank=True
    )

    how_we_help_title = models.CharField(max_length=255, blank=True)
    how_we_help_intro = models.TextField(max_length=255, blank=True)

    how_we_help_one_icon = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        on_delete=models.SET_NULL,
        related_name='+',
        blank=True
    )
    how_we_help_one_text = models.CharField(max_length=255, blank=True)

    how_we_help_two_icon = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        on_delete=models.SET_NULL,
        related_name='+', blank=True
    )
    how_we_help_two_text = models.CharField(max_length=255, blank=True)

    how_we_help_three_icon = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        on_delete=models.SET_NULL,
        related_name='+', blank=True
    )
    how_we_help_three_text = models.CharField(max_length=255, blank=True)

    how_we_help_four_icon = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        on_delete=models.SET_NULL,
        related_name='+', blank=True
    )
    how_we_help_four_text = models.CharField(max_length=255, blank=True)

    how_we_help_cta_text = models.CharField(max_length=255, blank=True)
    how_we_help_cta_link = models.CharField(max_length=255, blank=True)

    contact_section_title = models.CharField(max_length=255, blank=True)
    contact_section_text = models.CharField(max_length=255, blank=True)
    contact_section_cta_text = models.CharField(max_length=255, blank=True)


class RelatedSector(models.Model):
    related_sector = models.ForeignKey(
        'great_international.InternationalSectorPage',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    panels = [
        PageChooserPanel(
            'related_sector',
            [
                'great_international.'
                'InternationalSectorPage'
            ]
        ),
    ]

    class Meta:
        abstract = True


class RelatedSubSector(models.Model):
    related_sub_sector = models.ForeignKey(
        'great_international.InternationalSubSectorPage',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    panels = [
        PageChooserPanel(
            'related_sub_sector',
            [
                'great_international.'
                'InternationalSubSectorPage'
            ]
        ),
    ]

    class Meta:
        abstract = True


class CapitalInvestContactFormPage(
    panels.CapitalInvestContactFormPagePanels, WagtailAdminExclusivePageMixin, BaseInternationalPage
):
    parent_page_types = [
        'great_international.InternationalCapitalInvestLandingPage',
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
