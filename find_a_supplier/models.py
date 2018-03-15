from directory_constants.constants import choices
from wagtail.wagtailadmin.edit_handlers import (
    FieldPanel, FieldRowPanel, ObjectList, PageChooserPanel
)
from wagtail.api import APIField
from wagtail.wagtailcore.fields import RichTextField
from wagtail.wagtailimages.api.fields import ImageRenditionField
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel

from django.db import models

from core import constants
from core.models import AddTranslationsBrokerFieldsMixin, BasePage
from core.helpers import make_translated_interface
from core.fields import APIHyperlinkField, APIRichTextField


class ImageChooserPanel(ImageChooserPanel):
    classname = ""


class IndustryPage(AddTranslationsBrokerFieldsMixin, BasePage):

    view_app = constants.FIND_A_SUPPLIER
    view_path = 'industries/'

    hero_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    hero_text = RichTextField()
    lede = RichTextField()
    lede_column_one = RichTextField()
    lede_column_two = RichTextField()
    lede_column_three = RichTextField()
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
        FieldPanel('lede', classname='full'),
        FieldRowPanel(
            children=[
                FieldPanel('lede_column_one'),
                FieldPanel('lede_column_two'),
                FieldPanel('lede_column_three'),
            ],
            classname='full field-row-panel'
        ),
        FieldRowPanel(
            children=[
                ImageChooserPanel('lede_column_one_icon'),
                ImageChooserPanel('lede_column_two_icon'),
                ImageChooserPanel('lede_column_three_icon'),
            ],
            classname='full field-row-panel'
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
        other_panels=[
            ObjectList(
                settings_panels, heading='Settings', classname='settings'
            ),
            ObjectList(image_panels, heading='Images'),
            ObjectList(article_panels, heading='Articles')
        ]
    )

    api_fields = [
        APIField(
            'hero_image',
            serializer=ImageRenditionField('original')
        ),
        APIField('hero_text'),
        APIField('lede'),
        APIField('lede_column_one'),
        APIField('lede_column_two'),
        APIField('lede_column_three'),
        APIField(
            'lede_column_one_icon',
            serializer=ImageRenditionField('original')
        ),
        APIField(
            'lede_column_two_icon',
            serializer=ImageRenditionField('original')
        ),
        APIField(
            'lede_column_three_icon',
            serializer=ImageRenditionField('original')
        ),
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
    ]


class IndustryArticlePage(AddTranslationsBrokerFieldsMixin, BasePage):

    view_app = constants.FIND_A_SUPPLIER
    view_path = 'industry-articles/'

    body = RichTextField()
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
    settings_panels = BasePage.settings_panels

    edit_handler = make_translated_interface(
        content_panels=content_panels,
        other_panels=[
            ObjectList(
                settings_panels, heading='Settings', classname='settings'
            ),
        ]
    )

    api_fields = [
        APIField('author_name'),
        APIField('job_title'),
        APIField('date'),
        APIRichTextField('body'),
        APIField('title'),
        APIHyperlinkField('url'),
    ]
