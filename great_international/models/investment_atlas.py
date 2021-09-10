from django.db import models

from wagtail.core.fields import StreamField
from wagtail.core.models import Orderable
from wagtail.admin.edit_handlers import (
    HelpPanel,
    FieldPanel,
    PageChooserPanel,
    StreamFieldPanel,
)

from .base import BaseInternationalPage

from core.fields import single_struct_block_stream_field_factory
from core.model_fields import MarkdownField

from core.models import WagtailAdminExclusivePageMixin

from modelcluster.fields import ParentalKey, ParentalManyToManyField
import great_international.blocks.great_international as great_international_blocks
from great_international.models import great_international as great_international_models
import great_international.blocks.investment_atlas as investment_atlas_blocks
import great_international.panels.investment_atlas as investment_atlas_panels

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

# FOR ALL THE SNIPPETS:
# TODO: translation support: https://wagtail-modeltranslation.readthedocs.io/en/latest/Registering%20Models.html


@register_snippet
class InvestmentType(models.Model):
    # TODO: add modeltranslation support as required, at the snippet model level
    name = models.CharField(
        max_length=50
    )

    def __str__(self):
        return self.name


@register_snippet
class PlanningStatus(models.Model):
    # TODO: add modeltranslation support as required, at the snippet model level
    name = models.CharField(
        max_length=50
    )
    verbose_description = models.CharField(
        max_length=500
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Planning Status choices'


@register_snippet
class ReusableContentSection(models.Model):
    # Identical content structure to the main content on an InvestmentOpportunityPage,
    # but designed for re-use

    title = models.CharField(
        max_length=200,
        blank=False,
    )

    content = StreamField(
        investment_atlas_blocks.page_section_block_spec_list,
        blank=False,
    )

    block_slug = models.CharField(
        max_length=255,
        blank=True,
        help_text="Only needed if special styling is involved: check with a developer. If in doubt, it's not needed"
    )

    panels = [
        HelpPanel(
            "<b>For repeated content that is the same across all pages, author it "
            "here and then include it in a StreamField in the relevant page.</b>"
            "<ul><li>The title field is only for internal reference - "
            "its content will not be used in the public site.</li>"
            "<li>The structure of the main content panel is the same as for each "
            "Content Section in an Opportunity page.</li></ul>"
        ),
        FieldPanel('title'),
        StreamFieldPanel('content'),
        FieldPanel('block_slug'),
    ]

    def __str__(self):
        return f"Reusable content: {self.title}"


# FOR ALL THE SNIPPETS:
# TODO: translation support: https://wagtail-modeltranslation.readthedocs.io/en/latest/Registering%20Models.html


class InvestmentAtlasLandingPage(
    BaseInternationalPage,
    WagtailAdminExclusivePageMixin,
    investment_atlas_panels.InvestmentAtlasLandingPagePanels,
):
    subpage_types = [
        'great_international.InvestmentOpportunityListingPage',
        # TO COME: more subpage_types to control CMS page heirarchy
        'great_international.AboutUkWhyChooseTheUkPage',
        'great_international.AboutUkRegionListingPage',
        'great_international.InternationalTopicLandingPage',
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
    mobile_hero_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text='Dedicated image for use on small/mobile-screen rendering of the page'
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
            (
                'panel',
                investment_atlas_blocks.AtlasLandingPagePanelBlock(
                    help_text=(
                        "If 'Block slug' is set to 'with-regions-map', the panel will show the regions map"
                    ),
                ),
            ),
        ],
        null=True,
        blank=True,
    )

    @property
    def full_url(self):
        full_url_items = super().full_url.split('/')
        full_url_items.remove('content')
        return '/'.join(full_url_items)


class InvestmentOpportunityListingPage(
    WagtailAdminExclusivePageMixin,
    BaseInternationalPage,
    investment_atlas_panels.InvestmentOpportunityListingPagePanels,
):
    parent_page_types = ['great_international.InvestmentAtlasLandingPage', ]
    subpage_types = [
        'great_international.InvestmentOpportunityPage',
        'great_international.AboutUkWhyChooseTheUkPage',
    ]

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

    @property
    def full_url(self):
        full_url_items = super().full_url.split('/')
        full_url_items.remove('content')
        return '/'.join(full_url_items)


class RelatedSector(models.Model):
    related_sector = models.ForeignKey(
        'great_international.InternationalInvestmentSectorPage',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    panels = [
        PageChooserPanel(
            'related_sector',
            [
                'great_international.InternationalInvestmentSectorPage'
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
        'great_international.InternationalInvestmentSubSectorPage',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    panels = [
        PageChooserPanel(
            'related_sub_sector',
            ['great_international.InternationalInvestmentSubSectorPage']
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
        block_class_instance=great_international_blocks.FeaturedImageBlock(),
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
        blank=False,
        help_text=(
            'A single paragraph to introduce the opportunity '
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
        great_international_models.AboutUkRegionPage,
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

    # Note that a `related_sectors` reverse relation
    # comes from InvestmentOpportunityRelatedectors
    # and a `related_sub_sectors` reverse relation comes
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
            ('content_section', investment_atlas_blocks.PageSectionBlock(
                help_text=(
                    "If 'Block slug' is set to 'with-key-links', the 'Key links' "
                    "panel is shown next to the text. "
                    "If 'Block slug' is set to 'with-region-spotlight', "
                    "the 'Region spotlight' panel is shown next to the text."
                )
            )),
            (
                'snippet_content',
                investment_atlas_blocks.ReusableSnippetChooserBlock(
                    ReusableContentSection
                )
            )
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
