from wagtail.api import APIField
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel

from django.db import models

from core import constants
from core.fields import AbsoluteUrlImageRenditionField
from core.models import BasePage


class DemoPage(BasePage):
    lede = RichTextField()
    body = RichTextField()
    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    image_description = models.CharField(max_length=255)
    quote_one_name = models.TextField(max_length=100)
    quote_one_text = models.TextField(max_length=200)
    quote_one_job_title = models.TextField(max_length=100)
    quote_one_link = models.URLField()
    quote_two_name = models.TextField(max_length=100)
    quote_two_text = models.TextField(max_length=200)
    quote_two_job_title = models.TextField(max_length=100)
    quote_two_link = models.URLField()

    view_app = models.CharField(
        max_length=255,
        choices=constants.APP_CHOICES,
        help_text='The app the template will be rendered on'
    )
    view_path = models.CharField(
        max_length=255,
        help_text='The path to view the rendered template'
    )

    content_panels = BasePage.content_panels + [
        FieldPanel('lede', classname="full"),
        FieldPanel('body', classname="full"),
        ImageChooserPanel('image'),
        FieldPanel('image_description'),
        FieldPanel('quote_one_name'),
        FieldPanel('quote_one_text'),
        FieldPanel('quote_one_job_title'),
        FieldPanel('quote_one_link'),
        FieldPanel('quote_two_name'),
        FieldPanel('quote_two_text'),
        FieldPanel('quote_two_job_title'),
        FieldPanel('quote_two_link'),
    ]

    api_fields = [
        APIField('lede'),
        APIField('body'),
        APIField(
            'image', serializer=AbsoluteUrlImageRenditionField('original')
        ),
        APIField('image_description'),
        APIField('quote_one_name'),
        APIField('quote_one_text'),
        APIField('quote_one_job_title'),
        APIField('quote_one_link'),
        APIField('quote_two_name'),
        APIField('quote_two_text'),
        APIField('quote_two_job_title'),
        APIField('quote_two_link'),
    ]

    settings_panels = BasePage.settings_panels + [
        FieldPanel('view_app'),
        FieldPanel('view_path'),
    ]
