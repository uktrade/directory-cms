from wagtail.admin.edit_handlers import (
    FieldPanel, FieldRowPanel, MultiFieldPanel, ObjectList, HelpPanel
)
from wagtail.images.edit_handlers import ImageChooserPanel

from core.helpers import make_translated_interface
from core.panels import SearchEngineOptimisationPanel


class InvestInternationalHomePagePanels:

    image_panels = [
        ImageChooserPanel('hero_image'),
        ImageChooserPanel('how_to_expand_image'),
    ]

    content_panels = [
        FieldPanel('title'),
        MultiFieldPanel(
            heading='Hero',
            classname='collapsible',
            children=[
                FieldPanel('breadcrumbs_label'),
                FieldPanel('heading'),
                FieldPanel('sub_heading'),
                HelpPanel('Cta\'s require both text and a link to show '
                          'on page. '),
                FieldPanel('hero_call_to_action_text'),
                FieldPanel('hero_call_to_action_url'),
            ],

        ),

        MultiFieldPanel(
            heading='Teaser',
            classname='collapsible',
            children=[
                FieldPanel('teaser')
            ]
        ),

        MultiFieldPanel(
            heading='Benefits section',
            classname='collapsible',
            children=[
                HelpPanel('Required fields for section to show: '
                          'Benefits Section Title, Benefits Section Content'),
                FieldPanel('benefits_section_title'),
                FieldPanel('benefits_section_intro'),
                FieldPanel('benefits_section_content'),
                HelpPanel('CTAs require both text and a link to show on page'),
                FieldPanel('benefits_section_cta_text'),
                FieldPanel('benefits_section_cta_url'),
                ImageChooserPanel('benefits_section_img'),
            ],
        ),

        MultiFieldPanel(
            heading='EU Exit section',
            classname='collapsible collapsed',
            children=[
                FieldPanel('eu_exit_section_title'),
                FieldPanel('eu_exit_section_content'),
                FieldPanel('eu_exit_section_call_to_action_text'),
                FieldPanel('eu_exit_section_call_to_action_url'),
                ImageChooserPanel('eu_exit_section_img'),
            ],

        ),
        MultiFieldPanel(
            heading='How to Expand section',
            classname='collapsible',
            children=[
                HelpPanel('Required fields for section to show: How to expand title, image and '
                          'at least one item with title and text'),
                FieldPanel('how_to_expand_title'),
                FieldPanel('how_to_expand_intro'),
                FieldRowPanel(
                    [
                        MultiFieldPanel(
                            [
                                FieldPanel('how_to_expand_title_one'),
                                FieldPanel('how_to_expand_text_one')
                            ],
                        ),
                        MultiFieldPanel(
                            [
                                FieldPanel('how_to_expand_title_two'),
                                FieldPanel('how_to_expand_text_two')
                            ],
                        ),
                        MultiFieldPanel(
                            [
                                FieldPanel('how_to_expand_title_three'),
                                FieldPanel('how_to_expand_text_three')
                            ]
                        ),
                        MultiFieldPanel(
                            [
                                FieldPanel('how_to_expand_title_four'),
                                FieldPanel('how_to_expand_text_four')
                            ],
                        ),
                    ]
                ),
            ],
        ),
        MultiFieldPanel(
            heading='How we help section',
            classname='collapsible',
            children=[
                HelpPanel('Required fields for section to show: '
                          'How We Help Title, How We Help Lead In'),
                FieldPanel('how_we_help_title'),
                FieldPanel('how_we_help_lead_in'),
                HelpPanel('Each icon requires the corresponding text to '
                          'show on the page'),
                FieldRowPanel(
                    [
                        MultiFieldPanel(
                            [
                                FieldPanel('how_we_help_text_one'),
                                ImageChooserPanel('how_we_help_icon_one')
                            ],
                        ),
                        MultiFieldPanel(
                            [
                                FieldPanel('how_we_help_text_two'),
                                ImageChooserPanel('how_we_help_icon_two')
                            ],
                        ),
                        MultiFieldPanel(
                            [
                                FieldPanel('how_we_help_text_three'),
                                ImageChooserPanel('how_we_help_icon_three')
                            ],
                        ),
                    ],
                ),
                FieldRowPanel(
                    [
                        MultiFieldPanel(
                            [
                                FieldPanel('how_we_help_text_four'),
                                ImageChooserPanel('how_we_help_icon_four')
                            ],
                        ),
                        MultiFieldPanel(
                            [
                                FieldPanel('how_we_help_text_five'),
                                ImageChooserPanel('how_we_help_icon_five')
                            ],
                        )
                    ],
                ),
                FieldPanel('how_we_help_cta_text'),
                FieldPanel('how_we_help_cta_link'),
            ],
        ),
        MultiFieldPanel(
            heading='Contact Section',
            classname='collapsible',
            children=[
                HelpPanel('Required fields for section to show: '
                          'Contact Title, Contact Content'),
                FieldPanel('contact_section_title'),
                FieldPanel('contact_section_content'),
                HelpPanel('Cta\'s require both text and a link to show '
                          'on page. '),
                FieldPanel('contact_section_call_to_action_text'),
                FieldPanel('contact_section_call_to_action_url'),
            ],
        ), MultiFieldPanel(
            heading='Investment Support Directory Section',
            classname='collapsible',
            children=[
                HelpPanel('Required fields for section to show: '
                          'ISD section title and text'),
                FieldPanel('isd_section_title'),
                FieldPanel('isd_section_text'),
                HelpPanel('Cta\'s require both text and a link to show '
                          'on page. '),
                FieldPanel('isd_section_cta_text'),
                FieldPanel('isd_section_cta_link'),
            ],
        ),
        MultiFieldPanel(
            heading='High Potential Opportunities',
            children=[
                HelpPanel('Required fields for section to show: '
                          'HPO title, 1 HPO in active language'),
                FieldPanel('hpo_title'),
                FieldPanel('hpo_intro')
            ],
        ),
        MultiFieldPanel(
            heading='Industries section',
            children=[
                HelpPanel('Required fields for section to show: '
                          'Sector Title, Sector Content and at least one featured industry '
                          '(choose in \'featured industries\' tab)'),
                FieldPanel('sector_title'),
                FieldPanel('sector_intro'),
                FieldPanel('sector_button_text'),
                FieldPanel('sector_button_url'),
            ],
        ),
        MultiFieldPanel(
            heading='Featured card links ',
            classname='collapsible collapsed',
            children=[
                HelpPanel('Required fields for section to show: '
                          'All images, titles and summaries'),
                FieldRowPanel(
                    [
                        MultiFieldPanel(
                            [
                                ImageChooserPanel('featured_card_one_image'),
                                FieldPanel('featured_card_one_title'),
                                FieldPanel('featured_card_one_summary'),
                                FieldPanel('featured_card_one_cta_link'),
                            ],
                        ),
                        MultiFieldPanel(
                            [
                                ImageChooserPanel('featured_card_two_image'),
                                FieldPanel('featured_card_two_title'),
                                FieldPanel('featured_card_two_summary'),
                                FieldPanel('featured_card_two_cta_link'),
                            ],
                        ),
                        MultiFieldPanel(
                            [
                                ImageChooserPanel('featured_card_three_image'),
                                FieldPanel('featured_card_three_title'),
                                FieldPanel('featured_card_three_summary'),
                                FieldPanel('featured_card_three_cta_link'),
                            ]
                        ),
                    ]
                ),
            ],
        ),
        SearchEngineOptimisationPanel()
    ]

    settings_panels = [
        FieldPanel('slug'),
    ]

    edit_handler = make_translated_interface(
        content_panels=content_panels,
        settings_panels=settings_panels,
        other_panels=[
            ObjectList(image_panels, heading='Images'),
        ]
    )


class InvestHighPotentialOpportunitiesPagePanels:
    settings_panels = [
        FieldPanel('slug'),
    ]


class InvestRegionLandingPagePanels:

    image_panels = [
        ImageChooserPanel('hero_image'),
    ]
    content_panels = [
        FieldPanel('title'),
        FieldPanel('heading'),
        SearchEngineOptimisationPanel()
    ]
    settings_panels = [
        FieldPanel('slug'),
    ]

    edit_handler = make_translated_interface(
        content_panels=content_panels,
        settings_panels=settings_panels,
        other_panels=[
            ObjectList(image_panels, heading='Images'),
        ]
    )


class InvestRegionPagePanels:

    image_panels = [
        ImageChooserPanel('hero_image'),
    ]
    content_panels = [
        FieldPanel('title'),
        FieldPanel('heading'),
        FieldPanel('description'),
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
