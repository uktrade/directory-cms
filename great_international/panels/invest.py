from wagtail.admin.edit_handlers import (
    FieldPanel, FieldRowPanel, MultiFieldPanel, ObjectList, HelpPanel, PageChooserPanel
)
from wagtail.documents.edit_handlers import DocumentChooserPanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtailmedia.widgets import AdminMediaChooser

from core.helpers import make_translated_interface
from core.panels import SearchEngineOptimisationPanel


class InvestInternationalHomePagePanels:

    image_panels = [
        ImageChooserPanel('hero_image'),
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
            heading='Featured card links ',
            classname='collapsible',
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
        MultiFieldPanel(
            heading='Industries section',
            children=[
                HelpPanel('Required fields for section to show: '
                          'Sector Title, Sector Content'),
                FieldPanel('sector_title'),
                FieldPanel('sector_intro'),
                FieldPanel('sector_button_text'),
                FieldPanel('sector_button_url'),
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
        ),
        SearchEngineOptimisationPanel()
    ]

    settings_panels = [
        FieldPanel('slug'),
    ]

    featured_industries_panels = [
        MultiFieldPanel(
            heading='Featured industries',
            children=[
                PageChooserPanel('featured_industry_one'),
                PageChooserPanel('featured_industry_two'),
                PageChooserPanel('featured_industry_three'),
            ])
    ]

    edit_handler = make_translated_interface(
        content_panels=content_panels,
        settings_panels=settings_panels,
        other_panels=[
            ObjectList(image_panels, heading='Images'),
            ObjectList(featured_industries_panels, heading='Featured industries'),
        ]
    )


class InvestHighPotentialOpportunitiesPagePanels:
    settings_panels = [
        FieldPanel('slug'),
    ]


class InvestHighPotentialOpportunityDetailPagePanels:

    content_panels = [
        MultiFieldPanel(
            classname='collapsible',
            heading='General',
            children=[
                FieldRowPanel(children=[
                    MultiFieldPanel(children=[
                        FieldPanel('title'),
                        FieldPanel('breadcrumbs_label'),
                        FieldPanel('heading'),
                        FieldPanel('description'),
                    ]),
                    MultiFieldPanel(children=[
                        ImageChooserPanel('hero_image')
                    ]),
                ])
            ]
        ),

        MultiFieldPanel(
            heading='Contact us',
            classname='collapsible',
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
                FieldRowPanel(children=[
                    FieldPanel('proposition_one'),
                    MultiFieldPanel(children=[
                        ImageChooserPanel('proposition_one_image'),
                        FieldPanel('proposition_one_image_alt'),
                        FieldPanel('proposition_one_video', widget=AdminMediaChooser),
                        FieldPanel('proposition_one_video_transcript'),
                    ])
                ])
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
                        MultiFieldPanel(children=[
                            ImageChooserPanel('opportunity_list_image'),
                            FieldPanel('opportunity_list_image_alt'),
                        ])
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
                                FieldPanel('proposition_two_image_alt'),
                                FieldPanel('proposition_two_video', widget=AdminMediaChooser),
                                FieldPanel('proposition_two_video_transcript'),
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
                        ImageChooserPanel('competitive_advantages_list_item_one_icon'),
                        ImageChooserPanel('competitive_advantages_list_item_two_icon'),
                        ImageChooserPanel('competitive_advantages_list_item_three_icon'),
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
                FieldRowPanel(children=[
                    MultiFieldPanel(children=[
                        ImageChooserPanel('companies_list_item_image_one'),
                        FieldPanel('companies_list_item_image_alt_one'),
                    ]),
                    MultiFieldPanel(children=[
                        ImageChooserPanel('companies_list_item_image_two'),
                        FieldPanel('companies_list_item_image_alt_two'),
                    ]),
                    MultiFieldPanel(children=[
                        ImageChooserPanel('companies_list_item_image_three'),
                        FieldPanel('companies_list_item_image_alt_three'),
                    ]),
                    MultiFieldPanel(children=[
                        ImageChooserPanel('companies_list_item_image_four'),
                        FieldPanel('companies_list_item_image_alt_four'),
                    ]),
                ]),
                FieldRowPanel(children=[
                    MultiFieldPanel(children=[
                        ImageChooserPanel('companies_list_item_image_five'),
                        FieldPanel('companies_list_item_image_alt_five'),
                    ]),
                    MultiFieldPanel(children=[
                        ImageChooserPanel('companies_list_item_image_six'),
                        FieldPanel('companies_list_item_image_alt_six'),
                    ]),
                    MultiFieldPanel(children=[
                        ImageChooserPanel('companies_list_item_image_seven'),
                        FieldPanel('companies_list_item_image_alt_seven'),
                    ]),
                    MultiFieldPanel(children=[
                        ImageChooserPanel('companies_list_item_image_eight'),
                        FieldPanel('companies_list_item_image_alt_eight'),
                    ])
                ])
            ]
        ),
        MultiFieldPanel(
            heading='Case studies',
            children=[
                FieldPanel('case_study_list_title'),
                FieldRowPanel(
                    children=[
                        FieldPanel('case_study_one_text'),
                        MultiFieldPanel(children=[
                            ImageChooserPanel('case_study_one_image'),
                            FieldPanel('case_study_one_image_alt'),
                        ])
                    ]
                ),
                FieldRowPanel(
                    children=[
                        FieldPanel('case_study_two_text'),
                        MultiFieldPanel(children=[
                            ImageChooserPanel('case_study_two_image'),
                            FieldPanel('case_study_two_image_alt'),
                        ])
                    ]
                ),
                FieldRowPanel(
                    children=[
                        FieldPanel('case_study_three_text'),
                        MultiFieldPanel(children=[
                            ImageChooserPanel('case_study_three_image'),
                            FieldPanel('case_study_three_image_alt'),
                        ])
                    ]
                ),
                FieldRowPanel(children=[
                    FieldPanel('case_study_four_text'),
                    MultiFieldPanel(children=[
                        ImageChooserPanel('case_study_four_image'),
                        FieldPanel('case_study_four_image_alt'),
                    ])
                ])
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
        FieldPanel('slug'),
        FieldPanel('featured'),
        DocumentChooserPanel('pdf_document'),
    ]

    edit_handler = make_translated_interface(
        content_panels=content_panels,
        settings_panels=settings_panels
    )


class InvestHighPotentialOpportunityFormPagePanels:

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


class InvestHighPotentialOpportunityFormSuccessPagePanels:

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
