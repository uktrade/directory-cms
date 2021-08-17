from wagtail.admin.edit_handlers import (
    FieldPanel,
    FieldRowPanel,
    HelpPanel,
    InlinePanel,
    MultiFieldPanel,
    StreamFieldPanel,
)

from core.helpers import make_translated_interface
from core.panels import SearchEngineOptimisationPanel


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
            heading='The Oppportunity',
            classname='collapsible',
            children=[
                StreamFieldPanel('featured_images'),
                StreamFieldPanel('main_content'),
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
