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


# `CapitalInvestRegionPage` is to be replaced with `AboutUkRegionPage`, can be deleted when CI-431 has been released in great-international-ui  # NOQA
class CapitalInvestRegionPage(panels.CapitalInvestRegionPagePanels, BaseInternationalPage):
    parent_page_types = ['great_international.InternationalHomePage']

    breadcrumbs_label = models.CharField(max_length=255)
    hero_title = models.CharField(max_length=255)
    hero_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    featured_description = models.TextField(max_length=255, blank=True)

    region_summary_section_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        on_delete=models.SET_NULL,
        related_name='+',
        blank=True
    )
    region_summary_section_intro = models.TextField(max_length=255, blank=True)
    region_summary_section_content = MarkdownField(blank=True)

    investment_opps_title = models.CharField(
        max_length=255,
        verbose_name="Investment opportunities title", blank=True
    )
    investment_opps_intro = models.CharField(
        max_length=255,
        blank=True,
        verbose_name="Investment opportunities intro"
    )

    economics_data_title = models.CharField(max_length=255, blank=True)
    economics_stat_1_number = models.CharField(max_length=255, blank=True)
    economics_stat_1_heading = models.CharField(max_length=255, blank=True)
    economics_stat_1_smallprint = models.CharField(max_length=255, blank=True)

    economics_stat_2_number = models.CharField(max_length=255, blank=True)
    economics_stat_2_heading = models.CharField(max_length=255, blank=True)
    economics_stat_2_smallprint = models.CharField(max_length=255, blank=True)

    economics_stat_3_number = models.CharField(max_length=255, blank=True)
    economics_stat_3_heading = models.CharField(max_length=255, blank=True)
    economics_stat_3_smallprint = models.CharField(max_length=255, blank=True)

    economics_stat_4_number = models.CharField(max_length=255, blank=True)
    economics_stat_4_heading = models.CharField(max_length=255, blank=True)
    economics_stat_4_smallprint = models.CharField(max_length=255, blank=True)

    economics_stat_5_number = models.CharField(max_length=255, blank=True)
    economics_stat_5_heading = models.CharField(max_length=255, blank=True)
    economics_stat_5_smallprint = models.CharField(max_length=255, blank=True)

    economics_stat_6_number = models.CharField(max_length=255, blank=True)
    economics_stat_6_heading = models.CharField(max_length=255, blank=True)
    economics_stat_6_smallprint = models.CharField(max_length=255, blank=True)

    location_data_title = models.CharField(
        max_length=255,
        blank=True
    )
    location_stat_1_number = models.CharField(
        max_length=255,
        blank=True
    )
    location_stat_1_heading = models.CharField(
        max_length=255,
        blank=True
    )
    location_stat_1_smallprint = models.CharField(
        max_length=255,
        blank=True
    )

    location_stat_2_number = models.CharField(
        max_length=255,
        blank=True
    )
    location_stat_2_heading = models.CharField(
        max_length=255,
        blank=True
    )
    location_stat_2_smallprint = models.CharField(
        max_length=255,
        blank=True
    )

    location_stat_3_number = models.CharField(
        max_length=255,
        blank=True
    )
    location_stat_3_heading = models.CharField(
        max_length=255,
        blank=True
    )
    location_stat_3_smallprint = models.CharField(
        max_length=255,
        blank=True
    )

    location_stat_4_number = models.CharField(
        max_length=255,
        blank=True
    )
    location_stat_4_heading = models.CharField(
        max_length=255,
        blank=True
    )
    location_stat_4_smallprint = models.CharField(
        max_length=255,
        blank=True
    )

    location_stat_5_number = models.CharField(
        max_length=255,
        blank=True
    )
    location_stat_5_heading = models.CharField(
        max_length=255,
        blank=True
    )
    location_stat_5_smallprint = models.CharField(
        max_length=255,
        blank=True
    )

    location_stat_6_number = models.CharField(
        max_length=255,
        blank=True
    )
    location_stat_6_heading = models.CharField(
        max_length=255,
        blank=True
    )
    location_stat_6_smallprint = models.CharField(
        max_length=255,
        blank=True
    )

    subsections_title = models.CharField(max_length=255, blank=True)
    sub_section_one_title = models.CharField(max_length=255, blank=True)
    sub_section_one_icon = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        on_delete=models.SET_NULL,
        related_name='+',
        blank=True
    )
    sub_section_one_content = MarkdownField(blank=True)

    sub_section_two_title = models.CharField(max_length=255, blank=True)
    sub_section_two_icon = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        on_delete=models.SET_NULL,
        related_name='+',
        blank=True
    )
    sub_section_two_content = MarkdownField(blank=True)

    sub_section_three_title = models.CharField(max_length=255, blank=True)
    sub_section_three_icon = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        on_delete=models.SET_NULL,
        related_name='+',
        blank=True
    )
    sub_section_three_content = MarkdownField(blank=True)

    property_and_infrastructure_section_title = models.CharField(
        max_length=255,
        blank=True
    )
    property_and_infrastructure_section_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        on_delete=models.SET_NULL,
        related_name='+',
        blank=True
    )
    property_and_infrastructure_section_content = MarkdownField(blank=True)

    case_study_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        on_delete=models.SET_NULL,
        related_name='+',
        blank=True
    )
    case_study_title = models.CharField(max_length=255, blank=True)
    case_study_text = models.TextField(max_length=255, blank=True)
    case_study_cta_text = models.CharField(max_length=255, blank=True)
    case_study_cta_link = models.CharField(max_length=255, blank=True)

    contact_title = models.CharField(max_length=255, blank=True)
    contact_text = MarkdownField(blank=True)
    contact_cta_link = models.CharField(max_length=255, blank=True)
    contact_cta_text = models.CharField(max_length=255, blank=True)


class CapitalInvestOpportunityListingPage(
    panels.CapitalInvestOpportunityListingPagePanels, WagtailAdminExclusivePageMixin, BaseInternationalPage,
):

    slug_identity = 'opportunities'

    parent_page_types = ['great_international.InternationalHomePage']

    @classmethod
    def allowed_subpage_models(cls):
        return [CapitalInvestOpportunityPage]

    breadcrumbs_label = models.CharField(
        max_length=255,
        default="Opportunities"
    )
    search_results_title = models.CharField(
        max_length=255
    )


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


class CapitalInvestRelatedSectors(Orderable, RelatedSector):
    page = ParentalKey(
        'great_international.CapitalInvestOpportunityPage',
        on_delete=models.CASCADE,
        related_name='related_sectors',
        blank=True,
        null=True,
    )


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


class CapitalInvestRelatedSubSectors(Orderable, RelatedSubSector):
    page = ParentalKey(
        'great_international.CapitalInvestOpportunityPage',
        on_delete=models.CASCADE,
        related_name='related_sub_sectors',
        blank=True,
        null=True,
    )


class CapitalInvestOpportunityPage(panels.CapitalInvestOpportunityPagePanels, BaseInternationalPage):

    parent_page_types = [
        'great_international.CapitalInvestOpportunityListingPage'
    ]

    breadcrumbs_label = models.CharField(max_length=255)
    hero_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    hero_title = models.CharField(max_length=255)

    related_region = models.ForeignKey(
        'wagtailcore.Page',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    opportunity_summary_intro = models.TextField(max_length=255, blank=True)
    opportunity_summary_content = MarkdownField(blank=True)
    opportunity_summary_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        on_delete=models.SET_NULL,
        related_name='+',
        blank=True
    )

    location_icon = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        on_delete=models.SET_NULL,
        related_name='+',
        blank=True
    )
    location_heading = models.CharField(
        max_length=255,
        blank=True,
        default="Location"
    )
    location = models.CharField(max_length=255, blank=True)
    project_promoter_icon = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        on_delete=models.SET_NULL,
        related_name='+',
        blank=True
    )
    project_promoter_heading = models.CharField(
        max_length=255,
        blank=True,
        default="Project promoter"
    )
    project_promoter = models.CharField(max_length=255, blank=True)
    scale_icon = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        on_delete=models.SET_NULL,
        related_name='+',
        blank=True
    )
    scale_heading = models.CharField(
        max_length=255,
        blank=True,
        default="Scale"
    )
    scale = models.CharField(max_length=255, blank=True)
    scale_value = models.DecimalField(
        default=0,
        null=True,
        blank=True,
        max_digits=10,
        decimal_places=2,
        verbose_name="Scale value (in millions)"
    )
    sector_icon = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        on_delete=models.SET_NULL,
        related_name='+',
        blank=True
    )
    sector_heading = models.CharField(
        max_length=255,
        blank=True,
        default="Sector"
    )
    sector = models.CharField(max_length=255, blank=True)
    investment_type_icon = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        on_delete=models.SET_NULL,
        related_name='+',
        blank=True
    )
    investment_type_heading = models.CharField(
        max_length=255,
        blank=True,
        default="Investment type"
    )
    investment_type = models.CharField(max_length=255, blank=True)
    planning_status_icon = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        on_delete=models.SET_NULL,
        related_name='+',
        blank=True
    )
    planning_status_heading = models.CharField(
        max_length=255,
        blank=True,
        default="Planning status"
    )
    planning_status = models.CharField(max_length=255, blank=True)

    project_background_title = models.CharField(max_length=255)
    project_background_intro = MarkdownField()
    project_description_title = models.CharField(max_length=255, blank=True)
    project_description_content = MarkdownField(blank=True)
    project_promoter_title = models.CharField(max_length=255, blank=True)
    project_promoter_content = MarkdownField(blank=True)
    project_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        on_delete=models.SET_NULL,
        related_name='+',
        blank=True
    )

    case_study_title = models.CharField(max_length=255, blank=True)
    case_study_text = models.CharField(max_length=255, blank=True)
    case_study_cta_text = models.CharField(max_length=255, blank=True)
    case_study_cta_link = models.CharField(max_length=255, blank=True)
    case_study_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        on_delete=models.SET_NULL,
        related_name='+',
        blank=True
    )

    similar_projects_cta_text = models.CharField(max_length=255, blank=True)
    similar_projects_cta_link = models.CharField(max_length=255, blank=True)

    contact_title = models.CharField(max_length=255, blank=True)
    contact_text = MarkdownField(blank=True)


class CapitalInvestContactFormPage(
    panels.CapitalInvestContactFormPagePanels, WagtailAdminExclusivePageMixin, BaseInternationalPage
):
    parent_page_types = ['great_international.InternationalCapitalInvestLandingPage']
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
    parent_page_types = ['great_international.CapitalInvestContactFormPage']
    slug_identity = slugs.FORM_SUCCESS_SLUG

    message_box_heading = models.CharField(max_length=255)
    message_box_description = MarkdownField(blank=True)
    what_happens_next_description = MarkdownField(blank=True)
