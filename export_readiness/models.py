from directory_constants.constants import cms
from modelcluster.fields import ParentalManyToManyField
from wagtail.admin.edit_handlers import (
    FieldPanel, FieldRowPanel, MultiFieldPanel
)
from wagtail.api import APIField
from wagtail.core.models import Page
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.search import index
from wagtail.snippets.models import register_snippet
from wagtailmarkdown.edit_handlers import MarkdownPanel
from wagtailmedia.widgets import AdminMediaChooser

from django.db import models
from django.forms import CheckboxSelectMultiple, Textarea, Select
from django.utils.text import slugify

from core.api_fields import APIMarkdownToHTMLField, APIMetaField
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
    slug_identity = cms.EXPORT_READINESS_TERMS_AND_CONDITIONS_SLUG

    body = MarkdownField(blank=False)

    content_panels = [
        MultiFieldPanel(
            heading='Terms and conditions',
            children=[
                MarkdownPanel('body'),
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
                MarkdownPanel('body'),
            ]
        ),
        SearchEngineOptimisationPanel(),
    ]

    settings_panels = [
        FieldPanel('title_en_gb'),
        FieldPanel('slug'),
    ]

    promote_panels = []


class GetFinancePage(ExclusivePageMixin, BreadcrumbMixin, BasePage):

    service_name_value = cms.EXPORT_READINESS
    view_path = 'get-finance/'
    slug_identity = cms.EXPORT_READINESS_GET_FINANCE_SLUG

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
    view_path = ''
    subpage_types = ['export_readiness.PerformanceDashboardPage']

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

    content_panels = Page.content_panels + [
        FieldPanel('heading'),
        FieldPanel('description'),
        FieldPanel('product_link'),
        # row 1
        FieldPanel('data_title_row_one'),
        FieldPanel('data_number_row_one'),
        FieldPanel('data_period_row_one'),
        FieldPanel('data_description_row_one'),
        # row 2
        FieldPanel('data_title_row_two'),
        FieldPanel('data_number_row_two'),
        FieldPanel('data_period_row_two'),
        FieldPanel('data_description_row_two'),
        # row 3
        FieldPanel('data_title_row_three'),
        FieldPanel('data_number_row_three'),
        FieldPanel('data_period_row_three'),
        FieldPanel('data_description_row_three'),
        # row 4
        FieldPanel('data_title_row_four'),
        FieldPanel('data_number_row_four'),
        FieldPanel('data_period_row_four'),
        FieldPanel('data_description_row_four'),

        FieldPanel('guidance_notes'),
        FieldPanel('landing_dashboard')
    ]
    settings_panels = [
        FieldPanel('title_en_gb'),
        FieldPanel('slug'),
    ]


class PerformanceDashboardNotesPage(ExclusivePageMixin,
                                    BasePage):

    service_name_value = cms.EXPORT_READINESS
    view_path = 'performance-dashboard/'
    slug_identity = cms.EXPORT_READINESS_PERFORMANCE_DASHBOARD_NOTES_SLUG

    body = MarkdownField(blank=False)

    content_panels = [
        MultiFieldPanel(
            heading='Performance dashboard notes',
            children=[
                MarkdownPanel('body'),
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
    subpage_types = ['export_readiness.ArticleListingPage']

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


class ArticleListingPage(BasePage):
    service_name_value = cms.EXPORT_READINESS
    subpage_types = [
        'export_readiness.ArticlePage',
        'export_readiness.EUExitInternationalFormPage',
        'export_readiness.EUExitDomesticFormPage',
        'export_readiness.EUExitFormSuccessPage',
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


class MarketingPages(ExclusivePageMixin, BasePage):
    service_name_value = cms.EXPORT_READINESS
    slug_identity = cms.EXPORT_READINESS_MARKETING_PAGES_SLUG

    subpage_types = [
        'export_readiness.CampaignPage',
    ]

    title_value = 'Marketing pages'
    settings_panels = []

    def save(self, *args, **kwargs):
        self.title = self.title_value
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

    # CMS-647
    # TODO: crawl these urls and save metadata to the page
    related_page_one_url = models.CharField(
        max_length=255,
        null=True,
        blank=True
    )
    # if there is no metadata or it isn't appropriate we can override it here
    related_page_one_heading = models.CharField(
        max_length=255,
        null=True,
        blank=True
    )
    related_page_one_description = models.CharField(
        max_length=255,
        null=True,
        blank=True
    )
    related_page_one_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    related_page_two_url = models.CharField(
        max_length=255,
        null=True,
        blank=True
    )
    related_page_two_heading = models.CharField(
        max_length=255,
        null=True,
        blank=True
    )
    related_page_two_description = models.CharField(
        max_length=255,
        null=True,
        blank=True
    )
    related_page_two_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    related_page_three_url = models.CharField(
        max_length=255,
        null=True,
        blank=True
    )
    related_page_three_heading = models.CharField(
        max_length=255,
        null=True,
        blank=True
    )
    related_page_three_description = models.CharField(
        max_length=255,
        null=True,
        blank=True
    )
    related_page_three_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
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
                MarkdownPanel('section_one_intro'),
                ImageChooserPanel('section_one_image'),
                FieldRowPanel([
                    MultiFieldPanel(
                        children=[
                            ImageChooserPanel('selling_point_one_icon'),
                            FieldPanel('selling_point_one_heading'),
                            MarkdownPanel('selling_point_one_content'),
                        ]
                    ),
                    MultiFieldPanel(
                        children=[
                            ImageChooserPanel('selling_point_two_icon'),
                            FieldPanel('selling_point_two_heading'),
                            MarkdownPanel('selling_point_two_content'),
                        ]
                    ),
                    MultiFieldPanel(
                        children=[
                            ImageChooserPanel('selling_point_three_icon'),
                            FieldPanel('selling_point_three_heading'),
                            MarkdownPanel('selling_point_three_content'),
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
                MarkdownPanel('section_two_intro'),
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
                MarkdownPanel('related_content_intro'),
                FieldRowPanel([
                    MultiFieldPanel([
                        ImageChooserPanel('related_page_one_image'),
                        FieldPanel('related_page_one_heading'),
                        FieldPanel(
                            'related_page_one_description', widget=Textarea),
                        FieldPanel('related_page_one_url'),
                    ]),
                    MultiFieldPanel([
                        ImageChooserPanel('related_page_two_image'),
                        FieldPanel('related_page_two_heading'),
                        FieldPanel(
                            'related_page_two_description', widget=Textarea),
                        FieldPanel('related_page_two_url'),
                    ]),
                    MultiFieldPanel([
                        ImageChooserPanel('related_page_three_image'),
                        FieldPanel('related_page_three_heading'),
                        FieldPanel(
                            'related_page_three_description', widget=Textarea),
                        FieldPanel('related_page_three_url'),
                    ])
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

    article_teaser = models.CharField(max_length=255)
    article_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    article_body_text = MarkdownField()

    related_article_one_url = models.CharField(
        max_length=255,
        help_text='Paste the article path here (eg /foo/bar/)',
        null=True,
        blank=True
    )
    related_article_one_title = models.CharField(
        max_length=255,
        help_text='Paste the title of the article here',
        null=True,
        blank=True
    )
    related_article_one_teaser = models.CharField(
        max_length=255,
        help_text='Paste the article description here (max 255 characters)',
        null=True,
        blank=True
    )
    related_article_two_url = models.CharField(
        max_length=255,
        help_text='Paste the article path here (eg /foo/bar/)',
        null=True,
        blank=True
    )
    related_article_two_title = models.CharField(
        max_length=255,
        help_text='Paste the title of the article here',
        null=True,
        blank=True
    )
    related_article_two_teaser = models.CharField(
        max_length=255,
        help_text='Paste the article description here (max 255 characters)',
        null=True,
        blank=True
    )
    related_article_three_url = models.CharField(
        max_length=255,
        help_text='Paste the article path here (eg /foo/bar/)',
        null=True,
        blank=True
    )
    related_article_three_title = models.CharField(
        max_length=255,
        help_text='Paste the title of the article here',
        null=True,
        blank=True
    )
    related_article_three_teaser = models.CharField(
        max_length=255,
        help_text='Paste the article description here (max 255 characters)',
        null=True,
        blank=True
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
                MarkdownPanel('article_body_text')
            ]
        ),
        MultiFieldPanel(
            heading='Related article one',
            children=[
                FieldPanel('related_article_one_url'),
                FieldPanel('related_article_one_title'),
                FieldPanel('related_article_one_teaser'),
            ]
        ),
        MultiFieldPanel(
            heading='Related article two',
            children=[
                FieldPanel('related_article_two_url'),
                FieldPanel('related_article_two_title'),
                FieldPanel('related_article_two_teaser'),
            ]
        ),
        MultiFieldPanel(
            heading='Related article three',
            children=[
                FieldPanel('related_article_three_url'),
                FieldPanel('related_article_three_title'),
                FieldPanel('related_article_three_teaser'),
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
    slug_identity = cms.EXPORT_READINESS_HOME_SLUG
    subpage_types = [
        'export_readiness.TopicLandingPage',
        'export_readiness.ArticleListingPage',
        'export_readiness.ArticlePage'
    ]

    news_title = models.CharField(max_length=255)
    news_description = MarkdownField()

    content_panels = [
        MultiFieldPanel(
            heading='EU exit news',
            children=[
                FieldPanel('news_title'),
                MarkdownPanel('news_description')
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
    slug_identity = cms.EXPORT_READINESS_HOME_INTERNATIONAL_SLUG
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
    view_path = 'eu-exit/international/contact/'
    slug_identity = cms.EXPORT_READINESS_EUEXIT_INTERNATIONAL_FORM_SLUG

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
                MarkdownPanel('body_text'),
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

    # metaclass appends `form_field_names` to `api_fields`
    api_fields = [
        APIField('breadcrumbs_label'),
        APIField('heading'),
        APIMarkdownToHTMLField('body_text'),
        APIField('submit_button_text'),
        APIField('disclaimer'),
        APIField('seo_title'),
        APIField('search_description'),
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
    view_path = 'eu-exit/contact/'
    slug_identity = cms.EXPORT_READINESS_EUEXIT_DOMESTIC_FORM_SLUG

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
                MarkdownPanel('body_text'),
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

    # metaclass appends `form_field_names` to `api_fields`
    api_fields = [
        APIField('breadcrumbs_label'),
        APIField('heading'),
        APIField('submit_button_text'),
        APIMarkdownToHTMLField('body_text'),
        APIField('disclaimer'),
        APIField('seo_title'),
        APIField('search_description'),
    ]


class EUExitFormSuccessPage(ExclusivePageMixin, BasePage):
    service_name_value = cms.EXPORT_READINESS
    view_path = 'eu-exit/contact/success/'
    slug_identity = cms.EXPORT_READINESS_EUEXIT_FORM_SUCCESS_SLUG

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

    api_fields = [
        APIField('breadcrumbs_label'),
        APIField('heading'),
        APIField('body_text'),
        APIField('next_title'),
        APIField('next_body_text'),
        APIMetaField('meta'),
        APIField('seo_title'),
        APIField('search_description'),
    ]


class ContactUsGuidancePage(BasePage):

    service_name_value = cms.EXPORT_READINESS

    topic_mapping = {
        cms.EXPORT_READINESS_HELP_EXOPP_ALERTS_IRRELEVANT_SLUG: {
            'title': 'Guidance - Daily alerts are not relevant',
            'view_path': (
                'contact/triage/export-opportunities/alerts-not-relevant/'
            ),
        },
        cms.EXPORT_READINESS_HELP_EXOPP_NO_RESPONSE: {
            'title': 'Guidance - Export Opportunity application no response',
            'view_path': (
                'contact/triage/export-opportunities/opportunity-no-response/'
            ),
        },
        cms.EXPORT_READINESS_HELP_MISSING_VERIFY_EMAIL_SLUG: {
            'title': 'Guidance - Email verification missing',
            'view_path': 'contact/triage/great-account/no-verification-email/',
        },
        cms.EXPORT_READINESS_HELP_PASSWORD_RESET_SLUG: {
            'title': 'Guidance - Missing password reset link',
            'view_path': 'contact/triage/great-account/password-reset/',
        },
        cms.EXPORT_READINESS_HELP_COMPANIES_HOUSE_LOGIN_SLUG: {
            'title': 'Guidance - Companies House login not working',
            'view_path': 'contact/triage/great-account/companies-house-login/',
        },
        cms.EXPORT_READINESS_HELP_VERIFICATION_CODE_ENTER_SLUG: {
            'title': 'Guidance - Where to enter letter verification code',
            'view_path': (
                'contact/triage/great-account/verification-letter-code/'
            ),
        },
        cms.EXPORT_READINESS_HELP_VERIFICATION_CODE_LETTER_SLUG: {
            'title': 'Guidance - Verification letter not delivered',
            'view_path': (
                'contact/triage/great-account/no-verification-letter/'
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

    api_fields = [
        APIMarkdownToHTMLField('body'),
        APIMetaField('meta'),
        APIField('seo_title'),
        APIField('search_description'),
    ]

    def save(self, *args, **kwargs):
        field_values = self.topic_mapping[self.topic]
        self.title = field_values['title']
        self.slug = self.topic
        return super().save(*args, **kwargs)


class ContactSuccessPage(BasePage):

    service_name_value = cms.EXPORT_READINESS

    topic_mapping = {
        cms.EXPORT_READINESS_CONTACT_US_FORM_SUCCESS_SLUG: {
            'title': 'Contact domestic form success',
            'view_path': 'contact/domestic/success/',
        },
        cms.EXPORT_READINESS_CONTACT_US_FORM_SUCCESS_EVENTS_SLUG: {
            'title': 'Contact Events form success',
            'view_path': 'contact/events/success/',
        },
        cms.EXPORT_READINESS_CONTACT_US_FORM_SUCCESS_DSO_SLUG: {
            'title': 'Contact Defence and Security Organisation form success',
            'view_path': 'contact/defence-and-security-organisation/success/',
        },
        cms.EXPORT_READINESS_CONTACT_US_FORM_SUCCESS_EXPORT_ADVICE_SLUG: {
            'title': 'Contact exporting from the UK form success',
            'view_path': 'contact/export-advice/success/',
        },
        cms.EXPORT_READINESS_CONTACT_US_FORM_SUCCESS_FEEDBACK_SLUG: {
            'title': 'Contact feedback form success',
            'view_path': 'contact/feedback/success/',
        },
        cms.EXPORT_READINESS_CONTACT_US_FORM_SUCCESS_FIND_COMPANIES_SLUG: {
            'title': 'Contact find UK companies form success',
            'view_path': 'contact/find-uk-companies/success/',
        },
        cms.EXPORT_READINESS_CONTACT_US_FORM_SUCCESS_INTERNATIONAL_SLUG: {
            'title': 'Contact international form success',
            'view_path': 'contact/international/success/',
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

    api_fields = [
        APIField('heading'),
        APIField('body_text'),
        APIField('next_title'),
        APIField('next_body_text'),
        APIMetaField('meta'),
        APIField('seo_title'),
        APIField('search_description'),
    ]

    def save(self, *args, **kwargs):
        field_values = self.topic_mapping[self.topic]
        self.title = field_values['title']
        self.slug = self.topic
        return super().save(*args, **kwargs)
