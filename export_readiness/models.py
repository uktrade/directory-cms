from django.db import models

from wagtail.core.models import Page

from modelcluster.fields import ParentalManyToManyField

from directory_constants import cms, slugs

from core.model_fields import MarkdownField
from core.models import (
    BasePage,
    ExclusivePageMixin,
    FormPageMetaClass,
)
from core.constants import ARTICLE_TYPES
from core.mixins import ServiceHomepageMixin, ServiceNameUniqueSlugMixin
from export_readiness.blocks import CampaignBlock

from . import panels, snippets
from core import blocks, fields

VIDEO_TRANSCRIPT_HELP_TEXT = (
    "If the video is present, a transcript must be provided."
)


class BaseDomesticPage(ServiceNameUniqueSlugMixin, BasePage):
    service_name_value = cms.EXPORT_READINESS

    class Meta:
        abstract = True


class TermsAndConditionsPage(
    panels.TermsAndConditionsPagePanels, ExclusivePageMixin, BaseDomesticPage
):
    slug_identity = slugs.GREAT_TERMS_AND_CONDITIONS
    body = MarkdownField(blank=False)


class PrivacyAndCookiesPage(panels.PrivacyAndCookiesPagePanels, BaseDomesticPage):
    subpage_types = ['export_readiness.PrivacyAndCookiesPage']
    body = MarkdownField(blank=False)


class SitePolicyPages(ExclusivePageMixin, BaseDomesticPage):
    # a folder for T&C and privacy & cookies pages
    slug_identity = slugs.GREAT_SITE_POLICY_PAGES
    folder_page = True

    subpage_types = [
        'export_readiness.TermsAndConditionsPage',
        'export_readiness.PrivacyAndCookiesPage',
    ]

    settings_panels = []

    def save(self, *args, **kwargs):
        self.title = self.get_verbose_name()
        return super().save(*args, **kwargs)


class PerformanceDashboardNotesPage(panels.PerformanceDashboardNotesPagePanels, ExclusivePageMixin, BaseDomesticPage):

    slug_identity = slugs.PERFORMANCE_DASHBOARD_NOTES
    slug_override = 'guidance-notes'

    body = MarkdownField(
        help_text=(
            'Please include an h1 in this field e.g. # Heading level 1'),
        blank=False)


class TopicLandingPage(panels.TopicLandingPagePanels, BaseDomesticPage):
    subpage_types = [
        'export_readiness.ArticleListingPage',
        'export_readiness.SuperregionPage',
        'export_readiness.ArticlePage'
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
    banner_text = MarkdownField(blank=True)
    teaser = models.TextField(blank=True)


class SuperregionPage(TopicLandingPage):

    @property
    def articles_count(self):
        return self.get_descendants().live().count()


class ArticleListingPage(panels.ArticleListingPagePanels, BaseDomesticPage):

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


class MarketingPages(ExclusivePageMixin, BaseDomesticPage):

    slug_identity = 'campaigns'

    subpage_types = [
        'export_readiness.MarketingArticlePage',
        'export_readiness.ArticlePage',
    ]

    settings_panels = []

    @staticmethod
    def get_verbose_name():
        return 'Marketing campaign pages'

    def save(self, *args, **kwargs):
        self.title = self.get_verbose_name()
        return super().save(*args, **kwargs)


# !!! TO BE REPLACED BY `ArticlePage` !!!
class CampaignPage(panels.CampaignPagePanels, BaseDomesticPage):

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


class ArticlePage(panels.ArticlePagePanels, BaseDomesticPage):

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
        null=True,
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
    article_video_transcript = MarkdownField(
        null=True,
        blank=True,
        help_text=VIDEO_TRANSCRIPT_HELP_TEXT
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
    tags = ParentalManyToManyField(snippets.Tag, blank=True)


# !!! TO BE REPLACED BY `ArticlePage` !!!
class MarketingArticlePage(panels.MarketingArticlePagePanels, BaseDomesticPage):

    subpage_types = []

    article_title = models.CharField(max_length=255)

    article_teaser = models.CharField(
        max_length=255,
        blank=True,
        null=True
    )
    article_image = models.ForeignKey(
        'wagtailimages.Image',
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
    tags = ParentalManyToManyField(snippets.Tag, blank=True)

    class Meta:
        verbose_name = 'Marketing Article Page'
        verbose_name_plural = 'Marketing Article Pages'


class HomePage(
    panels.HomePagePanels, ExclusivePageMixin, ServiceHomepageMixin, BaseDomesticPage
):
    slug_identity = slugs.GREAT_HOME
    parent_page_types = ['wagtailcore.Page']

    # hero
    hero_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    hero_text = models.TextField(null=True, blank=True)
    hero_cta_text = models.CharField(null=True, blank=True, max_length=255)
    hero_cta_url = models.CharField(null=True, blank=True, max_length=255)

    # chevron component
    chevron_url = models.CharField(null=True, blank=True, max_length=255)
    chevron_text = models.CharField(null=True, blank=True, max_length=255)
    chevron_links = fields.single_struct_block_stream_field_factory(
        field_name='links',
        block_class_instance=blocks.LinkBlock(),
        max_num=3, null=True, blank=True
    )

    # how DIT helps
    how_dit_helps_title = models.TextField(null=True, blank=True)
    how_dit_helps_columns = fields.single_struct_block_stream_field_factory(
        field_name='columns',
        block_class_instance=blocks.LinkWithImageAndContentBlock(),
        max_num=3, null=True, blank=True
    )

    # Market access database
    madb_title = models.CharField(null=True, blank=True, max_length=255, verbose_name='Title')
    madb_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        verbose_name='Image'
    )
    madb_image_alt = models.TextField(null=True, blank=True, verbose_name='Image alt text')
    madb_content = MarkdownField(null=True, blank=True, verbose_name='Content')
    madb_cta_text = models.CharField(null=True, blank=True, max_length=255, verbose_name='CTA text')
    madb_cta_url = models.CharField(null=True, blank=True, max_length=255, verbose_name='CTA URL')

    # what's new
    what_is_new_title = models.CharField(max_length=255, null=True, blank=True)
    what_is_new_pages = fields.single_struct_block_stream_field_factory(
        field_name='pages',
        block_class_instance=blocks.LinkWithImageAndContentBlock(),
        max_num=6, null=True, blank=True
    )

    campaign = fields.single_struct_block_stream_field_factory(
        field_name='campaign',
        block_class_instance=CampaignBlock(),
        max_num=1, null=True, blank=True
    )

    @staticmethod
    def get_verbose_name():
        return 'Great domestic home page'

    @classmethod
    def allowed_subpage_models(cls):
        allowed_name = cls.service_name_value
        return [
            model for model in Page.allowed_subpage_models()
            if (getattr(model, 'service_name_value', None) == allowed_name and model is not cls)
        ]


class EUExitDomesticFormPage(ExclusivePageMixin, BaseDomesticPage, metaclass=FormPageMetaClass):
    # metaclass creates <field_name>_label and <field_name>_help_text
    form_field_names = [
        'first_name',
        'last_name',
        'email',
        'organisation_type',
        'company_name',
        'comment',
    ]

    full_path_override = '/eu-exit-news/contact/'
    slug_identity = slugs.EUEXIT_DOMESTIC_FORM

    breadcrumbs_label = models.CharField(max_length=50)
    heading = models.CharField(max_length=255)
    body_text = MarkdownField()
    submit_button_text = models.CharField(max_length=50)
    disclaimer = models.TextField(max_length=500)

    content_panels_before_form = panels.EUExitDomesticFormPagePanels.content_panels_before_form
    content_panels_after_form = panels.EUExitDomesticFormPagePanels.content_panels_after_form
    settings_panels = panels.EUExitDomesticFormPagePanels.settings_panels


class EUExitFormSuccessPage(panels.EUExitFormSuccessPagePanels, ExclusivePageMixin, BaseDomesticPage):
    full_path_override = '/eu-exit-news/contact/success/'
    slug_identity = slugs.EUEXIT_FORM_SUCCESS

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


class EUExitFormPages(ExclusivePageMixin, BaseDomesticPage):
    # this is just a folder. it will not be requested by the client.
    slug_identity = 'eu-exit-form-pages'
    folder_page = True

    subpage_types = [
        'export_readiness.EUExitDomesticFormPage',
        'export_readiness.EUExitFormSuccessPage',
    ]

    settings_panels = []

    def save(self, *args, **kwargs):
        self.title = self.get_verbose_name()
        return super().save(*args, **kwargs)


class ContactUsGuidancePages(ExclusivePageMixin, BaseDomesticPage):
    # this is just a folder. it will not be requested by the client.
    slug_identity = 'contact-us-guidance-pages'
    folder_page = True

    subpage_types = [
        'export_readiness.ContactUsGuidancePage',
    ]

    settings_panels = []

    def save(self, *args, **kwargs):
        self.title = self.get_verbose_name()
        return super().save(*args, **kwargs)


class ContactSuccessPages(ExclusivePageMixin, BaseDomesticPage):
    # this is just a folder. it will not be requested by the client.
    slug_identity = 'contact-us-success-pages'
    folder_page = True

    subpage_types = [
        'export_readiness.ContactSuccessPage',
    ]

    settings_panels = []

    def save(self, *args, **kwargs):
        self.title = self.get_verbose_name()
        return super().save(*args, **kwargs)


class ContactUsGuidancePage(panels.ContactUsGuidancePagePanels, BaseDomesticPage):

    topic_mapping = {
        slugs.HELP_EXOPP_ALERTS_IRRELEVANT: {
            'title': 'Guidance - Daily alerts are not relevant',
            'full_path_override': (
                '/contact/triage/export-opportunities/alerts-not-relevant/'
            ),
        },
        slugs.HELP_EXOPPS_NO_RESPONSE: {
            'title': 'Guidance - Export Opportunity application no response',
            'full_path_override': (
                '/contact/triage/export-opportunities/opportunity-no-response/'
            ),
        },
        slugs.HELP_MISSING_VERIFY_EMAIL: {
            'title': 'Guidance - Email verification missing',
            'full_path_override': (
                '/contact/triage/great-account/no-verification-email/'),
        },
        slugs.HELP_PASSWORD_RESET: {
            'title': 'Guidance - Missing password reset link',
            'full_path_override': (
                '/contact/triage/great-account/password-reset/'),
        },
        slugs.HELP_COMPANIES_HOUSE_LOGIN: {
            'title': 'Guidance - Companies House login not working',
            'full_path_override': (
                '/contact/triage/great-account/companies-house-login/'),
        },
        slugs.HELP_VERIFICATION_CODE_ENTER: {
            'title': 'Guidance - Where to enter letter verification code',
            'full_path_override': (
                '/contact/triage/great-account/verification-letter-code/'
            ),
        },
        slugs.HELP_VERIFICATION_CODE_LETTER: {
            'title': 'Guidance - Verification letter not delivered',
            'full_path_override': (
                '/contact/triage/great-account/no-verification-letter/'
            ),
        },
        slugs.HELP_VERIFICATION_CODE_MISSING: {
            'title': 'Guidance - Verification code not delivered',
            'full_path_override': (
                '/contact/triage/great-account/verification-missing/'
            ),
        },
        slugs.HELP_ACCOUNT_COMPANY_NOT_FOUND: {
            'title': 'Guidance - Company not found',
            'full_path_override': (
                '/contact/triage/great-account/company-not-found/'
            ),
        },
        slugs.HELP_EXPORTING_TO_UK: {
            'title': 'Guidance - Exporting to the UK',
            'full_path_override': (
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

    def save(self, *args, **kwargs):
        field_values = self.topic_mapping[self.topic]
        self.title = field_values['title']
        self.slug = self.topic
        return super().save(*args, **kwargs)


class ContactSuccessPage(panels.ContactSuccessPagePanels, BaseDomesticPage):

    topic_mapping = {
        slugs.HELP_FORM_SUCCESS: {
            'title': 'Contact domestic form success',
            'full_path_override': '/contact/domestic/success/',
        },
        slugs.HELP_FORM_SUCCESS_EVENTS: {
            'title': 'Contact Events form success',
            'full_path_override': '/contact/events/success/',
        },
        slugs.HELP_FORM_SUCCESS_DSO: {
            'title': 'Contact Defence and Security Organisation form success',
            'full_path_override': (
                '/contact/defence-and-security-organisation/success/'),
        },
        slugs.HELP_FORM_SUCCESS_EXPORT_ADVICE: {
            'title': 'Contact exporting from the UK form success',
            'full_path_override': '/contact/export-advice/success/',
        },
        slugs.HELP_FORM_SUCCESS_FEEDBACK: {
            'title': 'Contact feedback form success',
            'full_path_override': '/contact/feedback/success/',
        },
        slugs.HELP_FORM_SUCCESS_FIND_COMPANIES: {
            'title': 'Contact find UK companies form success',
            'full_path_override': '/contact/find-uk-companies/success/',
        },
        slugs.HELP_FORM_SUCCESS_INTERNATIONAL: {
            'title': 'Contact international form success',
            'full_path_override': '/contact/international/success/',
        },
        slugs.HELP_FORM_SUCCESS_SOO: {
            'title': 'Contact Selling Online Overseas form success',
            'full_path_override': '/contact/selling-online-overseas/success/',
        },
        slugs.HELP_FORM_SUCCESS_BEIS: {
            'title': 'Contact BEIS form success',
            'full_path_override': (
                'contact/department-for-business-energy-'
                'and-industrial-strategy/success/'
            )
        },
        slugs.HELP_FORM_SUCCESS_DEFRA: {
            'title': 'Contact DEFRA form success',
            'full_path_override': (
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

    def save(self, *args, **kwargs):
        field_values = self.topic_mapping[self.topic]
        self.title = field_values['title']
        self.slug = self.topic
        return super().save(*args, **kwargs)


class AllContactPagesPage(ExclusivePageMixin, BaseDomesticPage):
    # this is just a folder. it will not be requested by the client.

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
