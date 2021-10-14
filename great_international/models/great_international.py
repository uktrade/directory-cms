from directory_constants import slugs
from django.db import models
from modelcluster.fields import ParentalKey, ParentalManyToManyField
from wagtail.core.blocks import PageChooserBlock
from wagtail.core.fields import StreamField
from wagtail.core.models import Orderable

from core.constants import ARTICLE_TYPES
from core.fields import single_struct_block_stream_field_factory
from core.mixins import ServiceHomepageMixin
from core.model_fields import MarkdownField
from core.models import FormPageMetaClass, WagtailAdminExclusivePageMixin
from export_readiness import snippets
from great_international.blocks import great_international as blocks
from great_international.panels import great_international as panels

from . import capital_invest as capital_invest_models
from . import find_a_supplier as fas_models
from . import invest as invest_models
from .base import BaseInternationalPage


class BaseInternationalSectorPage(panels.BaseInternationalSectorPagePanels, BaseInternationalPage):
    class Meta:
        abstract = True

    parent_page_types = ['great_international.InternationalTopicLandingPage']
    subpage_types = []

    tags = ParentalManyToManyField(snippets.Tag, blank=True)

    heading = models.CharField(max_length=255, verbose_name='Sector name')
    sub_heading = models.TextField(blank=True)
    hero_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    heading_teaser = models.TextField(blank=True, verbose_name='Introduction')
    featured_description = models.TextField(
        blank=True,
        help_text="This is the description shown when the sector "
                  "is featured on another page i.e. the Invest Home Page"
    )

    section_one_body = MarkdownField(
        null=True,
        verbose_name='3 unique selling points markdown',
        blank=True
    )
    section_one_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        on_delete=models.SET_NULL,
        related_name='+',
        verbose_name='Image for unique selling points',
        blank=True
    )
    section_one_image_caption = models.CharField(
        max_length=255,
        blank=True,
        verbose_name='Image caption')
    section_one_image_caption_company = models.CharField(
        max_length=255,
        blank=True,
        verbose_name='Image caption attribution')

    statistic_1_number = models.CharField(max_length=255, blank=True)
    statistic_1_heading = models.CharField(max_length=255, blank=True)
    statistic_1_smallprint = models.CharField(max_length=255, blank=True)

    statistic_2_number = models.CharField(max_length=255, blank=True)
    statistic_2_heading = models.CharField(max_length=255, blank=True)
    statistic_2_smallprint = models.CharField(max_length=255, blank=True)

    statistic_3_number = models.CharField(max_length=255, blank=True)
    statistic_3_heading = models.CharField(max_length=255, blank=True)
    statistic_3_smallprint = models.CharField(max_length=255, blank=True)

    statistic_4_number = models.CharField(max_length=255, blank=True)
    statistic_4_heading = models.CharField(max_length=255, blank=True)
    statistic_4_smallprint = models.CharField(max_length=255, blank=True)

    statistic_5_number = models.CharField(max_length=255, blank=True)
    statistic_5_heading = models.CharField(max_length=255, blank=True)
    statistic_5_smallprint = models.CharField(max_length=255, blank=True)

    statistic_6_number = models.CharField(max_length=255, blank=True)
    statistic_6_heading = models.CharField(max_length=255, blank=True)
    statistic_6_smallprint = models.CharField(max_length=255, blank=True)

    section_two_heading = models.CharField(
        max_length=255,
        verbose_name='Spotlight',
        blank=True
    )
    section_two_teaser = models.TextField(
        verbose_name='Spotlight summary', blank=True
    )

    section_two_subsection_one_icon = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        verbose_name='Spotlight 1 icon'
    )
    section_two_subsection_one_heading = models.CharField(
        max_length=255,
        verbose_name='Spotlight 1 heading', blank=True
    )
    section_two_subsection_one_body = models.TextField(
        verbose_name='Spotlight 1 body', blank=True
    )

    section_two_subsection_two_icon = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        verbose_name='Spotlight 2 icon'
    )
    section_two_subsection_two_heading = models.CharField(
        max_length=255,
        verbose_name='Spotlight 2 heading', blank=True
    )
    section_two_subsection_two_body = models.TextField(
        verbose_name='Spotlight 2 body', blank=True
    )

    section_two_subsection_three_icon = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        verbose_name='Spotlight 3 icon'
    )
    section_two_subsection_three_heading = models.CharField(
        max_length=255,
        verbose_name='Spotlight 3 heading', blank=True
    )
    section_two_subsection_three_body = models.TextField(
        verbose_name='Spotlight 3 body', blank=True
    )

    case_study_title = models.CharField(max_length=255, blank=True)
    case_study_description = models.TextField(blank=True)
    case_study_cta_text = models.TextField(
        blank=True,
        verbose_name='Case study link text'
    )
    case_study_cta_page = models.ForeignKey(
        'wagtailcore.Page',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        verbose_name='Case study link URL'
    )
    case_study_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    section_three_heading = models.CharField(
        max_length=255,
        blank=True,
        verbose_name='Fact sheets heading'
    )
    section_three_teaser = models.TextField(
        blank=True,
        verbose_name='Fact sheets teaser'
    )

    section_three_subsection_one_heading = models.CharField(
        max_length=255,
        blank=True,
        verbose_name='Fact sheet 1 heading'
    )
    section_three_subsection_one_teaser = models.TextField(
        blank=True,
        verbose_name='Fact sheet 1 teaser'
    )
    section_three_subsection_one_body = MarkdownField(
        blank=True,
        null=True,
        verbose_name='Fact sheet 1 body'
    )

    section_three_subsection_two_heading = models.CharField(
        max_length=255,
        blank=True,
        verbose_name='Fact sheet 2 heading'
    )
    section_three_subsection_two_teaser = models.TextField(
        blank=True,
        verbose_name='Fact sheet 2 teaser'
    )
    section_three_subsection_two_body = MarkdownField(
        blank=True,
        null=True,
        verbose_name='Fact sheet 2 body'
    )

    related_page_one = models.ForeignKey(
        'wagtailcore.Page',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    related_page_two = models.ForeignKey(
        'wagtailcore.Page',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    related_page_three = models.ForeignKey(
        'wagtailcore.Page',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    project_opportunities_title = models.CharField(max_length=255, blank=True)
    related_opportunities_cta_text = models.CharField(
        max_length=255,
        blank=True
    )
    related_opportunities_cta_link = models.CharField(
        max_length=255,
        blank=True
    )


class InternationalSectorPage(BaseInternationalSectorPage):
    # DEPRECATED!
    # THIS HAS BEEN REPLACED IN USE BY InternationalInvestmentSectorPage
    class Meta:
        ordering = ['-heading']

    parent_page_types = ['great_international.InternationalTopicLandingPage']

    @classmethod
    def allowed_subpage_models(cls):
        return [
            InternationalSubSectorPage,
            InternationalArticlePage
        ]


class InternationalSubSectorPage(BaseInternationalSectorPage):
    # DEPRECATED!
    # THIS HAS BEEN REPLACED IN USE BY InternationalInvestmentSubSectorPage

    parent_page_types = ['great_international.InternationalSectorPage']


class InternationalInvestmentSectorPage(
    panels.InternationalInvestmentSectorPagePanels,
    BaseInternationalPage,
):
    # This model replaces InternationalSectorPage

    parent_page_types = ['great_international.InternationalTopicLandingPage']
    subpage_types = ['great_international.InternationalInvestmentSubSectorPage']

    tags = ParentalManyToManyField(
        snippets.Tag,
        blank=True,
    )
    hero_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    hero_video = models.ForeignKey(
        'wagtailmedia.Media',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
    )
    heading = models.CharField(
        max_length=255,
        verbose_name='Sector name',
    )
    standfirst = models.TextField(
        blank=True,
        help_text='Displayed below the sector name',
    )
    featured_description = models.TextField(
        blank=True,
        help_text='This is the description shown when the sector is featured on another page'
    )
    intro_text = MarkdownField(
        blank=True,
        null=True,
    )
    intro_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        on_delete=models.SET_NULL,
        related_name='+'
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
    contact_link_button_preamble = models.CharField(
        max_length=255,
        blank=True,
        help_text='eg: "Contact the sector lead"'
    )
    contact_link_button_label = models.CharField(
        max_length=255,
        blank=True,
    )
    related_opportunities_header = models.CharField(
        max_length=255,
        blank=True,
        help_text='You may want to phrase this to suit the kind of opportunities being featured, if not automatic'
    )
    manually_selected_related_opportunities = single_struct_block_stream_field_factory(
        field_name='related_opportunity',
        block_class_instance=PageChooserBlock(
            page_type='great_international.InvestmentOpportunityPage',
        ),
        null=True,
        blank=True,
        max_num=3,
        help_text=(
            'Max 3 will be shown. If none is specified, three will be automatically chosen '
            'based on matching sector, their priority_weighting and most recent creation'
        )
    )

    downpage_content = single_struct_block_stream_field_factory(
        field_name='content_section',
        block_class_instance=blocks.InternationalInvestmentSectorPageBlock(),
        null=True,
        blank=True,
    )

    early_opportunities_header = models.CharField(
        max_length=255,
        blank=True,
        help_text='Set to "Early investment opportunities" or customise based on the sector, as appropriate'
    )

    early_opportunities = single_struct_block_stream_field_factory(
        field_name='early_opportunity',
        block_class_instance=blocks.InternationalInvestmentSectorPageEarlyOpportunityBlock(),
        null=True,
        blank=True,
        max_num=6,
    )


class InternationalInvestmentSubSectorPage(
    panels.InternationalInvestmentSubSectorPagePanels,
    BaseInternationalPage,
):
    # This model replaces InternationalSubSectorPage

    # It is more of a category/snippet than an actual page right now,
    # but was originally created this way to potentially support its
    # own content. We're keeping this pattern for expediency in the
    # re-working of the site, in case we to need to easily add content for
    # sub-sectors in the future -- we just add fields to this model.

    parent_page_types = ['great_international.InternationalInvestmentSectorPage']
    heading = models.CharField(
        max_length=255,
        verbose_name='Sub-sector name',
    )


class InternationalHomePage(
    panels.InternationalHomePagePanels,
    WagtailAdminExclusivePageMixin,
    ServiceHomepageMixin,
    BaseInternationalPage,
):
    slug_identity = slugs.GREAT_HOME_INTERNATIONAL

    # ---- START FIELDS IN USE  ----
    hero_title = models.CharField(max_length=255)
    homepage_link_panels = StreamField(
        [
            ('link_panel', blocks.InternationalHomepagePanelBlock()),
        ],
        blank=True,
        null=True,
    )
    # For now the hero_image and CSS colour for the page background will
    # be hard-coded, but we can make it editable via the CMS

    # ---- END FIELDS IN USE  ----

    # ---- START UNUSED LEGACY FIELDS ----
    # ALL OF THE FIELDS BELOW ARE NOW REDUNDANT
    # However, removing them from the DB creates a gigantic migration that times
    # out on the PaaS because it takes 20 minutes to run.

    hero_subtitle = models.CharField(max_length=255, blank=True)
    hero_cta_text = models.CharField(
        max_length=255,
        null=True,
        blank=True
    )
    hero_cta_link = models.CharField(max_length=255, blank=True)
    hero_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
    )
    hero_video = models.ForeignKey(
        'wagtailmedia.Media',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
    )

    brexit_banner_text = MarkdownField(blank=True)

    # Old home page fields
    invest_title = models.CharField(max_length=255, blank=True)
    invest_content = MarkdownField(blank=True)
    invest_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
    )

    trade_title = models.CharField(max_length=255, blank=True)
    trade_content = MarkdownField(blank=True)
    trade_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
    )

    # features highlight
    section_two_heading = models.CharField(
        max_length=255,
        blank=True,
        verbose_name='Features highlight title'
    )
    section_two_teaser = models.TextField(
        blank=True,
        verbose_name='Features highlight summary'
    )

    section_two_subsection_one_icon = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        verbose_name='Features highlight 1 icon'
    )
    section_two_subsection_one_heading = models.CharField(
        max_length=255,
        blank=True,
        verbose_name='Features highlight 1 heading'
    )
    section_two_subsection_one_body = models.TextField(
        blank=True,
        verbose_name='Features highlight 1 body'
    )

    section_two_subsection_two_icon = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        verbose_name='Features highlight 2 icon'
    )
    section_two_subsection_two_heading = models.CharField(
        max_length=255,
        blank=True,
        verbose_name='Features highlight 2 heading'
    )
    section_two_subsection_two_body = models.TextField(
        blank=True,
        verbose_name='Features highlight 2 body'
    )

    section_two_subsection_three_icon = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        verbose_name='Features highlight 3 icon'
    )
    section_two_subsection_three_heading = models.CharField(
        blank=True,
        max_length=255,
        verbose_name='Features highlight 3 heading'
    )
    section_two_subsection_three_body = models.TextField(
        blank=True,
        verbose_name='Features highlight 3 body'
    )

    section_two_subsection_four_icon = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        verbose_name='Features highlight 4 icon'
    )
    section_two_subsection_four_heading = models.CharField(
        max_length=255,
        blank=True,
        verbose_name='Features highlight 4 heading'
    )
    section_two_subsection_four_body = models.TextField(
        blank=True,
        verbose_name='Features highlight 4 body'
    )

    section_two_subsection_five_icon = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        verbose_name='Features highlight 5 icon'
    )
    section_two_subsection_five_heading = models.CharField(
        max_length=255,
        blank=True,
        verbose_name='Features highlight 5 heading'
    )
    section_two_subsection_five_body = models.TextField(
        blank=True,
        verbose_name='Features highlight 5 body'
    )

    section_two_subsection_six_icon = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        verbose_name='Features highlight 6 icon'
    )
    section_two_subsection_six_heading = models.CharField(
        blank=True,
        max_length=255,
        verbose_name='Features highlight 6 heading'
    )
    section_two_subsection_six_body = models.TextField(
        blank=True,
        verbose_name='Features highlight 6 body'
    )

    # tariffs
    tariffs_title = models.CharField(max_length=255, blank=True)
    tariffs_description = MarkdownField(blank=True)
    tariffs_link = models.URLField(blank=True)
    tariffs_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    tariffs_call_to_action_text = models.CharField(max_length=255, blank=True)

    # featured links
    featured_links_title = models.CharField(
        blank=True,
        max_length=255,
    )
    featured_links_summary = models.TextField(blank=True)

    featured_link_one_heading = models.TextField(blank=True)
    featured_link_one_url = models.CharField(blank=True, max_length=255)
    featured_link_one_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    featured_link_two_heading = models.TextField(blank=True)
    featured_link_two_url = models.CharField(blank=True, max_length=255)
    featured_link_two_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    featured_link_three_heading = models.TextField(blank=True)
    featured_link_three_url = models.CharField(blank=True, max_length=255)
    featured_link_three_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    # news
    news_title = models.CharField(max_length=255, blank=True)
    related_page_one = models.ForeignKey(
        'wagtailcore.Page',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
    )
    related_page_two = models.ForeignKey(
        'wagtailcore.Page',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
    )
    related_page_three = models.ForeignKey(
        'wagtailcore.Page',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
    )

    study_in_uk_cta_text = models.CharField(max_length=255, blank=True)
    visit_uk_cta_text = models.CharField(max_length=255, blank=True)

    # New International home page fields

    is_new_page_ready = models.BooleanField(default=False, blank=True)

    ready_to_trade_story_one = MarkdownField(blank=True)
    ready_to_trade_story_two = MarkdownField(blank=True)
    ready_to_trade_story_three = MarkdownField(blank=True)

    benefits_of_uk_title = models.CharField(max_length=255, blank=True)
    benefits_of_uk_intro = models.TextField(blank=True)

    benefits_of_uk_one = MarkdownField(blank=True)
    benefits_of_uk_two = MarkdownField(blank=True)
    benefits_of_uk_three = MarkdownField(blank=True)
    benefits_of_uk_four = MarkdownField(blank=True)
    benefits_of_uk_five = MarkdownField(blank=True)
    benefits_of_uk_six = MarkdownField(blank=True)

    ready_for_brexit_title = models.CharField(max_length=255, blank=True)
    ready_for_brexit_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    ready_for_brexit_cta_text = models.CharField(max_length=255, blank=True)
    ready_for_brexit_cta_link = models.CharField(max_length=255, blank=True)

    how_dit_help_title = models.CharField(max_length=255, blank=True)

    related_how_dit_help_page_one = models.ForeignKey(
        'great_international.AboutDitServicesPage',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
    )

    related_how_dit_help_page_two = models.ForeignKey(
        'great_international.AboutDitServicesPage',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
    )

    related_how_dit_help_page_three = models.ForeignKey(
        'great_international.AboutDitServicesPage',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
    )

    how_we_help_title = models.CharField(max_length=255, blank=True)
    how_we_help_intro = models.TextField(blank=True)
    how_we_help_one_icon = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    how_we_help_one_text = MarkdownField(blank=True)
    how_we_help_two_icon = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    how_we_help_two_text = MarkdownField(blank=True)
    how_we_help_three_icon = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    how_we_help_three_text = MarkdownField(blank=True)

    ways_of_doing_business_title = models.CharField(max_length=255, blank=True)
    related_page_expand = models.ForeignKey(
        'wagtailcore.Page',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
    )
    related_page_expand_description = models.TextField(max_length=255, blank=True)
    related_page_invest_capital = models.ForeignKey(
        'wagtailcore.Page',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
    )
    related_page_invest_capital_description = models.TextField(max_length=255, blank=True)
    related_page_buy = models.ForeignKey(
        'wagtailcore.Page',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
    )
    related_page_buy_description = models.TextField(max_length=255, blank=True)

    case_study_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    case_study_title = models.CharField(max_length=255, blank=True)
    case_study_text = models.TextField(blank=True)
    case_study_cta_text = models.CharField(max_length=255, blank=True)
    case_study_cta_link = models.CharField(max_length=255, blank=True)

    industries_section_title = models.CharField(max_length=255, blank=True)
    industries_section_intro = models.TextField(blank=True)
    industries_section_industry_label = models.CharField(max_length=255, blank=True)
    industries_section_cta_text = models.CharField(max_length=255, blank=True)
    industries_section_cta_link = models.CharField(max_length=255, blank=True)

    link_to_section_title = models.CharField(max_length=255, blank=True)
    link_to_section_intro = models.TextField(blank=True)
    link_to_section_one = MarkdownField(blank=True)
    link_to_section_one_cta_text = models.CharField(max_length=255, blank=True)
    link_to_section_one_cta_link = models.CharField(max_length=255, blank=True)
    link_to_section_two = MarkdownField(blank=True)
    link_to_section_two_cta_text = models.CharField(max_length=255, blank=True)
    link_to_section_two_cta_link = models.CharField(max_length=255, blank=True)
    link_to_section_three = MarkdownField(blank=True)
    link_to_section_three_cta_text = models.CharField(max_length=255, blank=True)
    link_to_section_three_cta_link = models.CharField(max_length=255, blank=True)

    # ---- END UNUSED LEGACY FIELDS ----

    @classmethod
    def allowed_subpage_models(cls):
        from . import investment_atlas as investment_atlas_models
        return [
            InternationalArticleListingPage,
            InternationalTopicLandingPage,
            InternationalCuratedTopicLandingPage,
            InternationalGuideLandingPage,
            InternationalEUExitFormPage,
            InternationalEUExitFormSuccessPage,
            AboutDitLandingPage,
            AboutUkLandingPage,
            capital_invest_models.InternationalCapitalInvestLandingPage,
            capital_invest_models.CapitalInvestOpportunityListingPage,
            capital_invest_models.CapitalInvestRegionPage,
            invest_models.InvestInternationalHomePage,
            investment_atlas_models.InvestmentAtlasLandingPage,
            fas_models.InternationalTradeHomePage,
            AboutUkWhyChooseTheUkPage
        ]


class InternationalArticlePage(panels.InternationalArticlePagePanels, BaseInternationalPage):
    parent_page_types = [
        'great_international.InternationalArticleListingPage',
        'great_international.InternationalCampaignPage',
        'great_international.InternationalCuratedTopicLandingPage',
        'great_international.InternationalGuideLandingPage',
        'great_international.InternationalSectorPage',  # deprecated
        'great_international.InternationalInvestmentSectorPage',  # new, replaces InternationalSectorPage
        'great_international.AboutUkWhyChooseTheUkPage',
        'great_international.WhyInvestInTheUKPage',
        'great_international.InvestmentGeneralContentPage',
    ]
    subpage_types = []

    type_of_article = models.TextField(choices=ARTICLE_TYPES, null=True)

    article_title = models.TextField()
    article_subheading = models.TextField(
        blank=True,
        help_text="This is a subheading that displays "
                  "below the main title on the article page"
    )
    article_teaser = models.TextField(
        blank=True,
        help_text="This is a subheading that displays when the article "
                  "is featured on another page"
    )
    article_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    article_video = models.ForeignKey(
        'wagtailmedia.Media',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    article_body_text = MarkdownField()

    cta_title = models.CharField(
        max_length=255,
        blank=True,
        verbose_name='CTA title'
    )
    cta_teaser = models.TextField(
        blank=True,
        verbose_name='CTA teaser'
    )

    cta_link_label = models.CharField(
        max_length=255,
        blank=True,
        verbose_name='CTA link label'
    )
    cta_link = models.CharField(
        max_length=255,
        blank=True,
        verbose_name='CTA link'
    )

    related_page_one = models.ForeignKey(
        'great_international.InternationalArticlePage',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
    )
    related_page_two = models.ForeignKey(
        'great_international.InternationalArticlePage',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
    )
    related_page_three = models.ForeignKey(
        'great_international.InternationalArticlePage',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
    )
    tags = ParentalManyToManyField(snippets.Tag, blank=True)


class InternationalArticleListingPage(panels.InternationalArticleListingPagePanels, BaseInternationalPage):
    parent_page_types = [
        'great_international.InternationalHomePage',
        'great_international.InternationalTopicLandingPage'
    ]
    subpage_types = [
        'great_international.InternationalArticlePage',
        'great_international.InternationalCampaignPage',
    ]

    landing_page_title = models.CharField(max_length=255)
    hero_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    hero_teaser = models.CharField(max_length=255, null=True, blank=True)
    list_teaser = MarkdownField(null=True, blank=True)
    tags = ParentalManyToManyField(snippets.Tag, blank=True)

    @property
    def articles_count(self):
        return self.get_descendants().type(
            InternationalArticlePage
        ).live().count()


class InternationalCampaignPage(panels.InternationalCampaignPagePanels, BaseInternationalPage):
    parent_page_types = [
        'great_international.InternationalArticleListingPage',
        'great_international.InternationalTopicLandingPage',
    ]
    subpage_types = [
        'great_international.InternationalArticlePage'
    ]
    view_path = 'campaigns/'

    campaign_subheading = models.CharField(
        max_length=255,
        blank=True,
        help_text="This is a subheading that displays "
                  "when the article is featured on another page"
    )
    campaign_teaser = models.CharField(max_length=255, null=True, blank=True)
    campaign_heading = models.CharField(max_length=255)
    campaign_hero_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    section_one_heading = models.CharField(max_length=255)
    section_one_intro = MarkdownField()
    section_one_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    selling_point_one_icon = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    selling_point_one_heading = models.CharField(max_length=255)
    selling_point_one_content = MarkdownField()

    selling_point_two_icon = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    selling_point_two_heading = models.CharField(
        max_length=255,
        null=True,
        blank=True,
    )
    selling_point_two_content = MarkdownField(null=True, blank=True)

    selling_point_three_icon = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    selling_point_three_heading = models.CharField(
        max_length=255,
        null=True,
        blank=True
    )
    selling_point_three_content = MarkdownField(null=True, blank=True)

    section_one_contact_button_url = models.CharField(
        max_length=255,
        null=True,
        blank=True
    )
    section_one_contact_button_text = models.CharField(
        max_length=255,
        null=True,
        blank=True
    )

    section_two_heading = models.CharField(max_length=255)
    section_two_intro = MarkdownField()

    section_two_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    section_two_contact_button_url = models.CharField(
        max_length=255,
        null=True,
        blank=True
    )
    section_two_contact_button_text = models.CharField(
        max_length=255,
        null=True,
        blank=True
    )

    related_content_heading = models.CharField(max_length=255)
    related_content_intro = MarkdownField()

    related_page_one = models.ForeignKey(
        'great_international.InternationalArticlePage',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
    )
    related_page_two = models.ForeignKey(
        'great_international.InternationalArticlePage',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
    )
    related_page_three = models.ForeignKey(
        'great_international.InternationalArticlePage',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
    )

    cta_box_message = models.CharField(max_length=255)
    cta_box_button_url = models.CharField(max_length=255)
    cta_box_button_text = models.CharField(max_length=255)

    tags = ParentalManyToManyField(snippets.Tag, blank=True)


class InternationalTopicLandingPage(panels.InternationalTopicLandingPagePanels, BaseInternationalPage):
    parent_page_types = [
        'great_international.InternationalHomePage',
        'great_international.AboutUkLandingPage',
        'great_international.InvestmentAtlasLandingPage',
        'great_international.WhyInvestInTheUKPage',
    ]
    subpage_types = [
        'great_international.InternationalArticleListingPage',
        'great_international.InternationalCampaignPage',
        # 'great_international.InternationalSectorPage',  # OLD CapInvest sector page - deprecated
        'great_international.InternationalInvestmentSectorPage',  # NEW Atlas sector page
    ]

    landing_page_title = models.CharField(max_length=255)

    hero_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    hero_teaser = models.CharField(max_length=255, null=True, blank=True)
    tags = ParentalManyToManyField(snippets.Tag, blank=True)
    hero_video = models.ForeignKey(
        'wagtailmedia.Media',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
    )

    related_page_one = models.ForeignKey(
        'wagtailcore.Page',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    related_page_two = models.ForeignKey(
        'wagtailcore.Page',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    related_page_three = models.ForeignKey(
        'wagtailcore.Page',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )


class InternationalCuratedTopicLandingPage(panels.InternationalCuratedTopicLandingPagePanels, BaseInternationalPage):
    parent_page_types = ['great_international.InternationalHomePage']
    subpage_types = []

    display_title = models.CharField(max_length=255, blank=True, null=True)

    hero_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    teaser = models.CharField(max_length=255)

    feature_section_heading = models.CharField(max_length=255)

    feature_one_heading = models.CharField(max_length=100)
    feature_one_image = models.ForeignKey(
        'wagtailimages.Image',
        verbose_name="image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    feature_one_content = MarkdownField(verbose_name="content")

    feature_two_heading = models.CharField(max_length=100)
    feature_two_image = models.ForeignKey(
        'wagtailimages.Image',
        verbose_name="image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    feature_two_content = MarkdownField(verbose_name="content")

    feature_three_heading = models.CharField(max_length=100)
    feature_three_image = models.ForeignKey(
        'wagtailimages.Image',
        verbose_name="image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    feature_three_url = models.URLField(verbose_name="URL")

    feature_four_heading = models.CharField(max_length=100)
    feature_four_image = models.ForeignKey(
        'wagtailimages.Image',
        verbose_name="image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    feature_four_url = models.URLField(verbose_name="URL")

    feature_five_heading = models.CharField(max_length=100)
    feature_five_image = models.ForeignKey(
        'wagtailimages.Image',
        verbose_name="image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    feature_five_url = models.URLField(verbose_name="URL")

    tags = ParentalManyToManyField(snippets.Tag, blank=True)


class InternationalGuideLandingPage(panels.InternationalGuideLandingPagePanels, BaseInternationalPage):
    parent_page_types = [
        'great_international.InternationalHomePage',
        'great_international.InvestInternationalHomePage',
        'great_international.InternationalCapitalInvestLandingPage'
    ]
    subpage_types = ['great_international.InternationalArticlePage']

    display_title = models.CharField(max_length=255)

    hero_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    teaser = models.CharField(max_length=255)

    section_one_content = MarkdownField(verbose_name="content")
    section_one_image = models.ForeignKey(
        'wagtailimages.Image',
        verbose_name="image",
        null=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    section_one_image_caption = models.CharField(
        verbose_name="image caption",
        max_length=100,
        blank=True,
        null=True,
    )

    section_two_heading = models.CharField(
        verbose_name="heading",
        max_length=100
    )
    section_two_teaser = models.TextField(verbose_name="teaser")
    section_two_button_text = models.CharField(
        verbose_name="button text",
        max_length=100
    )
    section_two_button_url = models.CharField(
        verbose_name="button URL",
        max_length=255
    )
    section_two_image = models.ForeignKey(
        'wagtailimages.Image',
        verbose_name="image",
        null=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    guides_section_heading = models.CharField(
        verbose_name="section heading",
        max_length=100,
    )

    section_three_title = models.CharField(max_length=255, blank=True)
    section_three_text = models.TextField(blank=True)
    section_three_cta_text = models.CharField(max_length=255, blank=True)
    section_three_cta_link = models.CharField(max_length=255, blank=True)

    tags = ParentalManyToManyField(snippets.Tag, blank=True)


class InternationalEUExitFormPage(
    WagtailAdminExclusivePageMixin,
    BaseInternationalPage,
    metaclass=FormPageMetaClass
):
    # metaclass creates <fild_name>_label and <field_name>_help_text
    form_field_names = [
        'first_name',
        'last_name',
        'email',
        'organisation_type',
        'company_name',
        'country',
        'city',
        'comment',
    ]

    full_path_override = '/eu-exit-news/contact/'
    slug_identity = slugs.EUEXIT_INTERNATIONAL_FORM

    subpage_types = [
        'great_international.InternationalEUExitFormSuccessPage']

    breadcrumbs_label = models.CharField(max_length=50)
    heading = models.CharField(max_length=255)
    body_text = MarkdownField()
    submit_button_text = models.CharField(max_length=50)
    disclaimer = models.TextField(max_length=500)

    content_panels_before_form = \
        panels.InternationalEUExitFormPagePanels.content_panels_before_form
    content_panels_after_form = \
        panels.InternationalEUExitFormPagePanels.content_panels_after_form
    settings_panels = panels.InternationalEUExitFormPagePanels.settings_panels


class InternationalEUExitFormSuccessPage(
    panels.InternationalEUExitFormSuccessPagePanels, WagtailAdminExclusivePageMixin, BaseInternationalPage,
):
    full_path_override = '/eu-exit-news/contact/success/'
    slug_identity = slugs.EUEXIT_FORM_SUCCESS

    parent_page_types = ['great_international.InternationalEUExitFormPage']

    breadcrumbs_label = models.CharField(max_length=50)
    heading = models.CharField(
        max_length=255,
        verbose_name='Title'
    )
    body_text = models.CharField(
        max_length=255,
        verbose_name='Body text',
    )
    next_title = models.CharField(
        max_length=255,
        verbose_name='Title'
    )
    next_body_text = models.CharField(
        max_length=255,
        verbose_name='Body text',
    )


class AboutDitLandingPage(panels.AboutDitLandingPagePanels, BaseInternationalPage):
    parent_page_types = ['great_international.InternationalHomePage']
    subpage_types = [
        'great_international.AboutDitServicesPage'
    ]

    breadcrumbs_label = models.CharField(max_length=255)
    hero_title = models.CharField(max_length=255)
    hero_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    intro = models.TextField(blank=True)
    section_one_content = MarkdownField(blank=True)
    section_one_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        on_delete=models.SET_NULL,
        related_name='+',
        blank=True
    )

    how_dit_help_title = models.CharField(max_length=255, blank=True)

    related_page_one = models.ForeignKey(
        'great_international.AboutDitServicesPage',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
    )

    related_page_two = models.ForeignKey(
        'great_international.AboutDitServicesPage',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
    )

    related_page_three = models.ForeignKey(
        'great_international.AboutDitServicesPage',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
    )

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


class AboutDitServiceField(panels.AboutDitServiceFieldPanels, models.Model):
    icon = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        on_delete=models.SET_NULL,
        related_name='+',
        blank=True
    )
    title = models.CharField(max_length=255, blank=True)
    summary = models.TextField(max_length=255, blank=True)
    link_text = models.CharField(max_length=255,
                                 blank=True,
                                 verbose_name='Link text')
    link_url = models.CharField(max_length=255,
                                blank=True,
                                verbose_name='Link URL')

    class Meta:
        abstract = True


class AboutDitServicesFields(Orderable, AboutDitServiceField):
    page = ParentalKey(
        'great_international.AboutDitServicesPage',
        on_delete=models.CASCADE,
        related_name='about_dit_services_fields',
        blank=True,
        null=True,
    )


class AboutDitServicesPage(panels.AboutDitServicesPagePanels, BaseInternationalPage):
    parent_page_types = [
        'great_international.AboutDitLandingPage',
        'great_international.InternationalCapitalInvestLandingPage',
        'great_international.InternationalTradeHomePage',
        'great_international.InvestInternationalHomePage'
    ]

    breadcrumbs_label = models.CharField(max_length=255)
    hero_title = models.CharField(max_length=255)
    hero_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    teaser = MarkdownField(
        null=True,
        verbose_name='',
        blank=True
    )
    featured_description = models.TextField(
        null=True,
        blank=True,
        help_text="This will be used when this page is featured as a "
                  "card on another page i.e. the About DIT landing page"
    )

    ebook_section_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        on_delete=models.SET_NULL,
        related_name='+',
        blank=True
    )
    ebook_section_image_alt_text = models.CharField(
        max_length=255,
        blank=True,
        help_text="Description of image for screenreaders"
    )
    ebook_section_body = MarkdownField(null=True, blank=True)
    ebook_section_cta_text = models.CharField(max_length=255, blank=True)
    ebook_section_cta_link = models.CharField(max_length=255, blank=True)

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

    contact_us_section_title = models.CharField(
        max_length=255,
        blank=True,
        verbose_name='Title'
    )
    contact_us_section_summary = MarkdownField(
        null=True,
        blank=True,
        verbose_name='Summary'
    )
    contact_us_section_cta_text = models.CharField(
        max_length=255,
        blank=True,
        verbose_name='CTA text'
    )
    contact_us_section_cta_link = models.CharField(
        max_length=255,
        blank=True,
        verbose_name='CTA URL'
    )


class AboutUkLandingPage(panels.AboutUkLandingPagePanels, BaseInternationalPage):
    parent_page_types = ['great_international.InternationalHomePage']
    subpage_types = [
        'great_international.AboutUkWhyChooseTheUkPage',
        'great_international.AboutUkRegionListingPage',
        'great_international.InternationalTopicLandingPage'
    ]

    breadcrumbs_label = models.CharField(max_length=255)
    hero_title = models.CharField(max_length=255)
    hero_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    intro = MarkdownField(blank=True)

    why_choose_uk_title = models.CharField(max_length=255, blank=True)
    why_choose_uk_content = MarkdownField(blank=True)
    why_choose_uk_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        on_delete=models.SET_NULL,
        related_name='+',
        blank=True
    )
    why_choose_uk_cta_text = models.CharField(max_length=255, blank=True)
    why_choose_uk_cta_link = models.CharField(max_length=255, blank=True)

    industries_section_title = models.CharField(max_length=255, blank=True)
    industries_section_intro = MarkdownField(blank=True)
    industries_section_cta_text = models.CharField(max_length=255, blank=True)
    industries_section_cta_link = models.CharField(max_length=255, blank=True)

    regions_section_title = models.CharField(max_length=255, blank=True)
    regions_section_intro = MarkdownField(blank=True)

    scotland = models.ForeignKey(
        'wagtailcore.Page',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
    )
    scotland_text = models.CharField(max_length=255, blank=True)

    northern_ireland = models.ForeignKey(
        'wagtailcore.Page',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
    )
    northern_ireland_text = models.CharField(max_length=255, blank=True)

    north_england = models.ForeignKey(
        'wagtailcore.Page',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
    )
    north_england_text = models.CharField(max_length=255, blank=True)

    wales = models.ForeignKey(
        'wagtailcore.Page',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
    )
    wales_text = models.CharField(max_length=255, blank=True)

    midlands = models.ForeignKey(
        'wagtailcore.Page',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
    )
    midlands_text = models.CharField(max_length=255, blank=True)

    south_england = models.ForeignKey(
        'wagtailcore.Page',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
    )
    south_england_text = models.CharField(max_length=255, blank=True)

    regions_section_cta_text = models.CharField(max_length=255, blank=True)
    regions_section_cta_link = models.CharField(max_length=255, blank=True)

    how_we_help_title = models.CharField(max_length=255, blank=True)
    how_we_help_intro = MarkdownField(blank=True)

    how_we_help_one_icon = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        on_delete=models.SET_NULL,
        related_name='+',
        blank=True
    )
    how_we_help_one_title = models.CharField(max_length=255, blank=True)
    how_we_help_one_text = models.TextField(max_length=255, blank=True)
    how_we_help_two_icon = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        on_delete=models.SET_NULL,
        related_name='+',
        blank=True
    )
    how_we_help_two_title = models.CharField(max_length=255, blank=True)
    how_we_help_two_text = models.TextField(max_length=255, blank=True)
    how_we_help_three_icon = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        on_delete=models.SET_NULL,
        related_name='+',
        blank=True
    )
    how_we_help_three_title = models.CharField(max_length=255, blank=True)
    how_we_help_three_text = models.TextField(max_length=255, blank=True)
    how_we_help_four_icon = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        on_delete=models.SET_NULL,
        related_name='+',
        blank=True
    )
    how_we_help_four_title = models.CharField(max_length=255, blank=True)
    how_we_help_four_text = models.TextField(max_length=255, blank=True)
    how_we_help_five_icon = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        on_delete=models.SET_NULL,
        related_name='+',
        blank=True
    )
    how_we_help_five_title = models.CharField(max_length=255, blank=True)
    how_we_help_five_text = models.TextField(max_length=255, blank=True)
    how_we_help_six_icon = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        on_delete=models.SET_NULL,
        related_name='+',
        blank=True
    )
    how_we_help_six_title = models.CharField(max_length=255, blank=True)
    how_we_help_six_text = models.TextField(max_length=255, blank=True)

    how_we_help_cta_text = models.CharField(max_length=255, blank=True)
    how_we_help_cta_link = models.CharField(max_length=255, blank=True)

    ebook_section_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        on_delete=models.SET_NULL,
        related_name='+',
        blank=True
    )
    ebook_section_image_alt_text = models.CharField(
        max_length=255,
        blank=True,
        help_text="Description of image for screenreaders"
    )
    ebook_section_title = models.CharField(max_length=255, blank=True)
    ebook_section_body = MarkdownField(null=True, blank=True)
    ebook_section_cta_text = models.CharField(max_length=255, blank=True)
    ebook_section_cta_link = models.ForeignKey(
        'wagtaildocs.Document',
        null=True,
        on_delete=models.SET_NULL,
        related_name='+',
        blank=True
    )

    contact_title = models.CharField(max_length=255, blank=True)
    contact_text = MarkdownField(blank=True)
    contact_cta_text = models.CharField(max_length=255, blank=True)
    contact_cta_link = models.CharField(max_length=255, blank=True)


class AboutUkRegionListingPage(
    panels.AboutUkRegionListingPagePanels,
    WagtailAdminExclusivePageMixin,
    BaseInternationalPage
):

    slug_identity = 'regions'

    parent_page_types = [
        'great_international.AboutUkLandingPage',
        'great_international.InvestmentAtlasLandingPage',
    ]
    subpage_types = [
        'great_international.AboutUkRegionPage',
    ]

    breadcrumbs_label = models.CharField(max_length=255)
    hero_title = models.CharField(max_length=255)
    hero_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        on_delete=models.SET_NULL,
        related_name='+',
        blank=True
    )
    hero_video = models.ForeignKey(
        'wagtailmedia.Media',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
    )

    intro = MarkdownField(blank=True)

    contact_title = models.CharField(max_length=255, blank=True)
    contact_text = MarkdownField(blank=True)
    contact_cta_text = models.CharField(max_length=255, blank=True)
    contact_cta_link = models.CharField(max_length=255, blank=True)

    related_page_one = models.ForeignKey(
        'wagtailcore.Page',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    related_page_two = models.ForeignKey(
        'wagtailcore.Page',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    related_page_three = models.ForeignKey(
        'wagtailcore.Page',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )


class AboutUkRegionPage(panels.AboutUkRegionPagePanels, BaseInternationalPage):
    parent_page_types = ['great_international.AboutUkRegionListingPage']

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
    region_summary_section_strapline = models.TextField(
        max_length=255,
        blank=True,
        help_text="Displayd above Region Section Summary Intro"
    )
    region_summary_section_intro = models.TextField(blank=True)
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
    case_study_text = MarkdownField(blank=True)
    case_study_cta_text = models.CharField(max_length=255, blank=True)
    case_study_cta_link = models.CharField(max_length=255, blank=True)

    contact_title = models.CharField(max_length=255, blank=True)
    contact_text = MarkdownField(blank=True)
    contact_cta_link = models.CharField(max_length=255, blank=True)
    contact_cta_text = models.CharField(max_length=255, blank=True)


class AboutUkArticleField(panels.AboutUkArticleFieldPanels, models.Model):
    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        on_delete=models.SET_NULL,
        related_name='+',
        blank=True
    )
    title = models.CharField(max_length=255, blank=True)
    summary = MarkdownField(blank=True)
    link_text = models.CharField(max_length=255,
                                 blank=True,
                                 verbose_name='Link text')
    link_url = models.CharField(max_length=255,
                                blank=True,
                                verbose_name='Link URL')

    class Meta:
        abstract = True


class AboutUkArticlesFields(Orderable, AboutUkArticleField):
    page = ParentalKey(
        'great_international.AboutUkWhyChooseTheUkPage',
        on_delete=models.CASCADE,
        related_name='about_uk_articles_fields',
        blank=True,
        null=True,
    )


class AboutUkWhyChooseTheUkPage(panels.AboutUkWhyChooseTheUkPagePanels, BaseInternationalPage):
    parent_page_types = [
        'great_international.AboutUkLandingPage',
        'great_international.InternationalHomePage',
        'great_international.InvestmentAtlasLandingPage'
    ]
    subpage_types = ['great_international.InternationalArticlePage']

    breadcrumbs_label = models.CharField(max_length=255)
    hero_title = models.CharField(max_length=255)
    hero_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    teaser = MarkdownField(
        null=True,
        verbose_name='',
        blank=True
    )

    primary_contact_cta_text = models.CharField(max_length=255, blank=True)
    primary_contact_cta_link = models.CharField(max_length=255, blank=True)

    section_one_body = MarkdownField(
        null=True,
        blank=True
    )
    section_one_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        on_delete=models.SET_NULL,
        related_name='+',
        blank=True
    )
    section_one_video = models.ForeignKey(
        'wagtailmedia.Media',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text="Section one image will be used over this video, please ensure section one image is empty "
                  "in order for this video to be used instead."
    )

    statistic_1_heading = models.CharField(max_length=255, blank=True)
    statistic_1_number = models.CharField(max_length=255, blank=True)
    statistic_1_smallprint = models.CharField(max_length=255, blank=True)

    statistic_2_heading = models.CharField(max_length=255, blank=True)
    statistic_2_number = models.CharField(max_length=255, blank=True)
    statistic_2_smallprint = models.CharField(max_length=255, blank=True)

    statistic_3_heading = models.CharField(max_length=255, blank=True)
    statistic_3_number = models.CharField(max_length=255, blank=True)
    statistic_3_smallprint = models.CharField(max_length=255, blank=True)

    statistic_4_heading = models.CharField(max_length=255, blank=True)
    statistic_4_number = models.CharField(max_length=255, blank=True)
    statistic_4_smallprint = models.CharField(max_length=255, blank=True)

    statistic_5_heading = models.CharField(max_length=255, blank=True)
    statistic_5_number = models.CharField(max_length=255, blank=True)
    statistic_5_smallprint = models.CharField(max_length=255, blank=True)

    statistic_6_heading = models.CharField(max_length=255, blank=True)
    statistic_6_number = models.CharField(max_length=255, blank=True)
    statistic_6_smallprint = models.CharField(max_length=255, blank=True)

    ebook_section_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        on_delete=models.SET_NULL,
        related_name='+',
        blank=True
    )
    ebook_section_image_alt_text = models.CharField(
        max_length=255,
        blank=True,
        help_text="Description of image for screenreaders"
    )
    ebook_section_title = models.CharField(max_length=255, blank=True)
    ebook_section_body = MarkdownField(null=True, blank=True)
    ebook_section_cta_text = models.CharField(max_length=255, blank=True)
    ebook_section_cta_link = models.CharField(max_length=255, blank=True)

    how_dit_help_title = models.CharField(max_length=255, blank=True)

    related_page_one = models.ForeignKey(
        'great_international.AboutDitServicesPage',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
    )

    related_page_two = models.ForeignKey(
        'great_international.AboutDitServicesPage',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
    )

    related_page_three = models.ForeignKey(
        'great_international.AboutDitServicesPage',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
    )

    contact_us_section_title = models.CharField(
        max_length=255,
        blank=True,
        verbose_name='Title'
    )
    contact_us_section_summary = MarkdownField(
        null=True,
        blank=True,
        verbose_name='Summary'
    )
    contact_us_section_cta_text = models.CharField(
        max_length=255,
        blank=True,
        verbose_name='CTA text'
    )
    contact_us_section_cta_link = models.CharField(
        max_length=255,
        blank=True,
        verbose_name='CTA URL'
    )


class WhyInvestInTheUKPage(
    panels.WhyInvestInTheUKPagePanels,
    BaseInternationalPage
):
    parent_page_types = ['great_international.InvestmentAtlasLandingPage', ]
    subpage_types = ['great_international.InternationalArticlePage']

    hero_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        on_delete=models.SET_NULL,
        related_name='+',
        blank=True,
        help_text='Main page hero image, above the title'
    )
    hero_video = models.ForeignKey(
        'wagtailmedia.Media',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
    )
    strapline = models.CharField(
        max_length=200,
        blank=False,
        null=True,
        help_text=(
            'A single sentence which goes beneath the page title'
        )
    )
    introduction = MarkdownField(
        blank=False,
        null=True,
    )
    intro_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        on_delete=models.SET_NULL,
        related_name='+',
        blank=True,
        help_text='Goes beside the intro text'
    )

    uk_strength_title = models.CharField(max_length=255, blank=True)
    uk_strength_intro = models.CharField(max_length=1000, blank=True)
    uk_strength_panels = StreamField(
        [
            ('article_panel', blocks.InternationalUKStrengthPanelBlock()),
        ],
        blank=True,
        null=True,
    )
