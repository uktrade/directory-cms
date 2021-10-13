from wagtail.admin.edit_handlers import (
    FieldPanel,
    FieldRowPanel,
    HelpPanel,
    InlinePanel,
    MultiFieldPanel,
    StreamFieldPanel,
)

from wagtail.images.edit_handlers import ImageChooserPanel
from wagtailmedia.edit_handlers import MediaChooserPanel

from core.helpers import make_translated_interface
from core.panels import SearchEngineOptimisationPanel


class InvestmentAtlasLandingPagePanels:

    content_panels = [
        MultiFieldPanel(
            heading="Title and breadcrumbs",
            classname='collapsible',
            children=[
                FieldPanel('title'),
                FieldPanel('breadcrumbs_label'),
            ]
        ),
        MultiFieldPanel(
            heading='Hero',
            classname='collapsible',
            children=[
                ImageChooserPanel('hero_image'),
                MediaChooserPanel('hero_video'),
                ImageChooserPanel('mobile_hero_image'),
                FieldPanel('hero_title'),
                FieldPanel('hero_strapline'),
            ]
        ),
        MultiFieldPanel(
            heading='Downpage content panels',
            classname='collapsible',
            children=[
                StreamFieldPanel('downpage_sections'),
            ],
        ),
        SearchEngineOptimisationPanel(),
    ]

    settings_panels = [
        FieldPanel('slug'),
    ]

    edit_handler = make_translated_interface(
        content_panels=content_panels,
        settings_panels=settings_panels,
    )


class InvestmentOpportunityListingPagePanels:

    content_panels = [
        MultiFieldPanel(
            heading='Opportunity Listing Page Title',
            children=[
                FieldPanel('title'),
                FieldPanel('search_results_title'),
                FieldPanel('breadcrumbs_label'),
            ],
        ),
        MultiFieldPanel(
            heading='Hero content',
            children=[
                MediaChooserPanel('hero_video'),
                FieldPanel('hero_text'),
            ],
        ),
        MultiFieldPanel(
            heading='CTA content',
            children=[
                FieldPanel('contact_cta_title'),
                FieldPanel('contact_cta_text'),
                FieldPanel('contact_cta_link'),
            ],
        ),
        SearchEngineOptimisationPanel(),
    ]
    settings_panels = [
        FieldPanel('slug'),
    ]

    edit_handler = make_translated_interface(
        content_panels=content_panels,
        settings_panels=settings_panels,
    )


class InvestmentOpportunityPagePanels:

    content_panels = [
        MultiFieldPanel(
            heading='Opportunity Page title, intro and summary',
            classname='collapsible',
            children=[
                FieldPanel('title'),
                FieldPanel('breadcrumbs_label'),
                ImageChooserPanel('hero_image'),
                MediaChooserPanel('hero_video'),
                FieldPanel('strapline'),
                FieldPanel('introduction'),
                ImageChooserPanel('intro_image'),
                FieldPanel('opportunity_summary'),
            ],
        ),
        MultiFieldPanel(
            heading="Key facts",
            classname='collapsible',
            children=[
                FieldRowPanel([
                    FieldPanel('promoter'),
                    FieldPanel('location'),
                    MultiFieldPanel(
                        heading='Scale',
                        children=[
                            FieldPanel('scale'),
                            FieldPanel('scale_value'),
                        ]
                    ),
                ]),
                FieldRowPanel([
                    FieldPanel('planning_status'),
                    FieldPanel('investment_type'),
                    FieldPanel('time_to_investment_decision'),
                ]),
                HelpPanel('In addition to these, please also set a location in the Location tab'),
            ],
        ),
        MultiFieldPanel(
            heading='Opportunity Contact',
            classname='collapsible',
            children=[
                FieldPanel('contact_name'),
                ImageChooserPanel('contact_avatar'),
                FieldPanel('contact_job_title'),
                FieldPanel('contact_link'),
            ],
        ),
        MultiFieldPanel(
            heading='The Opportunity',
            classname='collapsible',
            children=[
                StreamFieldPanel('main_content'),
                FieldPanel('important_links'),
            ],
        ),
        SearchEngineOptimisationPanel(),
    ]

    related_entities_panels = [
        FieldRowPanel(
            heading='Location and Relevant Regions',
            classname='collapsible',
            children=[
                StreamFieldPanel('regions_with_locations'),
            ]
        ),
        FieldRowPanel(
            heading="Sectors and Sub-sectors",
            classname='collapsible collapsed',
            children=[
                InlinePanel('related_sectors', label="Related Sectors"),
                InlinePanel('related_sub_sectors', label="Related Sub-sectors")
            ],
        ),
    ]

    settings_panels = [
        FieldPanel('slug'),
        FieldPanel('priority_weighting'),
    ]

    edit_handler = make_translated_interface(
        content_panels=content_panels,
        other_panels=related_entities_panels,  # These are shown as separate tabs
        settings_panels=settings_panels,
    )


class InvestmentGeneralContentPagePanels:
    content_panels = [
        MultiFieldPanel(
            heading="Hero and Intro",
            classname='collapsible',
            children=[
                FieldPanel('title'),
                ImageChooserPanel('hero_image'),
                FieldPanel('strapline'),
                FieldPanel('introduction'),
                ImageChooserPanel('intro_image'),
            ],
        ),
        StreamFieldPanel('main_content'),
        SearchEngineOptimisationPanel(),
    ]
    settings_panels = [
        FieldPanel('slug'),
    ]

    edit_handler = make_translated_interface(
        content_panels=content_panels,
        settings_panels=settings_panels
    )


class ForeignDirectInvestmentFormPagePanels:

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


class ForeignDirectInvestmentFormSuccessPagePanels:

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
