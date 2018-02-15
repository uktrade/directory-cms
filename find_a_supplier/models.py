from directory_constants.constants import choices
from modelcluster.fields import ParentalKey
from wagtail.wagtailadmin.edit_handlers import FieldPanel
from wagtail.api import APIField
from wagtail.wagtailcore.fields import RichTextField
from wagtail.wagtailcore.models import Orderable
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel

from django.contrib.postgres.fields import ArrayField
from django.db import models

from core import constants
from core.fields import AbsoluteUrlImageRenditionField
from core.models import AddTranslationsBrokerFieldsMixin, BasePage
from core.helpers import make_translated_interface


class Company(Orderable):
    page = ParentalKey(
        'find_a_supplier.CaseStudyPage',
        on_delete=models.CASCADE,
        related_name='companies'
    )
    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    image_alt = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    description = RichTextField()
    url = models.URLField()

    panels = [
        ImageChooserPanel('image'),
        FieldPanel('image_alt'),
        FieldPanel('name'),
        FieldPanel('description'),
        FieldPanel('url'),
    ]

    api_fields = [
        APIField('image_alt'),
        APIField(
            'image', serializer=AbsoluteUrlImageRenditionField('original')
        ),
        APIField('name'),
        APIField('description'),
        APIField('url'),
    ]


class Showcase(Orderable):
    page = ParentalKey(
        'find_a_supplier.CaseStudyPage',
        on_delete=models.CASCADE,
        related_name='case_study'
    )
    image_alt = models.CharField(max_length=255)
    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    image_caption = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    synopsis = RichTextField()
    url = models.URLField()
    testimonial = RichTextField()
    testimonial_name = models.CharField(max_length=255)
    testimonial_company = models.CharField(max_length=255)
    company_name = models.CharField(max_length=255)
    sectors = ArrayField(
        models.CharField(choices=choices.INDUSTRIES, max_length=255)
    )
    keywords = models.CharField(max_length=255)

    panels = [
        FieldPanel('image_alt'),
        ImageChooserPanel('image'),
        FieldPanel('image_caption'),
        FieldPanel('title'),
        FieldPanel('synopsis'),
        FieldPanel('url'),
        FieldPanel('testimonial'),
        FieldPanel('testimonial_name'),
        FieldPanel('testimonial_company'),
        FieldPanel('company_name'),
        FieldPanel('sectors'),
        FieldPanel('keywords'),
    ]

    api_fields = [
        APIField('image_alt'),
        APIField(
            'image', serializer=AbsoluteUrlImageRenditionField('original')
        ),
        APIField('image_caption'),
        APIField('title'),
        APIField('synopsis'),
        APIField('url'),
        APIField('testimonial'),
        APIField('testimonial_name'),
        APIField('testimonial_company'),
        APIField('company_name'),
        APIField('sectors'),
        APIField('keywords'),
    ]


class CaseStudyPage(AddTranslationsBrokerFieldsMixin, BasePage):

    view_app = constants.FIND_A_SUPPLIER
    view_path = 'industries/'

    footer_text = models.CharField(max_length=255)
    footer_title = models.CharField(max_length=255)
    companies_section_title = models.CharField(max_length=255)
    lede = RichTextField()
    body = RichTextField()
    key_facts = RichTextField()
    read_more_text = models.CharField(max_length=255)
    layout_class = models.CharField(max_length=255)
    seo_description = models.CharField(max_length=255)
    sector = models.CharField(
        max_length=255,
        choices=choices.INDUSTRIES,
    )

    content_panels = [
        FieldPanel('slug'),
        FieldPanel('seo_title'),
        FieldPanel('seo_description'),
        FieldPanel('title', classname='full'),
        FieldPanel('lede', classname='full'),
        FieldPanel('read_more_text'),
        FieldPanel('body', classname='full'),
        FieldPanel('key_facts', classname='full'),
        FieldPanel('companies_section_title'),
        FieldPanel('footer_text'),
        FieldPanel('footer_title'),
    ]
    settings_panels = BasePage.settings_panels + [
        FieldPanel('layout_class'),
        FieldPanel('sector')
    ]

    edit_handler = make_translated_interface(
        content_panels=content_panels,
        settings_panels=settings_panels
    )

    api_fields = [
        APIField('lede'),
        APIField('read_more_text'),
        APIField('body'),
        APIField('key_facts'),
        APIField('sector'),
        APIField('companies_section_title'),
        APIField('companies'),
        APIField('case_study'),
        APIField('footer_text'),
        APIField('footer_title'),
        APIField('layout_class'),
        APIField('seo_description'),
        APIField('title')
    ]
