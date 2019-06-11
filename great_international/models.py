from wagtail.documents.edit_handlers import DocumentChooserPanel

from directory_constants.constants import cms
from django.forms import Textarea, CheckboxSelectMultiple
from django.utils.text import slugify
from modelcluster.fields import ParentalManyToManyField
from wagtail.admin.edit_handlers import (
    HelpPanel, FieldPanel, FieldRowPanel, MultiFieldPanel, PageChooserPanel,
    InlinePanel, ObjectList
)
from wagtail.images.edit_handlers import ImageChooserPanel

from django.db import models
from wagtailmedia.widgets import AdminMediaChooser

from core.helpers import make_translated_interface
from core.model_fields import MarkdownField

from core.models import (
    BasePage,
    ExclusivePageMixin,
    WagtailAdminExclusivePageMixin,
    FormPageMetaClass,
    ServiceMixin,
)
from core.mixins import ServiceHomepageMixin
from core.panels import SearchEngineOptimisationPanel
from export_readiness.models import Tag
from wagtail.core.models import Orderable
from modelcluster.fields import ParentalKey


class BaseInternationalPage(BasePage):
    service_name_value = cms.GREAT_INTERNATIONAL

    class Meta:
        abstract = True


class GreatInternationalApp(
    ExclusivePageMixin, ServiceMixin, BaseInternationalPage
):
    slug_identity = 'great-international-app'

    @classmethod
    def get_required_translatable_fields(cls):
        return []

    @classmethod
    def allowed_subpage_models(cls):
        return [
            InternationalArticleListingPage,
            InternationalTopicLandingPage,
            InternationalCuratedTopicLandingPage,
            InternationalGuideLandingPage,
            InternationalRegionPage,
            InternationalHomePage,
            InternationalEUExitFormPage,
            InternationalEUExitFormSuccessPage,
            InternationalCapitalInvestLandingPage,
            CapitalInvestOpportunityListingPage,
            CapitalInvestRegionPage,
            InvestInternationalHomePage,
            InvestHighPotentialOpportunityDetailPage,
            InvestHighPotentialOpportunityFormPage,
            InvestHighPotentialOpportunityFormSuccessPage
        ]


class InternationalSectorPage(BaseInternationalPage):
    class Meta:
        ordering = ['-heading']

    parent_page_types = ['great_international.InternationalTopicLandingPage']
    subpage_types = []

    tags = ParentalManyToManyField(Tag, blank=True)

    heading = models.CharField(max_length=255, verbose_name='Sector name')
    sub_heading = models.TextField(blank=True)
    hero_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    heading_teaser = models.TextField(blank=True, verbose_name='Introduction')

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

    content_panels = [
        MultiFieldPanel(
            heading='Heading',
            children=[
                FieldPanel('heading'),
                FieldPanel('sub_heading'),
                ImageChooserPanel('hero_image'),
                FieldPanel('heading_teaser')
            ]

        ),
        MultiFieldPanel(
            heading='Unique selling points',
            children=[
                HelpPanel(
                    'Use H2 (##) markdown for the three subheadings.'
                    ' Required fields for section to show: 3 Unique Selling '
                    'Points Markdown'),
                FieldRowPanel(
                    [
                        FieldPanel('section_one_body'),
                        MultiFieldPanel(
                            [
                                ImageChooserPanel('section_one_image'),
                                FieldPanel('section_one_image_caption'),
                                FieldPanel('section_one_image_caption_company')
                            ]
                        )
                    ]
                )
            ]
        ),
        MultiFieldPanel(
            heading='Statistics',
            children=[
                FieldRowPanel(
                    [
                        MultiFieldPanel(
                            [
                                FieldPanel('statistic_1_number'),
                                FieldPanel('statistic_1_heading'),
                                FieldPanel('statistic_1_smallprint')
                            ]
                        ),
                        MultiFieldPanel(
                            [
                                FieldPanel('statistic_2_number'),
                                FieldPanel('statistic_2_heading'),
                                FieldPanel('statistic_2_smallprint')
                            ]
                        ),
                        MultiFieldPanel(
                            [
                                FieldPanel('statistic_3_number'),
                                FieldPanel('statistic_3_heading'),
                                FieldPanel('statistic_3_smallprint')
                            ]
                        ),
                        MultiFieldPanel(
                            [
                                FieldPanel('statistic_4_number'),
                                FieldPanel('statistic_4_heading'),
                                FieldPanel('statistic_4_smallprint')
                            ]
                        ),
                        MultiFieldPanel(
                            [
                                FieldPanel('statistic_5_number'),
                                FieldPanel('statistic_5_heading'),
                                FieldPanel('statistic_5_smallprint')
                            ]
                        ),
                        MultiFieldPanel(
                            [
                                FieldPanel('statistic_6_number'),
                                FieldPanel('statistic_6_heading'),
                                FieldPanel('statistic_6_smallprint')
                            ]
                        ),
                    ]
                )
            ]
        ),
        MultiFieldPanel(
            heading='Spotlight',
            children=[
                FieldPanel('section_two_heading'),
                FieldPanel('section_two_teaser'),
                HelpPanel(
                    'Each icon needs a heading for it to show on the page.'),
                FieldRowPanel(
                    [
                        MultiFieldPanel(
                            [
                                ImageChooserPanel(
                                    'section_two_subsection_one_icon'),
                                FieldPanel(
                                    'section_two_subsection_one_heading'),
                                FieldPanel(
                                    'section_two_subsection_one_body')
                            ]
                        ),
                        MultiFieldPanel(
                            [
                                ImageChooserPanel(
                                    'section_two_subsection_two_icon'),
                                FieldPanel(
                                    'section_two_subsection_two_heading'),
                                FieldPanel(
                                    'section_two_subsection_two_body')
                            ]
                        ),
                        MultiFieldPanel(
                            [
                                ImageChooserPanel(
                                    'section_two_subsection_three_icon'),
                                FieldPanel(
                                    'section_two_subsection_three_heading'),
                                FieldPanel(
                                    'section_two_subsection_three_body')
                            ]
                        )
                    ]
                )
            ]
        ),
        MultiFieldPanel(
            heading='Case Study',
            classname='collapsible',
            children=[
                HelpPanel('Required fields for section to show: '
                          'Case Study Image, Case Study Title'),
                ImageChooserPanel('case_study_image'),
                FieldPanel('case_study_title'),
                FieldPanel('case_study_description'),
                FieldPanel('case_study_cta_text'),
                HelpPanel('Cta\'s require both text and a link to show '
                          'on page. '),
                PageChooserPanel(
                    'case_study_cta_page',
                    [
                        'great_international.InternationalArticlePage',
                        'great_international.InternationalCampaignPage',
                    ]),
                ImageChooserPanel('case_study_image')
            ]
        ),
        MultiFieldPanel(
            heading='Fact Sheets',
            classname='collapsible collapsed',
            children=[
                FieldPanel('section_three_heading'),
                FieldPanel('section_three_teaser'),
                FieldRowPanel(
                    [
                        MultiFieldPanel(
                            [
                                FieldPanel(
                                    'section_three_subsection_one_heading'),
                                FieldPanel(
                                    'section_three_subsection_one_teaser'),
                                HelpPanel(
                                    'For accessibility reasons, use only '
                                    '"#### [Your text here]" for subheadings '
                                    'in this markdown field'),
                                FieldPanel(
                                    'section_three_subsection_one_body')
                            ]
                        ),
                        MultiFieldPanel(
                            [
                                FieldPanel(
                                    'section_three_subsection_two_heading'),
                                FieldPanel(
                                    'section_three_subsection_two_teaser'),
                                HelpPanel(
                                    'For accessibility reasons, use only '
                                    '"#### [Your text here]" for subheadings '
                                    'in this markdown field'),
                                FieldPanel(
                                    'section_three_subsection_two_body')
                            ]
                        )
                    ]
                )
            ]
        ),
        MultiFieldPanel(
            heading='Related articles',
            children=[
                FieldRowPanel([
                    PageChooserPanel(
                        'related_page_one',
                        [
                            'great_international.InternationalArticlePage',
                            'great_international.InternationalCampaignPage',
                        ]),
                    PageChooserPanel(
                        'related_page_two',
                        [
                            'great_international.InternationalArticlePage',
                            'great_international.InternationalCampaignPage',
                        ]),
                    PageChooserPanel(
                        'related_page_three',
                        [
                            'great_international.InternationalArticlePage',
                            'great_international.InternationalCampaignPage',
                        ]),
                ])
            ]
        ),
        MultiFieldPanel(
            heading='Project Opportunities',
            classname='collapsible ',
            children=[
                FieldPanel('project_opportunities_title'),
                HelpPanel('Prioritised opportunity pages that link to this '
                          'sector will display here. Required fields for '
                          'section to show: Project Opportunities Title, 1 '
                          'Prioritised Opportunity Related to this sector'),
            ]
        ),
        SearchEngineOptimisationPanel()
    ]

    settings_panels = [
        FieldPanel('title_en_gb'),
        FieldPanel('slug'),
        FieldPanel('uses_tree_based_routing'),
        FieldPanel('tags', widget=CheckboxSelectMultiple)
    ]

    edit_handler = make_translated_interface(
        content_panels=content_panels,
        settings_panels=settings_panels
    )


class InternationalHomePage(
    WagtailAdminExclusivePageMixin, ServiceHomepageMixin, BaseInternationalPage
):
    slug_identity = cms.GREAT_HOME_INTERNATIONAL_SLUG
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

    content_panels = [
        MultiFieldPanel(
            heading="Hero Section",
            children=[
                FieldPanel('hero_title'),
                FieldPanel('hero_subtitle'),
                FieldPanel("hero_cta_text"),
                FieldPanel("hero_cta_link"),
                ImageChooserPanel("hero_image")
            ]
        ),
        MultiFieldPanel(
            heading="Featured Cards",
            children=[
                FieldRowPanel([
                    MultiFieldPanel(
                        heading='Invest Card',
                        children=[
                            FieldPanel('invest_title'),
                            FieldPanel('invest_content'),
                            ImageChooserPanel('invest_image')
                        ]
                    ),
                    MultiFieldPanel(
                        heading='Trade Card',
                        children=[
                            FieldPanel('trade_title'),
                            FieldPanel('trade_content'),
                            ImageChooserPanel('trade_image')
                        ]
                    ),
                ]),
            ]
        ),

        MultiFieldPanel(
            heading='Features highlight',
            children=[
                FieldPanel('section_two_heading'),
                FieldPanel('section_two_teaser'),
                FieldRowPanel([
                    MultiFieldPanel(
                        children=[
                            ImageChooserPanel(
                                'section_two_subsection_one_icon'
                            ),
                            FieldPanel('section_two_subsection_one_heading'),
                            FieldPanel('section_two_subsection_one_body')
                        ]),
                    MultiFieldPanel(
                        children=[
                            ImageChooserPanel(
                                'section_two_subsection_two_icon'
                            ),
                            FieldPanel('section_two_subsection_two_heading'),
                            FieldPanel('section_two_subsection_two_body')
                        ]),
                    MultiFieldPanel(
                        children=[
                            ImageChooserPanel(
                                'section_two_subsection_three_icon'
                            ),
                            FieldPanel('section_two_subsection_three_heading'),
                            FieldPanel('section_two_subsection_three_body')
                        ]),
                    MultiFieldPanel(
                        children=[
                            ImageChooserPanel(
                                'section_two_subsection_four_icon'
                            ),
                            FieldPanel('section_two_subsection_four_heading'),
                            FieldPanel('section_two_subsection_four_body')
                        ]),
                    MultiFieldPanel(
                        children=[
                            ImageChooserPanel(
                                'section_two_subsection_five_icon'
                            ),
                            FieldPanel('section_two_subsection_five_heading'),
                            FieldPanel('section_two_subsection_five_body')
                        ]),
                    MultiFieldPanel(
                        children=[
                            ImageChooserPanel(
                                'section_two_subsection_six_icon'),
                            FieldPanel('section_two_subsection_six_heading'
                                       ),
                            FieldPanel('section_two_subsection_six_body')
                        ])
                ])
            ]),

        MultiFieldPanel(
            heading='Tariffs',
            children=[
                FieldPanel('tariffs_title'),
                FieldPanel('tariffs_description'),
                FieldPanel('tariffs_link'),
                ImageChooserPanel('tariffs_image'),
                FieldPanel('tariffs_call_to_action_text')
            ]
        ),

        MultiFieldPanel(
            heading='Featured links',
            children=[
                FieldPanel('featured_links_title'),
                FieldPanel('featured_links_summary'),
                FieldRowPanel([
                    MultiFieldPanel(
                        children=[
                            FieldPanel('featured_link_one_heading'),
                            ImageChooserPanel('featured_link_one_image')
                        ]),
                    MultiFieldPanel(
                        children=[
                            FieldPanel('featured_link_two_heading'),
                            ImageChooserPanel('featured_link_two_image')
                        ]),
                    MultiFieldPanel(
                        children=[
                            FieldPanel('featured_link_three_heading'),
                            ImageChooserPanel('featured_link_three_image')
                        ])
                ])]
        ),

        MultiFieldPanel(
            heading='News section',
            children=[
                FieldPanel('news_title'),
                FieldRowPanel([
                    PageChooserPanel(
                        'related_page_one',
                        [
                            'great_international.InternationalArticlePage',
                            'great_international.InternationalCampaignPage',
                        ]),
                    PageChooserPanel(
                        'related_page_two',
                        [
                            'great_international.InternationalArticlePage',
                            'great_international.InternationalCampaignPage',
                        ]),
                    PageChooserPanel(
                        'related_page_three',
                        [
                            'great_international.InternationalArticlePage',
                            'great_international.InternationalCampaignPage',
                        ]),
                ])
            ]
        ),

        MultiFieldPanel(
            heading='Featured CTA\'s',
            children=[
                FieldRowPanel([
                    MultiFieldPanel(
                        heading="Study in the UK",
                        children=[
                            FieldPanel('study_in_uk_cta_text')
                        ]
                    ),
                    MultiFieldPanel(
                        heading="Visit the UK",
                        children=[
                            FieldPanel('visit_uk_cta_text')
                        ]
                    ),
                ]),
            ]
        ),

        SearchEngineOptimisationPanel(),
    ]

    settings_panels = [
        FieldPanel('title_en_gb'),
        FieldPanel('slug'),
        FieldPanel('uses_tree_based_routing'),
    ]

    edit_handler = make_translated_interface(
        content_panels=content_panels,
        settings_panels=settings_panels
    )


class InternationalRegionPage(BaseInternationalPage):
    parent_page_types = ['great_international.GreatInternationalApp']
    subpage_types = [
        'great_international.InternationalLocalisedFolderPage'
    ]

    tags = ParentalManyToManyField(Tag, blank=True)

    settings_panels = [
        FieldPanel('title_en_gb'),
        FieldPanel('slug'),
        FieldPanel('uses_tree_based_routing'),
        FieldPanel('tags', widget=CheckboxSelectMultiple)
    ]

    def save(self, *args, **kwargs):
        return super().save(*args, **kwargs)


class InternationalLocalisedFolderPage(BaseInternationalPage):
    parent_page_types = ['great_international.InternationalRegionPage']
    subpage_types = [
        'great_international.InternationalArticlePage',
        'great_international.InternationalCampaignPage'
    ]

    settings_panels = [
        FieldPanel('title_en_gb'),
        FieldPanel('slug'),
        FieldPanel('uses_tree_based_routing'),
    ]

    def save(self, *args, **kwargs):
        if self.pk is None:
            self.slug = slugify(f'{self.slug}-{self.get_parent().slug}')
        return super().save(*args, **kwargs)


class InternationalArticlePage(BaseInternationalPage):
    parent_page_types = [
        'great_international.InternationalArticleListingPage',
        'great_international.InternationalCampaignPage',
        'great_international.InternationalLocalisedFolderPage',
        'great_international.InternationalCuratedTopicLandingPage',
        'great_international.InternationalGuideLandingPage',
    ]
    subpage_types = []

    article_title = models.TextField()
    article_subheading = models.TextField(
        blank=True,
        help_text="This is a subheading that displays "
                  "below the main title on the article page"
    )
    article_teaser = models.TextField(
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
    tags = ParentalManyToManyField(Tag, blank=True)

    content_panels = [
        FieldPanel('article_title'),
        MultiFieldPanel(
            heading='Article content',
            children=[
                FieldPanel('article_subheading'),
                FieldPanel('article_teaser'),
                ImageChooserPanel('article_image'),
                FieldPanel('article_body_text')
            ]
        ),
        MultiFieldPanel(
            heading='Related articles',
            children=[
                FieldRowPanel([
                    PageChooserPanel(
                        'related_page_one',
                        'great_international.InternationalArticlePage'),
                    PageChooserPanel(
                        'related_page_two',
                        'great_international.InternationalArticlePage'),
                    PageChooserPanel(
                        'related_page_three',
                        'great_international.InternationalArticlePage'),
                ]),
            ]
        ),
        SearchEngineOptimisationPanel(),
    ]

    settings_panels = [
        FieldPanel('title_en_gb'),
        FieldPanel('slug'),
        FieldPanel('uses_tree_based_routing'),
        FieldPanel('tags', widget=CheckboxSelectMultiple)
    ]

    edit_handler = make_translated_interface(
        content_panels=content_panels,
        settings_panels=settings_panels
    )


class InternationalArticleListingPage(BaseInternationalPage):
    parent_page_types = [
        'great_international.GreatInternationalApp',
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
    tags = ParentalManyToManyField(Tag, blank=True)

    @property
    def articles_count(self):
        return self.get_descendants().type(
            InternationalArticlePage
        ).live().count()

    content_panels = [
        FieldPanel('landing_page_title'),
        MultiFieldPanel(
            heading='Hero',
            children=[
                ImageChooserPanel('hero_image'),
                FieldPanel('hero_teaser')
            ]
        ),
        FieldPanel('list_teaser'),
        SearchEngineOptimisationPanel(),
    ]

    settings_panels = [
        FieldPanel('title_en_gb'),
        FieldPanel('slug'),
        FieldPanel('uses_tree_based_routing'),
        FieldPanel('tags', widget=CheckboxSelectMultiple)
    ]

    edit_handler = make_translated_interface(
        content_panels=content_panels,
        settings_panels=settings_panels
    )


class InternationalCampaignPage(BaseInternationalPage):
    parent_page_types = [
        'great_international.InternationalArticleListingPage',
        'great_international.InternationalTopicLandingPage',
        'great_international.InternationalLocalisedFolderPage'
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

    tags = ParentalManyToManyField(Tag, blank=True)

    content_panels = [
        MultiFieldPanel(
            heading='Hero section',
            children=[
                FieldPanel('campaign_heading'),
                FieldPanel('campaign_subheading'),
                FieldPanel('campaign_teaser'),
                ImageChooserPanel('campaign_hero_image'),
            ]
        ),
        MultiFieldPanel(
            heading='Section one',
            children=[
                FieldPanel('section_one_heading'),
                FieldPanel('section_one_intro'),
                ImageChooserPanel('section_one_image'),
                FieldRowPanel([
                    MultiFieldPanel(
                        children=[
                            ImageChooserPanel('selling_point_one_icon'),
                            FieldPanel('selling_point_one_heading'),
                            FieldPanel('selling_point_one_content'),
                        ]
                    ),
                    MultiFieldPanel(
                        children=[
                            ImageChooserPanel('selling_point_two_icon'),
                            FieldPanel('selling_point_two_heading'),
                            FieldPanel('selling_point_two_content'),
                        ]
                    ),
                    MultiFieldPanel(
                        children=[
                            ImageChooserPanel('selling_point_three_icon'),
                            FieldPanel('selling_point_three_heading'),
                            FieldPanel('selling_point_three_content'),
                        ]
                    ),
                ]),
                FieldRowPanel([
                    FieldPanel('section_one_contact_button_text'),
                    FieldPanel('section_one_contact_button_url'),
                ])
            ]
        ),
        MultiFieldPanel(
            heading='Section two',
            children=[
                FieldPanel('section_two_heading'),
                FieldPanel('section_two_intro'),
                ImageChooserPanel('section_two_image'),
                FieldRowPanel([
                    FieldPanel('section_two_contact_button_text'),
                    FieldPanel('section_two_contact_button_url'),
                ])
            ]
        ),
        MultiFieldPanel(
            heading='Related content section',
            children=[
                FieldPanel('related_content_heading'),
                FieldPanel('related_content_intro'),
                FieldRowPanel([
                    PageChooserPanel(
                        'related_page_one',
                        'great_international.InternationalArticlePage'),
                    PageChooserPanel(
                        'related_page_two',
                        'great_international.InternationalArticlePage'),
                    PageChooserPanel(
                        'related_page_three',
                        'great_international.InternationalArticlePage'),
                ])
            ]
        ),
        MultiFieldPanel(
            heading='Contact box',
            children=[
                FieldRowPanel([
                    FieldPanel('cta_box_message', widget=Textarea),
                    MultiFieldPanel([
                        FieldPanel('cta_box_button_url'),
                        FieldPanel('cta_box_button_text'),
                    ])
                ])
            ]
        ),
        SearchEngineOptimisationPanel(),
    ]

    settings_panels = [
        FieldPanel('title_en_gb'),
        FieldPanel('slug'),
        FieldPanel('uses_tree_based_routing'),
        FieldPanel('tags', widget=CheckboxSelectMultiple)
    ]

    edit_handler = make_translated_interface(
        content_panels=content_panels,
        settings_panels=settings_panels
    )


class InternationalTopicLandingPage(BaseInternationalPage):
    parent_page_types = ['great_international.GreatInternationalApp']
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
    tags = ParentalManyToManyField(Tag, blank=True)

    content_panels = [
        FieldPanel('landing_page_title'),
        MultiFieldPanel(
            heading='Hero',
            children=[
                ImageChooserPanel('hero_image'),
                FieldPanel('hero_teaser')
            ]
        ),
        SearchEngineOptimisationPanel(),
    ]

    settings_panels = [
        FieldPanel('title_en_gb'),
        FieldPanel('slug'),
        FieldPanel('uses_tree_based_routing'),
        FieldPanel('tags', widget=CheckboxSelectMultiple)
    ]

    edit_handler = make_translated_interface(
        content_panels=content_panels,
        settings_panels=settings_panels
    )


class InternationalCuratedTopicLandingPage(BaseInternationalPage):
    parent_page_types = ['great_international.GreatInternationalApp']
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

    tags = ParentalManyToManyField(Tag, blank=True)

    content_panels = [
        FieldPanel('display_title'),
        ImageChooserPanel('hero_image'),
        FieldPanel('teaser'),
        MultiFieldPanel(
            heading="featured content section",
            children=[
                FieldPanel('feature_section_heading'),
                FieldRowPanel([
                    MultiFieldPanel([
                        FieldPanel('feature_one_heading'),
                        ImageChooserPanel('feature_one_image'),
                        FieldPanel('feature_one_content'),
                    ]),
                    MultiFieldPanel([
                        FieldPanel('feature_two_heading'),
                        ImageChooserPanel('feature_two_image'),
                        FieldPanel('feature_two_content'),
                    ]),
                ]),
                FieldRowPanel([
                    MultiFieldPanel([
                        FieldPanel('feature_three_heading'),
                        ImageChooserPanel('feature_three_image'),
                        FieldPanel('feature_three_url'),
                    ]),
                    MultiFieldPanel([
                        FieldPanel('feature_four_heading'),
                        ImageChooserPanel('feature_four_image'),
                        FieldPanel('feature_four_url'),
                    ]),
                    MultiFieldPanel([
                        FieldPanel('feature_five_heading'),
                        ImageChooserPanel('feature_five_image'),
                        FieldPanel('feature_five_url'),
                    ]),
                ]),
            ]
        )
    ]

    settings_panels = [
        FieldPanel('title_en_gb'),
        SearchEngineOptimisationPanel(),
        FieldPanel('slug'),
        FieldPanel('uses_tree_based_routing'),
        FieldPanel('tags', widget=CheckboxSelectMultiple)
    ]

    edit_handler = make_translated_interface(
        content_panels=content_panels,
        settings_panels=settings_panels
    )


class InternationalGuideLandingPage(BaseInternationalPage):
    parent_page_types = ['great_international.GreatInternationalApp']
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

    tags = ParentalManyToManyField(Tag, blank=True)

    content_panels = [
        FieldPanel('display_title'),
        ImageChooserPanel('hero_image'),
        FieldPanel('teaser'),
        MultiFieldPanel(
            heading="Attractive features",
            children=[
                FieldPanel('section_one_content'),
                HelpPanel(
                    'For accessibility reasons, use only '
                    '"#### [Your text here]" for subheadings '
                    'in this markdown field'
                ),
                ImageChooserPanel('section_one_image'),
                FieldPanel('section_one_image_caption'),
            ]
        ),
        MultiFieldPanel(
            heading="Feature banner",
            children=[
                FieldPanel('section_two_heading'),
                FieldPanel('section_two_teaser'),
                FieldPanel('section_two_button_text'),
                FieldPanel('section_two_button_url'),
                ImageChooserPanel('section_two_image'),
            ]
        ),
        MultiFieldPanel(
            heading="Guides section",
            children=[
                FieldPanel('guides_section_heading'),
            ]
        ),
        MultiFieldPanel(
            heading="Section three",
            children=[
                FieldPanel('section_three_title'),
                FieldPanel('section_three_text'),
                FieldPanel('section_three_cta_text'),
                FieldPanel('section_three_cta_link'),
            ]
        )
    ]

    settings_panels = [
        FieldPanel('title_en_gb'),
        SearchEngineOptimisationPanel(),
        FieldPanel('slug'),
        FieldPanel('uses_tree_based_routing'),
        FieldPanel('tags', widget=CheckboxSelectMultiple)
    ]

    edit_handler = make_translated_interface(
        content_panels=content_panels,
        settings_panels=settings_panels
    )


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
    slug_identity = cms.GREAT_EUEXIT_INTERNATIONAL_FORM_SLUG

    subpage_types = [
        'great_international.InternationalEUExitFormSuccessPage']

    breadcrumbs_label = models.CharField(max_length=50)
    heading = models.CharField(max_length=255)
    body_text = MarkdownField()
    submit_button_text = models.CharField(max_length=50)
    disclaimer = models.TextField(max_length=500)

    content_panels_before_form = [
        MultiFieldPanel(
            heading='Hero',
            children=[
                FieldPanel('breadcrumbs_label'),
                FieldPanel('heading'),
                FieldPanel('body_text'),
            ]
        ),
    ]
    content_panels_after_form = [
        FieldPanel('disclaimer', widget=Textarea),
        FieldPanel('submit_button_text'),
        SearchEngineOptimisationPanel(),
    ]

    settings_panels = [
        FieldPanel('title_en_gb'),
        FieldPanel('slug'),
    ]


class InternationalEUExitFormSuccessPage(
    WagtailAdminExclusivePageMixin, BaseInternationalPage
):
    full_path_override = '/eu-exit-news/contact/success/'
    slug_identity = cms.GREAT_EUEXIT_FORM_SUCCESS_SLUG

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

    content_panels = [
        FieldPanel('breadcrumbs_label'),
        MultiFieldPanel(
            heading='heading',
            children=[
                FieldPanel('heading'),
                FieldPanel('body_text'),
            ]
        ),
        MultiFieldPanel(
            heading='Next steps',
            children=[
                FieldPanel('next_title'),
                FieldPanel('next_body_text'),
            ]
        ),
        SearchEngineOptimisationPanel(),
    ]

    settings_panels = [
        FieldPanel('title_en_gb'),
        FieldPanel('slug'),
    ]


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
    Orderable,
    HomesInEnglandCardField
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
        'great_international.CapitalInvestRegionPage',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    panels = [
        PageChooserPanel(
            'related_region',
            [
                'great_international.'
                'CapitalInvestRegionPage'
            ]
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
    WagtailAdminExclusivePageMixin, BaseInternationalPage
):
    slug_identity = 'capital-invest'

    parent_page_types = ['great_international.GreatInternationalApp']

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

    contact_section_title = models.CharField(max_length=255, blank=True)
    contact_section_text = models.CharField(max_length=255, blank=True)
    contact_section_cta_text = models.CharField(max_length=255, blank=True)

    content_panels = [
        MultiFieldPanel(
            heading="Hero",
            children=[
                ImageChooserPanel('hero_image'),
                FieldPanel('hero_title'),
                FieldPanel('hero_subheading'),
                FieldPanel('hero_subtitle'),
                FieldPanel('hero_cta_text')
            ]
        ),
        MultiFieldPanel(
            heading="Reason to invest in the UK section",
            classname='collapsible',
            children=[
                HelpPanel('Required fields for section to show: '
                          'Reason to Invest Title, Reason to Invest Content'),
                FieldPanel('reason_to_invest_section_title'),
                FieldPanel('reason_to_invest_section_intro'),
                FieldPanel('reason_to_invest_section_content'),
                ImageChooserPanel('reason_to_invest_section_image'),
                FieldPanel('how_we_help_title'),
                FieldPanel('how_we_help_intro'),
                HelpPanel('Each icon requires corresponding text to show '
                          'on page'),
                FieldRowPanel([
                    MultiFieldPanel([
                        ImageChooserPanel('how_we_help_one_icon'),
                        FieldPanel('how_we_help_one_text'),
                    ]),
                    MultiFieldPanel([
                        ImageChooserPanel('how_we_help_two_icon'),
                        FieldPanel('how_we_help_two_text'),
                    ]),
                ]),
                FieldRowPanel([
                    MultiFieldPanel([
                        ImageChooserPanel('how_we_help_three_icon'),
                        FieldPanel('how_we_help_three_text'),
                    ]),
                    MultiFieldPanel([
                        ImageChooserPanel('how_we_help_four_icon'),
                        FieldPanel('how_we_help_four_text'),
                    ]),
                ]),
            ]
        ),
        MultiFieldPanel(
            heading="Investment Opportunities by regions",
            classname='collapsible',
            children=[
                HelpPanel('Required fields for section to show: '
                          'Region Opportunity Title, 1 Related Region'),
                FieldPanel('region_ops_section_title'),
                FieldPanel('region_ops_section_intro'),
                InlinePanel(
                    'added_region_card_fields',
                    label="Region card fields"
                ),
            ]
        ),
        MultiFieldPanel(
            heading="Informative banner",
            children=[
                FieldPanel('banner_information')
            ],
        ),
        MultiFieldPanel(
            heading="Related region pages",
            classname='collapsible collapsed',
            children=[
                HelpPanel('Please use this to link to a related region, '
                          'rather than adding in manually the region title, '
                          'image and text in the above section when the '
                          'capital invest region pages are available'),
                InlinePanel(
                    'added_regions',
                    label="Related Regions"
                ),
            ]
        ),
        MultiFieldPanel(
            heading="Energy Sector",
            classname='collapsible',
            children=[
                HelpPanel('Required fields for section to show: '
                          'Energy Sector Title, Energy Sector Content'),
                FieldPanel('energy_sector_title'),
                FieldPanel('energy_sector_content'),
                ImageChooserPanel('energy_sector_image'),
                HelpPanel('CTA requires text and PDF to show on teh page.'),
                FieldPanel('energy_sector_cta_text'),
                DocumentChooserPanel('energy_sector_pdf_document'),
            ]
        ),
        MultiFieldPanel(
            heading="Homes in England Section",
            classname='collapsible',
            children=[
                HelpPanel('Required fields for section to show: '
                          'Homes In England Section Title, Title and PDF '
                          'for each card'),
                FieldPanel('homes_in_england_section_title'),
                InlinePanel(
                    'added_homes_in_england_card_fields',
                    label="Homes In England cards"
                )
            ]
        ),
        MultiFieldPanel(
            heading="Contact Section",
            classname='collapsible collapsed',
            children=[
                HelpPanel('Required fields for section to show: '
                          'Contact Title, Contact Text'),
                FieldPanel('contact_section_title'),
                FieldPanel('contact_section_text'),
                FieldPanel('contact_section_cta_text')
            ]
        ),
    ]

    settings_panels = [
        FieldPanel('title_en_gb'),
        FieldPanel('slug'),
        FieldPanel('uses_tree_based_routing'),
    ]

    edit_handler = make_translated_interface(
        content_panels=content_panels,
        settings_panels=settings_panels
    )


class CapitalInvestRegionPage(BaseInternationalPage):
    parent_page_types = ['great_international.GreatInternationalApp']

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

    content_panels = [
        FieldPanel('breadcrumbs_label'),
        MultiFieldPanel(
            heading="Hero",
            children=[
                FieldPanel('hero_title'),
                ImageChooserPanel('hero_image'),
            ],
        ),
        FieldPanel('featured_description'),
        MultiFieldPanel(
            heading="Region summary",
            children=[
                HelpPanel('Required fields for section to show: '
                          'Region Summary Section Intro'),
                ImageChooserPanel('region_summary_section_image'),
                FieldPanel('region_summary_section_intro'),
                FieldPanel('region_summary_section_content'),
            ],
        ),
        MultiFieldPanel(
            heading="Investment opportunities",
            children=[
                FieldPanel('investment_opps_title'),
                FieldPanel('investment_opps_intro'),
            ]
        ),
        MultiFieldPanel(
            heading="Economics Statistics",
            children=[
                HelpPanel('Required fields for section to show: '
                          'Economics Data Title'),
                FieldPanel('economics_data_title'),
                FieldRowPanel([
                    MultiFieldPanel([
                        FieldPanel('economics_stat_1_number'),
                        FieldPanel('economics_stat_1_heading'),
                        FieldPanel('economics_stat_1_smallprint'),
                    ]),
                    MultiFieldPanel([
                        FieldPanel('economics_stat_2_number'),
                        FieldPanel('economics_stat_2_heading'),
                        FieldPanel('economics_stat_2_smallprint'),
                    ]),
                    MultiFieldPanel([
                        FieldPanel('economics_stat_3_number'),
                        FieldPanel('economics_stat_3_heading'),
                        FieldPanel('economics_stat_3_smallprint'),
                    ]),
                    MultiFieldPanel([
                        FieldPanel('economics_stat_4_number'),
                        FieldPanel('economics_stat_4_heading'),
                        FieldPanel('economics_stat_4_smallprint'),
                    ]),
                ]),
            ],
        ),
        MultiFieldPanel(
            heading="Location Statistics",
            children=[
                HelpPanel('Required fields for section to show: '
                          'Location Data Title'),
                FieldPanel('location_data_title'),
                FieldRowPanel([
                    MultiFieldPanel([
                        FieldPanel('location_stat_1_number'),
                        FieldPanel('location_stat_1_heading'),
                        FieldPanel('location_stat_1_smallprint'),
                    ]),
                    MultiFieldPanel([
                        FieldPanel('location_stat_2_number'),
                        FieldPanel('location_stat_2_heading'),
                        FieldPanel('location_stat_2_smallprint'),
                    ]),
                    MultiFieldPanel([
                        FieldPanel('location_stat_3_number'),
                        FieldPanel('location_stat_3_heading'),
                        FieldPanel('location_stat_3_smallprint'),
                    ]),
                    MultiFieldPanel([
                        FieldPanel('location_stat_4_number'),
                        FieldPanel('location_stat_4_heading'),
                        FieldPanel('location_stat_4_smallprint'),
                    ]),
                ]),
            ],
        ),
        MultiFieldPanel(
            heading="Extra optional Property and Infrastructure section",
            children=[
                HelpPanel('Required fields for section to show: '
                          'Property and Infrastructure Section Title, '
                          'Property and Infrastructure Section Content'),
                ImageChooserPanel('property_and_infrastructure_section_image'),
                FieldPanel('property_and_infrastructure_section_title'),
                FieldPanel('property_and_infrastructure_section_content'),
            ],
        ),
        MultiFieldPanel(
            heading="Case study",
            classname='collapsible',
            children=[
                HelpPanel('Required fields for section to show: '
                          'Case Study Image, Case Study Title'),
                ImageChooserPanel('case_study_image'),
                FieldPanel('case_study_title'),
                FieldPanel('case_study_text'),
                HelpPanel('Cta\'s require both text and a link to show '
                          'on page. '),
                FieldPanel('case_study_cta_text'),
                FieldPanel('case_study_cta_link'),
            ],
        ),
        MultiFieldPanel(
            heading="Contact",
            classname='collapsible',
            children=[
                HelpPanel('Required fields for section to show: '
                          'Contact Title, Contact Text'),
                FieldPanel('contact_title'),
                FieldPanel('contact_text'),
            ],
        ),
    ]

    settings_panels = [
        FieldPanel('title_en_gb'),
        FieldPanel('slug'),
        FieldPanel('uses_tree_based_routing'),
    ]

    edit_handler = make_translated_interface(
        content_panels=content_panels,
        settings_panels=settings_panels
    )


class CapitalInvestOpportunityListingPage(ExclusivePageMixin, ServiceMixin,
                                          BaseInternationalPage):

    slug_identity = 'opportunities'

    parent_page_types = [
        'great_international.GreatInternationalApp'
    ]

    @classmethod
    def get_required_translatable_fields(cls):
        return []

    @classmethod
    def allowed_subpage_models(cls):
        return [CapitalInvestOpportunityPage]


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


class CapitalInvestOpportunityPage(BaseInternationalPage):

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
    location = models.CharField(max_length=255, blank=True)
    project_promoter_icon = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        on_delete=models.SET_NULL,
        related_name='+',
        blank=True
    )
    project_promoter = models.CharField(max_length=255, blank=True)
    scale_icon = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        on_delete=models.SET_NULL,
        related_name='+',
        blank=True
    )
    scale = models.CharField(max_length=255, blank=True)
    sector_icon = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        on_delete=models.SET_NULL,
        related_name='+',
        blank=True
    )
    sector = models.CharField(max_length=255, blank=True)
    investment_type_icon = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        on_delete=models.SET_NULL,
        related_name='+',
        blank=True
    )
    investment_type = models.CharField(max_length=255, blank=True)
    planning_status_icon = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        on_delete=models.SET_NULL,
        related_name='+',
        blank=True
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

    similar_projects_title = models.CharField(max_length=255, blank=True)
    related_page_one = models.ForeignKey(
        'great_international.CapitalInvestOpportunityPage',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    related_page_two = models.ForeignKey(
        'great_international.CapitalInvestOpportunityPage',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    related_page_three = models.ForeignKey(
        'great_international.CapitalInvestOpportunityPage',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    similar_projects_cta_text = models.CharField(max_length=255, blank=True)
    similar_projects_cta_link = models.CharField(max_length=255, blank=True)

    contact_title = models.CharField(max_length=255, blank=True)
    contact_text = MarkdownField(blank=True)

    prioritised_opportunity = models.BooleanField(
        default=False,
        verbose_name="Prioritise project?",
        help_text='Mark this if this opportunity is a priority and should be '
                  'promoted on the related sector page'
    )

    content_panels = [
        MultiFieldPanel(
            heading="Related sector",
            classname='collapsible collapsed',
            children=[
                InlinePanel('related_sectors', label="Related Sectors"),
            ],
        ),
        FieldPanel('breadcrumbs_label'),
        MultiFieldPanel(
            heading="Hero",
            children=[
                ImageChooserPanel('hero_image'),
                FieldPanel('hero_title'),
            ],
        ),
        MultiFieldPanel(
            heading="Opportunity summary",
            classname='collapsible',
            children=[
                HelpPanel('Required fields for section to show: '
                          'Opportunity Summary Intro'),
                FieldPanel('opportunity_summary_intro'),
                FieldPanel('opportunity_summary_content'),
                ImageChooserPanel('opportunity_summary_image'),
            ],
        ),
        MultiFieldPanel(
            heading="Opportunity Details",
            classname='collapsible',
            children=[
                HelpPanel('Icons require the corresponding text to show on '
                          'page'),
                FieldRowPanel([
                    MultiFieldPanel([
                        ImageChooserPanel('location_icon'),
                        FieldPanel('location'),
                    ]),
                    MultiFieldPanel([
                        ImageChooserPanel('project_promoter_icon'),
                        FieldPanel('project_promoter'),
                    ]),
                    MultiFieldPanel([
                        ImageChooserPanel('scale_icon'),
                        FieldPanel('scale'),
                    ]),
                ]),
                FieldRowPanel([
                    MultiFieldPanel([
                        ImageChooserPanel('sector_icon'),
                        FieldPanel('sector'),
                    ]),
                    MultiFieldPanel([
                        ImageChooserPanel('investment_type_icon'),
                        FieldPanel('investment_type'),
                    ]),
                    MultiFieldPanel([
                        ImageChooserPanel('planning_status_icon'),
                        FieldPanel('planning_status'),
                    ]),
                ]),
            ],
        ),
        MultiFieldPanel(
            heading="Project Details",
            classname='collapsible',
            children=[
                HelpPanel('Title requires corresponding text to show on page'),
                FieldPanel('project_background_title'),
                FieldPanel('project_background_intro'),
                FieldRowPanel([
                    MultiFieldPanel([
                        FieldPanel('project_description_title'),
                        FieldPanel('project_description_content'),
                    ]),
                    MultiFieldPanel([
                        FieldPanel('project_promoter_title'),
                        FieldPanel('project_promoter_content'),
                    ]),
                ]),
                ImageChooserPanel('project_image')
            ],
        ),
        MultiFieldPanel(
            heading="Similar projects",
            classname='collapsible',
            children=[
                HelpPanel('Required fields for section to show: '
                          'Similar Projects Title, 1 Related Page'),
                FieldPanel('similar_projects_title'),
                FieldRowPanel([
                    PageChooserPanel(
                        'related_page_one',
                        [
                            'great_international.'
                            'CapitalInvestOpportunityPage'
                        ]),
                    PageChooserPanel(
                        'related_page_two',
                        [
                            'great_international.'
                            'CapitalInvestOpportunityPage'
                        ]),
                    PageChooserPanel(
                        'related_page_three',
                        [
                            'great_international.'
                            'CapitalInvestOpportunityPage'
                        ]),
                ]),
                HelpPanel('Cta\'s require both text and a link to show '
                          'on page. '),
                FieldPanel('similar_projects_cta_text'),
                FieldPanel('similar_projects_cta_link'),
            ],
        ),
        MultiFieldPanel(
            heading="Case study",
            classname='collapsible',
            children=[
                HelpPanel('Required fields for section to show: '
                          'Case Study Image, Case Study Title'),
                ImageChooserPanel('case_study_image'),
                FieldPanel('case_study_title'),
                FieldPanel('case_study_text'),
                HelpPanel('Cta\'s require both text and a link to show '
                          'on page. '),
                FieldPanel('case_study_cta_text'),
                FieldPanel('case_study_cta_link'),
            ],
        ),
        MultiFieldPanel(
            heading="Contact",
            classname='collapsible',
            children=[
                HelpPanel('Required fields for section to show: '
                          'Contact Title, Contact Text'),
                FieldPanel('contact_title'),
                FieldPanel('contact_text'),
            ],
        ),
    ]

    settings_panels = [
        FieldPanel('title_en_gb'),
        FieldPanel('slug'),
        FieldPanel('prioritised_opportunity'),
        FieldPanel('uses_tree_based_routing'),
    ]

    edit_handler = make_translated_interface(
        content_panels=content_panels,
        settings_panels=settings_panels,
    )


# Invest models

class InvestInternationalHomePage(
    WagtailAdminExclusivePageMixin,
    ServiceHomepageMixin,
    BaseInternationalPage
):
    slug_identity = cms.INVEST_HOME_PAGE_SLUG
    view_path = ''

    breadcrumbs_label = models.CharField(max_length=50)
    heading = models.CharField(max_length=255)
    sub_heading = models.CharField(max_length=255)
    hero_call_to_action_text = models.CharField(max_length=255, blank=True)
    hero_call_to_action_url = models.CharField(max_length=255, blank=True)
    hero_image = models.ForeignKey(
        'wagtailimages.Image',
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    benefits_section_title = models.CharField(max_length=255)
    benefits_section_intro = models.TextField(max_length=255, blank=True)
    benefits_section_content = MarkdownField(blank=True)
    benefits_section_img = models.ForeignKey(
        'wagtailimages.Image',
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name='+',
        verbose_name="Benefits section image"
    )

    capital_invest_section_title = models.CharField(
        max_length=255
    )
    capital_invest_section_content = MarkdownField(
        blank=True
    )
    capital_invest_section_image = models.ForeignKey(
        'wagtailimages.Image',
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    eu_exit_section_title = models.CharField(
        max_length=255,
        blank=True,
        verbose_name="EU exit section title"
    )

    eu_exit_section_content = MarkdownField(
        blank=True,
        verbose_name="EU exit section content"
    )

    eu_exit_section_call_to_action_text = models.CharField(
        max_length=255,
        blank=True,
        verbose_name="EU exit section button text"
    )

    eu_exit_section_call_to_action_url = models.CharField(
        max_length=255,
        blank=True,
        verbose_name="EU exit section button url"
    )

    eu_exit_section_img = models.ForeignKey(
        'wagtailimages.Image',
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name='+',
        verbose_name="EU exit section image"
    )

    # subsections
    subsection_title_one = models.CharField(max_length=255, blank=True)
    subsection_content_one = MarkdownField(blank=True)

    subsection_title_two = models.CharField(max_length=255, blank=True)
    subsection_content_two = MarkdownField(blank=True)

    subsection_title_three = models.CharField(max_length=255, blank=True)
    subsection_content_three = MarkdownField(blank=True)

    subsection_title_four = models.CharField(max_length=255, blank=True)
    subsection_content_four = MarkdownField(blank=True)

    subsection_title_five = models.CharField(max_length=255, blank=True)
    subsection_content_five = MarkdownField(blank=True)

    subsection_title_six = models.CharField(max_length=255, blank=True)
    subsection_content_six = MarkdownField(blank=True)

    subsection_title_seven = models.CharField(max_length=255, blank=True)
    subsection_content_seven = MarkdownField(blank=True)

    sector_title = models.TextField(
        default="Discover UK Industries",
        max_length=255)

    sector_button_text = models.TextField(
        default="See more industries",
        max_length=255)

    sector_button_url = models.CharField(
        max_length=255)

    sector_intro = models.TextField(max_length=255, blank=True)

    hpo_title = models.CharField(
        max_length=255,
        verbose_name="High potential opportunity section title"
    )
    hpo_intro = models.TextField(
        max_length=255,
        blank=True,
        verbose_name="High potential opportunity section intro"
    )

    setup_guide_title = models.CharField(
        default='Set up an overseas business in the UK',
        max_length=255)

    setup_guide_lead_in = models.TextField(
        blank=True,
        null=True)

    setup_guide_content = MarkdownField(blank=True)
    setup_guide_img = models.ForeignKey(
        'wagtailimages.Image',
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name='+',
        verbose_name="Setup guide image"
    )
    setup_guide_call_to_action_url = models.CharField(max_length=255)

    isd_section_image = models.ForeignKey(
        'wagtailimages.Image',
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name='+',
        verbose_name='Investment Support Directory section image'
    )
    isd_section_title = models.CharField(
        max_length=255,
        blank=True,
        verbose_name='Investment Support Directory section title'
    )
    isd_section_text = MarkdownField(
        max_length=255,
        blank=True,
        verbose_name='Investment Support Directory section text'
    )

    how_we_help_title = models.CharField(default='How we help', max_length=255)
    how_we_help_lead_in = models.TextField(blank=True, null=True)
    # how we help
    how_we_help_text_one = models.CharField(max_length=255)
    how_we_help_icon_one = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    how_we_help_text_two = models.CharField(max_length=255)
    how_we_help_icon_two = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    how_we_help_text_three = models.CharField(max_length=255)
    how_we_help_icon_three = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    how_we_help_text_four = models.CharField(max_length=255)
    how_we_help_icon_four = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    how_we_help_text_five = models.CharField(max_length=255)
    how_we_help_icon_five = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    how_we_help_text_six = models.CharField(max_length=255, blank=True)
    how_we_help_icon_six = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    contact_section_title = models.CharField(max_length=255)
    contact_section_content = models.TextField(max_length=255, blank=True)
    contact_section_call_to_action_text = models.CharField(max_length=255)
    contact_section_call_to_action_url = models.CharField(max_length=255)

    image_panels = [
        ImageChooserPanel('hero_image'),
    ]

    content_panels = [
        MultiFieldPanel(
            heading='Hero',
            classname='collapsible',
            children=[
                FieldPanel('breadcrumbs_label'),
                FieldPanel('heading'),
                FieldPanel('sub_heading'),
                FieldPanel('hero_call_to_action_text'),
                FieldPanel('hero_call_to_action_url'),
            ],

        ),

        MultiFieldPanel(
            heading='Benefits section',
            classname='collapsible',
            children=[
                FieldPanel('benefits_section_title'),
                FieldPanel('benefits_section_intro'),
                FieldPanel('benefits_section_content'),
                ImageChooserPanel('benefits_section_img'),
            ],
        ),

        MultiFieldPanel(
            heading='EU Exit section',
            classname='collapsible',
            children=[
                FieldPanel('eu_exit_section_title'),
                FieldPanel('eu_exit_section_content'),
                FieldPanel('eu_exit_section_call_to_action_text'),
                FieldPanel('eu_exit_section_call_to_action_url'),
                ImageChooserPanel('eu_exit_section_img'),
            ],

        ),
        MultiFieldPanel(
            heading='Featured card links ',
            classname='collapsible',
            children=[
                FieldRowPanel(
                    [
                        MultiFieldPanel(
                            [
                                ImageChooserPanel('setup_guide_img'),
                                FieldPanel('setup_guide_title'),
                                FieldPanel('setup_guide_content'),
                                FieldPanel('setup_guide_call_to_action_url'),
                            ],
                        ),
                        MultiFieldPanel(
                            [
                                ImageChooserPanel('isd_section_image'),
                                FieldPanel('isd_section_title'),
                                FieldPanel('isd_section_text')
                            ],
                        ),
                        MultiFieldPanel(
                            [
                                ImageChooserPanel(
                                    'capital_invest_section_image'
                                ),
                                FieldPanel('capital_invest_section_title'),
                                FieldPanel('capital_invest_section_content'),
                            ]
                        ),
                    ]
                ),
            ],
        ),
        MultiFieldPanel(
            heading='Industries section',
            children=[
                FieldPanel('sector_title'),
                FieldPanel('sector_intro'),
                FieldPanel('sector_button_text'),
                FieldPanel('sector_button_url'),
            ],

        ),

        MultiFieldPanel(
            heading='High Potential Opportunities',
            children=[
                FieldPanel('hpo_title'),
                FieldPanel('hpo_intro')
            ],

        ),

        MultiFieldPanel(
            heading='How we help section',
            classname='collapsible',
            children=[
                FieldPanel('how_we_help_title'),
                FieldPanel('how_we_help_lead_in'),
                FieldRowPanel(
                    [
                        MultiFieldPanel(
                            [
                                FieldPanel('how_we_help_text_one'),
                                ImageChooserPanel('how_we_help_icon_one')
                            ],
                        ),
                        MultiFieldPanel(
                            [
                                FieldPanel('how_we_help_text_two'),
                                ImageChooserPanel('how_we_help_icon_two')
                            ],
                        ),
                        MultiFieldPanel(
                            [
                                FieldPanel('how_we_help_text_three'),
                                ImageChooserPanel('how_we_help_icon_three')
                            ],
                        ),
                    ],

                ),
                FieldRowPanel(
                    [
                        MultiFieldPanel(
                            [
                                FieldPanel('how_we_help_text_four'),
                                ImageChooserPanel('how_we_help_icon_four')
                            ],
                        ),
                        MultiFieldPanel(
                            [
                                FieldPanel('how_we_help_text_five'),
                                ImageChooserPanel('how_we_help_icon_five')
                            ],
                        )
                    ],

                ),
            ],
        ),

        MultiFieldPanel(
            heading='Contact Section',
            classname='collapsible',
            children=[
                FieldPanel('contact_section_title'),
                FieldPanel('contact_section_content'),
                FieldPanel('contact_section_call_to_action_text'),
                FieldPanel('contact_section_call_to_action_url'),
            ],

        ),
        SearchEngineOptimisationPanel()
    ]

    settings_panels = [
        FieldPanel('title_en_gb'),
        FieldPanel('slug'),
    ]

    edit_handler = make_translated_interface(
        content_panels=content_panels,
        settings_panels=settings_panels,
        other_panels=[
            ObjectList(image_panels, heading='Images'),
        ]
    )


class InvestHighPotentialOpportunityFormPage(
    WagtailAdminExclusivePageMixin,
    BaseInternationalPage,
    metaclass=FormPageMetaClass
):
    # metaclass creates <field_name>_label and <field_name>_help_text
    form_field_names = [
        'full_name',
        'role_in_company',
        'email_address',
        'phone_number',
        'company_name',
        'website_url',
        'country',
        'company_size',
        'opportunities',
        'comment',
    ]

    slug_identity = cms.INVEST_HIGH_POTENTIAL_OPPORTUNITY_FORM_SLUG
    full_path_override = 'high-potential-opportunities/rail/contact/'

    heading = models.CharField(max_length=255)
    sub_heading = models.CharField(max_length=255)
    breadcrumbs_label = models.CharField(max_length=50)

    content_panels_before_form = [
        MultiFieldPanel(
            heading='Hero',
            children=[
                FieldPanel('breadcrumbs_label'),
                FieldPanel('heading'),
                FieldPanel('sub_heading'),
            ]
        ),
    ]
    content_panels_after_form = [SearchEngineOptimisationPanel()]

    settings_panels = [
        FieldPanel('title_en_gb'),
        FieldPanel('slug'),
    ]


class InvestHighPotentialOpportunityDetailPage(BaseInternationalPage):
    subpage_types = ['invest.HighPotentialOpportunityDetailPage']
    view_path = 'high-potential-opportunities/'

    breadcrumbs_label = models.CharField(max_length=50)
    heading = models.CharField(max_length=255)
    hero_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    featured = models.BooleanField(default=True)
    description = models.TextField(
        blank=True,
        help_text="This is the description shown when the HPO "
                  "is featured on another page i.e. the Invest Home Page"
    )

    contact_proposition = MarkdownField(
        blank=False,
        verbose_name='Body text',
    )
    contact_button = models.CharField(max_length=500)
    proposition_one = MarkdownField(blank=False)
    proposition_one_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    proposition_one_video = models.ForeignKey(
        'wagtailmedia.Media',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    opportunity_list_title = models.CharField(max_length=300)
    opportunity_list_item_one = MarkdownField()
    opportunity_list_item_two = MarkdownField()
    opportunity_list_item_three = MarkdownField(blank=True)
    opportunity_list_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    proposition_two = MarkdownField(blank=False)
    proposition_two_list_item_one = MarkdownField()
    proposition_two_list_item_two = MarkdownField()
    proposition_two_list_item_three = MarkdownField()
    proposition_two_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    proposition_two_video = models.ForeignKey(
        'wagtailmedia.Media',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    competitive_advantages_title = models.CharField(
        max_length=300,
        verbose_name='Body text',
    )
    competitive_advantages_list_item_one = MarkdownField()
    competitive_advantages_list_item_one_icon = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    competitive_advantages_list_item_two = MarkdownField()
    competitive_advantages_list_item_two_icon = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    competitive_advantages_list_item_three = MarkdownField()
    competitive_advantages_list_item_three_icon = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    testimonial = MarkdownField(blank=True)
    testimonial_background = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        verbose_name='Background image',
    )
    companies_list_text = MarkdownField()
    companies_list_item_image_one = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    companies_list_item_image_two = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    companies_list_item_image_three = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    companies_list_item_image_four = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    companies_list_item_image_five = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    companies_list_item_image_six = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    companies_list_item_image_seven = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    companies_list_item_image_eight = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    case_study_list_title = models.CharField(max_length=300)
    case_study_one_text = MarkdownField(blank=True)
    case_study_one_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    case_study_two_text = MarkdownField(blank=True)
    case_study_two_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    case_study_three_text = MarkdownField(blank=True)
    case_study_three_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    case_study_four_text = MarkdownField(blank=True)
    case_study_four_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    other_opportunities_title = models.CharField(
        max_length=300,
        verbose_name='Title'
    )
    pdf_document = models.ForeignKey(
        'wagtaildocs.Document',
        null=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    summary_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text=(
            'Image used on the opportunity listing page for this opportunity'
        ),
        verbose_name='Image',
    )

    content_panels = [
        MultiFieldPanel(
            heading='Hero',
            children=[
                FieldPanel('breadcrumbs_label'),
                FieldPanel('heading'),
                ImageChooserPanel('hero_image'),
            ]
        ),

        MultiFieldPanel(
            heading='Featured Description',
            children=[
                FieldPanel('description')
            ]
        ),

        MultiFieldPanel(
            heading='Contact us',
            children=[
                FieldRowPanel(
                    children=[
                        FieldPanel('contact_proposition'),
                        FieldPanel('contact_button'),
                    ]
                )
            ]
        ),
        MultiFieldPanel(
            heading='Proposition one',
            children=[
                FieldRowPanel(
                    children=[
                        FieldPanel('proposition_one'),
                        MultiFieldPanel(
                            children=[
                                ImageChooserPanel('proposition_one_image'),
                                FieldPanel(
                                    'proposition_one_video',
                                    widget=AdminMediaChooser
                                ),
                            ]
                        )
                    ]
                )

            ]
        ),
        MultiFieldPanel(
            heading='Opportunity list',
            children=[
                FieldPanel('opportunity_list_title'),
                FieldRowPanel(
                    children=[
                        MultiFieldPanel(
                            children=[
                                FieldPanel('opportunity_list_item_one'),
                                FieldPanel('opportunity_list_item_two'),
                                FieldPanel('opportunity_list_item_three'),
                            ]
                        ),
                        ImageChooserPanel('opportunity_list_image'),
                    ]
                )
            ]
        ),
        MultiFieldPanel(
            heading='Opportunity list',
            children=[
                FieldRowPanel(
                    children=[
                        MultiFieldPanel(
                            children=[
                                FieldPanel('proposition_two'),
                                FieldPanel('proposition_two_list_item_one'),
                                FieldPanel('proposition_two_list_item_two'),
                                FieldPanel('proposition_two_list_item_three'),
                            ]
                        ),
                        MultiFieldPanel(
                            children=[
                                ImageChooserPanel('proposition_two_image'),
                                FieldPanel(
                                    'proposition_two_video',
                                    widget=AdminMediaChooser
                                ),
                            ]
                        )
                    ]
                )
            ]
        ),
        MultiFieldPanel(
            heading='Key facts',
            children=[
                FieldPanel('competitive_advantages_title'),
                FieldRowPanel(
                    children=[
                        FieldPanel('competitive_advantages_list_item_one'),
                        FieldPanel('competitive_advantages_list_item_two'),
                        FieldPanel('competitive_advantages_list_item_three'),
                    ]
                ),
                FieldRowPanel(
                    children=[
                        ImageChooserPanel(
                            'competitive_advantages_list_item_one_icon'
                        ),
                        ImageChooserPanel(
                            'competitive_advantages_list_item_two_icon'
                        ),
                        ImageChooserPanel(
                            'competitive_advantages_list_item_three_icon'
                        ),
                    ]
                )
            ]
        ),
        MultiFieldPanel(
            heading='Testimonial',
            children=[
                FieldPanel('testimonial'),
                ImageChooserPanel('testimonial_background'),
            ]
        ),
        MultiFieldPanel(
            heading='Company list',
            children=[
                FieldPanel('companies_list_text'),
                FieldRowPanel(
                    children=[
                        ImageChooserPanel('companies_list_item_image_one'),
                        ImageChooserPanel('companies_list_item_image_two'),
                        ImageChooserPanel('companies_list_item_image_three'),
                        ImageChooserPanel('companies_list_item_image_four'),
                    ]
                ),
                FieldRowPanel(
                    children=[
                        ImageChooserPanel('companies_list_item_image_five'),
                        ImageChooserPanel('companies_list_item_image_six'),
                        ImageChooserPanel('companies_list_item_image_seven'),
                        ImageChooserPanel('companies_list_item_image_eight'),
                    ]
                )
            ]
        ),
        MultiFieldPanel(
            heading='Case studies',
            children=[
                FieldPanel('case_study_list_title'),
                FieldRowPanel(
                    children=[
                        FieldPanel('case_study_one_text'),
                        ImageChooserPanel('case_study_one_image'),
                    ]
                ),
                FieldRowPanel(
                    children=[
                        FieldPanel('case_study_two_text'),
                        ImageChooserPanel('case_study_two_image'),
                    ]
                ),
                FieldRowPanel(
                    children=[
                        FieldPanel('case_study_three_text'),
                        ImageChooserPanel('case_study_three_image'),
                    ]
                ),
                FieldRowPanel(
                    children=[
                        FieldPanel('case_study_four_text'),
                        ImageChooserPanel('case_study_four_image'),
                    ]
                )
            ]
        ),
        MultiFieldPanel(
            heading='Other opportunities',
            children=[
                FieldPanel('other_opportunities_title'),
            ]
        ),
        MultiFieldPanel(
            heading='Summary',
            children=[
                ImageChooserPanel('summary_image')
            ],
        ),
        SearchEngineOptimisationPanel(),
    ]
    settings_panels = [
        FieldPanel('title_en_gb'),
        FieldPanel('slug'),
        FieldPanel('featured'),
        DocumentChooserPanel('pdf_document'),
    ]

    edit_handler = make_translated_interface(
        content_panels=content_panels,
        settings_panels=settings_panels
    )


class InvestHighPotentialOpportunityFormSuccessPage(BaseInternationalPage):
    view_path = 'high-potential-opportunities/rail/contact/'
    slug_identity = cms.INVEST_HIGH_POTENTIAL_OPPORTUNITY_FORM_SUCCESS_SLUG

    breadcrumbs_label = models.CharField(max_length=50)
    heading = models.CharField(
        max_length=255,
        verbose_name='section title'
    )
    sub_heading = models.CharField(
        max_length=255,
        verbose_name='section body',
    )
    next_steps_title = models.CharField(
        max_length=255,
        verbose_name='section title'
    )
    next_steps_body = models.CharField(
        max_length=255,
        verbose_name='section body',

    )
    documents_title = models.CharField(
        max_length=255,
        verbose_name='section title'
    )
    documents_body = models.CharField(
        max_length=255,
        verbose_name='section body',
    )

    content_panels = [
        FieldPanel('breadcrumbs_label'),
        MultiFieldPanel(
            heading='heading',
            children=[
                FieldPanel('heading'),
                FieldPanel('sub_heading'),
            ]
        ),
        MultiFieldPanel(
            heading='Next steps',
            children=[
                FieldPanel('next_steps_title'),
                FieldPanel('next_steps_body'),
            ]
        ),
        MultiFieldPanel(
            heading='Documents',
            children=[
                FieldPanel('documents_title'),
                FieldPanel('documents_body'),
            ]
        ),
        SearchEngineOptimisationPanel(),
    ]

    settings_panels = [
        FieldPanel('title_en_gb'),
        FieldPanel('slug'),
    ]
