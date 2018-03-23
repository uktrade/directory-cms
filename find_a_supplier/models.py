from directory_constants.constants import choices
from wagtail.wagtailadmin.edit_handlers import (
    FieldPanel, FieldRowPanel, MultiFieldPanel, ObjectList, PageChooserPanel
)
from wagtail.api import APIField
from wagtail.wagtailcore.fields import RichTextField
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel

from django.db import models

from core import constants
from core.models import BasePage
from core.helpers import make_translated_interface
from core.fields import (
    APIHyperlinkField, APIRichTextField, APIImageField, APITranslationsField
)


class ImageChooserPanel(ImageChooserPanel):
    classname = ""


class IndustryLandingPage(BasePage):
    view_app = constants.FIND_A_SUPPLIER
    view_path = 'industries/'

    hero_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    proposition_text = models.CharField(max_length=500)
    call_to_action_text = models.CharField(max_length=500)
    breadcrumbs_label = models.CharField(max_length=500)
    seo_description = models.CharField(max_length=1000)

    @property
    def url_path_parts(self):
        return [self.view_path]

    api_fields = [
        APIImageField('hero_image'),
        APIField('proposition_text'),
        APIField('call_to_action_text'),
        APIHyperlinkField('url'),
        APIField('title'),
        APIField('seo_description'),
        APIField('breadcrumbs_label'),
        APITranslationsField('languages'),
    ]

    image_panels = [
        ImageChooserPanel('hero_image'),
    ]

    content_panels = [
        FieldPanel('breadcrumbs_label'),
        FieldPanel('title'),
        FieldRowPanel(
            children=[
                FieldPanel('proposition_text'),
                FieldPanel('call_to_action_text'),
            ],
            classname='full field-row-panel'
        ),
        FieldPanel('slug'),
        FieldPanel('seo_description'),
    ]

    edit_handler = make_translated_interface(
        content_panels=content_panels,
        other_panels=[
            ObjectList(image_panels, heading='Images'),
        ]
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
    hero_text = RichTextField(blank=False)
    lede = RichTextField(blank=False)
    lede_column_one = RichTextField(blank=False)
    lede_column_two = RichTextField(blank=False)
    lede_column_three = RichTextField(blank=False)
    lede_column_one_icon = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    lede_column_two_icon = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    lede_column_three_icon = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    sector_label = models.CharField(
        max_length=255,
    )
    sector_value = models.CharField(
        max_length=255,
        choices=choices.INDUSTRIES,
    )
    seo_description = models.CharField(max_length=1000)

    article_one = models.ForeignKey(
        'find_a_supplier.IndustryArticlePage',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
    )
    article_two = models.ForeignKey(
        'find_a_supplier.IndustryArticlePage',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
    )
    article_three = models.ForeignKey(
        'find_a_supplier.IndustryArticlePage',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
    )
    article_four = models.ForeignKey(
        'find_a_supplier.IndustryArticlePage',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
    )
    article_five = models.ForeignKey(
        'find_a_supplier.IndustryArticlePage',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
    )
    article_six = models.ForeignKey(
        'find_a_supplier.IndustryArticlePage',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
    )
    image_panels = [
        ImageChooserPanel('hero_image'),
    ]
    content_panels = [
        FieldPanel('hero_text', classname='full'),
        MultiFieldPanel(
            heading='Introduction',
            children=[
                FieldPanel('lede', classname='full'),
                FieldRowPanel(
                    classname='full field-row-panel',
                    children=[
                        MultiFieldPanel([
                            FieldPanel('lede_column_one'),
                            ImageChooserPanel('lede_column_one_icon'),
                        ]),
                        MultiFieldPanel([
                            FieldPanel('lede_column_two'),
                            ImageChooserPanel('lede_column_two_icon'),
                        ]),
                        MultiFieldPanel([
                            FieldPanel('lede_column_three'),
                            ImageChooserPanel('lede_column_three_icon'),
                        ])
                    ]
                )
            ]
        ),
        FieldPanel('sector_label'),
        FieldPanel('slug'),
        FieldPanel('seo_description'),
        FieldPanel('title'),
    ]
    settings_panels = BasePage.settings_panels + [
        FieldPanel('sector_value'),
    ]
    article_panels = [
        PageChooserPanel('article_one', 'find_a_supplier.IndustryArticlePage'),
        PageChooserPanel('article_two', 'find_a_supplier.IndustryArticlePage'),
        PageChooserPanel(
            'article_three', 'find_a_supplier.IndustryArticlePage'
        ),
        PageChooserPanel(
            'article_four', 'find_a_supplier.IndustryArticlePage'
        ),
        PageChooserPanel(
            'article_five', 'find_a_supplier.IndustryArticlePage'
        ),
        PageChooserPanel('article_six', 'find_a_supplier.IndustryArticlePage'),
    ]

    edit_handler = make_translated_interface(
        content_panels=content_panels,
        settings_panels=settings_panels,
        other_panels=[
            ObjectList(image_panels, heading='Images'),
            ObjectList(article_panels, heading='Articles')
        ]
    )

    api_fields = [
        APIImageField('hero_image'),
        APIField('hero_text'),
        APIField('lede'),
        APIField('lede_column_one'),
        APIField('lede_column_two'),
        APIField('lede_column_three'),
        APIImageField('lede_column_one_icon'),
        APIImageField('lede_column_two_icon'),
        APIImageField('lede_column_three_icon'),
        APIField('sector_label'),
        APIField('sector_value'),
        APIField('seo_description'),
        APIField('title'),
        APIField('article_one'),
        APIField('article_two'),
        APIField('article_three'),
        APIField('article_four'),
        APIField('article_five'),
        APIField('article_six'),
        APIHyperlinkField('url'),
        APITranslationsField('languages'),
    ]


class IndustryArticlePage(BasePage):

    view_app = constants.FIND_A_SUPPLIER
    view_path = 'industry-articles/'

    body = RichTextField(blank=False)
    author_name = models.CharField(max_length=255)
    job_title = models.CharField(max_length=255)
    date = models.DateField()

    content_panels = [
        FieldPanel('slug'),
        FieldPanel('title'),
        FieldPanel('author_name'),
        FieldPanel('job_title'),
        FieldPanel('date'),
        FieldPanel('body', classname='full'),
    ]

    edit_handler = make_translated_interface(
        content_panels=content_panels,
        settings_panels=BasePage.settings_panels
    )

    api_fields = [
        APIField('author_name'),
        APIField('job_title'),
        APIField('date'),
        APIRichTextField('body'),
        APIField('title'),
        APIHyperlinkField('url'),
        APITranslationsField('languages'),
    ]


class LandingPage(BasePage):
    view_app = constants.FIND_A_SUPPLIER
    view_path = '/'

    hero_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    hero_text = RichTextField(blank=False)
    search_field_placeholder = models.CharField(max_length=500)
    search_button_text = models.CharField(max_length=500)
    proposition_text = RichTextField(blank=False)
    call_to_action_text = models.CharField(max_length=500)
    industries_list_text = RichTextField(blank=False)
    industries_list_call_to_action_text = models.CharField(max_length=500)
    services_list_text = RichTextField(blank=False)
    services_column_one = RichTextField(blank=False)
    services_column_two = RichTextField(blank=False)
    services_column_three = RichTextField(blank=False)
    services_column_four = RichTextField(blank=False)
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
    article_one = models.ForeignKey(
        'find_a_supplier.IndustryArticlePage',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
    )
    article_two = models.ForeignKey(
        'find_a_supplier.IndustryArticlePage',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
    )
    article_three = models.ForeignKey(
        'find_a_supplier.IndustryArticlePage',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
    )
    article_four = models.ForeignKey(
        'find_a_supplier.IndustryArticlePage',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
    )
    article_five = models.ForeignKey(
        'find_a_supplier.IndustryArticlePage',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
    )
    article_six = models.ForeignKey(
        'find_a_supplier.IndustryArticlePage',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
    )

    seo_description = models.CharField(max_length=1000)

    @property
    def url_path_parts(self):
        return [self.view_path]

    api_fields = [
        APIImageField('hero_image'),
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
        APIField('article_one'),
        APIField('article_two'),
        APIField('article_three'),
        APIField('article_four'),
        APIField('article_five'),
        APIField('article_six'),
        APIField('seo_description'),
        APIHyperlinkField('url'),
        APIField('title'),
        APITranslationsField('languages'),
    ]

    image_panels = [
        ImageChooserPanel('hero_image'),
    ]
    article_panels = [
        PageChooserPanel('article_one', 'find_a_supplier.IndustryArticlePage'),
        PageChooserPanel('article_two', 'find_a_supplier.IndustryArticlePage'),
        PageChooserPanel(
            'article_three', 'find_a_supplier.IndustryArticlePage'
        ),
        PageChooserPanel(
            'article_four', 'find_a_supplier.IndustryArticlePage'
        ),
        PageChooserPanel(
            'article_five', 'find_a_supplier.IndustryArticlePage'
        ),
        PageChooserPanel('article_six', 'find_a_supplier.IndustryArticlePage'),
    ]

    content_panels = [
        FieldPanel('title'),
        MultiFieldPanel(
            heading='Hero',
            children=[
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
        FieldPanel('slug'),
        FieldPanel('seo_description'),
    ]

    edit_handler = make_translated_interface(
        content_panels=content_panels,
        other_panels=[
            ObjectList(image_panels, heading='Images'),
            ObjectList(article_panels, heading='Articles'),
        ]
    )
