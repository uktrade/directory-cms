from directory_constants.constants import choices
from modelcluster.fields import ParentalKey
from wagtail.wagtailadmin.edit_handlers import (
    FieldPanel, FieldRowPanel, MultiFieldPanel, ObjectList, InlinePanel
)
from wagtail.api import APIField
from wagtail.wagtailcore.models import Orderable
from wagtail.wagtailcore.fields import RichTextField
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel

from django.db import models

from core import constants
from core.fields import (
    APIBreadcrumbsField, APIRichTextField, APIImageField, APIMetaField,
    APIVideoField
)
from core.helpers import make_translated_interface
from core.models import BasePage, BaseApp, ExclusivePageMixin, ChoiceArrayField
from core.panels import SearchEngineOptimisationPanel
from find_a_supplier import fields

from wagtail.utils.decorators import cached_classmethod


class ImageChooserPanel(ImageChooserPanel):
    classname = ""


class FindASupplierApp(ExclusivePageMixin, BaseApp):
    view_app = constants.FIND_A_SUPPLIER


class ArticleSummary(models.Model):
    industry_name = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    body = RichTextField(features=constants.RICH_TEXT_FEATURES)
    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    video = models.URLField(blank=True)

    panels = [
        FieldPanel('industry_name'),
        FieldPanel('title'),
        FieldPanel('body'),
        ImageChooserPanel('image'),
        FieldPanel('video')
    ]

    api_fields = [
        APIField('industry_name'),
        APIField('title'),
        APIRichTextField('body'),
        APIImageField('image'),
        APIVideoField('video'),
    ]

    class Meta:
        abstract = True


class IndustryPageArticleSummary(Orderable, ArticleSummary):
    page = ParentalKey(
        'find_a_supplier.IndustryPage',
        on_delete=models.CASCADE,
        related_name='article_summaries',
        blank=True,
        null=True,
    )


class LandingPageArticleSummary(Orderable, ArticleSummary):
    page = ParentalKey(
        'find_a_supplier.LandingPage',
        on_delete=models.CASCADE,
        related_name='article_summaries',
        blank=True,
        null=True,
    )


class IndustryPage(BasePage):

    view_app = constants.FIND_A_SUPPLIER
    view_path = 'industries/'

    hero_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    mobile_hero_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    summary_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    hero_text = RichTextField(
        blank=False,
        features=constants.RICH_TEXT_FEATURES
    )
    introduction_text = models.CharField(max_length=400)
    introduction_call_to_action_button_text = models.CharField(max_length=50)
    introduction_column_one_text = RichTextField(
        blank=False,
        features=constants.RICH_TEXT_FEATURES,
    )
    introduction_column_two_text = RichTextField(
        blank=False,
        features=constants.RICH_TEXT_FEATURES,
    )
    introduction_column_three_text = RichTextField(
        blank=False,
        features=constants.RICH_TEXT_FEATURES,
    )
    introduction_column_one_icon = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    introduction_column_two_icon = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    introduction_column_three_icon = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    breadcrumbs_label = models.CharField(max_length=50)
    search_filter_sector = ChoiceArrayField(
        base_field=models.CharField(
            max_length=255,
            choices=choices.INDUSTRIES,
        ),
        blank=True,
        null=True,
        verbose_name='Sector filter',
        help_text='Limit to companies within these sectors.'
    )
    search_filter_text = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        verbose_name='Profile text filter',
        help_text='Limit to companies that contain this term in their profile.'
    )
    search_filter_showcase_only = models.BooleanField(
        default=False,
        verbose_name='Whitelisted companies filter',
        help_text='Limit to companies that have explicitly been whitelisted.',
    )
    company_list_text = RichTextField(
        blank=False,
        features=constants.RICH_TEXT_FEATURES,
    )
    company_list_search_input_placeholder_text = models.CharField(
        max_length=255,
        blank=True,
    )
    company_list_call_to_action_text = models.CharField(
        max_length=255,
    )

    image_panels = [
        ImageChooserPanel('hero_image'),
        ImageChooserPanel('mobile_hero_image'),
        ImageChooserPanel('summary_image'),
    ]
    content_panels = [
        MultiFieldPanel(
            heading='Hero',
            children=[
                FieldPanel('hero_text', classname='full'),
                FieldPanel('breadcrumbs_label'),
            ]
        ),
        MultiFieldPanel(
            heading='Introduction',
            children=[
                FieldRowPanel(
                    children=[
                        FieldPanel('introduction_text'),
                        FieldPanel('introduction_call_to_action_button_text'),
                    ]
                ),
                FieldRowPanel(
                    classname='full field-row-panel',
                    children=[
                        MultiFieldPanel([
                            FieldPanel('introduction_column_one_text'),
                            ImageChooserPanel('introduction_column_one_icon'),
                        ]),
                        MultiFieldPanel([
                            FieldPanel('introduction_column_two_text'),
                            ImageChooserPanel('introduction_column_two_icon'),
                        ]),
                        MultiFieldPanel([
                            FieldPanel('introduction_column_three_text'),
                            ImageChooserPanel(
                                'introduction_column_three_icon'
                            ),
                        ])
                    ]
                )
            ]
        ),
        MultiFieldPanel(
            heading='Companies',
            children=[
                FieldPanel('company_list_text'),
                FieldPanel('company_list_search_input_placeholder_text'),
                FieldPanel('company_list_call_to_action_text'),
            ]
        ),
        InlinePanel('article_summaries', label="Articles"),
        SearchEngineOptimisationPanel(),
    ]
    settings_panels = [
        FieldPanel('title_en_gb'),
        FieldPanel('slug_en_gb'),
        MultiFieldPanel(
            heading='Company list filters',
            children=[
                FieldPanel('search_filter_showcase_only'),
                FieldPanel('search_filter_sector'),
                FieldPanel('search_filter_text'),
            ]
        )
    ]

    edit_handler = make_translated_interface(
        content_panels=content_panels,
        settings_panels=settings_panels,
        other_panels=[
            ObjectList(image_panels, heading='Images'),
        ]
    )

    api_fields = [
        APIImageField('hero_image'),
        APIImageField('mobile_hero_image'),
        APIImageField('summary_image'),
        APIRichTextField('hero_text'),
        APIField('introduction_text'),
        APIField('introduction_call_to_action_button_text'),
        APIRichTextField('introduction_column_one_text'),
        APIRichTextField('introduction_column_two_text'),
        APIRichTextField('introduction_column_three_text'),
        APIImageField('introduction_column_one_icon'),
        APIImageField('introduction_column_two_icon'),
        APIImageField('introduction_column_three_icon'),
        APIRichTextField('company_list_text'),
        APIField('company_list_call_to_action_text'),
        APIField('company_list_search_input_placeholder_text'),
        APIField('search_filter_sector'),
        APIField('search_filter_text'),
        APIField('search_filter_showcase_only'),
        APIField('title'),
        fields.APIArticleSummariesField('article_summaries'),
        APIField('seo_title'),
        APIField('search_description'),
        APIField('breadcrumbs_label'),
        APIBreadcrumbsField('breadcrumbs', app_label='find_a_supplier'),
        APIMetaField('meta'),
    ]


class IndustryLandingPage(ExclusivePageMixin, BasePage):
    view_app = constants.FIND_A_SUPPLIER
    view_path = 'industries/'
    slug_identity = 'industries-landing-page'

    hero_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    mobile_hero_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    breadcrumbs_label = models.CharField(max_length=50)
    hero_title = models.CharField(max_length=500)
    proposition_text = models.CharField(max_length=500)
    call_to_action_text = models.CharField(max_length=500)
    more_industries_title = models.CharField(max_length=100)

    def get_url_path_parts(self, *args, **kwargs):
        return [self.view_path]

    api_fields = [
        APIField('hero_title'),
        APIImageField('hero_image'),
        APIImageField('mobile_hero_image'),
        APIField('proposition_text'),
        APIField('call_to_action_text'),
        APIField('title'),
        APIField('breadcrumbs_label'),
        APIField('seo_title'),
        APIField('search_description'),
        APIField('more_industries_title'),
        APIMetaField('meta'),
        fields.APIIndustriesListField(
            'industries',
            queryset=IndustryPage.objects.all().order_by('slug'),
        ),
        APIBreadcrumbsField('breadcrumbs', app_label='find_a_supplier'),
    ]

    image_panels = [
        ImageChooserPanel('hero_image'),
        ImageChooserPanel('mobile_hero_image'),
    ]

    content_panels = [
        FieldPanel('breadcrumbs_label'),
        FieldPanel('hero_title'),
        MultiFieldPanel(
            heading='Contact us',
            children=[
                FieldRowPanel(
                    children=[
                        FieldPanel('proposition_text'),
                        FieldPanel('call_to_action_text'),
                    ],
                    classname='full field-row-panel'
                ),
            ]
        ),
        FieldPanel('more_industries_title'),
        SearchEngineOptimisationPanel(),
    ]
    settings_panels = [
        FieldPanel('title_en_gb'),
    ]

    edit_handler = make_translated_interface(
        content_panels=content_panels,
        settings_panels=settings_panels,
        other_panels=[
            ObjectList(image_panels, heading='Images'),
        ]
    )


class IndustryArticlePage(BasePage):

    view_app = constants.FIND_A_SUPPLIER
    view_path = 'industry-articles/'

    breadcrumbs_label = models.CharField(max_length=50)
    introduction_title = models.CharField(max_length=255)
    body = RichTextField(
        blank=False,
        features=constants.RICH_TEXT_FEATURES,
    )
    author_name = models.CharField(max_length=255)
    job_title = models.CharField(max_length=255)
    proposition_text = RichTextField(
        blank=False,
        features=constants.RICH_TEXT_FEATURES,
    )
    call_to_action_text = models.CharField(max_length=500)
    show_table_of_content = models.BooleanField(
        default=False,
        help_text=(
            'Any H2 in the body will be listed in the table of content. '
            'Allows users to click to go to sections of the page. Useful for '
            'long articles.'
        )
    )

    date = models.DateField()

    content_panels = [
        FieldPanel('breadcrumbs_label'),
        MultiFieldPanel(
            heading='Contact us',
            children=[
                FieldPanel('proposition_text'),
                FieldPanel('call_to_action_text'),
            ],
            classname='collapsible',
        ),
        MultiFieldPanel(
            heading='Article',
            children=[
                FieldPanel('introduction_title'),
                FieldPanel('body', classname='full'),
            ]
        ),
        MultiFieldPanel(
            heading='Author',
            children=[
                FieldPanel('author_name'),
                FieldPanel('job_title'),
                FieldPanel('date'),
            ]
        ),
        SearchEngineOptimisationPanel(),
    ]

    settings_panels = [
        FieldPanel('title_en_gb'),
        FieldPanel('slug_en_gb'),
        MultiFieldPanel(
            heading='Page structure',
            children=[FieldPanel('show_table_of_content')]
        )
    ]

    edit_handler = make_translated_interface(
        content_panels=content_panels,
        settings_panels=settings_panels
    )

    api_fields = [
        APIField('breadcrumbs_label'),
        APIField('author_name'),
        APIField('job_title'),
        APIField('date'),
        APIRichTextField('body'),
        APIField('title'),
        APIField('seo_title'),
        APIField('search_description'),
        APIRichTextField('proposition_text'),
        APIField('call_to_action_text'),
        APIField('introduction_title'),
        APIField('show_table_of_content'),
        APIBreadcrumbsField('breadcrumbs', app_label='find_a_supplier'),
        APIMetaField('meta'),
    ]


class LandingPage(ExclusivePageMixin, BasePage):
    view_app = constants.FIND_A_SUPPLIER
    view_path = '/'
    slug_identity = 'landing-page'

    hero_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    mobile_hero_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    breadcrumbs_label = models.CharField(max_length=50)
    hero_text = RichTextField(
        blank=False,
        features=constants.RICH_TEXT_FEATURES,
    )
    search_field_placeholder = models.CharField(max_length=500)
    search_button_text = models.CharField(max_length=500)
    proposition_text = RichTextField(
        blank=False,
        features=constants.RICH_TEXT_FEATURES,
    )
    call_to_action_text = models.CharField(max_length=500)
    industries_list_text = RichTextField(
        blank=False,
        features=constants.RICH_TEXT_FEATURES,
    )
    industries_list_call_to_action_text = models.CharField(max_length=500)
    services_list_text = RichTextField(
        blank=False,
        features=constants.RICH_TEXT_FEATURES,
    )
    services_column_one = RichTextField(
        blank=False,
        features=constants.RICH_TEXT_FEATURES,
    )
    services_column_two = RichTextField(
        blank=False,
        features=constants.RICH_TEXT_FEATURES,
    )
    services_column_three = RichTextField(
        blank=False,
        features=constants.RICH_TEXT_FEATURES,
    )
    services_column_four = RichTextField(
        blank=False,
        features=constants.RICH_TEXT_FEATURES,
    )
    services_column_one_icon = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    services_column_two_icon = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    services_column_three_icon = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    services_column_four_icon = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    def get_url_path_parts(self, *args, **kwargs):
        return [self.view_path]

    api_fields = [
        APIImageField('hero_image'),
        APIImageField('mobile_hero_image'),
        APIField('breadcrumbs_label'),
        APIRichTextField('hero_text'),
        APIField('search_field_placeholder'),
        APIField('search_button_text'),
        APIRichTextField('proposition_text'),
        APIField('call_to_action_text'),
        APIRichTextField('industries_list_text'),
        APIField('industries_list_call_to_action_text'),
        APIRichTextField('services_list_text'),
        APIRichTextField('services_column_one'),
        APIRichTextField('services_column_two'),
        APIRichTextField('services_column_three'),
        APIRichTextField('services_column_four'),
        APIImageField('services_column_one_icon'),
        APIImageField('services_column_two_icon'),
        APIImageField('services_column_three_icon'),
        APIImageField('services_column_four_icon'),
        APIField('title'),
        APIField('search_description'),
        APIField('seo_title'),
        fields.APIIndustriesListField(
            'industries',
            queryset=IndustryPage.objects.all().order_by('slug')[:3],
        ),
        fields.APIArticleSummariesField('article_summaries'),
        APIBreadcrumbsField('breadcrumbs', app_label='find_a_supplier'),
        APIMetaField('meta'),
    ]

    image_panels = [
        ImageChooserPanel('hero_image'),
        ImageChooserPanel('mobile_hero_image'),
    ]

    content_panels = [
        MultiFieldPanel(
            heading='Hero',
            children=[
                FieldPanel('breadcrumbs_label'),
                FieldPanel('hero_text'),
                FieldPanel('search_field_placeholder'),
                FieldPanel('search_button_text'),
            ],
            classname='collapsible',
        ),
        MultiFieldPanel(
            heading='Contact us',
            children=[
                FieldPanel('proposition_text'),
                FieldPanel('call_to_action_text'),
            ],
            classname='collapsible',
        ),
        MultiFieldPanel(
            heading='Industries',
            children=[
                FieldPanel('industries_list_text'),
                FieldPanel('industries_list_call_to_action_text'),
            ],
            classname='collapsible',
        ),
        MultiFieldPanel(
            heading='Services',
            children=[
                FieldPanel('services_list_text'),
                FieldRowPanel(
                    classname='full field-row-panel',
                    children=[
                        MultiFieldPanel([
                            ImageChooserPanel('services_column_one_icon'),
                            FieldPanel('services_column_one'),
                        ]),
                        MultiFieldPanel([
                            ImageChooserPanel('services_column_two_icon'),
                            FieldPanel('services_column_two'),
                        ]),
                        MultiFieldPanel([
                            ImageChooserPanel('services_column_three_icon'),
                            FieldPanel('services_column_three'),
                        ]),
                        MultiFieldPanel([
                            ImageChooserPanel('services_column_four_icon'),
                            FieldPanel('services_column_four'),
                        ]),
                    ]
                ),
            ],
            classname='collapsible',
        ),
        InlinePanel('article_summaries', label='Articles'),
        SearchEngineOptimisationPanel()
    ]

    settings_panels = [
        FieldPanel('title_en_gb'),
    ]

    edit_handler = make_translated_interface(
        content_panels=content_panels,
        settings_panels=settings_panels,
        other_panels=[
            ObjectList(image_panels, heading='Images'),
        ]
    )


class IndustryContactPage(ExclusivePageMixin, BasePage):

    view_app = constants.FIND_A_SUPPLIER
    view_path = 'industries/help/contact-us/'
    slug_identity = 'industry-contact'

    def get_url_path_parts(self, *args, **kwargs):
        return [self.view_path]

    breadcrumbs_label = models.CharField(max_length=50)
    introduction_text = RichTextField(
        blank=False,
        features=constants.RICH_TEXT_FEATURES,
    )
    submit_button_text = models.CharField(max_length=100)
    success_message_text = RichTextField(
        blank=False,
        features=constants.RICH_TEXT_FEATURES,
    )
    success_back_link_text = models.CharField(max_length=100)

    content_panels = [
        MultiFieldPanel(
            heading='Contact form',
            children=[
                FieldPanel('breadcrumbs_label'),
                FieldPanel('introduction_text'),
                FieldPanel('submit_button_text'),
            ]
        ),
        MultiFieldPanel(
            heading='Success page',
            children=[
                FieldPanel('success_message_text'),
                FieldPanel('success_back_link_text'),
            ]
        ),
        SearchEngineOptimisationPanel(),
    ]

    settings_panels = [
        FieldPanel('title_en_gb'),
    ]

    edit_handler = make_translated_interface(
        content_panels=content_panels,
        settings_panels=settings_panels,
    )

    api_fields = [
        APIField('seo_title'),
        APIField('search_description'),
        APIField('breadcrumbs_label'),
        APIField('introduction_text'),
        APIField('submit_button_text'),
        APIField('success_message_text'),
        APIField('success_back_link_text'),
        APIBreadcrumbsField('breadcrumbs', app_label='find_a_supplier'),
        APIMetaField('meta'),
    ]
