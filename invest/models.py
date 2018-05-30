from django.db import models
from wagtail.api import APIField
from wagtail.core.blocks import CharBlock, StructBlock, PageChooserBlock
from wagtail.core.fields import StreamField
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.core.models import Page
from wagtail.images.blocks import ImageChooserBlock
from wagtail.images.edit_handlers import ImageChooserPanel

from core import constants
from core.fields import APIImageField, APIMetaField
from core.models import BaseApp, BasePage, ExclusivePageMixin

from .blocks import MarkdownAccordionItemBlock
from .fields import APIStreamMarkdownAccordionBlockField


class InvestApp(ExclusivePageMixin, BaseApp):
    view_app = constants.INVEST


class SectorPage():
    pass


class SetupGuidePage():
    pass


class InvestHomePage(ExclusivePageMixin, BasePage):
    heading = models.CharField(max_length=255)
    sub_heading = models.CharField(max_length=255)

    hero_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    # accordion
    subsections = StreamField([
        ('markdown', MarkdownAccordionItemBlock()),
    ], null=True)

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

    content_panels = Page.content_panels + [
        FieldPanel('heading'),
        FieldPanel('sub_heading'),
        ImageChooserPanel('hero_image'),
        StreamFieldPanel('subsections'),

        FieldPanel('sector_title'),
        FieldPanel('sector_button_text'),
        FieldPanel('setup_guide_title'),
        FieldPanel('setup_guide_lead_in'),
        FieldPanel('how_we_help_title'),
        FieldPanel('how_we_help_lead_in'),

        StreamFieldPanel('how_we_help')
    ]

    api_fields = [
        APIField('heading'),
        APIField('subheading'),
        APIImageField('hero_image'),
        APIStreamMarkdownAccordionBlockField('subsections'),

        APIField('sector_title'),
        APIField('sector_button_text'),
        APIField('setup_guide_title'),
        APIField('setup_guide_lead_in'),
        APIField('how_we_help_title'),
        APIField('how_we_help_lead_in'),
        APIMetaField('meta')
    ]

    def get_context(self, request):
        # imports here, as otherwise a circular dependency can happen
        # during the initial migration
        context = super().get_context(request)
        sector_cards = SectorPage.objects \
            .live() \
            .filter(featured=True) \
            .order_by('heading')
        setup_guide_cards = SetupGuidePage.objects \
            .live() \
            .order_by('heading')
        context.update(
            sector_cards=sector_cards,
            setup_guide_cards=setup_guide_cards,
            sector_title="Discover UK Industries",
        )
        return context
