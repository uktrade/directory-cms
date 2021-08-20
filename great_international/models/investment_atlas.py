from django.db import models

from wagtail.core.fields import StreamField
from wagtail.core.models import Orderable
from wagtail.admin.edit_handlers import PageChooserPanel

from .base import BaseInternationalPage

from core.fields import single_struct_block_stream_field_factory
from core.model_fields import MarkdownField

from core.models import WagtailAdminExclusivePageMixin

from modelcluster.fields import ParentalKey, ParentalManyToManyField
import great_international.panels.investment_atlas as investment_atlas_panels
import great_international.models.great_international as gi_models
import great_international.blocks.investment_atlas as investment_atlas_blocks

from wagtail.snippets.models import register_snippet


TIME_TO_INVESTMENT_DECISION_0M_6M = 'TIME_TO_INVESTMENT_DECISION_0M_6M'
TIME_TO_INVESTMENT_DECISION_6M_12M = 'TIME_TO_INVESTMENT_DECISION_6M_12M'
TIME_TO_INVESTMENT_DECISION_1Y_2Y = 'TIME_TO_INVESTMENT_DECISION_1Y_2Y'
TIME_TO_INVESTMENT_DECISION_2Y_PLUS = 'TIME_TO_INVESTMENT_DECISION_2Y_PLUS'

TIME_TO_INVESTMENT_DECISION_OPTIONS = (
    (TIME_TO_INVESTMENT_DECISION_0M_6M, '0-6 months'),
    (TIME_TO_INVESTMENT_DECISION_6M_12M, '6-12 months'),
    (TIME_TO_INVESTMENT_DECISION_1Y_2Y, '1-2 years'),
    (TIME_TO_INVESTMENT_DECISION_2Y_PLUS, '2 years +'),
)


@register_snippet
class InvestmentType(models.Model):
    name = models.CharField(
        max_length=50
    )

    def __str__(self):
        return self.name


@register_snippet
class PlanningStatus(models.Model):
    name = models.CharField(
        max_length=50
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Planning Status choices'


class InvestmentAtlasLandingPage(
    BaseInternationalPage,
    WagtailAdminExclusivePageMixin,
    investment_atlas_panels.InvestmentAtlasLandingPagePanels,
):
    subpage_types = [
        'great_international.InvestmentOpportunityListingPage',
        # TO COME: more subpage_types to control CMS page heirarchy
    ]

    # title comes from base page
    breadcrumbs_label = models.CharField(max_length=100)

    hero_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        on_delete=models.SET_NULL,
        related_name='+',
        blank=False
    )

    hero_title = models.CharField(
        blank=False,
        null=False,
        max_length=150,
        help_text='Distinct from the page title, this is the title text for the main hero'
    )

    hero_strapline = models.TextField(
        max_length=500,
        blank=True,
        null=True,
    )

    downpage_sections = StreamField(
        [
            ('panel', investment_atlas_blocks.AtlasLandingPagePanelBlock()),
        ],
        null=True,
        blank=True,
    )


class InvestmentOpportunityListingPage(
    WagtailAdminExclusivePageMixin,
    BaseInternationalPage,
    investment_atlas_panels.InvestmentOpportunityListingPagePanels,
):
    parent_page_types = ['great_international.InvestmentAtlasLandingPage', ]
    subpage_types = ['great_international.InvestmentOpportunityPage', ]

    # `title` comes from the base class
    breadcrumbs_label = models.CharField(max_length=50)
    search_results_title = models.CharField(
        max_length=255
    )
    hero_text = models.TextField(
        max_length=2000,
        blank=False,
        help_text='Text that appears beneath the page title',
    )
    contact_cta_title = models.CharField(
        blank=True,
        max_length=50,
    )
    contact_cta_text = models.TextField(
        blank=True,
        max_length=1000,
    )
    contact_cta_link = models.URLField(
        blank=True,
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
                'great_international.InternationalSectorPage'
            ]
        ),
    ]

    class Meta:
        abstract = True


class InvestmentOpportunityRelatedSectors(Orderable, RelatedSector):
    # link to a sector FROM an InvestmentOpportunityPage (defined lower in this module)
    page = ParentalKey(
        'great_international.InvestmentOpportunityPage',
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
            ['great_international.InternationalSubSectorPage']
        ),
    ]

    class Meta:
        abstract = True


class InvestmentOpportunityRelatedSubSectors(
    Orderable,
    RelatedSubSector,
):
    # link to a subsector FROM an InvestmentOpportunityPage (defined lower in this module)
    page = ParentalKey(
        'great_international.InvestmentOpportunityPage',
        on_delete=models.CASCADE,
        related_name='related_sub_sectors',
        blank=True,
        null=True,
    )


class InvestmentOpportunityPage(
    BaseInternationalPage,
    investment_atlas_panels.InvestmentOpportunityPagePanels,
):
    # `title` comes from the base class
    breadcrumbs_label = models.CharField(max_length=50)

    priority_weighting = models.DecimalField(
        default='0.0',
        max_digits=5,
        decimal_places=2,
        help_text=(
            'For use when auto-ordering results or automatically choosing which to show '
            '- an Opportunity with a higher priority weighting will be shown earlier. '
            'Max val: 999.99'
        ),
    )

    featured_images = single_struct_block_stream_field_factory(
        field_name='images',
        block_class_instance=investment_atlas_blocks.FeaturedImageBlock(),
        max_num=5,
        null=True,
        blank=True,
    )

    strapline = models.CharField(
        max_length=200,
        blank=False,
        help_text=(
            'A single sentence which directly brings to the direct opportunity '
            'to the fore. 200 chars max.'
        )
    )

    introduction = MarkdownField(
        max_length=300,
        blank=False,
        help_text=(
            'A single paragraph of 300 characters max including spaces to introduce the opportunity '
            '– what is the vision / ambition of the opportunity, timeline and where relevant, procurement method. '
            'What type of investor is this suitable for? Where is it and why is that important? '
            'Further detail can be provided in the “The Opportunity” section.'
        ),
    )

    opportunity_summary = models.TextField(
        max_length=300,
        blank=False,
        help_text=(
            'Simple summary of the Opportunity, for display on OTHER pages (eg listing pages) '
            'which link TO a full page about this opportunity. 300 chars max.'
        ),
    )

    # Key facts
    location = models.CharField(
        blank=True,
        max_length=200,
        help_text=(
            'Verbose display name for the location. '
            'Geospatial and region data is set in the Location and Relevant Regions tab.'
        )
    )
    location_coords = models.CharField(
        # NB: deliberately not a PointField [yet?], as we don't need GIS functionality at the DB level
        blank=True,
        max_length=200,
    )

    related_regions = ParentalManyToManyField(
        gi_models.AboutUkRegionPage,
        blank=True,
    )

    promoter = models.CharField(
        blank=True,
        max_length=200,
    )

    scale = models.CharField(
        max_length=255,
        blank=True,
        help_text='Verbose description of investment scale',
    )
    scale_value = models.DecimalField(
        default=0,
        null=True,
        blank=True,
        max_digits=10,
        decimal_places=2,
        verbose_name="Scale value (in millions)"
    )

    # Note that a `related_sub_sectors` reverse relation comes
    # from InvestmentOpportunityRelatedSubSectors

    planning_status = models.ForeignKey(
        PlanningStatus,
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
    )

    investment_type = models.ForeignKey(
        InvestmentType,
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
    )

    time_to_investment_decision = models.CharField(
        choices=TIME_TO_INVESTMENT_DECISION_OPTIONS,
        max_length=50,
        blank=True,
    )

    # The Opportunity
    main_content = StreamField(
        [
            ('content_section', investment_atlas_blocks.PageSectionBlock()),
        ],
        null=True,
        blank=True,
    )

    important_links = MarkdownField(
        blank=True,
        null=True,
    )

    # Contact details
    contact_name = models.CharField(
        max_length=255,
        blank=True,
    )
    contact_avatar = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        on_delete=models.SET_NULL,
        related_name='+',
        blank=True
    )
    contact_job_title = models.CharField(
        max_length=255,
        blank=True,
    )
    contact_link = models.URLField(
        blank=True,
        null=True,
        max_length=1500,
    )
