from directory_constants.constants import cms
from wagtail.admin.edit_handlers import (
    FieldPanel, ObjectList, MultiFieldPanel, FieldRowPanel
)
from wagtail.documents.edit_handlers import DocumentChooserPanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtailmedia.widgets import AdminMediaChooser

from django.db import models

from core.helpers import make_translated_interface
from core.model_fields import MarkdownField
from core.models import (
    BasePage, ExclusivePageMixin, ServiceMixin, FormPageMetaClass
)
from core.panels import SearchEngineOptimisationPanel


class InvestApp(ExclusivePageMixin, ServiceMixin, BasePage):
    service_name_value = cms.INVEST
    slug_identity = 'invest-app'

    @classmethod
    def get_required_translatable_fields(cls):
        return []


# Sector models

class SectorLandingPage(ExclusivePageMixin, BasePage):
    service_name_value = cms.INVEST
    subpage_types = ['invest.sectorPage']
    slug_identity = cms.INVEST_SECTOR_LANDING_PAGE_SLUG
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
    content_panels = [
        FieldPanel('heading'),
        SearchEngineOptimisationPanel()

    ]
    settings_panels = [
        FieldPanel('title_en_gb'),
        FieldPanel('slug'),
    ]

    edit_handler = make_translated_interface(
        content_panels=content_panels,
        settings_panels=settings_panels,
        other_panels=[
            ObjectList(image_panels, heading='Images'),
        ]
    )


class RegionLandingPage(ExclusivePageMixin, BasePage):
    service_name_value = cms.INVEST
    subpage_types = ['invest.sectorPage']
    slug_identity = cms.INVEST_UK_REGION_LANDING_PAGE_SLUG
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
    content_panels = [
        FieldPanel('heading'),
        SearchEngineOptimisationPanel()
    ]
    settings_panels = [
        FieldPanel('title_en_gb'),
        FieldPanel('slug'),
    ]

    edit_handler = make_translated_interface(
        content_panels=content_panels,
        settings_panels=settings_panels,
        other_panels=[
            ObjectList(image_panels, heading='Images'),
        ]
    )


class SectorPage(BasePage):
    # Related sector are implemented as subpages
    service_name_value = cms.INVEST
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

    pullout_text = MarkdownField(blank=True, null=True)
    pullout_stat = models.CharField(max_length=255, blank=True, null=True)
    pullout_stat_text = models.CharField(max_length=255, blank=True, null=True)

    subsection_title_one = models.CharField(max_length=200)
    subsection_content_one = MarkdownField()
    subsection_map_one = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    subsection_title_two = models.CharField(max_length=200)
    subsection_content_two = MarkdownField()
    subsection_map_two = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    subsection_title_three = models.CharField(max_length=200, blank=True)
    subsection_content_three = MarkdownField(blank=True)
    subsection_map_three = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    subsection_title_four = models.CharField(max_length=200, blank=True)
    subsection_content_four = MarkdownField(blank=True)
    subsection_map_four = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    subsection_title_five = models.CharField(max_length=200, blank=True)
    subsection_content_five = MarkdownField(blank=True)
    subsection_map_five = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    subsection_title_six = models.CharField(max_length=200, blank=True)
    subsection_content_six = MarkdownField(blank=True)
    subsection_map_six = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    subsection_title_seven = models.CharField(max_length=200, blank=True)
    subsection_content_seven = MarkdownField(blank=True)
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
    content_panels = [
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
                ImageChooserPanel('subsection_map_one')
            ],
            heading='subsections one',
            classname='collapsible'
        ),
        MultiFieldPanel(
            [
                FieldPanel('subsection_title_two'),
                FieldPanel('subsection_content_two'),
                ImageChooserPanel('subsection_map_two')
            ],
            heading='subsections two',
            classname='collapsible'
        ),
        MultiFieldPanel(
            [
                FieldPanel('subsection_title_three'),
                FieldPanel('subsection_content_three'),
                ImageChooserPanel('subsection_map_three')
            ],
            heading='subsections three',
            classname='collapsible collapsed'
        ),
        MultiFieldPanel(
            [
                FieldPanel('subsection_title_four'),
                FieldPanel('subsection_content_four'),
                ImageChooserPanel('subsection_map_four')
            ],
            heading='subsections four',
            classname='collapsible collapsed'
        ),
        MultiFieldPanel(
            [
                FieldPanel('subsection_title_five'),
                FieldPanel('subsection_content_five'),
                ImageChooserPanel('subsection_map_five')
            ],
            heading='subsections five',
            classname='collapsible collapsed'
        ),
        MultiFieldPanel(
            [
                FieldPanel('subsection_title_six'),
                FieldPanel('subsection_content_six'),
                ImageChooserPanel('subsection_map_six')
            ],
            heading='subsections six',
            classname='collapsible collapsed'
        ),
        MultiFieldPanel(
            [
                FieldPanel('subsection_title_seven'),
                FieldPanel('subsection_content_seven'),
                ImageChooserPanel('subsection_map_seven')
            ],
            heading='Subsection seven',
            classname='collapsible collapsed'
        ),
        SearchEngineOptimisationPanel()
    ]
    settings_panels = [
        FieldPanel('title_en_gb'),
        FieldPanel('slug'),
        FieldPanel('featured')
    ]

    edit_handler = make_translated_interface(
        content_panels=content_panels,
        settings_panels=settings_panels,
        other_panels=[
            ObjectList(image_panels, heading='Images'),
        ]
    )


# Setup guide models

class SetupGuideLandingPage(ExclusivePageMixin, BasePage):
    service_name_value = cms.INVEST
    subpage_types = ['invest.SetupGuidePage']
    slug_identity = cms.INVEST_GUIDE_LANDING_PAGE_SLUG
    view_path = 'setup-guide-landing/'

    # page fields
    heading = models.CharField(max_length=255)
    sub_heading = models.CharField(max_length=255)
    lead_in = models.TextField(blank=True)

    content_panels = [
        FieldPanel('heading'),
        FieldPanel('sub_heading'),
        FieldPanel('lead_in'),
        SearchEngineOptimisationPanel()
    ]

    settings_panels = [
        FieldPanel('title_en_gb'),
        FieldPanel('slug'),
    ]

    edit_handler = make_translated_interface(
        content_panels=content_panels,
        settings_panels=settings_panels,
    )


class SetupGuidePage(BasePage):
    service_name_value = cms.INVEST
    view_path = 'setup-guides/'

    description = models.TextField()  # appears in card on external pages

    heading = models.CharField(max_length=255)
    sub_heading = models.CharField(max_length=255)

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

    content_panels = [
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
        FieldPanel('slug'),
    ]

    edit_handler = make_translated_interface(
        content_panels=content_panels,
        settings_panels=settings_panels,
    )


class InvestHomePage(ExclusivePageMixin, BasePage):
    service_name_value = cms.INVEST
    slug_identity = cms.INVEST_HOME_PAGE_SLUG
    view_path = '/'

    breadcrumbs_label = models.CharField(max_length=50)
    heading = models.CharField(max_length=255)
    sub_heading = models.CharField(max_length=255)
    hero_call_to_action_text = models.CharField(max_length=255, blank=True)
    hero_image = models.ForeignKey(
        'wagtailimages.Image',
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    benefits_section_title = models.CharField(max_length=255)
    benefits_section_intro = models.TextField(max_length=255, blank=True)
    benefits_section_content = MarkdownField(blank=True)
    benefits_section_img = models.ForeignKey(
        'wagtailimages.Image',
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name='+',
        verbose_name="Benefits section image"
    )
    benefits_section_img_caption = models.CharField(
        max_length=255,
        blank=True,
        verbose_name="Benefits section image caption"
    )

    eu_exit_section_title = models.CharField(
        max_length=255,
        blank=True,
        verbose_name="EU exit section title"
    )

    eu_exit_section_content = MarkdownField(
        blank=True,
        verbose_name="EU exit section content"
    )

    eu_exit_section_call_to_action_text = models.CharField(
        max_length=255,
        blank=True,
        verbose_name="EU exit section button text"
    )

    eu_exit_section_img = models.ForeignKey(
        'wagtailimages.Image',
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name='+',
        verbose_name="EU exit section image"
    )
    eu_exit_section_img_caption = models.CharField(
        max_length=255,
        blank=True,
        verbose_name="EU Exit section image caption"
    )

    # subsections
    subsection_title_one = models.CharField(max_length=255, blank=True)
    subsection_content_one = MarkdownField(blank=True)

    subsection_title_two = models.CharField(max_length=255, blank=True)
    subsection_content_two = MarkdownField(blank=True)

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

    sector_intro = models.TextField(max_length=255, blank=True)

    hpo_title = models.CharField(
        max_length=255,
        verbose_name="High potential opportunity section title"
    )
    hpo_intro = models.TextField(
        max_length=255,
        blank=True,
        verbose_name="High potential opportunity section intro"
    )

    setup_guide_title = models.CharField(
        default='Set up an overseas business in the UK',
        max_length=255)

    setup_guide_lead_in = models.TextField(
        blank=True,
        null=True)

    setup_guide_content = MarkdownField(blank=True)
    setup_guide_img = models.ForeignKey(
        'wagtailimages.Image',
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name='+',
        verbose_name="Setup guide image"
    )

    setup_guide_img_caption = models.CharField(
        max_length=255,
        blank=True,
        verbose_name="Setup guide image caption"
    )

    setup_guide_call_to_action_text = models.CharField(max_length=255)

    how_we_help_title = models.CharField(default='How we help', max_length=255)
    how_we_help_lead_in = models.TextField(blank=True, null=True)
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
    how_we_help_text_six = models.CharField(max_length=255, blank=True)

    contact_section_title = models.CharField(max_length=255)
    contact_section_content = models.TextField(max_length=255, blank=True)
    contact_section_call_to_action_text = models.CharField(max_length=255)

    image_panels = [
        ImageChooserPanel('hero_image'),
    ]

    content_panels = [
        MultiFieldPanel(
            [
                FieldPanel('breadcrumbs_label'),
                FieldPanel('heading'),
                FieldPanel('sub_heading'),
                FieldPanel('hero_call_to_action_text'),
            ],
            heading='Hero',
            classname='collapsible'
        ),

        MultiFieldPanel(
            [
                FieldPanel('benefits_section_title'),
                FieldPanel('benefits_section_intro'),
                FieldPanel('benefits_section_content'),
                ImageChooserPanel('benefits_section_img'),
                FieldPanel('benefits_section_img_caption'),
            ],
            heading='Benefits section',
            classname='collapsible'
        ),

        MultiFieldPanel(
            [
                FieldPanel('eu_exit_section_title'),
                FieldPanel('eu_exit_section_content'),
                FieldPanel('eu_exit_section_call_to_action_text'),
                ImageChooserPanel('eu_exit_section_img'),
                FieldPanel('eu_exit_section_img_caption'),
            ],
            heading='EU Exit section',
            classname='collapsible'
        ),

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

        MultiFieldPanel(
            [
                FieldPanel('sector_title'),
                FieldPanel('sector_intro'),
                FieldPanel('sector_button_text'),
            ],
            heading='Industries section'
        ),

        MultiFieldPanel(
            [
                FieldPanel('hpo_title'),
                FieldPanel('hpo_intro')
            ],
            heading='High Potential Opportunities'
        ),

        MultiFieldPanel([
            FieldPanel('setup_guide_title'),
            FieldPanel('setup_guide_content'),
            ImageChooserPanel('setup_guide_img'),
            FieldPanel('setup_guide_img_caption'),
            FieldPanel('setup_guide_call_to_action_text')
            ],
            heading='Set up guide section',
            classname='collapsible'
        ),

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

        MultiFieldPanel(
            [
                FieldPanel('contact_section_title'),
                FieldPanel('contact_section_content'),
                FieldPanel('contact_section_call_to_action_text'),
            ],
            heading='Contact Section',
            classname='collapsible'
        ),
        SearchEngineOptimisationPanel()
    ]

    settings_panels = [
        FieldPanel('title_en_gb'),
        FieldPanel('slug'),
    ]

    edit_handler = make_translated_interface(
        content_panels=content_panels,
        settings_panels=settings_panels,
        other_panels=[
            ObjectList(image_panels, heading='Images'),
        ]
    )


class InfoPage(BasePage):
    """
    Markdown page - used for terms and conditions
    and privacy policy
    """
    service_name_value = cms.INVEST
    view_path = 'info/'
    content = MarkdownField()

    content_panels = [
        FieldPanel('content'),
        SearchEngineOptimisationPanel()
    ]

    settings_panels = [
        FieldPanel('title_en_gb'),
        FieldPanel('slug')
    ]

    edit_handler = make_translated_interface(
        content_panels=content_panels,
        settings_panels=settings_panels,
    )


class HighPotentialOpportunityFormPage(
    ExclusivePageMixin, BasePage, metaclass=FormPageMetaClass
):
    # metaclass creates <fild_name>_label and <field_name>_help_text
    form_field_names = [
        'full_name',
        'role_in_company',
        'email_address',
        'phone_number',
        'company_name',
        'website_url',
        'country',
        'company_size',
        'opportunities',
        'comment',
    ]

    service_name_value = cms.INVEST
    view_path = 'high-potential-opportunities/rail/contact/'
    slug_identity = cms.INVEST_HIGH_POTENTIAL_OPPORTUNITY_FORM_SLUG

    heading = models.CharField(max_length=255)
    sub_heading = models.CharField(max_length=255)
    breadcrumbs_label = models.CharField(max_length=50)

    content_panels_before_form = [
        MultiFieldPanel(
            heading='Hero',
            children=[
                FieldPanel('breadcrumbs_label'),
                FieldPanel('heading'),
                FieldPanel('sub_heading'),
            ]
        ),
    ]
    content_panels_after_form = [SearchEngineOptimisationPanel()]

    settings_panels = [
        FieldPanel('title_en_gb'),
        FieldPanel('slug'),
    ]


class HighPotentialOpportunityDetailPage(BasePage):
    service_name_value = cms.INVEST
    subpage_types = ['invest.HighPotentialOpportunityDetailPage']
    view_path = 'high-potential-opportunities/'

    breadcrumbs_label = models.CharField(max_length=50)
    heading = models.CharField(max_length=255)
    hero_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    featured = models.BooleanField(default=True)
    description = models.TextField(blank=True)

    contact_proposition = MarkdownField(
        blank=False,
        verbose_name='Body text',
    )
    contact_button = models.CharField(max_length=500)
    proposition_one = MarkdownField(blank=False)
    proposition_one_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    proposition_one_video = models.ForeignKey(
        'wagtailmedia.Media',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    opportunity_list_title = models.CharField(max_length=300)
    opportunity_list_item_one = MarkdownField()
    opportunity_list_item_two = MarkdownField()
    opportunity_list_item_three = MarkdownField(blank=True)
    opportunity_list_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    proposition_two = MarkdownField(blank=False)
    proposition_two_list_item_one = MarkdownField()
    proposition_two_list_item_two = MarkdownField()
    proposition_two_list_item_three = MarkdownField()
    proposition_two_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    proposition_two_video = models.ForeignKey(
        'wagtailmedia.Media',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    competitive_advantages_title = models.CharField(
        max_length=300,
        verbose_name='Body text',
    )
    competitive_advantages_list_item_one = MarkdownField()
    competitive_advantages_list_item_one_icon = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    competitive_advantages_list_item_two = MarkdownField()
    competitive_advantages_list_item_two_icon = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    competitive_advantages_list_item_three = MarkdownField()
    competitive_advantages_list_item_three_icon = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    testimonial = MarkdownField(blank=True)
    testimonial_background = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        verbose_name='Background image',
    )
    companies_list_text = MarkdownField()
    companies_list_item_image_one = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    companies_list_item_image_two = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    companies_list_item_image_three = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    companies_list_item_image_four = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    companies_list_item_image_five = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    companies_list_item_image_six = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    companies_list_item_image_seven = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    companies_list_item_image_eight = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    case_study_list_title = models.CharField(max_length=300)
    case_study_one_text = MarkdownField(blank=True)
    case_study_one_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    case_study_two_text = MarkdownField(blank=True)
    case_study_two_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    case_study_three_text = MarkdownField(blank=True)
    case_study_three_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    case_study_four_text = MarkdownField(blank=True)
    case_study_four_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    other_opportunities_title = models.CharField(
        max_length=300,
        verbose_name='Title'
    )
    pdf_document = models.ForeignKey(
        'wagtaildocs.Document',
        null=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    summary_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text=(
            'Image used on the opportunity listing page for this opportunity'
        ),
        verbose_name='Image',
    )

    content_panels = [
        MultiFieldPanel(
            heading='Hero',
            children=[
                FieldPanel('breadcrumbs_label'),
                FieldPanel('heading'),
                ImageChooserPanel('hero_image'),
            ]
        ),

        MultiFieldPanel(
            heading='Featured Description',
            children=[
                FieldPanel('description')
            ]
        ),

        MultiFieldPanel(
            heading='Contact us',
            children=[
                FieldRowPanel(
                    children=[
                        FieldPanel('contact_proposition'),
                        FieldPanel('contact_button'),
                    ]
                )
            ]
        ),
        MultiFieldPanel(
            heading='Proposition one',
            children=[
                FieldRowPanel(
                    children=[
                        FieldPanel('proposition_one'),
                        MultiFieldPanel(
                            children=[
                                ImageChooserPanel('proposition_one_image'),
                                FieldPanel(
                                    'proposition_one_video',
                                    widget=AdminMediaChooser
                                ),
                            ]
                        )
                    ]
                )

            ]
        ),
        MultiFieldPanel(
            heading='Opportunity list',
            children=[
                FieldPanel('opportunity_list_title'),
                FieldRowPanel(
                    children=[
                        MultiFieldPanel(
                            children=[
                                FieldPanel('opportunity_list_item_one'),
                                FieldPanel('opportunity_list_item_two'),
                                FieldPanel('opportunity_list_item_three'),
                            ]
                        ),
                        ImageChooserPanel('opportunity_list_image'),
                    ]
                )
            ]
        ),
        MultiFieldPanel(
            heading='Opportunity list',
            children=[
                FieldRowPanel(
                    children=[
                        MultiFieldPanel(
                            children=[
                                FieldPanel('proposition_two'),
                                FieldPanel('proposition_two_list_item_one'),
                                FieldPanel('proposition_two_list_item_two'),
                                FieldPanel('proposition_two_list_item_three'),
                            ]
                        ),
                        MultiFieldPanel(
                            children=[
                                ImageChooserPanel('proposition_two_image'),
                                FieldPanel(
                                    'proposition_two_video',
                                    widget=AdminMediaChooser
                                ),
                            ]
                        )
                    ]
                )
            ]
        ),
        MultiFieldPanel(
            heading='Key facts',
            children=[
                FieldPanel('competitive_advantages_title'),
                FieldRowPanel(
                    children=[
                        FieldPanel('competitive_advantages_list_item_one'),
                        FieldPanel('competitive_advantages_list_item_two'),
                        FieldPanel('competitive_advantages_list_item_three'),
                    ]
                ),
                FieldRowPanel(
                    children=[
                        ImageChooserPanel(
                            'competitive_advantages_list_item_one_icon'
                        ),
                        ImageChooserPanel(
                            'competitive_advantages_list_item_two_icon'
                        ),
                        ImageChooserPanel(
                            'competitive_advantages_list_item_three_icon'
                        ),
                    ]
                )
            ]
        ),
        MultiFieldPanel(
            heading='Testimonial',
            children=[
                FieldPanel('testimonial'),
                ImageChooserPanel('testimonial_background'),
            ]
        ),
        MultiFieldPanel(
            heading='Company list',
            children=[
                FieldPanel('companies_list_text'),
                FieldRowPanel(
                    children=[
                        ImageChooserPanel('companies_list_item_image_one'),
                        ImageChooserPanel('companies_list_item_image_two'),
                        ImageChooserPanel('companies_list_item_image_three'),
                        ImageChooserPanel('companies_list_item_image_four'),
                    ]
                ),
                FieldRowPanel(
                    children=[
                        ImageChooserPanel('companies_list_item_image_five'),
                        ImageChooserPanel('companies_list_item_image_six'),
                        ImageChooserPanel('companies_list_item_image_seven'),
                        ImageChooserPanel('companies_list_item_image_eight'),
                    ]
                )
            ]
        ),
        MultiFieldPanel(
            heading='Case studies',
            children=[
                FieldPanel('case_study_list_title'),
                FieldRowPanel(
                    children=[
                        FieldPanel('case_study_one_text'),
                        ImageChooserPanel('case_study_one_image'),
                    ]
                ),
                FieldRowPanel(
                    children=[
                        FieldPanel('case_study_two_text'),
                        ImageChooserPanel('case_study_two_image'),
                    ]
                ),
                FieldRowPanel(
                    children=[
                        FieldPanel('case_study_three_text'),
                        ImageChooserPanel('case_study_three_image'),
                    ]
                ),
                FieldRowPanel(
                    children=[
                        FieldPanel('case_study_four_text'),
                        ImageChooserPanel('case_study_four_image'),
                    ]
                )
            ]
        ),
        MultiFieldPanel(
            heading='Other opportunities',
            children=[
                FieldPanel('other_opportunities_title'),
            ]
        ),
        MultiFieldPanel(
            heading='Summary',
            children=[
                ImageChooserPanel('summary_image')
            ],
        ),
        SearchEngineOptimisationPanel(),
    ]
    settings_panels = [
        FieldPanel('title_en_gb'),
        FieldPanel('slug'),
        FieldPanel('featured'),
        DocumentChooserPanel('pdf_document'),
    ]


class HighPotentialOpportunityFormSuccessPage(BasePage):
    service_name_value = cms.INVEST
    view_path = 'high-potential-opportunities/rail/contact/'
    slug_identity = cms.INVEST_HIGH_POTENTIAL_OPPORTUNITY_FORM_SUCCESS_SLUG

    breadcrumbs_label = models.CharField(max_length=50)
    heading = models.CharField(
        max_length=255,
        verbose_name='section title'
    )
    sub_heading = models.CharField(
        max_length=255,
        verbose_name='section body',
    )
    next_steps_title = models.CharField(
        max_length=255,
        verbose_name='section title'
    )
    next_steps_body = models.CharField(
        max_length=255,
        verbose_name='section body',

    )
    documents_title = models.CharField(
        max_length=255,
        verbose_name='section title'
    )
    documents_body = models.CharField(
        max_length=255,
        verbose_name='section body',
    )

    content_panels = [
        FieldPanel('breadcrumbs_label'),
        MultiFieldPanel(
            heading='heading',
            children=[
                FieldPanel('heading'),
                FieldPanel('sub_heading'),
            ]
        ),
        MultiFieldPanel(
            heading='Next steps',
            children=[
                FieldPanel('next_steps_title'),
                FieldPanel('next_steps_body'),
            ]
        ),
        MultiFieldPanel(
            heading='Documents',
            children=[
                FieldPanel('documents_title'),
                FieldPanel('documents_body'),
            ]
        ),
        SearchEngineOptimisationPanel(),
    ]

    settings_panels = [
        FieldPanel('title_en_gb'),
        FieldPanel('slug'),
    ]
