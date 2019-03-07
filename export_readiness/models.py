from directory_constants.constants import cms
from directory_constants.constants import urls
from modelcluster.fields import ParentalManyToManyField
from wagtail.admin.edit_handlers import (
    FieldPanel, FieldRowPanel, MultiFieldPanel, PageChooserPanel
)
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
from core.panels import SearchEngineOptimisationPanel


class ExportReadinessApp(ExclusivePageMixin, ServiceMixin, BasePage):
    slug_identity = 'export-readiness-app'
    service_name_value = cms.EXPORT_READINESS

    @classmethod
    def get_required_translatable_fields(cls):
        return []


class TermsAndConditionsPage(ExclusivePageMixin, BasePage):

    service_name_value = cms.EXPORT_READINESS
    view_path = 'terms-and-conditions/'
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
    view_path = 'privacy-and-cookies/'

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
    view_path = 'get-finance/'
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
    product_link = models.URLField()
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
        urls.SERVICE_EXPORT_READINESS: {
            'slug': cms.GREAT_PERFORMANCE_DASHBOARD_SLUG,
            'heading': 'Great.gov.uk',
            'view_path': '',
            'landing_dashboard': True,
        },
        urls.SERVICES_SOO: {
            'slug': cms.GREAT_PERFORMANCE_DASHBOARD_SOO_SLUG,
            'heading': 'Selling Online Overseas',
            'view_path': 'performance-dashboard/',
            'landing_dashboard': False,
        },
        urls.SERVICES_EXOPPS: {
            'slug': cms.GREAT_PERFORMANCE_DASHBOARD_EXOPPS_SLUG,
            'heading': 'Export Opportunities',
            'view_path': 'performance-dashboard/',
            'landing_dashboard': False,
        },
        urls.SERVICES_FAB: {
            'slug': (
                cms.GREAT_PERFORMANCE_DASHBOARD_TRADE_PROFILE_SLUG),
            'heading': 'Business Profiles',
            'view_path': 'performance-dashboard/',
            'landing_dashboard': False,
        },
        urls.SERVICES_INVEST: {
            'slug': cms.GREAT_PERFORMANCE_DASHBOARD_INVEST_SLUG,
            'heading': 'Invest in Great Britain',
            'view_path': 'performance-dashboard/',
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

    def save(self, *args, **kwargs):
        field_values = self.service_mapping[self.product_link]
        self.title = field_values['heading'] + ' Performance Dashboard'
        self.heading = field_values['heading']
        self.slug = field_values['slug']
        self.landing_dashboard = field_values['landing_dashboard']
        self.view_path = field_values['view_path']
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
    view_path = 'performance-dashboard/'
    slug_identity = cms.GREAT_PERFORMANCE_DASHBOARD_NOTES_SLUG

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

    section_one_heading = models.CharField(max_length=50)
    section_one_content = MarkdownField()

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
        max_length=255, null=True, blank=True)
    selling_point_two_content = MarkdownField(null=True, blank=True)

    selling_point_three_icon = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    selling_point_three_heading = models.CharField(
        max_length=255, null=True, blank=True)
    selling_point_three_content = MarkdownField(null=True, blank=True)

    section_two_heading = models.CharField(max_length=255)
    section_two_content = MarkdownField()

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

    @property
    def articles_count(self):
        return self.get_descendants().type(ArticlePage).live().count()

    content_panels = [
        MultiFieldPanel(
            heading='Hero',
            children=[
                FieldPanel('landing_page_title'),
                ImageChooserPanel('hero_image'),
            ]
        ),
        MultiFieldPanel(
            heading='Section one/intro',
            children=[
                FieldPanel('section_one_heading'),
                FieldPanel('section_one_content'),
            ]
        ),
        FieldRowPanel(
            heading='Section two/selling points',
            children=[
                MultiFieldPanel([
                    ImageChooserPanel('selling_point_one_icon'),
                    FieldPanel('selling_point_one_heading'),
                    FieldPanel('selling_point_one_content'),
                ]),
                MultiFieldPanel([
                    ImageChooserPanel('selling_point_two_icon'),
                    FieldPanel('selling_point_two_heading'),
                    FieldPanel('selling_point_two_content'),
                ]),
                MultiFieldPanel([
                    ImageChooserPanel('selling_point_three_icon'),
                    FieldPanel('selling_point_three_heading'),
                    FieldPanel('selling_point_three_content'),
                ]),
            ]
        ),
        MultiFieldPanel(
            heading='Section two/article section',
            children=[
                FieldPanel('section_two_heading'),
                FieldPanel('section_two_content'),
            ]
        ),
        MultiFieldPanel(
            heading='Section three/related content',
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
        SearchEngineOptimisationPanel(),
    ]

    settings_panels = [
        FieldPanel('title_en_gb'),
        FieldPanel('slug'),
    ]


class MarketingPages(ExclusivePageMixin, BasePage):
    service_name_value = cms.EXPORT_READINESS
    slug_identity = cms.GREAT_MARKETING_PAGES_SLUG

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
    view_path = 'campaigns/'

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


class HomePage(ExclusivePageMixin, BasePage):
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
    view_path = 'international/eu-exit-news/contact/'
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
    view_path = 'eu-exit-news/contact/'
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
    view_path = 'eu-exit-news/contact/success/'
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
            'view_path': (
                'contact/triage/export-opportunities/alerts-not-relevant/'
            ),
        },
        cms.GREAT_HELP_EXOPP_NO_RESPONSE: {
            'title': 'Guidance - Export Opportunity application no response',
            'view_path': (
                'contact/triage/export-opportunities/opportunity-no-response/'
            ),
        },
        cms.GREAT_HELP_MISSING_VERIFY_EMAIL_SLUG: {
            'title': 'Guidance - Email verification missing',
            'view_path': 'contact/triage/great-account/no-verification-email/',
        },
        cms.GREAT_HELP_PASSWORD_RESET_SLUG: {
            'title': 'Guidance - Missing password reset link',
            'view_path': 'contact/triage/great-account/password-reset/',
        },
        cms.GREAT_HELP_COMPANIES_HOUSE_LOGIN_SLUG: {
            'title': 'Guidance - Companies House login not working',
            'view_path': 'contact/triage/great-account/companies-house-login/',
        },
        cms.GREAT_HELP_VERIFICATION_CODE_ENTER_SLUG: {
            'title': 'Guidance - Where to enter letter verification code',
            'view_path': (
                'contact/triage/great-account/verification-letter-code/'
            ),
        },
        cms.GREAT_HELP_VERIFICATION_CODE_LETTER_SLUG: {
            'title': 'Guidance - Verification letter not delivered',
            'view_path': (
                'contact/triage/great-account/no-verification-letter/'
            ),
        },
        cms.GREAT_HELP_VERIFICATION_CODE_MISSING_SLUG: {
            'title': 'Guidance - Verification code not delivered',
            'view_path': (
                'contact/triage/great-account/verification-missing/'
            ),
        },
        cms.GREAT_HELP_ACCOUNT_COMPANY_NOT_FOUND_SLUG: {
            'title': 'Guidance - Company not found',
            'view_path': (
                'contact/triage/great-account/company-not-found/'
            ),
        },
    }

    @property
    def view_path(self):
        return self.topic_mapping[self.topic]['view_path']

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
            'view_path': 'contact/domestic/success/',
        },
        cms.GREAT_CONTACT_US_FORM_SUCCESS_EVENTS_SLUG: {
            'title': 'Contact Events form success',
            'view_path': 'contact/events/success/',
        },
        cms.GREAT_CONTACT_US_FORM_SUCCESS_DSO_SLUG: {
            'title': 'Contact Defence and Security Organisation form success',
            'view_path': 'contact/defence-and-security-organisation/success/',
        },
        cms.GREAT_CONTACT_US_FORM_SUCCESS_EXPORT_ADVICE_SLUG: {
            'title': 'Contact exporting from the UK form success',
            'view_path': 'contact/export-advice/success/',
        },
        cms.GREAT_CONTACT_US_FORM_SUCCESS_FEEDBACK_SLUG: {
            'title': 'Contact feedback form success',
            'view_path': 'contact/feedback/success/',
        },
        cms.GREAT_CONTACT_US_FORM_SUCCESS_FIND_COMPANIES_SLUG: {
            'title': 'Contact find UK companies form success',
            'view_path': 'contact/find-uk-companies/success/',
        },
        cms.GREAT_CONTACT_US_FORM_SUCCESS_INTERNATIONAL_SLUG: {
            'title': 'Contact international form success',
            'view_path': 'contact/international/success/',
        },
        cms.GREAT_CONTACT_US_FORM_SUCCESS_SOO_SLUG: {
            'title': 'Contact Selling Online Overseas form success',
            'view_path': 'contact/selling-online-overseas/success/',
        },
    }

    @property
    def view_path(self):
        return self.topic_mapping[self.topic]['view_path']

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
