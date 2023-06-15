from directory_constants import slugs
from django.db import models
from modelcluster.fields import ParentalKey, ParentalManyToManyField
from wagtail.blocks import PageChooserBlock
from wagtail.fields import StreamField
from wagtail.models import Orderable
from core.constants import ARTICLE_TYPES
from core.fields import single_struct_block_stream_field_factory
from core.mixins import ServiceHomepageMixin
from core.model_fields import MarkdownField
from core.models import WagtailAdminExclusivePageMixin
from core import snippets
from great_international.blocks import great_international as blocks
from great_international.panels import great_international as panels
from . import find_a_supplier as fas_models
from .base import BaseInternationalPage


class InternationalInvestmentSectorPage(
    panels.InternationalInvestmentSectorPagePanels,
    BaseInternationalPage,
):
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

    hero_title = models.CharField(max_length=255)
    hero_video = models.ForeignKey(
        'wagtailmedia.Media',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
    )
    homepage_link_panels = StreamField(
        [
            ('link_panel', blocks.InternationalHomepagePanelBlock()),
        ],
        use_json_field=True,
        blank=True,
        null=True,
    )

    @classmethod
    def allowed_subpage_models(cls):
        from . import investment_atlas as investment_atlas_models
        return [
            InternationalArticleListingPage,
            InternationalTopicLandingPage,
            investment_atlas_models.InvestmentAtlasLandingPage,
            fas_models.InternationalTradeHomePage,
        ]


class InternationalArticlePage(panels.InternationalArticlePagePanels, BaseInternationalPage):

    parent_page_types = [
        'great_international.InternationalArticleListingPage',
        'great_international.InternationalCampaignPage',
        'great_international.InternationalInvestmentSectorPage',
        'great_international.WhyInvestInTheUKPage',
        'great_international.InvestmentGeneralContentPage',
    ]

    subpage_types = []

    type_of_article = models.TextField(choices=ARTICLE_TYPES, null=True, blank=True)

    hero_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
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
        'great_international.InvestmentAtlasLandingPage',
        'great_international.WhyInvestInTheUKPage',
    ]
    subpage_types = [
        'great_international.InternationalArticleListingPage',
        'great_international.InternationalCampaignPage',
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
        'great_international.InternationalTradeHomePage',
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


class AboutUkRegionListingPage(
    panels.AboutUkRegionListingPagePanels,
    WagtailAdminExclusivePageMixin,
    BaseInternationalPage
):

    slug_identity = 'regions'

    parent_page_types = [
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
        use_json_field=True,
        blank=True,
        null=True,
    )
