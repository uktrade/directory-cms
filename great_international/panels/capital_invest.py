from wagtail.admin.edit_handlers import (
    InlinePanel, HelpPanel, FieldPanel, FieldRowPanel, MultiFieldPanel,
    PageChooserPanel,
)
from wagtail.documents.edit_handlers import DocumentChooserPanel
from wagtail.images.edit_handlers import ImageChooserPanel

from core.helpers import make_translated_interface


class InternationalCapitalInvestLandingPagePanels:

    content_panels = [
        FieldPanel('title'),
        FieldPanel('breadcrumbs_label'),
        MultiFieldPanel(
            heading="Hero",
            children=[
                ImageChooserPanel('hero_image'),
                FieldPanel('hero_title'),
                FieldPanel('hero_subheading'),
                FieldPanel('hero_subtitle'),
                FieldPanel('hero_cta_text')
            ]
        ),
        MultiFieldPanel(
            heading="Reason to invest in the UK section",
            classname='collapsible',
            children=[
                HelpPanel('Required fields for section to show: '
                          'Reason to Invest Title, Reason to Invest Content'),
                FieldPanel('reason_to_invest_section_title'),
                FieldPanel('reason_to_invest_section_intro'),
                FieldPanel('reason_to_invest_section_content'),
                ImageChooserPanel('reason_to_invest_section_image'),
                FieldPanel('how_we_help_title'),
                FieldPanel('how_we_help_intro'),
                HelpPanel('Each icon requires corresponding text to show '
                          'on page'),
                FieldRowPanel([
                    MultiFieldPanel([
                        ImageChooserPanel('how_we_help_one_icon'),
                        FieldPanel('how_we_help_one_text'),
                    ]),
                    MultiFieldPanel([
                        ImageChooserPanel('how_we_help_two_icon'),
                        FieldPanel('how_we_help_two_text'),
                    ]),
                ]),
                FieldRowPanel([
                    MultiFieldPanel([
                        ImageChooserPanel('how_we_help_three_icon'),
                        FieldPanel('how_we_help_three_text'),
                    ]),
                    MultiFieldPanel([
                        ImageChooserPanel('how_we_help_four_icon'),
                        FieldPanel('how_we_help_four_text'),
                    ]),
                ]),
            ]
        ),
        MultiFieldPanel(
            heading="Investment Opportunities by regions",
            classname='collapsible',
            children=[
                HelpPanel('Required fields for section to show: '
                          'Region Opportunity Title, 1 Related Region'),
                FieldPanel('region_ops_section_title'),
                FieldPanel('region_ops_section_intro'),
                InlinePanel(
                    'added_region_card_fields',
                    label="Region card fields"
                ),
            ]
        ),
        MultiFieldPanel(
            heading="Informative banner",
            children=[
                FieldPanel('banner_information')
            ],
        ),
        MultiFieldPanel(
            heading="Related region pages",
            classname='collapsible collapsed',
            children=[
                HelpPanel('Please use this to link to a related region, '
                          'rather than adding in manually the region title, '
                          'image and text in the above section when the '
                          'capital invest region pages are available'),
                InlinePanel(
                    'added_regions',
                    label="Related Regions"
                ),
            ]
        ),
        MultiFieldPanel(
            heading="Energy Sector",
            classname='collapsible',
            children=[
                HelpPanel('Required fields for section to show: '
                          'Energy Sector Title, Energy Sector Content'),
                FieldPanel('energy_sector_title'),
                FieldPanel('energy_sector_content'),
                ImageChooserPanel('energy_sector_image'),
                HelpPanel('CTA requires text and PDF to show on teh page.'),
                FieldPanel('energy_sector_cta_text'),
                DocumentChooserPanel('energy_sector_pdf_document'),
            ]
        ),
        MultiFieldPanel(
            heading="Homes in England Section",
            classname='collapsible',
            children=[
                HelpPanel('Required fields for section to show: '
                          'Homes In England Section Title, Title and PDF '
                          'for each card'),
                FieldPanel('homes_in_england_section_title'),
                InlinePanel(
                    'added_homes_in_england_card_fields',
                    label="Homes In England cards"
                )
            ]
        ),
        MultiFieldPanel(
            heading="Contact Section",
            classname='collapsible collapsed',
            children=[
                HelpPanel('Required fields for section to show: '
                          'Contact Title, Contact Text'),
                FieldPanel('contact_section_title'),
                FieldPanel('contact_section_text'),
                FieldPanel('contact_section_cta_text')
            ]
        ),
    ]

    settings_panels = [
        FieldPanel('slug'),
    ]

    edit_handler = make_translated_interface(
        content_panels=content_panels,
        settings_panels=settings_panels
    )


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
    ]

    settings_panels = [
        FieldPanel('slug'),
    ]

    edit_handler = make_translated_interface(
        content_panels=content_panels,
        settings_panels=settings_panels
    )


class CapitalInvestOpportunityListingPagePanels:

    content_panels = [
        FieldPanel('title'),
        FieldPanel('breadcrumbs_label'),
        FieldPanel('search_results_title')
    ]

    settings_panels = [
        FieldPanel('slug'),
    ]

    edit_handler = make_translated_interface(
        content_panels=content_panels,
        settings_panels=settings_panels
    )


class CapitalInvestOpportunityPagePanels:

    content_panels = [
        FieldPanel('title'),
        MultiFieldPanel(
            heading="Related sector",
            classname='collapsible collapsed',
            children=[
                InlinePanel('related_sectors', label="Related Sectors"),
            ],
        ),
        MultiFieldPanel(
            heading="Related region",
            classname='collapsible collapsed',
            children=[
                PageChooserPanel(
                    'related_region',
                    [
                        'great_international.'
                        'AboutUkRegionPage'
                    ]
                ),
            ],
        ),
        FieldPanel('breadcrumbs_label'),
        MultiFieldPanel(
            heading="Hero",
            children=[
                ImageChooserPanel('hero_image'),
                FieldPanel('hero_title'),
            ],
        ),
        MultiFieldPanel(
            heading="Opportunity summary",
            classname='collapsible',
            children=[
                HelpPanel('Required fields for section to show: '
                          'Opportunity Summary Intro'),
                FieldPanel('opportunity_summary_intro'),
                FieldPanel('opportunity_summary_content'),
                ImageChooserPanel('opportunity_summary_image'),
            ],
        ),
        MultiFieldPanel(
            heading="Opportunity Details",
            classname='collapsible',
            children=[
                HelpPanel('Icons require the corresponding text to show on '
                          'page'),
                FieldRowPanel([
                    MultiFieldPanel([
                        ImageChooserPanel('location_icon'),
                        FieldPanel('location_heading'),
                        FieldPanel('location'),
                    ]),
                    MultiFieldPanel([
                        ImageChooserPanel('project_promoter_icon'),
                        FieldPanel('project_promoter_heading'),
                        FieldPanel('project_promoter'),
                    ]),
                    MultiFieldPanel([
                        ImageChooserPanel('scale_icon'),
                        FieldPanel('scale_heading'),
                        FieldPanel('scale'),
                        FieldPanel('scale_value'),
                    ]),
                ]),
                FieldRowPanel([
                    MultiFieldPanel([
                        ImageChooserPanel('sector_icon'),
                        FieldPanel('sector_heading'),
                        InlinePanel('related_sub_sectors',
                                    label="Related Sectors"),
                    ]),
                    MultiFieldPanel([
                        ImageChooserPanel('investment_type_icon'),
                        FieldPanel('investment_type_heading'),
                        FieldPanel('investment_type'),
                    ]),
                    MultiFieldPanel([
                        ImageChooserPanel('planning_status_icon'),
                        FieldPanel('planning_status_heading'),
                        FieldPanel('planning_status'),
                    ]),
                ]),
            ],
        ),
        MultiFieldPanel(
            heading="Project Details",
            classname='collapsible',
            children=[
                HelpPanel('Title requires corresponding text to show on page'),
                FieldPanel('project_background_title'),
                FieldPanel('project_background_intro'),
                FieldRowPanel([
                    MultiFieldPanel([
                        FieldPanel('project_description_title'),
                        FieldPanel('project_description_content'),
                    ]),
                    MultiFieldPanel([
                        FieldPanel('project_promoter_title'),
                        FieldPanel('project_promoter_content'),
                    ]),
                ]),
                ImageChooserPanel('project_image')
            ],
        ),
        MultiFieldPanel(
            heading="Similar projects",
            classname='collapsible',
            children=[
                HelpPanel('Section shows if there are opportunities with the same related sector. '
                          'They are chosen randomly. Cta\'s require both text and a link to show '
                          'on page. '),
                FieldPanel('similar_projects_cta_text'),
                FieldPanel('similar_projects_cta_link'),
            ],
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
            ],
        ),
    ]

    settings_panels = [
        FieldPanel('slug'),
    ]

    edit_handler = make_translated_interface(
        content_panels=content_panels,
        settings_panels=settings_panels,
    )


class CapitalInvestContactFormPagePanels:
    content_panels = [
        FieldPanel('title'),
        FieldPanel('breadcrumbs_label'),
        FieldPanel('heading'),
        FieldPanel('intro'),
        FieldPanel('comment'),
        FieldPanel('cta_text'),
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
        FieldPanel('what_happens_next_description'),
    ]

    settings_panels = [
        FieldPanel('slug'),
    ]

    edit_handler = make_translated_interface(
        content_panels=content_panels,
        settings_panels=settings_panels,
    )
