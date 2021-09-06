from wagtail.admin.edit_handlers import (
    FieldPanel,
    FieldRowPanel,
    HelpPanel,
    InlinePanel,
    MultiFieldPanel,
    StreamFieldPanel,
)

from wagtail.images.edit_handlers import ImageChooserPanel

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
        FieldPanel('hero_text'),
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
                FieldPanel('strapline'),
                FieldPanel('introduction'),
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
            heading='The Oppportunity',
            classname='collapsible',
            children=[
                StreamFieldPanel('featured_images'),
                StreamFieldPanel('main_content'),
                FieldPanel('important_links'),
            ],
        ),
        SearchEngineOptimisationPanel(),
    ]

    related_entities_panels = [
        FieldRowPanel(
            heading='Location and Relevant Regions',
            children=[
                FieldPanel('location_coords'),
                FieldPanel('related_regions'),
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
