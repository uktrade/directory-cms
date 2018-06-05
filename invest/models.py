from django.db import models
from wagtail.api import APIField
from wagtail.core.blocks import CharBlock, StructBlock, PageChooserBlock
from wagtail.core.fields import StreamField
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel, \
    ObjectList
from wagtail.core.models import Page
from wagtail.images.blocks import ImageChooserBlock
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtailmarkdown.blocks import MarkdownBlock

from core import constants
from core.fields import APIImageField, APIMetaField, \
    APIStreamFieldBlockField, MarkdownField
from core.helpers import make_translated_interface
from core.models import BaseApp, BasePage, ExclusivePageMixin

from . import fields


class InvestApp(ExclusivePageMixin, BaseApp):
    view_app = constants.INVEST
    slug_identity = 'invest-app'

    @classmethod
    def get_required_translatable_fields(cls):
        return []


# Sector models

class SectorLandingPage(ExclusivePageMixin, BasePage):
    view_app = constants.INVEST
    subpage_types = ['invest.sectorPage']

    # page fields
    heading = models.CharField(max_length=255)

    hero_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    image_panels = [
        ImageChooserPanel('hero_image'),
    ]
    content_panels = Page.content_panels + [
        FieldPanel('heading'),
    ]
    settings_panels = [
        FieldPanel('title_en_gb'),
        FieldPanel('slug_en_gb'),
    ]

    edit_handler = make_translated_interface(
        content_panels=content_panels,
        settings_panels=settings_panels,
        other_panels=[
            ObjectList(image_panels, heading='Images'),
        ]
    )

    api_fields = [
        APIField('heading'),
        APIImageField('hero_image'),
        APIMetaField('meta')
    ]


class SetupGuidePage(BasePage):
    view_app = constants.INVEST

    description = models.TextField()  # appears in card on external pages

    heading = models.CharField(max_length=255)
    sub_heading = models.CharField(max_length=255)

    # accordion
    subsections = StreamField([
        ('subsection', StructBlock([
            ('title', CharBlock()),
            ('content', MarkdownBlock())
        ])),
    ], null=True, blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('description'),
        FieldPanel('heading'),
        FieldPanel('sub_heading'),
        StreamFieldPanel('subsections')
    ]

    settings_panels = [
        FieldPanel('title_en_gb'),
        FieldPanel('slug_en_gb'),
    ]

    edit_handler = make_translated_interface(
        content_panels=content_panels,
        settings_panels=settings_panels,
    )

    api_fields = [
        APIField('description'),
        APIField('heading'),
        APIField('sub_heading'),
        APIStreamFieldBlockField('sections'),
        APIMetaField('meta')
    ]


class SectorPage(BasePage):
    # Related sector are implemented as subpages
    view_app = constants.INVEST
    subpage_types = ['invest.sectorPage']

    featured = models.BooleanField(default=False)
    description = models.TextField()  # appears in card on external pages

    # page fields
    heading = models.CharField(max_length=255)

    hero_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    pullout = StreamField([
        ('content', StructBlock([
            ('text', MarkdownBlock()),
            ('stat', CharBlock()),
            ('stat_text', CharBlock()
             )], max_num=1, min_num=0))
    ], blank=True)

    # accordion
    subsections = StreamField([
        ('markdown', StructBlock([
            ('title', CharBlock()),
            ('content', MarkdownBlock())
        ])),
        ('location', StructBlock([
            ('title', CharBlock()),
            ('info', MarkdownBlock()),
            ('map', ImageChooserBlock())
        ])),
    ])

    image_panels = [
        ImageChooserPanel('hero_image'),
    ]
    content_panels = Page.content_panels + [
        FieldPanel('description'),
        FieldPanel('heading'),
        StreamFieldPanel('pullout'),
        StreamFieldPanel('subsections')
    ]
    settings_panels = [
        FieldPanel('title_en_gb'),
        FieldPanel('slug_en_gb'),
        FieldPanel('featured')
    ]

    edit_handler = make_translated_interface(
        content_panels=content_panels,
        settings_panels=settings_panels,
        other_panels=[
            ObjectList(image_panels, heading='Images'),
        ]
    )

    api_fields = [
        APIField('description'),
        APIField('featured'),
        APIImageField('hero_image'),
        APIStreamFieldBlockField('pull_out'),
        APIStreamFieldBlockField('subsections'),
        APIMetaField('meta')
    ]


class InvestHomePage(ExclusivePageMixin, BasePage):
    view_app = constants.INVEST
    slug_identity = 'invest-home-page'
    view_path = 'invest/'

    heading = models.CharField(max_length=255)
    sub_heading = models.CharField(max_length=255)
    hero_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    subsections = StreamField([
        ('subsection', StructBlock([
            ('title', CharBlock()),
            ('content', MarkdownBlock())
        ])),
    ], null=True, blank=True)

    sector_title = models.TextField(
        default="Discover UK Industries",
        max_length=255)

    sector_button_text = models.TextField(
        default="See more industries",
        max_length=255)

    setup_guide_title = models.CharField(
        default='Set up an overseas business in the UK',
        max_length=255)

    setup_guide_lead_in = models.TextField(
        blank=True,
        null=True)

    how_we_help_title = models.CharField(default='How we help', max_length=255)
    how_we_help_lead_in = models.TextField(blank=True, null=True)

    how_we_help = StreamField(
        [
            ('items', StructBlock([
                ('icon', ImageChooserBlock()),
                ('text', CharBlock()),
            ])
             ),
            ('page_link', StructBlock([
                ('page', PageChooserBlock()),
                ('text', CharBlock()),
            ])
             ),
        ],
        blank=True)

    image_panels = [
        ImageChooserPanel('hero_image'),
    ]

    content_panels = Page.content_panels + [
        FieldPanel('heading'),
        FieldPanel('sub_heading'),
        StreamFieldPanel('subsections'),

        FieldPanel('sector_title'),
        FieldPanel('sector_button_text'),
        FieldPanel('setup_guide_title'),
        FieldPanel('setup_guide_lead_in'),
        FieldPanel('how_we_help_title'),
        FieldPanel('how_we_help_lead_in'),

        StreamFieldPanel('how_we_help')
    ]

    settings_panels = [
        FieldPanel('title_en_gb'),
        FieldPanel('slug_en_gb'),
    ]

    edit_handler = make_translated_interface(
        content_panels=content_panels,
        settings_panels=settings_panels,
        other_panels=[
            ObjectList(image_panels, heading='Images'),
        ]
    )

    api_fields = [
        APIField('heading'),
        APIField('sub_heading'),
        APIImageField('hero_image'),
        APIStreamFieldBlockField('subsections'),

        APIField('sector_title'),
        APIField('sector_button_text'),
        APIField('setup_guide_title'),
        APIField('setup_guide_lead_in'),
        APIField('how_we_help_title'),
        APIField('how_we_help_lead_in'),
        APIStreamFieldBlockField('how_we_help'),
        fields.APISectorPageListField(
            'sectors',
            queryset=(
                SectorPage.objects.all()
                .filter(featured=True)
                .live()
                .order_by('heading')
            )
        ),
        fields.APISetupGuidePageListField(
            'guides',
            queryset=(
                SetupGuidePage.objects.all()
                .live()
                .order_by('heading')
            )
        ),
        APIMetaField('meta')
    ]


class InfoPage(BasePage):
    """
    Markdown page - used for terms and conditions
    and privacy policy
    """
    view_app = constants.INVEST
    content = MarkdownField()

    content_panels = Page.content_panels + [
        FieldPanel('content'),
    ]

    settings_panels = [
        FieldPanel('title_en_gb'),
        FieldPanel('slug_en_gb'),
    ]

    edit_handler = make_translated_interface(
        content_panels=content_panels,
        settings_panels=settings_panels,
    )

    api_fields = [
        APIField('content'),
        APIMetaField('meta')
    ]


# Setup guide models

class SetupGuideLandingPage(ExclusivePageMixin, BasePage):
    view_app = constants.INVEST
    subpage_types = ['invest.SetupGuidePage']

    # page fields
    heading = models.CharField(max_length=255)
    sub_heading = models.CharField(max_length=255)
    lead_in = models.TextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('heading'),
        FieldPanel('sub_heading'),
        FieldPanel('lead_in'),
    ]

    settings_panels = [
        FieldPanel('title_en_gb'),
        FieldPanel('slug_en_gb'),
    ]

    edit_handler = make_translated_interface(
        content_panels=content_panels,
        settings_panels=settings_panels,
    )

    api_fields = [
        APIField('heading'),
        APIField('sub_heading'),
        APIField('lead_in'),
        APIMetaField('meta')
    ]
