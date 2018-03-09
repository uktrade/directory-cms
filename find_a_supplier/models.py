from directory_constants.constants import choices
from wagtail.wagtailadmin.edit_handlers import (
    FieldPanel, ObjectList, FieldRowPanel
)
from wagtail.api import APIField
from wagtail.wagtailcore.fields import RichTextField
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel

from django.db import models

from core import constants
from wagtail.wagtailimages.api.fields import ImageRenditionField
from core.models import AddTranslationsBrokerFieldsMixin, BasePage
from core.helpers import make_translated_interface


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
    case_study = RichTextField()
    case_study_image = models.ForeignKey(
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

    image_panels = [
        ImageChooserPanel('hero_image'),
        ImageChooserPanel('case_study_image'),
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
        FieldPanel('case_study', classname='full'),
        FieldPanel('sector_label'),
        FieldPanel('slug'),
        FieldPanel('seo_description'),
        FieldPanel('title'),
    ]
    settings_panels = BasePage.settings_panels + [
        FieldPanel('sector_value'),
    ]

    edit_handler = make_translated_interface(
        content_panels=content_panels,
        other_panels=[
            ObjectList(
                settings_panels, heading='Settings', classname='settings'
            ),
            ObjectList(image_panels, heading='Images'),
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
        APIField('case_study'),
        APIField(
            'case_study_image',
            serializer=ImageRenditionField('original')
        ),
        APIField('sector_label'),
        APIField('sector_value'),
        APIField('seo_description'),
        APIField('title'),
    ]
