from wagtail.admin.edit_handlers import (
    HelpPanel, FieldPanel, FieldRowPanel, MultiFieldPanel,
)
from wagtail.images.edit_handlers import ImageChooserPanel

from core.helpers import make_translated_interface
from core.panels import SearchEngineOptimisationPanel


class CapitalInvestRegionPagePanels:

    content_panels = [
        FieldPanel('title'),
        FieldPanel('breadcrumbs_label'),
        MultiFieldPanel(
            heading="Hero",
            children=[
                FieldPanel('hero_title'),
                ImageChooserPanel('hero_image'),
            ],
        ),
        FieldPanel('featured_description'),
        MultiFieldPanel(
            heading="Region summary",
            classname='collapsible',
            children=[
                HelpPanel('Required fields for section to show: '
                          'Region Summary Section Content'),
                ImageChooserPanel('region_summary_section_image'),
                FieldPanel('region_summary_section_intro'),
                FieldPanel('region_summary_section_content'),
            ],
        ),
        MultiFieldPanel(
            heading="Investment opportunities",
            classname='collapsible collapsed',
            children=[
                FieldPanel('investment_opps_title'),
                FieldPanel('investment_opps_intro'),
            ]
        ),
        MultiFieldPanel(
            heading="Economics Statistics",
            classname='collapsible',
            children=[
                HelpPanel('Required: at least 4 statistics for the section to show'),
                FieldRowPanel([
                    MultiFieldPanel([
                        FieldPanel('economics_stat_1_heading'),
                        FieldPanel('economics_stat_1_number'),
                        FieldPanel('economics_stat_1_smallprint'),
                    ]),
                    MultiFieldPanel([
                        FieldPanel('economics_stat_2_heading'),
                        FieldPanel('economics_stat_2_number'),
                        FieldPanel('economics_stat_2_smallprint'),
                    ]),
                    MultiFieldPanel([
                        FieldPanel('economics_stat_3_heading'),
                        FieldPanel('economics_stat_3_number'),
                        FieldPanel('economics_stat_3_smallprint'),
                    ]),
                ]),
                FieldRowPanel([
                    MultiFieldPanel([
                        FieldPanel('economics_stat_4_heading'),
                        FieldPanel('economics_stat_4_number'),
                        FieldPanel('economics_stat_4_smallprint'),
                    ]),
                    MultiFieldPanel([
                        FieldPanel('economics_stat_5_heading'),
                        FieldPanel('economics_stat_5_number'),
                        FieldPanel('economics_stat_5_smallprint'),
                    ]),
                    MultiFieldPanel([
                        FieldPanel('economics_stat_6_heading'),
                        FieldPanel('economics_stat_6_number'),
                        FieldPanel('economics_stat_6_smallprint'),
                    ]),
                ]),

            ],
        ),
        MultiFieldPanel(
            heading="Location Statistics",
            classname='collapsible',
            children=[
                HelpPanel('Required: at least 4 statistics for the section to show'),
                FieldRowPanel([
                    MultiFieldPanel([
                        FieldPanel('location_stat_1_heading'),
                        FieldPanel('location_stat_1_number'),
                        FieldPanel('location_stat_1_smallprint'),
                    ]),
                    MultiFieldPanel([
                        FieldPanel('location_stat_2_heading'),
                        FieldPanel('location_stat_2_number'),
                        FieldPanel('location_stat_2_smallprint'),
                    ]),
                    MultiFieldPanel([
                        FieldPanel('location_stat_3_heading'),
                        FieldPanel('location_stat_3_number'),
                        FieldPanel('location_stat_3_smallprint'),
                    ]),
                ]),
                FieldRowPanel([
                    MultiFieldPanel([
                        FieldPanel('location_stat_4_heading'),
                        FieldPanel('location_stat_4_number'),
                        FieldPanel('location_stat_4_smallprint'),
                    ]),
                    MultiFieldPanel([
                        FieldPanel('location_stat_5_heading'),
                        FieldPanel('location_stat_5_number'),
                        FieldPanel('location_stat_5_smallprint'),
                    ]),
                    MultiFieldPanel([
                        FieldPanel('location_stat_6_heading'),
                        FieldPanel('location_stat_6_number'),
                        FieldPanel('location_stat_6_smallprint'),
                    ]),
                ]),
            ],
        ),
        MultiFieldPanel(
            heading="Extra optional Property and Infrastructure section",
            classname='collapsible',
            children=[
                HelpPanel('Required fields for section to show: '
                          'Property and Infrastructure Section Title, '
                          'Property and Infrastructure Section Content'),
                ImageChooserPanel('property_and_infrastructure_section_image'),
                FieldPanel('property_and_infrastructure_section_title'),
                FieldPanel('property_and_infrastructure_section_content'),
            ],
        ),
        MultiFieldPanel(
            heading="Accordions subsections",
            classname='collapsible collapsed',
            children=[
                HelpPanel('Required: subsections title and at least one title and content for an accordion to show'),
                FieldPanel('subsections_title'),
                FieldRowPanel([
                    MultiFieldPanel([
                        FieldPanel('sub_section_one_title'),
                        ImageChooserPanel('sub_section_one_icon'),
                        FieldPanel('sub_section_one_content')
                    ]),
                    MultiFieldPanel([
                        FieldPanel('sub_section_two_title'),
                        ImageChooserPanel('sub_section_two_icon'),
                        FieldPanel('sub_section_two_content')
                    ]),
                    MultiFieldPanel([
                        FieldPanel('sub_section_three_title'),
                        ImageChooserPanel('sub_section_three_icon'),
                        FieldPanel('sub_section_three_content')
                    ]),
                ]),
            ]
        ),
        MultiFieldPanel(
            heading="Case study",
            classname='collapsible',
            children=[
                HelpPanel('Required fields for section to show: '
                          'Case Study Image, Case Study Title'),
                ImageChooserPanel('case_study_image'),
                FieldPanel('case_study_title'),
                FieldPanel('case_study_text'),
                HelpPanel('Cta\'s require both text and a link to show '
                          'on page. '),
                FieldPanel('case_study_cta_text'),
                FieldPanel('case_study_cta_link'),
            ],
        ),
        MultiFieldPanel(
            heading="Contact",
            classname='collapsible',
            children=[
                HelpPanel('Required fields for section to show: '
                          'Contact Title, Contact Text'),
                FieldPanel('contact_title'),
                FieldPanel('contact_text'),
                FieldPanel('contact_cta_text'),
                FieldPanel('contact_cta_link'),
            ],
        ),
        SearchEngineOptimisationPanel()
    ]

    settings_panels = [
        FieldPanel('slug'),
    ]

    edit_handler = make_translated_interface(
        content_panels=content_panels,
        settings_panels=settings_panels
    )


class CapitalInvestContactFormPagePanels:
    content_panels = [
        FieldPanel('title'),
        FieldPanel('breadcrumbs_label'),
        FieldPanel('heading'),
        FieldPanel('intro'),
        FieldPanel('comment'),
        FieldPanel('cta_text'),
        SearchEngineOptimisationPanel()
    ]

    settings_panels = [
        FieldPanel('slug'),
    ]

    edit_handler = make_translated_interface(
        content_panels=content_panels,
        settings_panels=settings_panels,
    )


class CapitalInvestContactFormSuccessPagePanels:
    content_panels = [
        FieldPanel('title'),
        FieldPanel('message_box_heading'),
        FieldPanel('message_box_description'),
        FieldPanel('what_happens_next_description')
    ]

    settings_panels = [
        FieldPanel('slug'),
    ]

    edit_handler = make_translated_interface(
        content_panels=content_panels,
        settings_panels=settings_panels,
    )
