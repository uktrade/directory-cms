from directory_constants.constants import choices
from modelcluster.fields import ParentalKey
from modeltranslation.utils import build_localized_fieldname
from wagtail.wagtailadmin.edit_handlers import (
    TabbedInterface, ObjectList, FieldPanel, InlinePanel
)
from wagtail.api import APIField
from wagtail.wagtailcore.fields import RichTextField
from wagtail.wagtailcore.models import Orderable
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel

from django.conf import settings
from django.contrib.postgres.fields import ArrayField
from django.db import models

from core.fields import AbsoluteUrlImageRenditionField
from core.models import BasePage
from core import constants



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


content_panel_parts = [
    (FieldPanel, {'field_name': 'slug'}),
    (FieldPanel, {'field_name': 'seo_title'}),
    (FieldPanel, {'field_name': 'seo_description'}),
    (FieldPanel, {'field_name': 'title', 'classname': 'full'}),
    (FieldPanel, {'field_name': 'lede', 'classname': 'full'}),
    (FieldPanel, {'field_name': 'read_more_text'}),
    (FieldPanel, {'field_name': 'body', 'classname': 'full'}),
    (FieldPanel, {'field_name': 'key_facts', 'classname': 'full'}),
    (FieldPanel, {'field_name': 'companies_section_title'}),
    (FieldPanel, {'field_name': 'footer_text'}),
    (FieldPanel, {'field_name': 'footer_title'}),
]

def make_panel(language_code=None):
    def add_suffix(kwargs):
        overrides = {}
        if language_code and 'field_name' in kwargs:
            overrides['field_name'] = build_localized_fieldname(
                kwargs['field_name'],
                language_code
            )
        return {**kwargs, **overrides}

    return[
        Panel(**add_suffix(kwargs)) for Panel, kwargs in content_panel_parts
    ]


class CaseStudyPage(BasePage):

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

    settings_panels = BasePage.settings_panels + [
        FieldPanel('layout_class'),
        FieldPanel(field_name='sector')
    ]

    edit_handler = TabbedInterface(
        [
            ObjectList(make_panel(language), heading=name)
            for language, name in settings.LANGUAGES
        ] +
        [ObjectList(settings_panels, heading='Settings', classname="settings")]
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
    ]
