from wagtail.admin.edit_handlers import (
    FieldPanel,
    FieldRowPanel,
    MultiFieldPanel,
    ObjectList,
    HelpPanel,
    PageChooserPanel,
    TabbedInterface,
)
from wagtail.documents.edit_handlers import DocumentChooserPanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtailmedia.widgets import AdminMediaChooser

from core.helpers import make_translated_interface
from core.panels import SearchEngineOptimisationPanel


class InvestmentOpportunityPagePanels:

    content_panels = [
        MultiFieldPanel(
            heading='Opportunity Page Title',
            children=[
                FieldPanel('title'),
                FieldPanel('breadcrumbs_label'),
            ]
        ),
        MultiFieldPanel(
            heading='Featured images',
            classname='collapsible',
            children=[
                MultiFieldPanel(
                    heading='First featured image',
                    children=[
                        ImageChooserPanel('featured_image_1'),
                        FieldPanel('featured_image_1_alt'),
                        FieldPanel('featured_image_1_caption'),
                    ]
                ),
                MultiFieldPanel(
                    heading='Second featured image',
                    children=[
                        ImageChooserPanel('featured_image_2'),
                        FieldPanel('featured_image_2_alt'),
                        FieldPanel('featured_image_2_caption'),
                    ]
                ),
                MultiFieldPanel(
                    heading='Third featured image',
                    children=[
                        ImageChooserPanel('featured_image_3'),
                        FieldPanel('featured_image_3_alt'),
                        FieldPanel('featured_image_3_caption'),
                    ]
                ),
                MultiFieldPanel(
                    heading='Fourth featured image',
                    children=[
                        ImageChooserPanel('featured_image_4'),
                        FieldPanel('featured_image_4_alt'),
                        FieldPanel('featured_image_4_caption'),
                    ]
                ),
                MultiFieldPanel(
                    heading='Fifth featured image',
                    children=[
                        ImageChooserPanel('featured_image_5'),
                        FieldPanel('featured_image_5_alt'),
                        FieldPanel('featured_image_5_caption'),
                    ]
                ),
            ],
        ),
        MultiFieldPanel(
            heading='Main content',
            classname='collapsible',
            children=[
                FieldPanel('executive_summary'),
                FieldPanel('data_snapshot'),
                MultiFieldPanel(
                    heading='Contact details',
                    children=[
                        ImageChooserPanel('contact_image'),
                        FieldPanel('contact_name'),
                        FieldPanel('contact_job_title'),
                        FieldPanel('contact_cta_email'),
                    ]
                ),
                FieldPanel('opportunity_details'),
                FieldPanel('location_details'),
                FieldPanel('financial_details'),
                FieldPanel('local_or_national_support'),
            ]
        ),
        MultiFieldPanel(
            heading='Related items',
            classname='collapsible',
            children=[
                FieldPanel('relevant_regions'),
                FieldPanel('relevant_sectors'),
                FieldPanel('related_opportunities'),
            ]
        ),
        SearchEngineOptimisationPanel()
    ]

    settings_panels = [
        FieldPanel('slug'),
    ]

    edit_handler = TabbedInterface([
        ObjectList(content_panels, heading='Content'),
        ObjectList(settings_panels, heading='Settings', classname='settings'),
    ])

    # edit_handler = make_translated_interface(
    #     content_panels=content_panels,
    #     settings_panels=settings_panels,
    # )
