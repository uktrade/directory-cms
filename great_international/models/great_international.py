from django.db import models
from django.utils.text import slugify

from modelcluster.fields import ParentalManyToManyField, ParentalKey
from wagtail.core.models import Orderable

from directory_constants import slugs

from core.model_fields import MarkdownField

from core.models import (
    ExclusivePageMixin,
    WagtailAdminExclusivePageMixin,
    FormPageMetaClass,
)
from core.mixins import ServiceHomepageMixin

from export_readiness import snippets

from great_international.panels import great_international as panels

from . import invest as invest_models
from . import capital_invest as capital_invest_models
from . import find_a_supplier as fas_models
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

    parent_page_types = ['great_international.InternationalSectorPage']


class InternationalHomePage(
    panels.InternationalHomePagePanels, WagtailAdminExclusivePageMixin, ServiceHomepageMixin,
    BaseInternationalPage,
):
    slug_identity = slugs.GREAT_HOME_INTERNATIONAL

    hero_title = models.CharField(max_length=255)
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

    invest_title = models.CharField(max_length=255)
    invest_content = MarkdownField(blank=True)
    invest_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
    )

    trade_title = models.CharField(max_length=255)
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
    tariffs_title = models.CharField(max_length=255)
    tariffs_description = MarkdownField()
    tariffs_link = models.URLField()
    tariffs_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    tariffs_call_to_action_text = models.CharField(max_length=255)

    # featured links
    featured_links_title = models.CharField(
        blank=True,
        max_length=255,
    )
    featured_links_summary = models.TextField(blank=True)

    featured_link_one_heading = models.TextField(blank=True)
    featured_link_one_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    featured_link_two_heading = models.TextField(blank=True)
    featured_link_two_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    featured_link_three_heading = models.TextField(blank=True)
    featured_link_three_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    # news
    news_title = models.CharField(max_length=255)
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

    study_in_uk_cta_text = models.CharField(max_length=255)
    visit_uk_cta_text = models.CharField(max_length=255)

    @classmethod
    def allowed_subpage_models(cls):
        return [
            InternationalArticleListingPage,
            InternationalTopicLandingPage,
            InternationalCuratedTopicLandingPage,
            InternationalGuideLandingPage,
            InternationalRegionPage,
            InternationalEUExitFormPage,
            InternationalEUExitFormSuccessPage,
            AboutDitLandingPage,
            AboutUkLandingPage,
            capital_invest_models.InternationalCapitalInvestLandingPage,
            capital_invest_models.CapitalInvestOpportunityListingPage,
            capital_invest_models.CapitalInvestRegionPage,
            invest_models.InvestInternationalHomePage,
            fas_models.InternationalTradeHomePage
        ]


class InternationalHomePageOld(
    panels.InternationalHomePageOldPanels, ExclusivePageMixin, ServiceHomepageMixin,
    BaseInternationalPage,
):
    slug_identity = slugs.GREAT_HOME_INTERNATIONAL_OLD
    subpage_types = []

    hero_title = models.CharField(max_length=255)
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

    invest_title = models.CharField(max_length=255)
    invest_content = MarkdownField(blank=True)
    invest_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
    )

    trade_title = models.CharField(max_length=255)
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
    tariffs_title = models.CharField(max_length=255)
    tariffs_description = MarkdownField()
    tariffs_link = models.URLField()
    tariffs_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    tariffs_call_to_action_text = models.CharField(max_length=255)

    # featured links
    featured_links_title = models.CharField(
        blank=True,
        max_length=255,
    )
    featured_links_summary = models.TextField(blank=True)

    featured_link_one_heading = models.TextField(blank=True)
    featured_link_one_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    featured_link_two_heading = models.TextField(blank=True)
    featured_link_two_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    featured_link_three_heading = models.TextField(blank=True)
    featured_link_three_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    # news
    news_title = models.CharField(max_length=255)
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

    study_in_uk_cta_text = models.CharField(max_length=255)
    visit_uk_cta_text = models.CharField(max_length=255)


# !!! TO BE REMOVED !!!
class InternationalRegionPage(panels.InternationalRegionPagePanels, BaseInternationalPage):
    parent_page_types = ['great_international.InternationalHomePage']
    subpage_types = []

    tags = ParentalManyToManyField(snippets.Tag, blank=True)

    def save(self, *args, **kwargs):
        return super().save(*args, **kwargs)


# !!! TO BE REMOVED !!!
class InternationalLocalisedFolderPage(panels.InternationalLocalisedFolderPagePanels, BaseInternationalPage):
    subpage_types = [
        'great_international.InternationalArticlePage',
        'great_international.InternationalCampaignPage'
    ]

    def save(self, *args, **kwargs):
        if self.pk is None:
            self.slug = slugify(f'{self.slug}-{self.get_parent().slug}')
        return super().save(*args, **kwargs)


class InternationalArticlePage(panels.InternationalArticlePagePanels, BaseInternationalPage):
    parent_page_types = [
        'great_international.InternationalArticleListingPage',
        'great_international.InternationalCampaignPage',
        'great_international.InternationalCuratedTopicLandingPage',
        'great_international.InternationalGuideLandingPage',
        'great_international.InternationalSectorPage'
    ]
    subpage_types = []

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
    article_body_text = MarkdownField()

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
    parent_page_types = ['great_international.InternationalHomePage']
    subpage_types = [
        'great_international.InternationalArticleListingPage',
        'great_international.InternationalCampaignPage',
        'great_international.InternationalSectorPage',
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
    parent_page_types = ['great_international.InternationalHomePage']
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
    parent_page_types = ['great_international.AboutDitLandingPage']

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
    teaser_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        on_delete=models.SET_NULL,
        related_name='+',
        blank=True
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
    regions_section_content = MarkdownField(blank=True)
    regions_section_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        on_delete=models.SET_NULL,
        related_name='+',
        blank=True
    )
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
    panels.AboutUkRegionListingPagePanels, WagtailAdminExclusivePageMixin, BaseInternationalPage
):

    slug_identity = 'regions'

    parent_page_types = ['great_international.AboutUkLandingPage']
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

    intro = MarkdownField(blank=True)


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


class AboutUkArticleField(panels.AboutUkArticleFieldPanels, models.Model):
    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        on_delete=models.SET_NULL,
        related_name='+',
        blank=True
    )
    title = models.CharField(max_length=255, blank=True)
    summary = models.TextField(blank=True)
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
    parent_page_types = ['great_international.AboutUkLandingPage']

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
    ebook_section_pdf_link = models.ForeignKey(
        'wagtaildocs.Document',
        null=True,
        on_delete=models.SET_NULL,
        related_name='+',
        blank=True
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
