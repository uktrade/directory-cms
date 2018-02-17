from directory_constants.constants import choices
from wagtail.wagtailadmin.edit_handlers import FieldPanel, ObjectList
from wagtail.api import APIField
from wagtail.wagtailcore.fields import RichTextField
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel

from django.db import models

from core import constants
from core.fields import AbsoluteUrlImageRenditionField
from core.models import AddTranslationsBrokerFieldsMixin, BasePage
from core.helpers import make_translated_interface


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
    seo_description = models.CharField(max_length=255)

    image_panels = [
        ImageChooserPanel('hero_image'),
        ImageChooserPanel('case_study_image'),
    ]

    content_panels = [
        FieldPanel('hero_text', classname='full'),
        FieldPanel('lede', classname='full'),
        FieldPanel('lede_column_one', classname='full'),
        FieldPanel('lede_column_two', classname='full'),
        FieldPanel('lede_column_three', classname='full'),
        FieldPanel('case_study', classname='full'),
        FieldPanel('sector_label'),
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
            serializer=AbsoluteUrlImageRenditionField('original')
        ),
        APIField('hero_text'),
        APIField('lede'),
        APIField('lede_column_one'),
        APIField('lede_column_two'),
        APIField('lede_column_three'),
        APIField('case_study'),
        APIField(
            'case_study_image',
            serializer=AbsoluteUrlImageRenditionField('original')
        ),
        APIField('sector_label'),
        APIField('sector_value'),
        APIField('seo_description'),
        APIField('title'),
    ]
