from wagtail.admin.edit_handlers import (
    FieldPanel,
    MultiFieldPanel,
    StreamFieldPanel,
)

from core.helpers import make_translated_interface
from core.panels import SearchEngineOptimisationPanel


class InvestmentOpportunityPagePanels:

    content_panels = [
        MultiFieldPanel(
            heading='Opportunity Page Title',
            children=[
                FieldPanel('title'),
                FieldPanel('breadcrumbs_label'),
            ],
        ),
        MultiFieldPanel(
            heading='Main content',
            children=[
                FieldPanel('opportunity_summary'),
                StreamFieldPanel('featured_images'),
                StreamFieldPanel('main_content'),
            ],
        ),
        SearchEngineOptimisationPanel(),
    ]

    related_entities_panels = [
        MultiFieldPanel(
            heading='Related items',
            classname='collapsible',
            children=[
                FieldPanel('relevant_regions'),
                FieldPanel('relevant_sectors'),
                FieldPanel('related_opportunities'),
            ],
        ),
    ]

    settings_panels = [
        FieldPanel('slug'),
        FieldPanel('priority_weighting'),
    ]

    edit_handler = make_translated_interface(
        content_panels=content_panels,
        other_panels=related_entities_panels,
        settings_panels=settings_panels,
    )
