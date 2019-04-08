from directory_constants.constants import cms
from directory_constants.constants import urls
from modelcluster.fields import ParentalManyToManyField
from wagtail.admin.edit_handlers import (
    FieldPanel, FieldRowPanel, MultiFieldPanel, PageChooserPanel, HelpPanel)
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.search import index
from wagtail.snippets.models import register_snippet
from wagtailmedia.widgets import AdminMediaChooser

from django.db import models
from django.forms import CheckboxSelectMultiple, Textarea, Select
from django.utils.text import slugify

from core.model_fields import MarkdownField

from core.models import (
    BasePage,
    BreadcrumbMixin,
    ExclusivePageMixin,
    FormPageMetaClass,
    ServiceMixin,
)
from core.mixins import ServiceHomepageMixin
from core.panels import SearchEngineOptimisationPanel


ACCORDION_FIELDS_HELP_TEXT = (
    'To be displayed, this industry needs at least: a title, a teaser, '
    '2 bullet points, and 2 calls to action (CTAs).')


class ExportReadinessApp(ExclusivePageMixin, ServiceMixin, BasePage):
    slug_identity = 'export-readiness-app'
    service_name_value = cms.EXPORT_READINESS

    @classmethod
    def get_required_translatable_fields(cls):
        return []


class TermsAndConditionsPage(ExclusivePageMixin, BasePage):

    service_name_value = cms.EXPORT_READINESS
    slug_identity = cms.GREAT_TERMS_AND_CONDITIONS_SLUG

    body = MarkdownField(blank=False)

    content_panels = [
        MultiFieldPanel(
            heading='Terms and conditions',
            children=[
                FieldPanel('body'),
            ]
        ),
        SearchEngineOptimisationPanel(),
    ]

    settings_panels = [
        FieldPanel('title_en_gb'),
        FieldPanel('slug'),
    ]


class PrivacyAndCookiesPage(BasePage):

    service_name_value = cms.EXPORT_READINESS
    subpage_types = ['export_readiness.PrivacyAndCookiesPage']

    body = MarkdownField(blank=False)

    content_panels = [
        MultiFieldPanel(
            heading='Privacy and cookies',
            children=[
                FieldPanel('body'),
            ]
        ),
        SearchEngineOptimisationPanel(),
    ]

    settings_panels = [
        FieldPanel('title_en_gb'),
        FieldPanel('slug'),
    ]

    promote_panels = []


class SitePolicyPages(ExclusivePageMixin, BasePage):
    # a folder for T&C and privacy & cookies pages
    service_name_value = cms.EXPORT_READINESS
    slug_identity = cms.GREAT_SITE_POLICY_PAGES_SLUG
    folder_page = True

    subpage_types = [
        'export_readiness.TermsAndConditionsPage',
        'export_readiness.PrivacyAndCookiesPage',
    ]

    settings_panels = []

    def save(self, *args, **kwargs):
        self.title = self.get_verbose_name()
        return super().save(*args, **kwargs)


class GetFinancePage(ExclusivePageMixin, BreadcrumbMixin, BasePage):

    service_name_value = cms.EXPORT_READINESS
    slug_identity = cms.GREAT_GET_FINANCE_SLUG

    breadcrumbs_label = models.CharField(max_length=50)
    hero_text = MarkdownField()
    hero_image = models.ForeignKey(
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

    contact_proposition = MarkdownField(blank=False)
    contact_button = models.CharField(max_length=500)
    advantages_title = models.CharField(max_length=500)
    advantages_one = MarkdownField()
    advantages_one_icon = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    advantages_two = MarkdownField()
    advantages_two_icon = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    advantages_three = MarkdownField()
    advantages_three_icon = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    evidence = MarkdownField()
    evidence_video = models.ForeignKey(
        'wagtailmedia.Media',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    content_panels = [
        FieldPanel('breadcrumbs_label'),
        MultiFieldPanel(
            heading='Banner',
            children=[
                ImageChooserPanel('hero_image'),
                FieldPanel('hero_text'),
                ImageChooserPanel('ukef_logo'),
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
            heading='Advantages',
            children=[
                FieldPanel('advantages_title'),
                FieldRowPanel(
                    children=[
                        ImageChooserPanel('advantages_one_icon'),
                        ImageChooserPanel('advantages_two_icon'),
                        ImageChooserPanel('advantages_three_icon'),
                    ]
                ),
                FieldRowPanel(
                    children=[
                        FieldPanel('advantages_one'),
                        FieldPanel('advantages_two'),
                        FieldPanel('advantages_three'),
                    ]
                )
            ]
        ),
        MultiFieldPanel(
            heading='Evidence',
            children=[
                FieldRowPanel(
                    children=[
                        FieldPanel('evidence'),
                        FieldPanel(
                            'evidence_video',
                            widget=AdminMediaChooser,
                        ),
                    ]
                )
            ]
        ),
        SearchEngineOptimisationPanel(),
    ]

    settings_panels = [
        FieldPanel('title_en_gb'),
        FieldPanel('slug'),
    ]


class PerformanceDashboardPage(BasePage):

    service_name_value = cms.EXPORT_READINESS
    subpage_types = [
        'export_readiness.PerformanceDashboardPage',
        'export_readiness.PerformanceDashboardNotesPage',
    ]

    heading = models.CharField(max_length=255)
    description = MarkdownField()
    # row 1
    data_title_row_one = models.CharField(max_length=100)
    data_number_row_one = models.CharField(max_length=15)
    data_period_row_one = models.CharField(max_length=100)
    data_description_row_one = MarkdownField()
    # row 2
    data_title_row_two = models.CharField(max_length=100)
    data_number_row_two = models.CharField(max_length=15)
    data_period_row_two = models.CharField(max_length=100)
    data_description_row_two = MarkdownField()
    # row 3
    data_title_row_three = models.CharField(max_length=100)
    data_number_row_three = models.CharField(max_length=15)
    data_period_row_three = models.CharField(max_length=100)
    data_description_row_three = MarkdownField()
    # row 4
    data_title_row_four = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )
    data_number_row_four = models.CharField(
        max_length=15,
        blank=True,
        null=True
    )
    data_period_row_four = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )
    data_description_row_four = MarkdownField(blank=True, null=True)

    guidance_notes = MarkdownField(blank=True, null=True)
    landing_dashboard = models.BooleanField(default=False)

    service_mapping = {
        urls.SERVICES_GREAT_DOMESTIC: {
            'slug': cms.GREAT_PERFORMANCE_DASHBOARD_SLUG,
            'full_path_override': '/performance-dashboard/',
            'heading': 'Great.gov.uk',
            'landing_dashboard': True,
        },
        urls.SERVICES_SOO: {
            'slug': cms.GREAT_PERFORMANCE_DASHBOARD_SOO_SLUG,
            'full_path_override': (
                '/performance-dashboard/selling-online-overseas/'),
            'heading': 'Selling Online Overseas',
            'landing_dashboard': False,
        },
        urls.SERVICES_EXOPPS: {
            'slug': cms.GREAT_PERFORMANCE_DASHBOARD_EXOPPS_SLUG,
            'full_path_override': (
                '/performance-dashboard/export-opportunities/'),
            'heading': 'Export Opportunities',
            'landing_dashboard': False,
        },
        urls.SERVICES_FAB: {
            'slug': (
                cms.GREAT_PERFORMANCE_DASHBOARD_TRADE_PROFILE_SLUG),
            'full_path_override': '/performance-dashboard/trade-profiles/',
            'heading': 'Business Profiles',
            'landing_dashboard': False,
        },
        urls.SERVICES_INVEST: {
            'slug': cms.GREAT_PERFORMANCE_DASHBOARD_INVEST_SLUG,
            'full_path_override': '/performance-dashboard/invest/',
            'heading': 'Invest in Great Britain',
            'landing_dashboard': False,
        },
    }
    product_link = models.TextField(
        choices=[
            (key, val['heading']) for key, val in service_mapping.items()],
        unique=True,
        help_text=(
            'The slug and page heading are inferred from the product link'),
    )

    @property
    def full_path_override(self):
        return self.service_mapping[self.product_link]['full_path_override']

    def save(self, *args, **kwargs):
        field_values = self.service_mapping[self.product_link]
        self.title = field_values['heading'] + ' Performance Dashboard'
        self.heading = field_values['heading']
        self.slug = field_values['slug']
        self.landing_dashboard = field_values['landing_dashboard']
        return super().save(*args, **kwargs)

    content_panels = [
        MultiFieldPanel(
            heading='Heading and description',
            children=[
                FieldPanel('description'),
                FieldPanel('product_link', widget=Select),
            ]
        ),
        FieldRowPanel(
            heading='Data columns',
            children=[
                MultiFieldPanel(
                    heading='Data row 1',
                    children=[
                        FieldPanel('data_title_row_one'),
                        FieldPanel('data_number_row_one'),
                        FieldPanel('data_period_row_one'),
                        FieldPanel('data_description_row_one'),
                    ]
                ),
                MultiFieldPanel(
                    heading='Data row 2',
                    children=[
                        FieldPanel('data_title_row_two'),
                        FieldPanel('data_number_row_two'),
                        FieldPanel('data_period_row_two'),
                        FieldPanel('data_description_row_two'),
                    ]
                ),
                MultiFieldPanel(
                    heading='Data row 3',
                    children=[
                        FieldPanel('data_title_row_three'),
                        FieldPanel('data_number_row_three'),
                        FieldPanel('data_period_row_three'),
                        FieldPanel('data_description_row_three'),
                    ]
                ),
                MultiFieldPanel(
                    heading='Data row 4',
                    children=[
                        FieldPanel('data_title_row_four'),
                        FieldPanel('data_number_row_four'),
                        FieldPanel('data_period_row_four'),
                        FieldPanel('data_description_row_four'),
                    ]
                ),
            ]
        ),
        FieldPanel('guidance_notes'),
    ]


class PerformanceDashboardNotesPage(ExclusivePageMixin, BasePage):

    service_name_value = cms.EXPORT_READINESS
    slug_identity = cms.GREAT_PERFORMANCE_DASHBOARD_NOTES_SLUG
    slug_override = 'guidance-notes'

    body = MarkdownField(
        help_text=(
            'Please include an h1 in this field e.g. # Heading level 1'),
        blank=False)

    content_panels = [
        MultiFieldPanel(
            heading='Performance dashboard notes',
            children=[
                FieldPanel('body'),
            ]
        ),
        SearchEngineOptimisationPanel(),
    ]

    settings_panels = [
        FieldPanel('title_en_gb'),
        FieldPanel('slug'),
    ]

    promote_panels = []


class TopicLandingPage(BasePage):
    service_name_value = cms.EXPORT_READINESS
    subpage_types = [
        'export_readiness.ArticleListingPage',
        'export_readiness.SuperregionPage',
        'export_readiness.CountryGuidePage'
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

    teaser = models.TextField(blank=True)

    content_panels = [
        FieldPanel('landing_page_title'),
        MultiFieldPanel(
            heading='Hero',
            children=[
                ImageChooserPanel('hero_image'),
                FieldPanel('hero_teaser')
            ]
        ),
        FieldPanel('teaser'),
        SearchEngineOptimisationPanel(),
    ]

    settings_panels = [
        FieldPanel('title_en_gb'),
        FieldPanel('slug'),
    ]


class SuperregionPage(TopicLandingPage):
    subpage_types = [
        'export_readiness.CountryGuidePage',
    ]

    @property
    def articles_count(self):
        return self.get_descendants().live().count()


class ArticleListingPage(BasePage):
    service_name_value = cms.EXPORT_READINESS
    subpage_types = [
        'export_readiness.ArticlePage',
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

    @property
    def articles_count(self):
        return self.get_descendants().type(ArticlePage).live().count()

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
    ]


class CountryGuidePage(BasePage):
    """Make a cup of tea, this model is BIG!"""

    class Meta:
        ordering = ['-heading']

    service_name_value = cms.EXPORT_READINESS
    subpage_types = [
        'export_readiness.ArticleListingPage',
        'export_readiness.ArticlePage',
        'export_readiness.CampaignPage'
    ]

    heading = models.CharField(
        max_length=255,
        verbose_name='Country name',
        help_text='Only enter the country name'
    )
    sub_heading = models.CharField(max_length=255, blank=True)
    hero_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    heading_teaser = models.TextField(
        blank=True,
        verbose_name='Introduction'
    )

    section_one_body = MarkdownField(
        null=True,
        verbose_name='3 unique selling points markdown',
        help_text='Use H3 (###) markdown for the 3 subheadings'
    )
    section_one_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        on_delete=models.SET_NULL,
        related_name='+',
        verbose_name='Image for unique selling points'
    )
    section_one_image_caption = models.CharField(
        max_length=255,
        blank=True,
        verbose_name='Bullets image caption')
    section_one_image_caption_company = models.CharField(
        max_length=255,
        blank=True,
        verbose_name='Bullets image caption — company name')

    statistic_1_number = models.CharField(max_length=255)
    statistic_1_heading = models.CharField(max_length=255)
    statistic_1_smallprint = models.CharField(max_length=255, blank=True)

    statistic_2_number = models.CharField(max_length=255)
    statistic_2_heading = models.CharField(max_length=255)
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
        verbose_name='High potential industries for UK businesses'
    )
    section_two_teaser = models.TextField(
        verbose_name='Summary of the industry opportunities'
    )

    # accordion 1
    accordion_1_icon = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        verbose_name='Industry Icon'
    )
    accordion_1_title = models.CharField(
        max_length=255,
        blank=True,
        verbose_name='Industry title'
    )
    accordion_1_teaser = models.TextField(
        blank=True,
        verbose_name='Industry teaser'
    )
    accordion_1_subsection_1_icon = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        verbose_name='Subsection 1 icon'
    )
    accordion_1_subsection_1_heading = models.CharField(
        max_length=255,
        blank=True,
        verbose_name='Subsection 1 heading'
    )
    accordion_1_subsection_1_body = models.TextField(
        blank=True,
        verbose_name='Subsection 1 body'
    )

    accordion_1_subsection_2_icon = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        verbose_name='Subsection 2 icon'
    )
    accordion_1_subsection_2_heading = models.CharField(
        max_length=255,
        blank=True,
        verbose_name='Subsection 2 heading'
    )
    accordion_1_subsection_2_body = models.TextField(
        blank=True,
        verbose_name='Subsection 2 body'
    )

    accordion_1_subsection_3_icon = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        verbose_name='Subsection 2 icon'
    )
    accordion_1_subsection_3_heading = models.CharField(
        max_length=255,
        blank=True,
        verbose_name='Subsection 2 heading'
    )
    accordion_1_subsection_3_body = models.TextField(
        blank=True,
        verbose_name='Subsection 2 body'
    )
    accordion_1_case_study_hero_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        verbose_name='Case study hero'
    )
    accordion_1_case_study_button_text = models.CharField(
        max_length=255,
        blank=True,
        verbose_name='Case study button text'
    )
    accordion_1_case_study_button_link = models.CharField(
        max_length=255,
        blank=True,
        verbose_name='Case study button link'
    )
    accordion_1_case_study_title = models.CharField(
        max_length=255,
        blank=True,
        verbose_name='Case study title'
    )
    accordion_1_case_study_description = models.CharField(
        max_length=255,
        blank=True,
        verbose_name='Case study description'
    )

    accordion_1_cta_1_link = models.CharField(
        max_length=255,
        blank=True,
        verbose_name='CTA link 1'
    )
    accordion_1_cta_1_title = models.CharField(
        max_length=255,
        blank=True,
        verbose_name='CTA title 1'
    )
    accordion_1_cta_2_link = models.CharField(
        max_length=255,
        blank=True,
        verbose_name='CTA link 2'
    )
    accordion_1_cta_2_title = models.CharField(
        max_length=255,
        blank=True,
        verbose_name='CTA title 2'
    )
    accordion_1_cta_3_link = models.CharField(
        max_length=255,
        blank=True,
        verbose_name='CTA link 3'
    )
    accordion_1_cta_3_title = models.CharField(
        max_length=255,
        blank=True,
        verbose_name='CTA title 3'
    )

    accordion_1_statistic_1_number = models.CharField(
        max_length=255,
        blank=True,
        verbose_name='Stat 1 number'
    )
    accordion_1_statistic_1_heading = models.CharField(
        max_length=255,
        blank=True,
        verbose_name='Stat 1 heading'
    )
    accordion_1_statistic_1_smallprint = models.CharField(
        max_length=255,
        blank=True,
        verbose_name='Stat 1 smallprint'
    )

    accordion_1_statistic_2_number = models.CharField(
        max_length=255,
        blank=True,
        verbose_name='Stat 2 number'
    )
    accordion_1_statistic_2_heading = models.CharField(
        max_length=255,
        blank=True,
        verbose_name='Stat 2 heading'
    )
    accordion_1_statistic_2_smallprint = models.CharField(
        max_length=255,
        blank=True,
        verbose_name='Stat 2 smallprint'
    )

    accordion_1_statistic_3_number = models.CharField(
        max_length=255,
        blank=True,
        verbose_name='Stat 3 number'
    )
    accordion_1_statistic_3_heading = models.CharField(
        max_length=255,
        blank=True,
        verbose_name='Stat 3 heading'
    )
    accordion_1_statistic_3_smallprint = models.CharField(
        max_length=255,
        blank=True,
        verbose_name='Stat 3 smallprint'
    )

    accordion_1_statistic_4_number = models.CharField(
        max_length=255,
        blank=True,
        verbose_name='Stat 4 number'
    )
    accordion_1_statistic_4_heading = models.CharField(
        max_length=255,
        blank=True,
        verbose_name='Stat 4 heading'
    )
    accordion_1_statistic_4_smallprint = models.CharField(
        max_length=255,
        blank=True,
        verbose_name='Stat 4 smallprint'
    )

    accordion_1_statistic_5_number = models.CharField(
        max_length=255,
        blank=True,
        verbose_name='Stat 5 number'
    )
    accordion_1_statistic_5_heading = models.CharField(
        max_length=255,
        blank=True,
        verbose_name='Stat 5 heading'
    )
    accordion_1_statistic_5_smallprint = models.CharField(
        max_length=255,
        blank=True,
        verbose_name='Stat 5 smallprint'
    )

    accordion_1_statistic_6_number = models.CharField(
        max_length=255,
        blank=True,
        verbose_name='Stat 6 number'
    )
    accordion_1_statistic_6_heading = models.CharField(
        max_length=255,
        blank=True,
        verbose_name='Stat 6 heading'
    )
    accordion_1_statistic_6_smallprint = models.CharField(
        max_length=255,
        blank=True,
        verbose_name='Stat 6 smallprint'
    )

    # accordion 2
    accordion_2_icon = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        verbose_name='Industry Icon'
    )
    accordion_2_title = models.CharField(
        max_length=255,
        blank=True,
        verbose_name='Industry title'
    )
    accordion_2_teaser = models.TextField(
        blank=True,
        verbose_name='Industry teaser'
    )
    accordion_2_subsection_1_icon = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        verbose_name='Subsection 1 icon'
    )
    accordion_2_subsection_1_heading = models.CharField(
        max_length=255,
        blank=True,
        verbose_name='Subsection 1 heading'
    )
    accordion_2_subsection_1_body = models.TextField(
        blank=True,
        verbose_name='Subsection 1 body'
    )
    accordion_2_subsection_2_icon = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        verbose_name='Subsection 2 icon'
    )
    accordion_2_subsection_2_heading = models.CharField(
        max_length=255,
        blank=True,
        verbose_name='Subsection 2 heading'
    )
    accordion_2_subsection_2_body = models.TextField(
        blank=True,
        verbose_name='Subsection 2 body'
    )
    accordion_2_subsection_3_icon = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        verbose_name='Subsection 2 icon'
    )
    accordion_2_subsection_3_heading = models.CharField(
        max_length=255,
        blank=True,
        verbose_name='Subsection 2 heading'
    )
    accordion_2_subsection_3_body = models.TextField(
        blank=True,
        verbose_name='Subsection 2 body'
    )

    accordion_2_case_study_hero_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        verbose_name='Case study hero'
    )
    accordion_2_case_study_button_text = models.CharField(
        max_length=255,
        blank=True,
        verbose_name='Case study button text'
    )
    accordion_2_case_study_button_link = models.CharField(
        max_length=255,
        blank=True,
        verbose_name='Case study button link'
    )
    accordion_2_case_study_title = models.CharField(
        max_length=255,
        blank=True,
        verbose_name='Case study title'
    )
    accordion_2_case_study_description = models.CharField(
        max_length=255,
        blank=True,
        verbose_name='Case study description'
    )

    accordion_2_cta_1_link = models.CharField(
        max_length=255,
        blank=True,
        verbose_name='CTA link 1'
    )
    accordion_2_cta_1_title = models.CharField(
        max_length=255,
        blank=True,
        verbose_name='CTA title 1'
    )
    accordion_2_cta_2_link = models.CharField(
        max_length=255,
        blank=True,
        verbose_name='CTA link 2'
    )
    accordion_2_cta_2_title = models.CharField(
        max_length=255,
        blank=True,
        verbose_name='CTA title 2'
    )
    accordion_2_cta_3_link = models.CharField(
        max_length=255,
        blank=True,
        verbose_name='CTA link 3'
    )
    accordion_2_cta_3_title = models.CharField(
        max_length=255,
        blank=True,
        verbose_name='CTA title 3'
    )

    accordion_2_statistic_1_number = models.CharField(
        max_length=255,
        blank=True,
        verbose_name='Stat 1 number'
    )
    accordion_2_statistic_1_heading = models.CharField(
        max_length=255,
        blank=True,
        verbose_name='Stat 1 heading'
    )
    accordion_2_statistic_1_smallprint = models.CharField(
        max_length=255,
        blank=True,
        verbose_name='Stat 1 smallprint'
    )

    accordion_2_statistic_2_number = models.CharField(
        max_length=255,
        blank=True,
        verbose_name='Stat 2 number'
    )
    accordion_2_statistic_2_heading = models.CharField(
        max_length=255,
        blank=True,
        verbose_name='Stat 2 heading'
    )
    accordion_2_statistic_2_smallprint = models.CharField(
        max_length=255,
        blank=True,
        verbose_name='Stat 2 smallprint'
    )

    accordion_2_statistic_3_number = models.CharField(
        max_length=255,
        blank=True,
        verbose_name='Stat 3 number'
    )
    accordion_2_statistic_3_heading = models.CharField(
        max_length=255,
        blank=True,
        verbose_name='Stat 3 heading'
    )
    accordion_2_statistic_3_smallprint = models.CharField(
        max_length=255,
        blank=True,
        verbose_name='Stat 3 smallprint'
    )

    accordion_2_statistic_4_number = models.CharField(
        max_length=255,
        blank=True,
        verbose_name='Stat 4 number'
    )
    accordion_2_statistic_4_heading = models.CharField(
        max_length=255,
        blank=True,
        verbose_name='Stat 4 heading'
    )
    accordion_2_statistic_4_smallprint = models.CharField(
        max_length=255,
        blank=True,
        verbose_name='Stat 4 smallprint'
    )

    accordion_2_statistic_5_number = models.CharField(
        max_length=255,
        blank=True,
        verbose_name='Stat 5 number'
    )
    accordion_2_statistic_5_heading = models.CharField(
        max_length=255,
        blank=True,
        verbose_name='Stat 5 heading'
    )
    accordion_2_statistic_5_smallprint = models.CharField(
        max_length=255,
        blank=True,
        verbose_name='Stat 5 smallprint'
    )

    accordion_2_statistic_6_number = models.CharField(
        max_length=255,
        blank=True,
        verbose_name='Stat 6 number'
    )
    accordion_2_statistic_6_heading = models.CharField(
        max_length=255,
        blank=True,
        verbose_name='Stat 6 heading'
    )
    accordion_2_statistic_6_smallprint = models.CharField(
        max_length=255,
        blank=True,
        verbose_name='Stat 6 smallprint'
    )

    # accordion 3
    accordion_3_icon = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        verbose_name='Industry Icon'
    )
    accordion_3_title = models.CharField(
        max_length=255,
        blank=True,
        verbose_name='Industry title'
    )
    accordion_3_teaser = models.TextField(
        blank=True,
        verbose_name='Industry teaser'
    )
    accordion_3_subsection_1_icon = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        verbose_name='Subsection 1 icon'
    )
    accordion_3_subsection_1_heading = models.CharField(
        max_length=255,
        blank=True,
        verbose_name='Subsection 1 heading'
    )
    accordion_3_subsection_1_body = models.TextField(
        blank=True,
        verbose_name='Subsection 1 body'
    )

    accordion_3_subsection_2_icon = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        verbose_name='Subsection 2 icon'
    )
    accordion_3_subsection_2_heading = models.CharField(
        max_length=255,
        blank=True,
        verbose_name='Subsection 2 heading'
    )
    accordion_3_subsection_2_body = models.TextField(
        blank=True,
        verbose_name='Subsection 2 body'
    )

    accordion_3_subsection_3_icon = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        verbose_name='Subsection 2 icon'
    )
    accordion_3_subsection_3_heading = models.CharField(
        max_length=255,
        blank=True,
        verbose_name='Subsection 2 heading'
    )
    accordion_3_subsection_3_body = models.TextField(
        blank=True,
        verbose_name='Subsection 2 body'
    )

    accordion_3_case_study_hero_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        verbose_name='Case study hero'
    )
    accordion_3_case_study_button_text = models.CharField(
        max_length=255,
        blank=True,
        verbose_name='Case study button text'
    )
    accordion_3_case_study_button_link = models.CharField(
        max_length=255,
        blank=True,
        verbose_name='Case study button link'
    )
    accordion_3_case_study_title = models.CharField(
        max_length=255,
        blank=True,
        verbose_name='Case study title'
    )
    accordion_3_case_study_description = models.CharField(
        max_length=255,
        blank=True,
        verbose_name='Case study description'
    )

    accordion_3_cta_1_link = models.CharField(
        max_length=255,
        blank=True,
        verbose_name='CTA link 1'
    )
    accordion_3_cta_1_title = models.CharField(
        max_length=255,
        blank=True,
        verbose_name='CTA title 1'
    )
    accordion_3_cta_2_link = models.CharField(
        max_length=255,
        blank=True,
        verbose_name='CTA link 2'
    )
    accordion_3_cta_2_title = models.CharField(
        max_length=255,
        blank=True,
        verbose_name='CTA title 2'
    )
    accordion_3_cta_3_link = models.CharField(
        max_length=255,
        blank=True,
        verbose_name='CTA link 3'
    )
    accordion_3_cta_3_title = models.CharField(
        max_length=255,
        blank=True,
        verbose_name='CTA title 3'
    )

    accordion_3_statistic_1_number = models.CharField(
        max_length=255,
        blank=True,
        verbose_name='Stat 1 number'
    )
    accordion_3_statistic_1_heading = models.CharField(
        max_length=255,
        blank=True,
        verbose_name='Stat 1 heading'
    )
    accordion_3_statistic_1_smallprint = models.CharField(
        max_length=255,
        blank=True,
        verbose_name='Stat 1 smallprint'
    )

    accordion_3_statistic_2_number = models.CharField(
        max_length=255,
        blank=True,
        verbose_name='Stat 2 number'
    )
    accordion_3_statistic_2_heading = models.CharField(
        max_length=255,
        blank=True,
        verbose_name='Stat 2 heading'
    )
    accordion_3_statistic_2_smallprint = models.CharField(
        max_length=255,
        blank=True,
        verbose_name='Stat 2 smallprint'
    )

    accordion_3_statistic_3_number = models.CharField(
        max_length=255,
        blank=True,
        verbose_name='Stat 3 number'
    )
    accordion_3_statistic_3_heading = models.CharField(
        max_length=255,
        blank=True,
        verbose_name='Stat 3 heading'
    )
    accordion_3_statistic_3_smallprint = models.CharField(
        max_length=255,
        blank=True,
        verbose_name='Stat 3 smallprint'
    )

    accordion_3_statistic_4_number = models.CharField(
        max_length=255,
        blank=True,
        verbose_name='Stat 4 number'
    )
    accordion_3_statistic_4_heading = models.CharField(
        max_length=255,
        blank=True,
        verbose_name='Stat 4 heading'
    )
    accordion_3_statistic_4_smallprint = models.CharField(
        max_length=255,
        blank=True,
        verbose_name='Stat 4 smallprint'
    )

    accordion_3_statistic_5_number = models.CharField(
        max_length=255,
        blank=True,
        verbose_name='Stat 5 number'
    )
    accordion_3_statistic_5_heading = models.CharField(
        max_length=255,
        blank=True,
        verbose_name='Stat 5 heading'
    )
    accordion_3_statistic_5_smallprint = models.CharField(
        max_length=255,
        blank=True,
        verbose_name='Stat 5 smallprint'
    )

    accordion_3_statistic_6_number = models.CharField(
        max_length=255,
        blank=True,
        verbose_name='Stat 6 number'
    )
    accordion_3_statistic_6_heading = models.CharField(
        max_length=255,
        blank=True,
        verbose_name='Stat 6 heading'
    )
    accordion_3_statistic_6_smallprint = models.CharField(
        max_length=255,
        blank=True,
        verbose_name='Stat 6 smallprint'
    )

    # accordion 4
    accordion_4_icon = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        verbose_name='Industry Icon'
    )
    accordion_4_title = models.CharField(
        max_length=255,
        blank=True,
        verbose_name='Industry title'
    )
    accordion_4_teaser = models.TextField(
        blank=True,
        verbose_name='Industry teaser'
    )
    accordion_4_subsection_1_icon = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        verbose_name='Subsection 1 icon'
    )
    accordion_4_subsection_1_heading = models.CharField(
        max_length=255,
        blank=True,
        verbose_name='Subsection 1 heading'
    )
    accordion_4_subsection_1_body = models.TextField(
        blank=True,
        verbose_name='Subsection 1 body'
    )

    accordion_4_subsection_2_icon = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        verbose_name='Subsection 2 icon'
    )
    accordion_4_subsection_2_heading = models.CharField(
        max_length=255,
        blank=True,
        verbose_name='Subsection 2 heading'
    )
    accordion_4_subsection_2_body = models.TextField(
        blank=True,
        verbose_name='Subsection 2 body'
    )

    accordion_4_subsection_3_icon = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        verbose_name='Subsection 2 icon'
    )
    accordion_4_subsection_3_heading = models.CharField(
        max_length=255,
        blank=True,
        verbose_name='Subsection 2 heading'
    )
    accordion_4_subsection_3_body = models.TextField(
        blank=True,
        verbose_name='Subsection 2 body'
    )

    accordion_4_case_study_hero_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        verbose_name='Case study hero'
    )
    accordion_4_case_study_button_text = models.CharField(
        max_length=255,
        blank=True,
        verbose_name='Case study button text'
    )
    accordion_4_case_study_button_link = models.CharField(
        max_length=255,
        blank=True,
        verbose_name='Case study button link'
    )
    accordion_4_case_study_title = models.CharField(
        max_length=255,
        blank=True,
        verbose_name='Case study title'
    )
    accordion_4_case_study_description = models.CharField(
        max_length=255,
        blank=True,
        verbose_name='Case study description'
    )

    accordion_4_cta_1_link = models.CharField(
        max_length=255,
        blank=True,
        verbose_name='CTA link 1'
    )
    accordion_4_cta_1_title = models.CharField(
        max_length=255,
        blank=True,
        verbose_name='CTA title 1'
    )
    accordion_4_cta_2_link = models.CharField(
        max_length=255,
        blank=True,
        verbose_name='CTA link 2'
    )
    accordion_4_cta_2_title = models.CharField(
        max_length=255,
        blank=True,
        verbose_name='CTA title 2'
    )
    accordion_4_cta_3_link = models.CharField(
        max_length=255,
        blank=True,
        verbose_name='CTA link 3'
    )
    accordion_4_cta_3_title = models.CharField(
        max_length=255,
        blank=True,
        verbose_name='CTA title 3'
    )

    accordion_4_statistic_1_number = models.CharField(
        max_length=255,
        blank=True,
        verbose_name='Stat 1 number'
    )
    accordion_4_statistic_1_heading = models.CharField(
        max_length=255,
        blank=True,
        verbose_name='Stat 1 heading'
    )
    accordion_4_statistic_1_smallprint = models.CharField(
        max_length=255,
        blank=True,
        verbose_name='Stat 1 smallprint'
    )

    accordion_4_statistic_2_number = models.CharField(
        max_length=255,
        blank=True,
        verbose_name='Stat 2 number'
    )
    accordion_4_statistic_2_heading = models.CharField(
        max_length=255,
        blank=True,
        verbose_name='Stat 2 heading'
    )
    accordion_4_statistic_2_smallprint = models.CharField(
        max_length=255,
        blank=True,
        verbose_name='Stat 2 smallprint'
    )

    accordion_4_statistic_3_number = models.CharField(
        max_length=255,
        blank=True,
        verbose_name='Stat 3 number'
    )
    accordion_4_statistic_3_heading = models.CharField(
        max_length=255,
        blank=True,
        verbose_name='Stat 3 heading'
    )
    accordion_4_statistic_3_smallprint = models.CharField(
        max_length=255,
        blank=True,
        verbose_name='Stat 3 smallprint'
    )

    accordion_4_statistic_4_number = models.CharField(
        max_length=255,
        blank=True,
        verbose_name='Stat 4 number'
    )
    accordion_4_statistic_4_heading = models.CharField(
        max_length=255,
        blank=True,
        verbose_name='Stat 4 heading'
    )
    accordion_4_statistic_4_smallprint = models.CharField(
        max_length=255,
        blank=True,
        verbose_name='Stat 4 smallprint'
    )

    accordion_4_statistic_5_number = models.CharField(
        max_length=255,
        blank=True,
        verbose_name='Stat 5 number'
    )
    accordion_4_statistic_5_heading = models.CharField(
        max_length=255,
        blank=True,
        verbose_name='Stat 5 heading'
    )
    accordion_4_statistic_5_smallprint = models.CharField(
        max_length=255,
        blank=True,
        verbose_name='Stat 5 smallprint'
    )

    accordion_4_statistic_6_number = models.CharField(
        max_length=255,
        blank=True,
        verbose_name='Stat 6 number'
    )
    accordion_4_statistic_6_heading = models.CharField(
        max_length=255,
        blank=True,
        verbose_name='Stat 6 heading'
    )
    accordion_4_statistic_6_smallprint = models.CharField(
        max_length=255,
        blank=True,
        verbose_name='Stat 6 smallprint'
    )

    # accordion 5
    accordion_5_icon = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        verbose_name='Industry Icon'
    )
    accordion_5_title = models.CharField(
        max_length=255,
        blank=True,
        verbose_name='Industry title'
    )
    accordion_5_teaser = models.TextField(
        blank=True,
        verbose_name='Industry teaser'
    )
    accordion_5_subsection_1_icon = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        verbose_name='Subsection 1 icon'
    )
    accordion_5_subsection_1_heading = models.CharField(
        max_length=255,
        blank=True,
        verbose_name='Subsection 1 heading'
    )
    accordion_5_subsection_1_body = models.TextField(
        blank=True,
        verbose_name='Subsection 1 body'
    )

    accordion_5_subsection_2_icon = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        verbose_name='Subsection 2 icon'
    )
    accordion_5_subsection_2_heading = models.CharField(
        max_length=255,
        blank=True,
        verbose_name='Subsection 2 heading'
    )
    accordion_5_subsection_2_body = models.TextField(
        blank=True,
        verbose_name='Subsection 2 body'
    )

    accordion_5_subsection_3_icon = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        verbose_name='Subsection 2 icon'
    )
    accordion_5_subsection_3_heading = models.CharField(
        max_length=255,
        blank=True,
        verbose_name='Subsection 2 heading'
    )
    accordion_5_subsection_3_body = models.TextField(
        blank=True,
        verbose_name='Subsection 2 body'
    )

    accordion_5_case_study_hero_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        verbose_name='Case study hero'
    )
    accordion_5_case_study_button_text = models.CharField(
        max_length=255,
        blank=True,
        verbose_name='Case study button text'
    )
    accordion_5_case_study_button_link = models.CharField(
        max_length=255,
        blank=True,
        verbose_name='Case study button link'
    )
    accordion_5_case_study_title = models.CharField(
        max_length=255,
        blank=True,
        verbose_name='Case study title'
    )
    accordion_5_case_study_description = models.CharField(
        max_length=255,
        blank=True,
        verbose_name='Case study description'
    )

    accordion_5_cta_1_link = models.CharField(
        max_length=255,
        blank=True,
        verbose_name='CTA link 1'
    )
    accordion_5_cta_1_title = models.CharField(
        max_length=255,
        blank=True,
        verbose_name='CTA title 1'
    )
    accordion_5_cta_2_link = models.CharField(
        max_length=255,
        blank=True,
        verbose_name='CTA link 2'
    )
    accordion_5_cta_2_title = models.CharField(
        max_length=255,
        blank=True,
        verbose_name='CTA title 2'
    )
    accordion_5_cta_3_link = models.CharField(
        max_length=255,
        blank=True,
        verbose_name='CTA link 3'
    )
    accordion_5_cta_3_title = models.CharField(
        max_length=255,
        blank=True,
        verbose_name='CTA title 3'
    )

    accordion_5_statistic_1_number = models.CharField(
        max_length=255,
        blank=True,
        verbose_name='Stat 1 number'
    )
    accordion_5_statistic_1_heading = models.CharField(
        max_length=255,
        blank=True,
        verbose_name='Stat 1 heading'
    )
    accordion_5_statistic_1_smallprint = models.CharField(
        max_length=255,
        blank=True,
        verbose_name='Stat 1 smallprint'
    )

    accordion_5_statistic_2_number = models.CharField(
        max_length=255,
        blank=True,
        verbose_name='Stat 2 number'
    )
    accordion_5_statistic_2_heading = models.CharField(
        max_length=255,
        blank=True,
        verbose_name='Stat 2 heading'
    )
    accordion_5_statistic_2_smallprint = models.CharField(
        max_length=255,
        blank=True,
        verbose_name='Stat 2 smallprint'
    )

    accordion_5_statistic_3_number = models.CharField(
        max_length=255,
        blank=True,
        verbose_name='Stat 3 number'
    )
    accordion_5_statistic_3_heading = models.CharField(
        max_length=255,
        blank=True,
        verbose_name='Stat 3 heading'
    )
    accordion_5_statistic_3_smallprint = models.CharField(
        max_length=255,
        blank=True,
        verbose_name='Stat 3 smallprint'
    )

    accordion_5_statistic_4_number = models.CharField(
        max_length=255,
        blank=True,
        verbose_name='Stat 4 number'
    )
    accordion_5_statistic_4_heading = models.CharField(
        max_length=255,
        blank=True,
        verbose_name='Stat 4 heading'
    )
    accordion_5_statistic_4_smallprint = models.CharField(
        max_length=255,
        blank=True,
        verbose_name='Stat 4 smallprint'
    )

    accordion_5_statistic_5_number = models.CharField(
        max_length=255,
        blank=True,
        verbose_name='Stat 5 number'
    )
    accordion_5_statistic_5_heading = models.CharField(
        max_length=255,
        blank=True,
        verbose_name='Stat 5 heading'
    )
    accordion_5_statistic_5_smallprint = models.CharField(
        max_length=255,
        blank=True,
        verbose_name='Stat 5 smallprint'
    )

    accordion_5_statistic_6_number = models.CharField(
        max_length=255,
        blank=True,
        verbose_name='Stat 6 number'
    )
    accordion_5_statistic_6_heading = models.CharField(
        max_length=255,
        blank=True,
        verbose_name='Stat 6 heading'
    )
    accordion_5_statistic_6_smallprint = models.CharField(
        max_length=255,
        blank=True,
        verbose_name='Stat 6 smallprint'
    )

    # accordion 6
    accordion_6_icon = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        verbose_name='Industry Icon'
    )
    accordion_6_title = models.CharField(
        max_length=255,
        blank=True,
        verbose_name='Industry title'
    )
    accordion_6_teaser = models.TextField(
        blank=True,
        verbose_name='Industry teaser'
    )
    accordion_6_subsection_1_icon = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        verbose_name='Subsection 1 icon'
    )
    accordion_6_subsection_1_heading = models.CharField(
        max_length=255,
        blank=True,
        verbose_name='Subsection 1 heading'
    )
    accordion_6_subsection_1_body = models.TextField(
        blank=True,
        verbose_name='Subsection 1 body'
    )

    accordion_6_subsection_2_icon = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        verbose_name='Subsection 2 icon'
    )
    accordion_6_subsection_2_heading = models.CharField(
        max_length=255,
        blank=True,
        verbose_name='Subsection 2 heading'
    )
    accordion_6_subsection_2_body = models.TextField(
        blank=True,
        verbose_name='Subsection 2 body'
    )

    accordion_6_subsection_3_icon = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        verbose_name='Subsection 2 icon'
    )
    accordion_6_subsection_3_heading = models.CharField(
        max_length=255,
        blank=True,
        verbose_name='Subsection 2 heading'
    )
    accordion_6_subsection_3_body = models.TextField(
        blank=True,
        verbose_name='Subsection 2 body'
    )

    accordion_6_case_study_hero_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        verbose_name='Case study hero'
    )
    accordion_6_case_study_button_text = models.CharField(
        max_length=255,
        blank=True,
        verbose_name='Case study button text'
    )
    accordion_6_case_study_button_link = models.CharField(
        max_length=255,
        blank=True,
        verbose_name='Case study button link'
    )
    accordion_6_case_study_title = models.CharField(
        max_length=255,
        blank=True,
        verbose_name='Case study title'
    )
    accordion_6_case_study_description = models.CharField(
        max_length=255,
        blank=True,
        verbose_name='Case study description'
    )

    accordion_6_cta_1_link = models.CharField(
        max_length=255,
        blank=True,
        verbose_name='CTA link 1'
    )
    accordion_6_cta_1_title = models.CharField(
        max_length=255,
        blank=True,
        verbose_name='CTA title 1'
    )
    accordion_6_cta_2_link = models.CharField(
        max_length=255,
        blank=True,
        verbose_name='CTA link 2'
    )
    accordion_6_cta_2_title = models.CharField(
        max_length=255,
        blank=True,
        verbose_name='CTA title 2'
    )
    accordion_6_cta_3_link = models.CharField(
        max_length=255,
        blank=True,
        verbose_name='CTA link 3'
    )
    accordion_6_cta_3_title = models.CharField(
        max_length=255,
        blank=True,
        verbose_name='CTA title 3'
    )

    accordion_6_statistic_1_number = models.CharField(
        max_length=255,
        blank=True,
        verbose_name='Stat 1 number'
    )
    accordion_6_statistic_1_heading = models.CharField(
        max_length=255,
        blank=True,
        verbose_name='Stat 1 heading'
    )
    accordion_6_statistic_1_smallprint = models.CharField(
        max_length=255,
        blank=True,
        verbose_name='Stat 1 smallprint'
    )

    accordion_6_statistic_2_number = models.CharField(
        max_length=255,
        blank=True,
        verbose_name='Stat 2 number'
    )
    accordion_6_statistic_2_heading = models.CharField(
        max_length=255,
        blank=True,
        verbose_name='Stat 2 heading'
    )
    accordion_6_statistic_2_smallprint = models.CharField(
        max_length=255,
        blank=True,
        verbose_name='Stat 2 smallprint'
    )

    accordion_6_statistic_3_number = models.CharField(
        max_length=255,
        blank=True,
        verbose_name='Stat 3 number'
    )
    accordion_6_statistic_3_heading = models.CharField(
        max_length=255,
        blank=True,
        verbose_name='Stat 3 heading'
    )
    accordion_6_statistic_3_smallprint = models.CharField(
        max_length=255,
        blank=True,
        verbose_name='Stat 3 smallprint'
    )

    accordion_6_statistic_4_number = models.CharField(
        max_length=255,
        blank=True,
        verbose_name='Stat 4 number'
    )
    accordion_6_statistic_4_heading = models.CharField(
        max_length=255,
        blank=True,
        verbose_name='Stat 4 heading'
    )
    accordion_6_statistic_4_smallprint = models.CharField(
        max_length=255,

        blank=True,
        verbose_name='Stat 4 smallprint'
    )

    accordion_6_statistic_5_number = models.CharField(
        max_length=255,
        blank=True,
        verbose_name='Stat 5 number'
    )
    accordion_6_statistic_5_heading = models.CharField(
        max_length=255,
        blank=True,
        verbose_name='Stat 5 heading'
    )
    accordion_6_statistic_5_smallprint = models.CharField(
        max_length=255,
        blank=True,
        verbose_name='Stat 5 smallprint'
    )

    accordion_6_statistic_6_number = models.CharField(
        max_length=255,
        blank=True,
        verbose_name='Stat 6 number'
    )
    accordion_6_statistic_6_heading = models.CharField(
        max_length=255,
        blank=True,
        verbose_name='Stat 6 heading'
    )
    accordion_6_statistic_6_smallprint = models.CharField(
        max_length=255,
        blank=True,
        verbose_name='Stat 6 smallprint'
    )

    # fact sheet
    fact_sheet_title = models.CharField(
        max_length=255,
        blank=True,
        verbose_name="Title for 'Doing business in' section"
    )
    fact_sheet_teaser = models.CharField(
        max_length=255,
        blank=True,
        verbose_name="Summary for 'Doing business in' section"
    )
    fact_sheet_column_1_title = models.CharField(
        max_length=255,
        blank=True,
        verbose_name="Title for 'Tax and customs'"
    )
    fact_sheet_column_1_teaser = models.CharField(
        max_length=255,
        blank=True,
        verbose_name="Summary for 'Tax and customs'"
    )
    fact_sheet_column_1_body = MarkdownField(
        blank=True,
        verbose_name="Detailed text for 'Tax and customs'",
        help_text='Use H4 (####) for each sub category heading. '
                  'Maximum five sub categories. Aim for 50 words each.'
    )
    fact_sheet_column_2_title = models.CharField(
        max_length=255,
        blank=True,
        verbose_name="Title for 'Protecting your business'"
    )
    fact_sheet_column_2_teaser = models.CharField(
        max_length=255,
        blank=True,
        verbose_name="Summary for 'Protecting your business'"
    )
    fact_sheet_column_2_body = MarkdownField(
        blank=True,
        verbose_name="Detailed text for 'Protecting your business'",
        help_text='Use H4 (####) for each sub category heading. '
                  'Maximum five sub categories. Aim for 50 words each.'
    )

    # need help
    help_market_guide_cta_link = models.CharField(
        max_length=255,
        blank=True,
        verbose_name='GOV.UK country guide URL'
    )

    # related pages
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
            heading='Unique selling points of the market for UK exporters',
            children=[
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
            classname='collapsible',
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
            heading='Highlights',
            children=[
                FieldPanel('section_two_heading'),
                FieldPanel('section_two_teaser')
            ]
        ),
        MultiFieldPanel(
            heading='Industry one',
            classname='collapsible collapsed',
            children=[
                HelpPanel(
                    content=ACCORDION_FIELDS_HELP_TEXT,
                    classname='help-panel-font-large'
                ),
                ImageChooserPanel('accordion_1_icon'),
                FieldPanel('accordion_1_title'),
                FieldPanel('accordion_1_teaser'),
                FieldRowPanel([
                    MultiFieldPanel(
                        [
                            ImageChooserPanel('accordion_1_subsection_1_icon'),
                            FieldPanel('accordion_1_subsection_1_heading'),
                            FieldPanel('accordion_1_subsection_1_body'),
                        ]
                    ),
                    MultiFieldPanel(
                        [
                            ImageChooserPanel('accordion_1_subsection_2_icon'),
                            FieldPanel('accordion_1_subsection_2_heading'),
                            FieldPanel('accordion_1_subsection_2_body'),
                        ]
                    ),
                    MultiFieldPanel(
                        [
                            ImageChooserPanel('accordion_1_subsection_3_icon'),
                            FieldPanel('accordion_1_subsection_3_heading'),
                            FieldPanel('accordion_1_subsection_3_body'),
                        ]
                    )
                ]),
                MultiFieldPanel([
                    ImageChooserPanel('accordion_1_case_study_hero_image'),
                    FieldPanel('accordion_1_case_study_button_text'),
                    FieldPanel('accordion_1_case_study_button_link'),
                    FieldPanel('accordion_1_case_study_title'),
                    FieldPanel('accordion_1_case_study_description')
                ]),
                FieldRowPanel([
                    MultiFieldPanel(
                        [
                            FieldPanel('accordion_1_statistic_1_number'),
                            FieldPanel('accordion_1_statistic_1_heading'),
                            FieldPanel('accordion_1_statistic_1_smallprint')
                        ]
                    ),
                    MultiFieldPanel(
                        [
                            FieldPanel('accordion_1_statistic_2_number'),
                            FieldPanel('accordion_1_statistic_2_heading'),
                            FieldPanel('accordion_1_statistic_2_smallprint')
                        ]
                    ),
                    MultiFieldPanel(
                        [
                            FieldPanel('accordion_1_statistic_3_number'),
                            FieldPanel('accordion_1_statistic_3_heading'),
                            FieldPanel('accordion_1_statistic_3_smallprint')
                        ]
                    ),
                    MultiFieldPanel(
                        [
                            FieldPanel('accordion_1_statistic_4_number'),
                            FieldPanel('accordion_1_statistic_4_heading'),
                            FieldPanel('accordion_1_statistic_4_smallprint'),
                        ]
                    ),
                    MultiFieldPanel(
                        [

                            FieldPanel('accordion_1_statistic_5_number'),
                            FieldPanel('accordion_1_statistic_5_heading'),
                            FieldPanel('accordion_1_statistic_5_smallprint')
                        ]
                    ),
                    MultiFieldPanel(
                        [
                            FieldPanel('accordion_1_statistic_6_number'),
                            FieldPanel('accordion_1_statistic_6_heading'),
                            FieldPanel('accordion_1_statistic_6_smallprint')
                        ]
                    )
                ]),
                FieldRowPanel([
                    MultiFieldPanel(
                        [
                            FieldPanel('accordion_1_cta_1_link'),
                            FieldPanel('accordion_1_cta_1_title'),
                        ]
                    ),
                    MultiFieldPanel(
                        [
                            FieldPanel('accordion_1_cta_2_link'),
                            FieldPanel('accordion_1_cta_2_title'),
                        ]
                    ),
                    MultiFieldPanel(
                        [
                            FieldPanel('accordion_1_cta_3_link'),
                            FieldPanel('accordion_1_cta_3_title'),
                        ]
                    )
                ])
            ]
        ),
        MultiFieldPanel(
            heading='Industry two',
            classname='collapsible collapsed',
            children=[
                HelpPanel(
                    content=ACCORDION_FIELDS_HELP_TEXT,
                    classname='help-panel-font-large'
                ),
                ImageChooserPanel('accordion_2_icon'),
                FieldPanel('accordion_2_title'),
                FieldPanel('accordion_2_teaser'),
                FieldRowPanel([
                    MultiFieldPanel(
                        [
                            ImageChooserPanel('accordion_2_subsection_1_icon'),
                            FieldPanel('accordion_2_subsection_1_heading'),
                            FieldPanel('accordion_2_subsection_1_body'),
                        ]
                    ),
                    MultiFieldPanel(
                        [
                            ImageChooserPanel('accordion_2_subsection_2_icon'),
                            FieldPanel('accordion_2_subsection_2_heading'),
                            FieldPanel('accordion_2_subsection_2_body'),
                        ]
                    ),
                    MultiFieldPanel(
                        [
                            ImageChooserPanel('accordion_2_subsection_3_icon'),
                            FieldPanel('accordion_2_subsection_3_heading'),
                            FieldPanel('accordion_2_subsection_3_body'),
                        ]
                    )
                ]),
                MultiFieldPanel([
                    ImageChooserPanel('accordion_2_case_study_hero_image'),
                    FieldPanel('accordion_2_case_study_button_text'),
                    FieldPanel('accordion_2_case_study_button_link'),
                    FieldPanel('accordion_2_case_study_title'),
                    FieldPanel('accordion_2_case_study_description')
                ]),
                FieldRowPanel([
                    MultiFieldPanel(
                        [
                            FieldPanel('accordion_2_statistic_1_number'),
                            FieldPanel('accordion_2_statistic_1_heading'),
                            FieldPanel('accordion_2_statistic_1_smallprint')
                        ]
                    ),
                    MultiFieldPanel(
                        [
                            FieldPanel('accordion_2_statistic_2_number'),
                            FieldPanel('accordion_2_statistic_2_heading'),
                            FieldPanel('accordion_2_statistic_2_smallprint')
                        ]
                    ),
                    MultiFieldPanel(
                        [
                            FieldPanel('accordion_2_statistic_3_number'),
                            FieldPanel('accordion_2_statistic_3_heading'),
                            FieldPanel('accordion_2_statistic_3_smallprint')
                        ]
                    ),
                    MultiFieldPanel(
                        [
                            FieldPanel('accordion_2_statistic_4_number'),
                            FieldPanel('accordion_2_statistic_4_heading'),
                            FieldPanel('accordion_2_statistic_4_smallprint'),
                        ]
                    ),
                    MultiFieldPanel(
                        [

                            FieldPanel('accordion_2_statistic_5_number'),
                            FieldPanel('accordion_2_statistic_5_heading'),
                            FieldPanel('accordion_2_statistic_5_smallprint')
                        ]
                    ),
                    MultiFieldPanel(
                        [
                            FieldPanel('accordion_2_statistic_6_number'),
                            FieldPanel('accordion_2_statistic_6_heading'),
                            FieldPanel('accordion_2_statistic_6_smallprint')
                        ]
                    )
                ]),
                FieldRowPanel([
                    MultiFieldPanel(
                        [
                            FieldPanel('accordion_2_cta_1_link'),
                            FieldPanel('accordion_2_cta_1_title'),
                        ]
                    ),
                    MultiFieldPanel(
                        [
                            FieldPanel('accordion_2_cta_2_link'),
                            FieldPanel('accordion_2_cta_2_title'),
                        ]
                    ),
                    MultiFieldPanel(
                        [
                            FieldPanel('accordion_2_cta_3_link'),
                            FieldPanel('accordion_2_cta_3_title'),
                        ]
                    )
                ])
            ]
        ),
        MultiFieldPanel(
            heading='Industry three',
            classname='collapsible collapsed',
            children=[
                HelpPanel(
                    content=ACCORDION_FIELDS_HELP_TEXT,
                    classname='help-panel-font-large'
                ),
                ImageChooserPanel('accordion_3_icon'),
                FieldPanel('accordion_3_title'),
                FieldPanel('accordion_3_teaser'),
                FieldRowPanel([
                    MultiFieldPanel(
                        [
                            ImageChooserPanel('accordion_3_subsection_1_icon'),
                            FieldPanel('accordion_3_subsection_1_heading'),
                            FieldPanel('accordion_3_subsection_1_body'),
                        ]
                    ),
                    MultiFieldPanel(
                        [
                            ImageChooserPanel('accordion_3_subsection_2_icon'),
                            FieldPanel('accordion_3_subsection_2_heading'),
                            FieldPanel('accordion_3_subsection_2_body'),
                        ]
                    ),
                    MultiFieldPanel(
                        [
                            ImageChooserPanel('accordion_3_subsection_3_icon'),
                            FieldPanel('accordion_3_subsection_3_heading'),
                            FieldPanel('accordion_3_subsection_3_body'),
                        ]
                    )
                ]),
                MultiFieldPanel([
                    ImageChooserPanel('accordion_3_case_study_hero_image'),
                    FieldPanel('accordion_3_case_study_button_text'),
                    FieldPanel('accordion_3_case_study_button_link'),
                    FieldPanel('accordion_3_case_study_title'),
                    FieldPanel('accordion_3_case_study_description')
                ]),
                FieldRowPanel([
                    MultiFieldPanel(
                        [
                            FieldPanel('accordion_3_statistic_1_number'),
                            FieldPanel('accordion_3_statistic_1_heading'),
                            FieldPanel('accordion_3_statistic_1_smallprint')
                        ]
                    ),
                    MultiFieldPanel(
                        [
                            FieldPanel('accordion_3_statistic_2_number'),
                            FieldPanel('accordion_3_statistic_2_heading'),
                            FieldPanel('accordion_3_statistic_2_smallprint')
                        ]
                    ),
                    MultiFieldPanel(
                        [
                            FieldPanel('accordion_3_statistic_3_number'),
                            FieldPanel('accordion_3_statistic_3_heading'),
                            FieldPanel('accordion_3_statistic_3_smallprint')
                        ]
                    ),
                    MultiFieldPanel(
                        [
                            FieldPanel('accordion_3_statistic_4_number'),
                            FieldPanel('accordion_3_statistic_4_heading'),
                            FieldPanel('accordion_3_statistic_4_smallprint'),
                        ]
                    ),
                    MultiFieldPanel(
                        [

                            FieldPanel('accordion_3_statistic_5_number'),
                            FieldPanel('accordion_3_statistic_5_heading'),
                            FieldPanel('accordion_3_statistic_5_smallprint')
                        ]
                    ),
                    MultiFieldPanel(
                        [
                            FieldPanel('accordion_3_statistic_6_number'),
                            FieldPanel('accordion_3_statistic_6_heading'),
                            FieldPanel('accordion_3_statistic_6_smallprint')
                        ]
                    )
                ]),
                FieldRowPanel([
                    MultiFieldPanel(
                        [
                            FieldPanel('accordion_3_cta_1_link'),
                            FieldPanel('accordion_3_cta_1_title'),
                        ]
                    ),
                    MultiFieldPanel(
                        [
                            FieldPanel('accordion_3_cta_2_link'),
                            FieldPanel('accordion_3_cta_2_title'),
                        ]
                    ),
                    MultiFieldPanel(
                        [
                            FieldPanel('accordion_3_cta_3_link'),
                            FieldPanel('accordion_3_cta_3_title'),
                        ]
                    )
                ])
            ]
        ),
        MultiFieldPanel(
            heading='Industry four',
            classname='collapsible collapsed',
            children=[
                HelpPanel(
                    content=ACCORDION_FIELDS_HELP_TEXT,
                    classname='help-panel-font-large'
                ),
                ImageChooserPanel('accordion_4_icon'),
                FieldPanel('accordion_4_title'),
                FieldPanel('accordion_4_teaser'),
                FieldRowPanel([
                    MultiFieldPanel(
                        [
                            ImageChooserPanel('accordion_4_subsection_1_icon'),
                            FieldPanel('accordion_4_subsection_1_heading'),
                            FieldPanel('accordion_4_subsection_1_body'),
                        ]
                    ),
                    MultiFieldPanel(
                        [
                            ImageChooserPanel('accordion_4_subsection_2_icon'),
                            FieldPanel('accordion_4_subsection_2_heading'),
                            FieldPanel('accordion_4_subsection_2_body'),
                        ]
                    ),
                    MultiFieldPanel(
                        [
                            ImageChooserPanel('accordion_4_subsection_3_icon'),
                            FieldPanel('accordion_4_subsection_3_heading'),
                            FieldPanel('accordion_4_subsection_3_body'),
                        ]
                    )
                ]),
                MultiFieldPanel([
                    ImageChooserPanel('accordion_4_case_study_hero_image'),
                    FieldPanel('accordion_4_case_study_button_text'),
                    FieldPanel('accordion_4_case_study_button_link'),
                    FieldPanel('accordion_4_case_study_title'),
                    FieldPanel('accordion_4_case_study_description')
                ]),
                FieldRowPanel([
                    MultiFieldPanel(
                        [
                            FieldPanel('accordion_4_statistic_1_number'),
                            FieldPanel('accordion_4_statistic_1_heading'),
                            FieldPanel('accordion_4_statistic_1_smallprint')
                        ]
                    ),
                    MultiFieldPanel(
                        [
                            FieldPanel('accordion_4_statistic_2_number'),
                            FieldPanel('accordion_4_statistic_2_heading'),
                            FieldPanel('accordion_4_statistic_2_smallprint')
                        ]
                    ),
                    MultiFieldPanel(
                        [
                            FieldPanel('accordion_4_statistic_3_number'),
                            FieldPanel('accordion_4_statistic_3_heading'),
                            FieldPanel('accordion_4_statistic_3_smallprint')
                        ]
                    ),
                    MultiFieldPanel(
                        [
                            FieldPanel('accordion_4_statistic_4_number'),
                            FieldPanel('accordion_4_statistic_4_heading'),
                            FieldPanel('accordion_4_statistic_4_smallprint'),
                        ]
                    ),
                    MultiFieldPanel(
                        [

                            FieldPanel('accordion_4_statistic_5_number'),
                            FieldPanel('accordion_4_statistic_5_heading'),
                            FieldPanel('accordion_4_statistic_5_smallprint')
                        ]
                    ),
                    MultiFieldPanel(
                        [
                            FieldPanel('accordion_4_statistic_6_number'),
                            FieldPanel('accordion_4_statistic_6_heading'),
                            FieldPanel('accordion_4_statistic_6_smallprint')
                        ]
                    )
                ]),
                FieldRowPanel([
                    MultiFieldPanel(
                        [
                            FieldPanel('accordion_4_cta_1_link'),
                            FieldPanel('accordion_4_cta_1_title'),
                        ]
                    ),
                    MultiFieldPanel(
                        [
                            FieldPanel('accordion_4_cta_2_link'),
                            FieldPanel('accordion_4_cta_2_title'),
                        ]
                    ),
                    MultiFieldPanel(
                        [
                            FieldPanel('accordion_4_cta_3_link'),
                            FieldPanel('accordion_4_cta_3_title'),
                        ]
                    )
                ])
            ]
        ),
        MultiFieldPanel(
            heading='Industry five',
            classname='collapsible collapsed',
            children=[
                HelpPanel(
                    content=ACCORDION_FIELDS_HELP_TEXT,
                    classname='help-panel-font-large'
                ),
                ImageChooserPanel('accordion_5_icon'),
                FieldPanel('accordion_5_title'),
                FieldPanel('accordion_5_teaser'),
                FieldRowPanel([
                    MultiFieldPanel(
                        [
                            ImageChooserPanel('accordion_5_subsection_1_icon'),
                            FieldPanel('accordion_5_subsection_1_heading'),
                            FieldPanel('accordion_5_subsection_1_body'),
                        ]
                    ),
                    MultiFieldPanel(
                        [
                            ImageChooserPanel('accordion_5_subsection_2_icon'),
                            FieldPanel('accordion_5_subsection_2_heading'),
                            FieldPanel('accordion_5_subsection_2_body'),
                        ]
                    ),
                    MultiFieldPanel(
                        [
                            ImageChooserPanel('accordion_5_subsection_3_icon'),
                            FieldPanel('accordion_5_subsection_3_heading'),
                            FieldPanel('accordion_5_subsection_3_body'),
                        ]
                    )
                ]),
                MultiFieldPanel([
                    ImageChooserPanel('accordion_4_case_study_hero_image'),
                    FieldPanel('accordion_5_case_study_button_text'),
                    FieldPanel('accordion_5_case_study_button_link'),
                    FieldPanel('accordion_5_case_study_title'),
                    FieldPanel('accordion_5_case_study_description')
                ]),
                FieldRowPanel([
                    MultiFieldPanel(
                        [
                            FieldPanel('accordion_5_statistic_1_number'),
                            FieldPanel('accordion_5_statistic_1_heading'),
                            FieldPanel('accordion_5_statistic_1_smallprint')
                        ]
                    ),
                    MultiFieldPanel(
                        [
                            FieldPanel('accordion_5_statistic_2_number'),
                            FieldPanel('accordion_5_statistic_2_heading'),
                            FieldPanel('accordion_5_statistic_2_smallprint')
                        ]
                    ),
                    MultiFieldPanel(
                        [
                            FieldPanel('accordion_5_statistic_3_number'),
                            FieldPanel('accordion_5_statistic_3_heading'),
                            FieldPanel('accordion_5_statistic_3_smallprint')
                        ]
                    ),
                    MultiFieldPanel(
                        [
                            FieldPanel('accordion_5_statistic_4_number'),
                            FieldPanel('accordion_5_statistic_4_heading'),
                            FieldPanel('accordion_5_statistic_4_smallprint'),
                        ]
                    ),
                    MultiFieldPanel(
                        [

                            FieldPanel('accordion_5_statistic_5_number'),
                            FieldPanel('accordion_5_statistic_5_heading'),
                            FieldPanel('accordion_5_statistic_5_smallprint')
                        ]
                    ),
                    MultiFieldPanel(
                        [
                            FieldPanel('accordion_5_statistic_6_number'),
                            FieldPanel('accordion_5_statistic_6_heading'),
                            FieldPanel('accordion_5_statistic_6_smallprint')
                        ]
                    )
                ]),
                FieldRowPanel([
                    MultiFieldPanel(
                        [
                            FieldPanel('accordion_5_cta_1_link'),
                            FieldPanel('accordion_5_cta_1_title'),
                        ]
                    ),
                    MultiFieldPanel(
                        [
                            FieldPanel('accordion_5_cta_2_link'),
                            FieldPanel('accordion_5_cta_2_title'),
                        ]
                    ),
                    MultiFieldPanel(
                        [
                            FieldPanel('accordion_5_cta_3_link'),
                            FieldPanel('accordion_5_cta_3_title'),
                        ]
                    )
                ])
            ]
        ),
        MultiFieldPanel(
            heading='Industry six',
            classname='collapsible collapsed',
            children=[
                HelpPanel(
                    content=ACCORDION_FIELDS_HELP_TEXT,
                    classname='help-panel-font-large'
                ),
                ImageChooserPanel('accordion_6_icon'),
                FieldPanel('accordion_6_title'),
                FieldPanel('accordion_6_teaser'),
                FieldRowPanel([
                    MultiFieldPanel(
                        [
                            ImageChooserPanel('accordion_6_subsection_1_icon'),
                            FieldPanel('accordion_6_subsection_1_heading'),
                            FieldPanel('accordion_6_subsection_1_body'),
                        ]
                    ),
                    MultiFieldPanel(
                        [
                            ImageChooserPanel('accordion_6_subsection_2_icon'),
                            FieldPanel('accordion_6_subsection_2_heading'),
                            FieldPanel('accordion_6_subsection_2_body'),
                        ]
                    ),
                    MultiFieldPanel(
                        [
                            ImageChooserPanel('accordion_6_subsection_3_icon'),
                            FieldPanel('accordion_6_subsection_3_heading'),
                            FieldPanel('accordion_6_subsection_3_body'),
                        ]
                    )
                ]),
                MultiFieldPanel([
                    ImageChooserPanel('accordion_6_case_study_hero_image'),
                    FieldPanel('accordion_6_case_study_button_text'),
                    FieldPanel('accordion_6_case_study_button_link'),
                    FieldPanel('accordion_6_case_study_title'),
                    FieldPanel('accordion_6_case_study_description')
                ]),
                FieldRowPanel([
                    MultiFieldPanel(
                        [
                            FieldPanel('accordion_6_statistic_1_number'),
                            FieldPanel('accordion_6_statistic_1_heading'),
                            FieldPanel('accordion_6_statistic_1_smallprint')
                        ]
                    ),
                    MultiFieldPanel(
                        [
                            FieldPanel('accordion_6_statistic_2_number'),
                            FieldPanel('accordion_6_statistic_2_heading'),
                            FieldPanel('accordion_6_statistic_2_smallprint')
                        ]
                    ),
                    MultiFieldPanel(
                        [
                            FieldPanel('accordion_6_statistic_3_number'),
                            FieldPanel('accordion_6_statistic_3_heading'),
                            FieldPanel('accordion_6_statistic_3_smallprint')
                        ]
                    ),
                    MultiFieldPanel(
                        [
                            FieldPanel('accordion_6_statistic_4_number'),
                            FieldPanel('accordion_6_statistic_4_heading'),
                            FieldPanel('accordion_6_statistic_4_smallprint'),
                        ]
                    ),
                    MultiFieldPanel(
                        [

                            FieldPanel('accordion_6_statistic_5_number'),
                            FieldPanel('accordion_6_statistic_5_heading'),
                            FieldPanel('accordion_6_statistic_5_smallprint')
                        ]
                    ),
                    MultiFieldPanel(
                        [
                            FieldPanel('accordion_6_statistic_6_number'),
                            FieldPanel('accordion_6_statistic_6_heading'),
                            FieldPanel('accordion_6_statistic_6_smallprint')
                        ]
                    )
                ]),
                FieldRowPanel([
                    MultiFieldPanel(
                        [
                            FieldPanel('accordion_6_cta_1_link'),
                            FieldPanel('accordion_6_cta_1_title'),
                        ]
                    ),
                    MultiFieldPanel(
                        [
                            FieldPanel('accordion_6_cta_2_link'),
                            FieldPanel('accordion_6_cta_2_title'),
                        ]
                    ),
                    MultiFieldPanel(
                        [
                            FieldPanel('accordion_6_cta_3_link'),
                            FieldPanel('accordion_6_cta_3_title'),
                        ]
                    )
                ])
            ]
        ),
        MultiFieldPanel(
            heading='Fact sheet',
            classname='collapsible',
            children=[
                FieldPanel('fact_sheet_title'),
                FieldPanel('fact_sheet_teaser'),
                FieldRowPanel([
                    FieldPanel('fact_sheet_column_1_title'),
                    FieldPanel('fact_sheet_column_1_teaser'),
                    FieldPanel('fact_sheet_column_1_body')
                ]),
                FieldRowPanel([
                    FieldPanel('fact_sheet_column_2_title'),
                    FieldPanel('fact_sheet_column_2_teaser'),
                    FieldPanel('fact_sheet_column_2_body')
                ]),
            ]
        ),
        MultiFieldPanel(
            heading='Need help',
            classname='collapsible',
            children=[
                FieldPanel('help_market_guide_cta_link')
            ]
        ),
        MultiFieldPanel(
            heading='News and events',
            children=[
                FieldRowPanel([
                    PageChooserPanel(
                        'related_page_one',
                        [
                            'export_readiness.ArticlePage',
                            'export_readiness.CampaignPage',
                            'export_readiness.ArticleListingPage'
                        ]),
                    PageChooserPanel(
                        'related_page_two',
                        [
                            'export_readiness.ArticlePage',
                            'export_readiness.CampaignPage',
                            'export_readiness.ArticleListingPage'
                        ]),
                    PageChooserPanel(
                        'related_page_three',
                        [
                            'export_readiness.ArticlePage',
                            'export_readiness.CampaignPage',
                            'export_readiness.ArticleListingPage'
                        ]),
                ])
            ]
        ),
        SearchEngineOptimisationPanel(),
    ]

    settings_panels = [
        FieldPanel('title_en_gb'),
        FieldPanel('slug'),
    ]


class MarketingPages(ExclusivePageMixin, BasePage):
    service_name_value = cms.EXPORT_READINESS
    slug_identity = cms.GREAT_MARKETING_PAGES_SLUG
    slug_override = 'campaigns'

    subpage_types = [
        'export_readiness.CampaignPage',
    ]

    settings_panels = []

    def save(self, *args, **kwargs):
        self.title = self.get_verbose_name()
        return super().save(*args, **kwargs)


class CampaignPage(BasePage):
    service_name_value = cms.EXPORT_READINESS
    subpage_types = []

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
        'export_readiness.ArticlePage',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
    )
    related_page_two = models.ForeignKey(
        'export_readiness.ArticlePage',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
    )
    related_page_three = models.ForeignKey(
        'export_readiness.ArticlePage',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
    )

    cta_box_message = models.CharField(max_length=255)
    cta_box_button_url = models.CharField(max_length=255)
    cta_box_button_text = models.CharField(max_length=255)

    content_panels = [
        MultiFieldPanel(
            heading='Hero section',
            children=[
                FieldPanel('campaign_heading'),
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
                        'export_readiness.ArticlePage'),
                    PageChooserPanel(
                        'related_page_two',
                        'export_readiness.ArticlePage'),
                    PageChooserPanel(
                        'related_page_three',
                        'export_readiness.ArticlePage'),
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
    ]


@register_snippet
class Tag(index.Indexed, models.Model):
    name = models.CharField(max_length=100)
    slug = models.CharField(max_length=255, blank=True)

    panels = [
        FieldPanel('name')
    ]

    search_fields = [
        index.SearchField('name', partial_match=True),
    ]

    def __str__(self):
        return self.name

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        self.slug = slugify(self.name)
        return super().save(force_insert, force_update, using, update_fields)


class ArticlePage(BasePage):
    service_name_value = cms.EXPORT_READINESS
    subpage_types = []

    article_title = models.CharField(max_length=255)

    article_teaser = models.CharField(max_length=255, blank=True, null=True)
    article_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    article_body_text = MarkdownField()

    related_page_one = models.ForeignKey(
        'export_readiness.ArticlePage',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
    )
    related_page_two = models.ForeignKey(
        'export_readiness.ArticlePage',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
    )
    related_page_three = models.ForeignKey(
        'export_readiness.ArticlePage',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
    )

    # settings fields
    tags = ParentalManyToManyField(Tag, blank=True)

    content_panels = [
        FieldPanel('article_title'),
        MultiFieldPanel(
            heading='Article content',
            children=[
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
                        'export_readiness.ArticlePage'),
                    PageChooserPanel(
                        'related_page_two',
                        'export_readiness.ArticlePage'),
                    PageChooserPanel(
                        'related_page_three',
                        'export_readiness.ArticlePage'),
                ]),
            ]
        ),
        SearchEngineOptimisationPanel(),
    ]

    settings_panels = [
        FieldPanel('title_en_gb'),
        FieldPanel('slug'),
        FieldPanel('tags', widget=CheckboxSelectMultiple),
    ]


class HomePage(ExclusivePageMixin, ServiceHomepageMixin, BasePage):
    service_name_value = cms.EXPORT_READINESS
    slug_identity = cms.GREAT_HOME_SLUG
    subpage_types = [
        'export_readiness.TopicLandingPage',
        'export_readiness.ArticleListingPage',
        'export_readiness.ArticlePage'
    ]

    banner_content = MarkdownField()
    banner_label = models.CharField(max_length=50, null=True, blank=True)
    news_title = models.CharField(max_length=255)
    news_description = MarkdownField()

    content_panels = [
        MultiFieldPanel(
            heading='EU Exit banner',
            children=[
                FieldPanel('banner_label'),
                FieldPanel('banner_content'),
            ]
        ),
        MultiFieldPanel(
            heading='EU exit news',
            children=[
                FieldPanel('news_title'),
                FieldPanel('news_description')
            ]
        ),
        SearchEngineOptimisationPanel(),
    ]

    settings_panels = [
        FieldPanel('title_en_gb'),
        FieldPanel('slug'),
    ]


class InternationalLandingPage(ExclusivePageMixin, BasePage):
    service_name_value = cms.EXPORT_READINESS
    slug_identity = cms.GREAT_HOME_INTERNATIONAL_SLUG
    # slug_override = 'international'
    subpage_types = [
        'export_readiness.ArticleListingPage',
    ]

    content_panels = [
        SearchEngineOptimisationPanel()
    ]

    settings_panels = [
        FieldPanel('title_en_gb'),
        FieldPanel('slug'),
    ]

    @property
    def articles_count(self):
        return sum(
            (listing_page.specific.articles_count for listing_page in
             self.get_descendants().type(ArticleListingPage).live())
        )


class EUExitInternationalFormPage(
    ExclusivePageMixin, BasePage, metaclass=FormPageMetaClass
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

    service_name_value = cms.EXPORT_READINESS
    full_path_override = '/international/eu-exit-news/contact/'
    slug_identity = cms.GREAT_EUEXIT_INTERNATIONAL_FORM_SLUG

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


class EUExitDomesticFormPage(
    ExclusivePageMixin, BasePage, metaclass=FormPageMetaClass
):
    # metaclass creates <fild_name>_label and <field_name>_help_text
    form_field_names = [
        'first_name',
        'last_name',
        'email',
        'organisation_type',
        'company_name',
        'comment',
    ]

    service_name_value = cms.EXPORT_READINESS
    full_path_override = '/eu-exit-news/contact/'
    slug_identity = cms.GREAT_EUEXIT_DOMESTIC_FORM_SLUG

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
        SearchEngineOptimisationPanel()
    ]

    settings_panels = [
        FieldPanel('title_en_gb'),
        FieldPanel('slug'),
    ]


class EUExitFormSuccessPage(ExclusivePageMixin, BasePage):
    service_name_value = cms.EXPORT_READINESS
    full_path_override = '/eu-exit-news/contact/success/'
    slug_identity = cms.GREAT_EUEXIT_FORM_SUCCESS_SLUG

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


class EUExitFormPages(ExclusivePageMixin, BasePage):
    # this is just a folder. it will not be requested by the client.
    service_name_value = cms.EXPORT_READINESS
    slug_identity = 'eu-exit-form-pages'
    folder_page = True

    subpage_types = [
        'export_readiness.EUExitInternationalFormPage',
        'export_readiness.EUExitDomesticFormPage',
        'export_readiness.EUExitFormSuccessPage',
    ]

    settings_panels = []

    def save(self, *args, **kwargs):
        self.title = self.get_verbose_name()
        return super().save(*args, **kwargs)


class ContactUsGuidancePages(ExclusivePageMixin, BasePage):
    # this is just a folder. it will not be requested by the client.
    service_name_value = cms.EXPORT_READINESS
    slug_identity = 'contact-us-guidance-pages'
    folder_page = True

    subpage_types = [
        'export_readiness.ContactUsGuidancePage',
    ]

    settings_panels = []

    def save(self, *args, **kwargs):
        self.title = self.get_verbose_name()
        return super().save(*args, **kwargs)


class ContactSuccessPages(ExclusivePageMixin, BasePage):
    # this is just a folder. it will not be requested by the client.
    service_name_value = cms.EXPORT_READINESS
    slug_identity = 'contact-us-success-pages'
    folder_page = True

    subpage_types = [
        'export_readiness.ContactSuccessPage',
    ]

    settings_panels = []

    def save(self, *args, **kwargs):
        self.title = self.get_verbose_name()
        return super().save(*args, **kwargs)


class ContactUsGuidancePage(BasePage):

    service_name_value = cms.EXPORT_READINESS

    topic_mapping = {
        cms.GREAT_HELP_EXOPP_ALERTS_IRRELEVANT_SLUG: {
            'title': 'Guidance - Daily alerts are not relevant',
            'full_path_override': (
                '/contact/triage/export-opportunities/alerts-not-relevant/'
            ),
        },
        cms.GREAT_HELP_EXOPP_NO_RESPONSE: {
            'title': 'Guidance - Export Opportunity application no response',
            'full_path_override': (
                '/contact/triage/export-opportunities/opportunity-no-response/'
            ),
        },
        cms.GREAT_HELP_MISSING_VERIFY_EMAIL_SLUG: {
            'title': 'Guidance - Email verification missing',
            'full_path_override': (
                '/contact/triage/great-account/no-verification-email/'),
        },
        cms.GREAT_HELP_PASSWORD_RESET_SLUG: {
            'title': 'Guidance - Missing password reset link',
            'full_path_override': (
                '/contact/triage/great-account/password-reset/'),
        },
        cms.GREAT_HELP_COMPANIES_HOUSE_LOGIN_SLUG: {
            'title': 'Guidance - Companies House login not working',
            'full_path_override': (
                '/contact/triage/great-account/companies-house-login/'),
        },
        cms.GREAT_HELP_VERIFICATION_CODE_ENTER_SLUG: {
            'title': 'Guidance - Where to enter letter verification code',
            'full_path_override': (
                '/contact/triage/great-account/verification-letter-code/'
            ),
        },
        cms.GREAT_HELP_VERIFICATION_CODE_LETTER_SLUG: {
            'title': 'Guidance - Verification letter not delivered',
            'full_path_override': (
                '/contact/triage/great-account/no-verification-letter/'
            ),
        },
        cms.GREAT_HELP_VERIFICATION_CODE_MISSING_SLUG: {
            'title': 'Guidance - Verification code not delivered',
            'full_path_override': (
                '/contact/triage/great-account/verification-missing/'
            ),
        },
        cms.GREAT_HELP_ACCOUNT_COMPANY_NOT_FOUND_SLUG: {
            'title': 'Guidance - Company not found',
            'full_path_override': (
                '/contact/triage/great-account/company-not-found/'
            ),
        },
        cms.GREAT_HELP_EXPORTING_TO_UK_SLUG: {
            'title': 'Guidance - Exporting to the UK',
            'view_path': (
                'contact/triage/international/exporting-to-the-uk/'
            )
        }
    }

    @property
    def full_path_override(self):
        return self.topic_mapping[self.topic]['full_path_override']

    topic = models.TextField(
        choices=[(key, val['title']) for key, val in topic_mapping.items()],
        unique=True,
        help_text='The slug and CMS page title are inferred from the topic',
    )
    body = MarkdownField(blank=False,)

    content_panels = [
        MultiFieldPanel(
            heading='Topic',
            children=[
                FieldPanel('topic', widget=Select),
            ]
        ),
        MultiFieldPanel(
            heading='Guidance',
            children=[
                FieldPanel('body'),
            ]
        ),
        SearchEngineOptimisationPanel(),
    ]

    settings_panels = []

    def save(self, *args, **kwargs):
        field_values = self.topic_mapping[self.topic]
        self.title = field_values['title']
        self.slug = self.topic
        return super().save(*args, **kwargs)


class ContactSuccessPage(BasePage):

    service_name_value = cms.EXPORT_READINESS

    topic_mapping = {
        cms.GREAT_CONTACT_US_FORM_SUCCESS_SLUG: {
            'title': 'Contact domestic form success',
            'full_path_override': '/contact/domestic/success/',
        },
        cms.GREAT_CONTACT_US_FORM_SUCCESS_EVENTS_SLUG: {
            'title': 'Contact Events form success',
            'full_path_override': '/contact/events/success/',
        },
        cms.GREAT_CONTACT_US_FORM_SUCCESS_DSO_SLUG: {
            'title': 'Contact Defence and Security Organisation form success',
            'full_path_override': (
                '/contact/defence-and-security-organisation/success/'),
        },
        cms.GREAT_CONTACT_US_FORM_SUCCESS_EXPORT_ADVICE_SLUG: {
            'title': 'Contact exporting from the UK form success',
            'full_path_override': '/contact/export-advice/success/',
        },
        cms.GREAT_CONTACT_US_FORM_SUCCESS_FEEDBACK_SLUG: {
            'title': 'Contact feedback form success',
            'full_path_override': '/contact/feedback/success/',
        },
        cms.GREAT_CONTACT_US_FORM_SUCCESS_FIND_COMPANIES_SLUG: {
            'title': 'Contact find UK companies form success',
            'full_path_override': '/contact/find-uk-companies/success/',
        },
        cms.GREAT_CONTACT_US_FORM_SUCCESS_INTERNATIONAL_SLUG: {
            'title': 'Contact international form success',
            'full_path_override': '/contact/international/success/',
        },
        cms.GREAT_CONTACT_US_FORM_SUCCESS_SOO_SLUG: {
            'title': 'Contact Selling Online Overseas form success',
            'full_path_override': '/contact/selling-online-overseas/success/',
        },
        cms.GREAT_CONTACT_US_FORM_SUCCESS_BEIS_SLUG: {
            'title': 'Contact BEIS form success',
            'view_path': (
                'contact/department-for-business-energy-'
                'and-industrial-strategy/success/'
            )
        },
        cms.GREAT_CONTACT_US_FORM_SUCCESS_DEFRA_SLUG: {
            'title': 'Contact DEFRA form success',
            'view_path': (
                'contact/department-for-environment-food-and-rural-affairs/'
                'success/'
            )
        },
    }

    @property
    def full_path_override(self):
        return self.topic_mapping[self.topic]['full_path_override']

    topic = models.TextField(
        choices=[(key, val['title']) for key, val in topic_mapping.items()],
        unique=True,
        help_text='The slug and CMS page title are inferred from the topic',
    )
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
        MultiFieldPanel(
            heading='Topic',
            children=[
                FieldPanel('topic', widget=Select),
            ]
        ),
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

    settings_panels = []

    def save(self, *args, **kwargs):
        field_values = self.topic_mapping[self.topic]
        self.title = field_values['title']
        self.slug = self.topic
        return super().save(*args, **kwargs)


class AllContactPagesPage(ExclusivePageMixin, BasePage):
    # this is just a folder. it will not be requested by the client.
    service_name_value = cms.EXPORT_READINESS
    slug_identity = 'all-export-readiness-contact-pages'
    folder_page = True

    subpage_types = [
        'export_readiness.ContactSuccessPages',
        'export_readiness.ContactUsGuidancePages',
        'export_readiness.EUExitFormPages',
    ]

    settings_panels = []

    class Meta:
        verbose_name = 'Forms'

    def save(self, *args, **kwargs):
        self.title = self.get_verbose_name()
        return super().save(*args, **kwargs)
