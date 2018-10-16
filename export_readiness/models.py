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
from django.forms import CheckboxSelectMultiple
from django.utils.text import slugify

from core.api_fields import APIMarkdownToHTMLField, APIImageField, \
    APIMetaField, APIVideoField, MarkdownField, APITagsField

from core.models import (
    BasePage,
    BreadcrumbMixin,
    ExclusivePageMixin,
    FormPageMetaClass,
    ServiceMixin,
)
from core.panels import SearchEngineOptimisationPanel
from .fields import (APIChildrenArticleListingPageListField,
                     APIChildrenTopicLandingPageListField,
                     APIArticleNewsPageListField,
                     APIGuidanceArticleListingListField
                     )


class ExportReadinessApp(ExclusivePageMixin, ServiceMixin, BasePage):
    slug_identity = 'export-readiness-app'
    service_name_value = cms.EXPORT_READINESS

    @classmethod
    def get_required_translatable_fields(cls):
        return []


class TermsAndConditionsPage(ExclusivePageMixin, BasePage):

    service_name_value = cms.EXPORT_READINESS
    view_path = 'terms-and-conditions/'
    slug_identity = 'terms-and-conditions'

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

    api_fields = [
        APIField('seo_title'),
        APIField('search_description'),
        APIMarkdownToHTMLField('body'),
        APIMetaField('meta'),
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

    api_fields = [
        APIField('seo_title'),
        APIField('search_description'),
        APIMarkdownToHTMLField('body'),
        APIMetaField('meta'),
    ]


class DeprecatedGetFinancePage(ExclusivePageMixin, BreadcrumbMixin, BasePage):

    service_name_value = cms.EXPORT_READINESS
    view_path = 'get-finance/'
    slug_identity = 'get-finance-deprecated'

    banner_image = models.ForeignKey(
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

    breadcrumbs_label = models.CharField(max_length=50)
    banner_content = MarkdownField()
    section_one_content = MarkdownField()
    section_two_content = MarkdownField()
    video_embed = models.CharField(max_length=500)
    section_three_content = MarkdownField()
    call_to_action_text = models.CharField(max_length=255)
    call_to_action_url = models.CharField(max_length=500)

    content_panels = [
        FieldPanel('breadcrumbs_label'),
        MultiFieldPanel(
            heading='Banner',
            children=[
                FieldPanel('banner_content'),
                ImageChooserPanel('banner_image'),
            ]
        ),
        MultiFieldPanel(
            heading='Section 1',
            children=[
                ImageChooserPanel('ukef_logo'),
                MarkdownPanel('section_one_content'),
                FieldPanel('call_to_action_text'),
                FieldPanel('call_to_action_url'),
            ]
        ),
        MultiFieldPanel(
            heading='Section 2',
            children=[
                MarkdownPanel('section_two_content'),
                FieldPanel('video_embed'),
            ]
        ),
        MultiFieldPanel(
            heading='Section 3',
            children=[
                MarkdownPanel('section_three_content'),
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
        APIMarkdownToHTMLField('banner_content'),
        APIImageField('banner_image'),
        APIMarkdownToHTMLField('section_one_content'),
        APIMarkdownToHTMLField('section_two_content'),
        APIImageField('ukef_logo'),
        APIField('video_embed'),
        APIMarkdownToHTMLField('section_three_content'),
        APIField('call_to_action_text'),
        APIField('call_to_action_url'),
        APIField('seo_title'),
        APIField('search_description'),
        APIMetaField('meta'),
    ]

    def get_admin_display_title(self):
        return '[deprecated] ' + super().get_admin_display_title()


# To rename to GetFinancePage once DeprecatedGetFinancePage has been deleted
class NewGetFinancePage(ExclusivePageMixin, BreadcrumbMixin, BasePage):

    service_name_value = cms.EXPORT_READINESS
    view_path = 'get-finance/'
    slug_identity = 'get-finance'

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

    api_fields = [
        APIField('breadcrumbs_label'),
        APIMarkdownToHTMLField('hero_text'),
        APIImageField('hero_image'),
        APIImageField('ukef_logo'),
        APIMarkdownToHTMLField('contact_proposition'),
        APIField('contact_button'),
        APIField('advantages_title'),
        APIMarkdownToHTMLField('advantages_one'),
        APIImageField('advantages_one_icon'),
        APIMarkdownToHTMLField('advantages_two'),
        APIImageField('advantages_two_icon'),
        APIMarkdownToHTMLField('advantages_three'),
        APIImageField('advantages_three_icon'),
        APIMarkdownToHTMLField('evidence'),
        APIVideoField('evidence_video'),
        APIMetaField('meta'),
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

    api_fields = [
        APIField('heading'),
        APIMarkdownToHTMLField('description'),
        APIField('product_link'),
        # row 1
        APIField('data_title_row_one'),
        APIField('data_number_row_one'),
        APIField('data_period_row_one'),
        APIMarkdownToHTMLField('data_description_row_one'),
        # row 2
        APIField('data_title_row_two'),
        APIField('data_number_row_two'),
        APIField('data_period_row_two'),
        APIMarkdownToHTMLField('data_description_row_two'),
        # row 3
        APIField('data_title_row_three'),
        APIField('data_number_row_three'),
        APIField('data_period_row_three'),
        APIMarkdownToHTMLField('data_description_row_three'),
        # row 4
        APIField('data_title_row_four'),
        APIField('data_number_row_four'),
        APIField('data_period_row_four'),
        APIMarkdownToHTMLField('data_description_row_four'),

        APIMarkdownToHTMLField('guidance_notes'),
        APIField('landing_dashboard'),
        APIMetaField('meta')
    ]


class PerformanceDashboardNotesPage(ExclusivePageMixin,
                                    BasePage):

    service_name_value = cms.EXPORT_READINESS
    view_path = 'performance-dashboard/'
    slug_identity = 'performance-dashboard-notes'

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

    api_fields = [
        APIField('seo_title'),
        APIField('search_description'),
        APIMarkdownToHTMLField('body'),
        APIMetaField('meta'),
    ]


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

    api_fields = [
        APIField('seo_title'),
        APIField('search_description'),
        APIField('landing_page_title'),
        APIImageField('hero_image'),
        APIField('hero_teaser'),
        APIChildrenTopicLandingPageListField('article_listing'),
        APIMetaField('meta')
    ]


class ArticleListingPage(BasePage):
    service_name_value = cms.EXPORT_READINESS
    subpage_types = ['export_readiness.ArticlePage']

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

    api_fields = [
        APIField('seo_title'),
        APIField('search_description'),
        APIField('landing_page_title'),
        APIImageField('hero_image'),
        APIField('hero_teaser'),
        APIMarkdownToHTMLField('list_teaser'),
        APIChildrenArticleListingPageListField('articles'),
        APIField('articles_count'),
        APIField('full_url'),
        APIField('full_path'),
        APIField('last_published_at'),
        APIMetaField('meta'),
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

    api_fields = [
        APIField('seo_title'),
        APIField('search_description'),
        APIField('article_title'),
        APIField('article_teaser'),
        APIImageField('article_image'),
        APIMarkdownToHTMLField('article_body_text'),
        APIField('related_article_one_url'),
        APIField('related_article_one_title'),
        APIField('related_article_one_teaser'),
        APIField('related_article_two_url'),
        APIField('related_article_two_title'),
        APIField('related_article_two_teaser'),
        APIField('related_article_three_url'),
        APIField('related_article_three_title'),
        APIField('related_article_three_teaser'),
        APIField('full_url'),
        APITagsField('tags'),
        APIField('full_path'),
        APIField('last_published_at'),
        APIMetaField('meta'),
    ]


class HomePage(ExclusivePageMixin, BasePage):
    service_name_value = cms.EXPORT_READINESS
    slug_identity = 'home'
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

    api_fields = [
        APIField('seo_title'),
        APIField('search_description'),
        APIField('news_title'),
        APIMarkdownToHTMLField('news_description'),
        APIArticleNewsPageListField('articles'),
        APIGuidanceArticleListingListField('guidance'),
        APIMetaField('meta')
    ]


class InternationalLandingPage(ExclusivePageMixin, BasePage):
    service_name_value = cms.EXPORT_READINESS
    slug_identity = 'international'
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

    api_fields = [
        APIField('seo_title'),
        APIField('search_description'),
        APIMetaField('meta')
    ]


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
    slug_identity = 'eu-exit-international'

    breadcrumbs_label = models.CharField(max_length=50)
    heading = models.CharField(max_length=255)
    body_text = MarkdownField()
    submit_button_text = models.CharField(max_length=50)

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
    slug_identity = 'eu-exit-domestic'

    breadcrumbs_label = models.CharField(max_length=50)
    heading = models.CharField(max_length=255)
    body_text = MarkdownField()
    submit_button_text = models.CharField(max_length=50)

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
        APIField('seo_title'),
        APIField('search_description'),
    ]


class EUExitFormSuccessPage(ExclusivePageMixin, BasePage):
    service_name_value = cms.EXPORT_READINESS
    view_path = 'eu-exit/contact/success/'
    slug_identity = 'eu-exit-form-success'

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
