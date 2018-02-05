from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel

from django.db import models


class DemoPage(Page):
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

    content_panels = Page.content_panels + [
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
