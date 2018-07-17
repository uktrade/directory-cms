from django.db import models
from wagtail.api import APIField
from wagtail.core.blocks import CharBlock, StructBlock, PageChooserBlock
from wagtail.core.fields import StreamField
from wagtail.admin.edit_handlers import FieldPanel, ObjectList, MultiFieldPanel
from wagtail.core.models import Page
from wagtail.images.blocks import ImageChooserBlock
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtailmarkdown.blocks import MarkdownBlock

from core import constants
from core.fields import APIImageField, APIMetaField, \
    APIStreamFieldBlockField, MarkdownField, APIMarkdownToHTMLField
from core.helpers import make_translated_interface
from core.models import BaseApp, BasePage, ExclusivePageMixin
from core.panels import SearchEngineOptimisationPanel

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
    slug_identity = 'invest-sector-landing-page'
    view_path = 'industries/'

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
        SearchEngineOptimisationPanel()

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
        APIField('seo_title'),
        APIField('search_description'),
        APIField('heading'),
        APIImageField('hero_image'),
        fields.APIChildrenSectorPageListField('children_sectors'),
        APIMetaField('meta')
    ]


class RegionLandingPage(ExclusivePageMixin, BasePage):
    view_app = constants.INVEST
    subpage_types = ['invest.sectorPage']
    slug_identity = 'invest-uk-region-landing-page'
    view_path = 'uk-regions/'

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
        SearchEngineOptimisationPanel()
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
        APIField('seo_title'),
        APIField('search_description'),
        APIField('heading'),
        APIImageField('hero_image'),
        fields.APIChildrenSectorPageListField('children_sectors'),
        APIMetaField('meta')
    ]


class SectorPage(BasePage):
    # Related sector are implemented as subpages
    view_app = constants.INVEST
    subpage_types = ['invest.sectorPage']
    view_path = 'industries/'

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
    ], blank=True, null=True)

    pullout_text = MarkdownField(blank=True, null=True)
    pullout_stat = models.CharField(max_length=255, blank=True, null=True)
    pullout_stat_text = models.CharField(max_length=255, blank=True, null=True)

    # subsections
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
    ], null=True, blank=True)

    subsection_title_one = models.CharField(max_length=200)
    subsection_content_one = MarkdownField(blank=True)
    subsection_info_one = MarkdownField(blank=True)
    subsection_map_one = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    subsection_title_two = models.CharField(max_length=200)
    subsection_content_two = MarkdownField(blank=True)
    subsection_info_two = MarkdownField(blank=True)
    subsection_map_two = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    subsection_title_three = models.CharField(max_length=200, blank=True)
    subsection_content_three = MarkdownField(blank=True)
    subsection_info_three = MarkdownField(blank=True)
    subsection_map_three = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    subsection_title_four = models.CharField(max_length=200, blank=True)
    subsection_content_four = MarkdownField(blank=True)
    subsection_info_four = MarkdownField(blank=True)
    subsection_map_four = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    subsection_title_five = models.CharField(max_length=200, blank=True)
    subsection_content_five = MarkdownField(blank=True)
    subsection_info_five = MarkdownField(blank=True)
    subsection_map_five = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    subsection_title_six = models.CharField(max_length=200, blank=True)
    subsection_content_six = MarkdownField(blank=True)
    subsection_info_six = MarkdownField(blank=True)
    subsection_map_six = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    subsection_title_seven = models.CharField(max_length=200, blank=True)
    subsection_content_seven = MarkdownField(blank=True)
    subsection_info_seven = MarkdownField(blank=True)
    subsection_map_seven = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    # subsections end

    image_panels = [
        ImageChooserPanel('hero_image'),
    ]
    content_panels = Page.content_panels + [
        FieldPanel('description'),
        FieldPanel('heading'),
        MultiFieldPanel(
            [
                FieldPanel('pullout_text'),
                FieldPanel('pullout_stat'),
                FieldPanel('pullout_stat_text')
            ],
            heading='Pullout',
            classname='collapsible'
        ),
        # subsections panels
        MultiFieldPanel(
            [
                FieldPanel('subsection_title_one'),
                FieldPanel('subsection_content_one'),
                FieldPanel('subsection_info_one'),
                ImageChooserPanel('subsection_map_one')
            ],
            heading='subsections one',
            classname='collapsible'
        ),
        MultiFieldPanel(
            [
                FieldPanel('subsection_title_two'),
                FieldPanel('subsection_content_two'),
                FieldPanel('subsection_info_two'),
                ImageChooserPanel('subsection_map_two')
            ],
            heading='subsections two',
            classname='collapsible'
        ),
        MultiFieldPanel(
            [
                FieldPanel('subsection_title_three'),
                FieldPanel('subsection_content_three'),
                FieldPanel('subsection_info_three'),
                ImageChooserPanel('subsection_map_three')
            ],
            heading='subsections three',
            classname='collapsible collapsed'
        ),
        MultiFieldPanel(
            [
                FieldPanel('subsection_title_four'),
                FieldPanel('subsection_content_four'),
                FieldPanel('subsection_info_four'),
                ImageChooserPanel('subsection_map_four')
            ],
            heading='subsections four',
            classname='collapsible collapsed'
        ),
        MultiFieldPanel(
            [
                FieldPanel('subsection_title_five'),
                FieldPanel('subsection_content_five'),
                FieldPanel('subsection_info_five'),
                ImageChooserPanel('subsection_map_five')
            ],
            heading='subsections five',
            classname='collapsible collapsed'
        ),
        MultiFieldPanel(
            [
                FieldPanel('subsection_title_six'),
                FieldPanel('subsection_content_six'),
                FieldPanel('subsection_info_six'),
                ImageChooserPanel('subsection_map_six')
            ],
            heading='subsections six',
            classname='collapsible collapsed'
        ),
        MultiFieldPanel(
            [
                FieldPanel('subsection_title_seven'),
                FieldPanel('subsection_content_seven'),
                FieldPanel('subsection_info_seven'),
                ImageChooserPanel('subsection_map_seven')
            ],
            heading='Subsection seven',
            classname='collapsible collapsed'
        ),

        SearchEngineOptimisationPanel()
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
        APIField('seo_title'),
        APIField('search_description'),
        APIField('description'),
        APIField('featured'),
        APIField('heading'),
        APIImageField('hero_image'),
        # pullout
        APIStreamFieldBlockField('pullout'),

        APIField('pullout_text'),
        APIField('pullout_stat'),
        APIField('pullout_stat_text'),
        # subsections
        APIStreamFieldBlockField('subsections'),

        APIField('subsection_title_one'),
        APIField('subsection_content_one'),
        APIField('subsection_info_one'),
        APIImageField('subsection_map_one'),

        APIField('subsection_title_two'),
        APIField('subsection_content_two'),
        APIField('subsection_info_two'),
        APIImageField('subsection_map_two'),

        APIField('subsection_title_three'),
        APIField('subsection_content_three'),
        APIField('subsection_info_three'),
        APIImageField('subsection_map_three'),

        APIField('subsection_title_four'),
        APIField('subsection_content_four'),
        APIField('subsection_info_four'),
        APIImageField('subsection_map_four'),

        APIField('subsection_title_five'),
        APIField('subsection_content_five'),
        APIField('subsection_info_five'),
        APIImageField('subsection_map_five'),

        APIField('subsection_title_six'),
        APIField('subsection_content_six'),
        APIField('subsection_info_six'),
        APIImageField('subsection_map_six'),

        APIField('subsection_title_seven'),
        APIField('subsection_content_seven'),
        APIField('subsection_info_seven'),
        APIImageField('subsection_map_seven'),

        fields.APIChildrenSectorPageListField('children_sectors'),
        APIMetaField('meta')
    ]


# Setup guide models

class SetupGuideLandingPage(ExclusivePageMixin, BasePage):
    view_app = constants.INVEST
    subpage_types = ['invest.SetupGuidePage']
    slug_identity = 'invest-setup-guide-landing-page'
    view_path = 'setup-guide-landing/'

    # page fields
    heading = models.CharField(max_length=255)
    sub_heading = models.CharField(max_length=255)
    lead_in = models.TextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('heading'),
        FieldPanel('sub_heading'),
        FieldPanel('lead_in'),
        SearchEngineOptimisationPanel()
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
        APIField('seo_title'),
        APIField('search_description'),
        APIField('heading'),
        APIField('sub_heading'),
        APIField('lead_in'),
        fields.APIChildrenSetupGuidePageListField('children_setup_guides'),
        APIMetaField('meta')
    ]


class SetupGuidePage(BasePage):
    view_app = constants.INVEST
    view_path = 'setup-guides/'

    description = models.TextField()  # appears in card on external pages

    heading = models.CharField(max_length=255)
    sub_heading = models.CharField(max_length=255)

    # subsections
    subsections = StreamField([
        ('subsection', StructBlock([
            ('title', CharBlock()),
            ('content', MarkdownBlock())
        ])),
    ], null=True, blank=True)

    subsection_title_one = models.CharField(max_length=255)
    subsection_content_one = MarkdownField()

    subsection_title_two = models.CharField(max_length=255)
    subsection_content_two = MarkdownField()

    subsection_title_three = models.CharField(max_length=255, blank=True)
    subsection_content_three = MarkdownField(blank=True)

    subsection_title_four = models.CharField(max_length=255, blank=True)
    subsection_content_four = MarkdownField(blank=True)

    subsection_title_five = models.CharField(max_length=255, blank=True)
    subsection_content_five = MarkdownField(blank=True)

    subsection_title_six = models.CharField(max_length=255, blank=True)
    subsection_content_six = MarkdownField(blank=True)

    subsection_title_seven = models.CharField(max_length=255, blank=True)
    subsection_content_seven = MarkdownField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('description'),
        FieldPanel('heading'),
        FieldPanel('sub_heading'),
        # subsections

        MultiFieldPanel(
            [
                FieldPanel('subsection_title_one'),
                FieldPanel('subsection_content_one'),
            ],
            heading='subsections one',
            classname='collapsible'
        ),

        MultiFieldPanel(
            [
                FieldPanel('subsection_title_two'),
                FieldPanel('subsection_content_two'),
            ],
            heading='subsections two',
            classname='collapsible'
        ),

        MultiFieldPanel(
            [
                FieldPanel('subsection_title_three'),
                FieldPanel('subsection_content_three'),
            ],
            heading='subsections three',
            classname='collapsible collapsed'
        ),

        MultiFieldPanel(
            [
                FieldPanel('subsection_title_four'),
                FieldPanel('subsection_content_four'),
            ],
            heading='subsections four',
            classname='collapsible collapsed'
        ),

        MultiFieldPanel(
            [
                FieldPanel('subsection_title_five'),
                FieldPanel('subsection_content_five'),
            ],
            heading='subsections five',
            classname='collapsible collapsed'
        ),

        MultiFieldPanel(
            [
                FieldPanel('subsection_title_six'),
                FieldPanel('subsection_content_six'),
            ],
            heading='subsections six',
            classname='collapsible collapsed'
        ),

        MultiFieldPanel(
            [
                FieldPanel('subsection_title_seven'),
                FieldPanel('subsection_content_seven'),
            ],
            heading='subsections seven',
            classname='collapsible collapsed'
        ),

        SearchEngineOptimisationPanel()
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
        APIField('seo_title'),
        APIField('search_description'),
        APIField('description'),
        APIField('heading'),
        APIField('sub_heading'),
        # subsections
        APIStreamFieldBlockField('subsections'),

        APIField('subsection_title_one'),
        APIField('subsection_content_one'),

        APIField('subsection_title_two'),
        APIField('subsection_content_two'),

        APIField('subsection_title_three'),
        APIField('subsection_content_three'),

        APIField('subsection_title_four'),
        APIField('subsection_content_four'),

        APIField('subsection_title_five'),
        APIField('subsection_content_five'),

        APIField('subsection_title_six'),
        APIField('subsection_content_six'),

        APIField('subsection_title_seven'),
        APIField('subsection_content_seven'),

        fields.APIChildrenSetupGuidePageListField('children_setup_guides'),
        APIMetaField('meta')
    ]


class InvestHomePage(ExclusivePageMixin, BasePage):
    view_app = constants.INVEST
    slug_identity = 'invest-home-page'
    view_path = ''

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

    # subsections
    subsection_title_one = models.CharField(max_length=255)
    subsection_content_one = MarkdownField()

    subsection_title_two = models.CharField(max_length=255)
    subsection_content_two = MarkdownField()

    subsection_title_three = models.CharField(max_length=255, blank=True)
    subsection_content_three = MarkdownField(blank=True)

    subsection_title_four = models.CharField(max_length=255, blank=True)
    subsection_content_four = MarkdownField(blank=True)

    subsection_title_five = models.CharField(max_length=255, blank=True)
    subsection_content_five = MarkdownField(blank=True)

    subsection_title_six = models.CharField(max_length=255, blank=True)
    subsection_content_six = MarkdownField(blank=True)

    subsection_title_seven = models.CharField(max_length=255, blank=True)
    subsection_content_seven = MarkdownField(blank=True)

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
        blank=True, null=True)

    # how we help
    how_we_help_text_one = models.CharField(max_length=255)
    how_we_help_icon_one = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    how_we_help_text_two = models.CharField(max_length=255)
    how_we_help_icon_two = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    how_we_help_text_three = models.CharField(max_length=255)
    how_we_help_icon_three = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    how_we_help_text_four = models.CharField(max_length=255)
    how_we_help_icon_four = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    how_we_help_text_five = models.CharField(max_length=255)
    how_we_help_icon_five = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    how_we_help_text_six = models.URLField()

    image_panels = [
        ImageChooserPanel('hero_image'),
    ]

    content_panels = Page.content_panels + [
        FieldPanel('heading'),
        FieldPanel('sub_heading'),
        # subsections
        MultiFieldPanel(
            [
                FieldPanel('subsection_title_one'),
                FieldPanel('subsection_content_one'),
            ],
            heading='subsections one',
            classname='collapsible'
        ),

        MultiFieldPanel(
            [
                FieldPanel('subsection_title_two'),
                FieldPanel('subsection_content_two'),
            ],
            heading='subsections two',
            classname='collapsible'
        ),

        MultiFieldPanel(
            [
                FieldPanel('subsection_title_three'),
                FieldPanel('subsection_content_three'),
            ],
            heading='subsections three',
            classname='collapsible collapsed'
        ),

        MultiFieldPanel(
            [
                FieldPanel('subsection_title_four'),
                FieldPanel('subsection_content_four'),
            ],
            heading='subsections four',
            classname='collapsible collapsed'
        ),

        MultiFieldPanel(
            [
                FieldPanel('subsection_title_five'),
                FieldPanel('subsection_content_five'),
            ],
            heading='subsections five',
            classname='collapsible collapsed'
        ),

        MultiFieldPanel(
            [
                FieldPanel('subsection_title_six'),
                FieldPanel('subsection_content_six'),
            ],
            heading='subsections six',
            classname='collapsible collapsed'
        ),

        MultiFieldPanel(
            [
                FieldPanel('subsection_title_seven'),
                FieldPanel('subsection_content_seven'),
            ],
            heading='subsections seven',
            classname='collapsible collapsed'
        ),

        FieldPanel('sector_title'),
        FieldPanel('sector_button_text'),
        FieldPanel('setup_guide_title'),
        FieldPanel('setup_guide_lead_in'),
        FieldPanel('how_we_help_title'),
        FieldPanel('how_we_help_lead_in'),
        MultiFieldPanel(
            [
                FieldPanel('how_we_help_text_one'),
                ImageChooserPanel('how_we_help_icon_one')
            ],
            heading='How we help one',
            classname='collapsible'
        ),
        MultiFieldPanel(
            [
                FieldPanel('how_we_help_text_two'),
                ImageChooserPanel('how_we_help_icon_two')
            ],
            heading='How we help two',
            classname='collapsible'
        ),
        MultiFieldPanel(
            [
                FieldPanel('how_we_help_text_three'),
                ImageChooserPanel('how_we_help_icon_three')
            ],
            heading='How we help three',
            classname='collapsible'
        ),
        MultiFieldPanel(
            [
                FieldPanel('how_we_help_text_four'),
                ImageChooserPanel('how_we_help_icon_four')
            ],
            heading='How we help four',
            classname='collapsible'
        ),
        MultiFieldPanel(
            [
                FieldPanel('how_we_help_text_five'),
                ImageChooserPanel('how_we_help_icon_five')
            ],
            heading='How we help five',
            classname='collapsible'
        ),
        MultiFieldPanel(
            [
                FieldPanel('how_we_help_text_six'),
            ],
            heading='How we help six',
            classname='collapsible'
        ),
        SearchEngineOptimisationPanel()
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
        APIField('seo_title'),
        APIField('search_description'),
        APIField('heading'),
        APIField('sub_heading'),
        APIImageField('hero_image'),
        # subsections
        APIStreamFieldBlockField('subsections'),
        APIField('subsection_title_one'),
        APIField('subsection_content_one'),

        APIField('subsection_title_two'),
        APIField('subsection_content_two'),

        APIField('subsection_title_three'),
        APIField('subsection_content_three'),

        APIField('subsection_title_four'),
        APIField('subsection_content_four'),

        APIField('subsection_title_five'),
        APIField('subsection_content_five'),

        APIField('subsection_title_six'),
        APIField('subsection_content_six'),

        APIField('subsection_title_seven'),
        APIField('subsection_content_seven'),

        APIField('sector_title'),
        APIField('sector_button_text'),
        APIField('setup_guide_title'),
        APIField('setup_guide_lead_in'),
        APIField('how_we_help_title'),
        APIField('how_we_help_lead_in'),
        # how we help
        APIStreamFieldBlockField('how_we_help'),
        APIField('how_we_help_text_one'),
        APIImageField('how_we_help_icon_one'),

        APIField('how_we_help_text_two'),
        APIImageField('how_we_help_icon_two'),

        APIField('how_we_help_text_three'),
        APIImageField('how_we_help_icon_three'),

        APIField('how_we_help_text_four'),
        APIImageField('how_we_help_icon_four'),

        APIField('how_we_help_text_five'),
        APIImageField('how_we_help_icon_five'),

        APIField('how_we_help_text_six'),

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
    view_path = 'info/'
    content = MarkdownField()

    content_panels = Page.content_panels + [
        FieldPanel('content'),
        SearchEngineOptimisationPanel()
    ]

    settings_panels = [
        FieldPanel('title_en_gb'),
        FieldPanel('slug_en_gb')
    ]

    edit_handler = make_translated_interface(
        content_panels=content_panels,
        settings_panels=settings_panels,
    )

    api_fields = [
        APIField('seo_title'),
        APIField('search_description'),
        APIMarkdownToHTMLField('content'),
        APIMetaField('meta')
    ]
