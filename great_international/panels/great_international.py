from django.forms import Textarea, CheckboxSelectMultiple

from wagtail.admin.edit_handlers import (
    HelpPanel, FieldPanel, FieldRowPanel, MultiFieldPanel, PageChooserPanel
)
from wagtail.images.edit_handlers import ImageChooserPanel

from core.helpers import make_translated_interface
from core.panels import SearchEngineOptimisationPanel


class InternationalHomePagePanels:

    content_panels = [
        MultiFieldPanel(
            heading="Hero Section",
            children=[
                FieldPanel('hero_title'),
                FieldPanel('hero_subtitle'),
                FieldPanel("hero_cta_text"),
                FieldPanel("hero_cta_link"),
                ImageChooserPanel("hero_image")
            ]
        ),
        MultiFieldPanel(
            heading="Featured Cards",
            children=[
                FieldRowPanel([
                    MultiFieldPanel(
                        heading='Invest Card',
                        children=[
                            FieldPanel('invest_title'),
                            FieldPanel('invest_content'),
                            ImageChooserPanel('invest_image')
                        ]
                    ),
                    MultiFieldPanel(
                        heading='Trade Card',
                        children=[
                            FieldPanel('trade_title'),
                            FieldPanel('trade_content'),
                            ImageChooserPanel('trade_image')
                        ]
                    ),
                ]),
            ]
        ),

        MultiFieldPanel(
            heading='Features highlight',
            children=[
                FieldPanel('section_two_heading'),
                FieldPanel('section_two_teaser'),
                FieldRowPanel([
                    MultiFieldPanel(
                        children=[
                            ImageChooserPanel(
                                'section_two_subsection_one_icon'
                            ),
                            FieldPanel('section_two_subsection_one_heading'),
                            FieldPanel('section_two_subsection_one_body')
                        ]),
                    MultiFieldPanel(
                        children=[
                            ImageChooserPanel(
                                'section_two_subsection_two_icon'
                            ),
                            FieldPanel('section_two_subsection_two_heading'),
                            FieldPanel('section_two_subsection_two_body')
                        ]),
                    MultiFieldPanel(
                        children=[
                            ImageChooserPanel(
                                'section_two_subsection_three_icon'
                            ),
                            FieldPanel('section_two_subsection_three_heading'),
                            FieldPanel('section_two_subsection_three_body')
                        ]),
                    MultiFieldPanel(
                        children=[
                            ImageChooserPanel(
                                'section_two_subsection_four_icon'
                            ),
                            FieldPanel('section_two_subsection_four_heading'),
                            FieldPanel('section_two_subsection_four_body')
                        ]),
                    MultiFieldPanel(
                        children=[
                            ImageChooserPanel(
                                'section_two_subsection_five_icon'
                            ),
                            FieldPanel('section_two_subsection_five_heading'),
                            FieldPanel('section_two_subsection_five_body')
                        ]),
                    MultiFieldPanel(
                        children=[
                            ImageChooserPanel(
                                'section_two_subsection_six_icon'),
                            FieldPanel('section_two_subsection_six_heading'
                                       ),
                            FieldPanel('section_two_subsection_six_body')
                        ])
                ])
            ]),

        MultiFieldPanel(
            heading='Tariffs',
            children=[
                FieldPanel('tariffs_title'),
                FieldPanel('tariffs_description'),
                FieldPanel('tariffs_link'),
                ImageChooserPanel('tariffs_image'),
                FieldPanel('tariffs_call_to_action_text')
            ]
        ),

        MultiFieldPanel(
            heading='Featured links',
            children=[
                FieldPanel('featured_links_title'),
                FieldPanel('featured_links_summary'),
                FieldRowPanel([
                    MultiFieldPanel(
                        children=[
                            FieldPanel('featured_link_one_heading'),
                            ImageChooserPanel('featured_link_one_image')
                        ]),
                    MultiFieldPanel(
                        children=[
                            FieldPanel('featured_link_two_heading'),
                            ImageChooserPanel('featured_link_two_image')
                        ]),
                    MultiFieldPanel(
                        children=[
                            FieldPanel('featured_link_three_heading'),
                            ImageChooserPanel('featured_link_three_image')
                        ])
                ])]
        ),

        MultiFieldPanel(
            heading='News section',
            children=[
                FieldPanel('news_title'),
                FieldRowPanel([
                    PageChooserPanel(
                        'related_page_one',
                        [
                            'great_international.InternationalArticlePage',
                            'great_international.InternationalCampaignPage',
                        ]),
                    PageChooserPanel(
                        'related_page_two',
                        [
                            'great_international.InternationalArticlePage',
                            'great_international.InternationalCampaignPage',
                        ]),
                    PageChooserPanel(
                        'related_page_three',
                        [
                            'great_international.InternationalArticlePage',
                            'great_international.InternationalCampaignPage',
                        ]),
                ])
            ]
        ),

        MultiFieldPanel(
            heading='Featured CTA\'s',
            children=[
                FieldRowPanel([
                    MultiFieldPanel(
                        heading="Study in the UK",
                        children=[
                            FieldPanel('study_in_uk_cta_text')
                        ]
                    ),
                    MultiFieldPanel(
                        heading="Visit the UK",
                        children=[
                            FieldPanel('visit_uk_cta_text')
                        ]
                    ),
                ]),
            ]
        ),

        SearchEngineOptimisationPanel(),
    ]

    settings_panels = [
        FieldPanel('title_en_gb'),
        FieldPanel('slug'),
        FieldPanel('uses_tree_based_routing'),
    ]

    edit_handler = make_translated_interface(
        content_panels=content_panels,
        settings_panels=settings_panels
    )


class InternationalHomePageOldPanels:

    content_panels = [
        MultiFieldPanel(
            heading="Hero Section",
            children=[
                FieldPanel('hero_title'),
                FieldPanel('hero_subtitle'),
                FieldPanel("hero_cta_text"),
                FieldPanel("hero_cta_link"),
                ImageChooserPanel("hero_image")
            ]
        ),
        MultiFieldPanel(
            heading="Featured Cards",
            children=[
                FieldRowPanel([
                    MultiFieldPanel(
                        heading='Invest Card',
                        children=[
                            FieldPanel('invest_title'),
                            FieldPanel('invest_content'),
                            ImageChooserPanel('invest_image')
                        ]
                    ),
                    MultiFieldPanel(
                        heading='Trade Card',
                        children=[
                            FieldPanel('trade_title'),
                            FieldPanel('trade_content'),
                            ImageChooserPanel('trade_image')
                        ]
                    ),
                ]),
            ]
        ),

        MultiFieldPanel(
            heading='Features highlight',
            children=[
                FieldPanel('section_two_heading'),
                FieldPanel('section_two_teaser'),
                FieldRowPanel([
                    MultiFieldPanel(
                        children=[
                            ImageChooserPanel(
                                'section_two_subsection_one_icon'
                            ),
                            FieldPanel('section_two_subsection_one_heading'),
                            FieldPanel('section_two_subsection_one_body')
                        ]),
                    MultiFieldPanel(
                        children=[
                            ImageChooserPanel(
                                'section_two_subsection_two_icon'
                            ),
                            FieldPanel('section_two_subsection_two_heading'),
                            FieldPanel('section_two_subsection_two_body')
                        ]),
                    MultiFieldPanel(
                        children=[
                            ImageChooserPanel(
                                'section_two_subsection_three_icon'
                            ),
                            FieldPanel('section_two_subsection_three_heading'),
                            FieldPanel('section_two_subsection_three_body')
                        ]),
                    MultiFieldPanel(
                        children=[
                            ImageChooserPanel(
                                'section_two_subsection_four_icon'
                            ),
                            FieldPanel('section_two_subsection_four_heading'),
                            FieldPanel('section_two_subsection_four_body')
                        ]),
                    MultiFieldPanel(
                        children=[
                            ImageChooserPanel(
                                'section_two_subsection_five_icon'
                            ),
                            FieldPanel('section_two_subsection_five_heading'),
                            FieldPanel('section_two_subsection_five_body')
                        ]),
                    MultiFieldPanel(
                        children=[
                            ImageChooserPanel(
                                'section_two_subsection_six_icon'),
                            FieldPanel('section_two_subsection_six_heading'
                                       ),
                            FieldPanel('section_two_subsection_six_body')
                        ])
                ])
            ]),

        MultiFieldPanel(
            heading='Tariffs',
            children=[
                FieldPanel('tariffs_title'),
                FieldPanel('tariffs_description'),
                FieldPanel('tariffs_link'),
                ImageChooserPanel('tariffs_image'),
                FieldPanel('tariffs_call_to_action_text')
            ]
        ),

        MultiFieldPanel(
            heading='Featured links',
            children=[
                FieldPanel('featured_links_title'),
                FieldPanel('featured_links_summary'),
                FieldRowPanel([
                    MultiFieldPanel(
                        children=[
                            FieldPanel('featured_link_one_heading'),
                            ImageChooserPanel('featured_link_one_image')
                        ]),
                    MultiFieldPanel(
                        children=[
                            FieldPanel('featured_link_two_heading'),
                            ImageChooserPanel('featured_link_two_image')
                        ]),
                    MultiFieldPanel(
                        children=[
                            FieldPanel('featured_link_three_heading'),
                            ImageChooserPanel('featured_link_three_image')
                        ])
                ])]
        ),

        MultiFieldPanel(
            heading='News section',
            children=[
                FieldPanel('news_title'),
                FieldRowPanel([
                    PageChooserPanel(
                        'related_page_one',
                        [
                            'great_international.InternationalArticlePage',
                            'great_international.InternationalCampaignPage',
                        ]),
                    PageChooserPanel(
                        'related_page_two',
                        [
                            'great_international.InternationalArticlePage',
                            'great_international.InternationalCampaignPage',
                        ]),
                    PageChooserPanel(
                        'related_page_three',
                        [
                            'great_international.InternationalArticlePage',
                            'great_international.InternationalCampaignPage',
                        ]),
                ])
            ]
        ),

        MultiFieldPanel(
            heading='Featured CTA\'s',
            children=[
                FieldRowPanel([
                    MultiFieldPanel(
                        heading="Study in the UK",
                        children=[
                            FieldPanel('study_in_uk_cta_text')
                        ]
                    ),
                    MultiFieldPanel(
                        heading="Visit the UK",
                        children=[
                            FieldPanel('visit_uk_cta_text')
                        ]
                    ),
                ]),
            ]
        ),

        SearchEngineOptimisationPanel(),
    ]

    settings_panels = [
        FieldPanel('title_en_gb'),
        FieldPanel('slug'),
        FieldPanel('uses_tree_based_routing'),
    ]

    edit_handler = make_translated_interface(
        content_panels=content_panels,
        settings_panels=settings_panels
    )


class InternationalSectorPagePanels:

    content_panels = [
        MultiFieldPanel(
            heading='Heading',
            children=[
                FieldPanel('heading'),
                FieldPanel('sub_heading'),
                ImageChooserPanel('hero_image'),
                FieldPanel('heading_teaser')
            ]

        ),
        MultiFieldPanel(
            heading='Unique selling points',
            children=[
                HelpPanel(
                    'Use H2 (##) markdown for the three subheadings.'
                    ' Required fields for section to show: 3 Unique Selling '
                    'Points Markdown'),
                FieldRowPanel(
                    [
                        FieldPanel('section_one_body'),
                        MultiFieldPanel(
                            [
                                ImageChooserPanel('section_one_image'),
                                FieldPanel('section_one_image_caption'),
                                FieldPanel('section_one_image_caption_company')
                            ]
                        )
                    ]
                )
            ]
        ),
        MultiFieldPanel(
            heading='Statistics',
            children=[
                FieldRowPanel(
                    [
                        MultiFieldPanel(
                            [
                                FieldPanel('statistic_1_number'),
                                FieldPanel('statistic_1_heading'),
                                FieldPanel('statistic_1_smallprint')
                            ]
                        ),
                        MultiFieldPanel(
                            [
                                FieldPanel('statistic_2_number'),
                                FieldPanel('statistic_2_heading'),
                                FieldPanel('statistic_2_smallprint')
                            ]
                        ),
                        MultiFieldPanel(
                            [
                                FieldPanel('statistic_3_number'),
                                FieldPanel('statistic_3_heading'),
                                FieldPanel('statistic_3_smallprint')
                            ]
                        ),
                        MultiFieldPanel(
                            [
                                FieldPanel('statistic_4_number'),
                                FieldPanel('statistic_4_heading'),
                                FieldPanel('statistic_4_smallprint')
                            ]
                        ),
                        MultiFieldPanel(
                            [
                                FieldPanel('statistic_5_number'),
                                FieldPanel('statistic_5_heading'),
                                FieldPanel('statistic_5_smallprint')
                            ]
                        ),
                        MultiFieldPanel(
                            [
                                FieldPanel('statistic_6_number'),
                                FieldPanel('statistic_6_heading'),
                                FieldPanel('statistic_6_smallprint')
                            ]
                        ),
                    ]
                )
            ]
        ),
        MultiFieldPanel(
            heading='Spotlight',
            children=[
                FieldPanel('section_two_heading'),
                FieldPanel('section_two_teaser'),
                HelpPanel(
                    'Each icon needs a heading for it to show on the page.'),
                FieldRowPanel(
                    [
                        MultiFieldPanel(
                            [
                                ImageChooserPanel(
                                    'section_two_subsection_one_icon'),
                                FieldPanel(
                                    'section_two_subsection_one_heading'),
                                FieldPanel(
                                    'section_two_subsection_one_body')
                            ]
                        ),
                        MultiFieldPanel(
                            [
                                ImageChooserPanel(
                                    'section_two_subsection_two_icon'),
                                FieldPanel(
                                    'section_two_subsection_two_heading'),
                                FieldPanel(
                                    'section_two_subsection_two_body')
                            ]
                        ),
                        MultiFieldPanel(
                            [
                                ImageChooserPanel(
                                    'section_two_subsection_three_icon'),
                                FieldPanel(
                                    'section_two_subsection_three_heading'),
                                FieldPanel(
                                    'section_two_subsection_three_body')
                            ]
                        )
                    ]
                )
            ]
        ),
        MultiFieldPanel(
            heading='Case Study',
            classname='collapsible',
            children=[
                HelpPanel('Required fields for section to show: '
                          'Case Study Image, Case Study Title'),
                FieldPanel('case_study_title'),
                FieldPanel('case_study_description'),
                FieldPanel('case_study_cta_text'),
                HelpPanel('Cta\'s require both text and a link to show '
                          'on page. '),
                PageChooserPanel(
                    'case_study_cta_page',
                    [
                        'great_international.InternationalArticlePage',
                        'great_international.InternationalCampaignPage',
                    ]),
                ImageChooserPanel('case_study_image')
            ]
        ),
        MultiFieldPanel(
            heading='Fact Sheets',
            classname='collapsible collapsed',
            children=[
                FieldPanel('section_three_heading'),
                FieldPanel('section_three_teaser'),
                FieldRowPanel(
                    [
                        MultiFieldPanel(
                            [
                                FieldPanel(
                                    'section_three_subsection_one_heading'),
                                FieldPanel(
                                    'section_three_subsection_one_teaser'),
                                HelpPanel(
                                    'For accessibility reasons, use only '
                                    '"#### [Your text here]" for subheadings '
                                    'in this markdown field'),
                                FieldPanel(
                                    'section_three_subsection_one_body')
                            ]
                        ),
                        MultiFieldPanel(
                            [
                                FieldPanel(
                                    'section_three_subsection_two_heading'),
                                FieldPanel(
                                    'section_three_subsection_two_teaser'),
                                HelpPanel(
                                    'For accessibility reasons, use only '
                                    '"#### [Your text here]" for subheadings '
                                    'in this markdown field'),
                                FieldPanel(
                                    'section_three_subsection_two_body')
                            ]
                        )
                    ]
                )
            ]
        ),
        MultiFieldPanel(
            heading='Related articles',
            children=[
                FieldRowPanel([
                    PageChooserPanel(
                        'related_page_one',
                        [
                            'great_international.InternationalArticlePage',
                            'great_international.InternationalCampaignPage',
                        ]),
                    PageChooserPanel(
                        'related_page_two',
                        [
                            'great_international.InternationalArticlePage',
                            'great_international.InternationalCampaignPage',
                        ]),
                    PageChooserPanel(
                        'related_page_three',
                        [
                            'great_international.InternationalArticlePage',
                            'great_international.InternationalCampaignPage',
                        ]),
                ])
            ]
        ),
        MultiFieldPanel(
            heading='Project Opportunities',
            classname='collapsible ',
            children=[
                FieldPanel('project_opportunities_title'),
                HelpPanel('Prioritised opportunity pages that link to this '
                          'sector will display here. Required fields for '
                          'section to show: Project Opportunities Title, 1 '
                          'Prioritised Opportunity Related to this sector'),
                FieldPanel('related_opportunities_cta_text'),
                FieldPanel('related_opportunities_cta_link')
            ]
        ),
        SearchEngineOptimisationPanel()
    ]

    settings_panels = [
        FieldPanel('title_en_gb'),
        FieldPanel('slug'),
        FieldPanel('uses_tree_based_routing'),
        FieldPanel('tags', widget=CheckboxSelectMultiple)
    ]

    edit_handler = make_translated_interface(
        content_panels=content_panels,
        settings_panels=settings_panels
    )


class InternationalRegionPagePanels:

    settings_panels = [
        FieldPanel('title_en_gb'),
        FieldPanel('slug'),
        FieldPanel('uses_tree_based_routing'),
        FieldPanel('tags', widget=CheckboxSelectMultiple)
    ]


class InternationalLocalisedFolderPagePanels:

    settings_panels = [
        FieldPanel('title_en_gb'),
        FieldPanel('slug'),
        FieldPanel('uses_tree_based_routing'),
    ]


class InternationalArticlePagePanels:

    content_panels = [
        FieldPanel('article_title'),
        MultiFieldPanel(
            heading='Article content',
            children=[
                FieldPanel('article_subheading'),
                FieldPanel('article_teaser'),
                ImageChooserPanel('article_image'),
                FieldPanel('article_body_text')
            ]
        ),
        MultiFieldPanel(
            heading='Related articles',
            children=[
                FieldRowPanel([
                    PageChooserPanel(
                        'related_page_one',
                        'great_international.InternationalArticlePage'),
                    PageChooserPanel(
                        'related_page_two',
                        'great_international.InternationalArticlePage'),
                    PageChooserPanel(
                        'related_page_three',
                        'great_international.InternationalArticlePage'),
                ]),
            ]
        ),
        SearchEngineOptimisationPanel(),
    ]

    settings_panels = [
        FieldPanel('title_en_gb'),
        FieldPanel('slug'),
        FieldPanel('uses_tree_based_routing'),
        FieldPanel('tags', widget=CheckboxSelectMultiple)
    ]

    edit_handler = make_translated_interface(
        content_panels=content_panels,
        settings_panels=settings_panels
    )


class InternationalArticleListingPagePanels:

    content_panels = [
        FieldPanel('landing_page_title'),
        MultiFieldPanel(
            heading='Hero',
            children=[
                ImageChooserPanel('hero_image'),
                FieldPanel('hero_teaser')
            ]
        ),
        FieldPanel('list_teaser'),
        SearchEngineOptimisationPanel(),
    ]

    settings_panels = [
        FieldPanel('title_en_gb'),
        FieldPanel('slug'),
        FieldPanel('uses_tree_based_routing'),
        FieldPanel('tags', widget=CheckboxSelectMultiple)
    ]

    edit_handler = make_translated_interface(
        content_panels=content_panels,
        settings_panels=settings_panels
    )


class InternationalCampaignPagePanels:

    content_panels = [
        MultiFieldPanel(
            heading='Hero section',
            children=[
                FieldPanel('campaign_heading'),
                FieldPanel('campaign_subheading'),
                FieldPanel('campaign_teaser'),
                ImageChooserPanel('campaign_hero_image'),
            ]
        ),
        MultiFieldPanel(
            heading='Section one',
            children=[
                FieldPanel('section_one_heading'),
                FieldPanel('section_one_intro'),
                ImageChooserPanel('section_one_image'),
                FieldRowPanel([
                    MultiFieldPanel(
                        children=[
                            ImageChooserPanel('selling_point_one_icon'),
                            FieldPanel('selling_point_one_heading'),
                            FieldPanel('selling_point_one_content'),
                        ]
                    ),
                    MultiFieldPanel(
                        children=[
                            ImageChooserPanel('selling_point_two_icon'),
                            FieldPanel('selling_point_two_heading'),
                            FieldPanel('selling_point_two_content'),
                        ]
                    ),
                    MultiFieldPanel(
                        children=[
                            ImageChooserPanel('selling_point_three_icon'),
                            FieldPanel('selling_point_three_heading'),
                            FieldPanel('selling_point_three_content'),
                        ]
                    ),
                ]),
                FieldRowPanel([
                    FieldPanel('section_one_contact_button_text'),
                    FieldPanel('section_one_contact_button_url'),
                ])
            ]
        ),
        MultiFieldPanel(
            heading='Section two',
            children=[
                FieldPanel('section_two_heading'),
                FieldPanel('section_two_intro'),
                ImageChooserPanel('section_two_image'),
                FieldRowPanel([
                    FieldPanel('section_two_contact_button_text'),
                    FieldPanel('section_two_contact_button_url'),
                ])
            ]
        ),
        MultiFieldPanel(
            heading='Related content section',
            children=[
                FieldPanel('related_content_heading'),
                FieldPanel('related_content_intro'),
                FieldRowPanel([
                    PageChooserPanel(
                        'related_page_one',
                        'great_international.InternationalArticlePage'),
                    PageChooserPanel(
                        'related_page_two',
                        'great_international.InternationalArticlePage'),
                    PageChooserPanel(
                        'related_page_three',
                        'great_international.InternationalArticlePage'),
                ])
            ]
        ),
        MultiFieldPanel(
            heading='Contact box',
            children=[
                FieldRowPanel([
                    FieldPanel('cta_box_message', widget=Textarea),
                    MultiFieldPanel([
                        FieldPanel('cta_box_button_url'),
                        FieldPanel('cta_box_button_text'),
                    ])
                ])
            ]
        ),
        SearchEngineOptimisationPanel(),
    ]

    settings_panels = [
        FieldPanel('title_en_gb'),
        FieldPanel('slug'),
        FieldPanel('uses_tree_based_routing'),
        FieldPanel('tags', widget=CheckboxSelectMultiple)
    ]

    edit_handler = make_translated_interface(
        content_panels=content_panels,
        settings_panels=settings_panels
    )


class InternationalTopicLandingPagePanels:

    content_panels = [
        FieldPanel('landing_page_title'),
        MultiFieldPanel(
            heading='Hero',
            children=[
                ImageChooserPanel('hero_image'),
                FieldPanel('hero_teaser')
            ]
        ),
        SearchEngineOptimisationPanel(),
    ]

    settings_panels = [
        FieldPanel('title_en_gb'),
        FieldPanel('slug'),
        FieldPanel('uses_tree_based_routing'),
        FieldPanel('tags', widget=CheckboxSelectMultiple)
    ]

    edit_handler = make_translated_interface(
        content_panels=content_panels,
        settings_panels=settings_panels
    )


class InternationalCuratedTopicLandingPagePanels:

    content_panels = [
        FieldPanel('display_title'),
        ImageChooserPanel('hero_image'),
        FieldPanel('teaser'),
        MultiFieldPanel(
            heading="featured content section",
            children=[
                FieldPanel('feature_section_heading'),
                FieldRowPanel([
                    MultiFieldPanel([
                        FieldPanel('feature_one_heading'),
                        ImageChooserPanel('feature_one_image'),
                        FieldPanel('feature_one_content'),
                    ]),
                    MultiFieldPanel([
                        FieldPanel('feature_two_heading'),
                        ImageChooserPanel('feature_two_image'),
                        FieldPanel('feature_two_content'),
                    ]),
                ]),
                FieldRowPanel([
                    MultiFieldPanel([
                        FieldPanel('feature_three_heading'),
                        ImageChooserPanel('feature_three_image'),
                        FieldPanel('feature_three_url'),
                    ]),
                    MultiFieldPanel([
                        FieldPanel('feature_four_heading'),
                        ImageChooserPanel('feature_four_image'),
                        FieldPanel('feature_four_url'),
                    ]),
                    MultiFieldPanel([
                        FieldPanel('feature_five_heading'),
                        ImageChooserPanel('feature_five_image'),
                        FieldPanel('feature_five_url'),
                    ]),
                ]),
            ]
        )
    ]

    settings_panels = [
        FieldPanel('title_en_gb'),
        SearchEngineOptimisationPanel(),
        FieldPanel('slug'),
        FieldPanel('uses_tree_based_routing'),
        FieldPanel('tags', widget=CheckboxSelectMultiple)
    ]

    edit_handler = make_translated_interface(
        content_panels=content_panels,
        settings_panels=settings_panels
    )


class InternationalGuideLandingPagePanels:

    content_panels = [
        FieldPanel('display_title'),
        ImageChooserPanel('hero_image'),
        FieldPanel('teaser'),
        MultiFieldPanel(
            heading="Attractive features",
            children=[
                FieldPanel('section_one_content'),
                HelpPanel(
                    'For accessibility reasons, use only '
                    '"#### [Your text here]" for subheadings '
                    'in this markdown field'
                ),
                ImageChooserPanel('section_one_image'),
                FieldPanel('section_one_image_caption'),
            ]
        ),
        MultiFieldPanel(
            heading="Feature banner",
            children=[
                FieldPanel('section_two_heading'),
                FieldPanel('section_two_teaser'),
                FieldPanel('section_two_button_text'),
                FieldPanel('section_two_button_url'),
                ImageChooserPanel('section_two_image'),
            ]
        ),
        MultiFieldPanel(
            heading="Guides section",
            children=[
                FieldPanel('guides_section_heading'),
            ]
        ),
        MultiFieldPanel(
            heading="Section three",
            children=[
                FieldPanel('section_three_title'),
                FieldPanel('section_three_text'),
                FieldPanel('section_three_cta_text'),
                FieldPanel('section_three_cta_link'),
            ]
        )
    ]

    settings_panels = [
        FieldPanel('title_en_gb'),
        SearchEngineOptimisationPanel(),
        FieldPanel('slug'),
        FieldPanel('uses_tree_based_routing'),
        FieldPanel('tags', widget=CheckboxSelectMultiple)
    ]

    edit_handler = make_translated_interface(
        content_panels=content_panels,
        settings_panels=settings_panels
    )


class InternationalEUExitFormPagePanels:

    content_panels_before_form = [
        MultiFieldPanel(
            heading='Hero',
            children=[
                FieldPanel('breadcrumbs_label'),
                FieldPanel('heading'),
                FieldPanel('body_text'),
            ]
        ),
    ]
    content_panels_after_form = [
        FieldPanel('disclaimer', widget=Textarea),
        FieldPanel('submit_button_text'),
        SearchEngineOptimisationPanel(),
    ]

    settings_panels = [
        FieldPanel('title_en_gb'),
        FieldPanel('slug'),
    ]


class InternationalEUExitFormSuccessPagePanels:

    content_panels = [
        FieldPanel('breadcrumbs_label'),
        MultiFieldPanel(
            heading='heading',
            children=[
                FieldPanel('heading'),
                FieldPanel('body_text'),
            ]
        ),
        MultiFieldPanel(
            heading='Next steps',
            children=[
                FieldPanel('next_title'),
                FieldPanel('next_body_text'),
            ]
        ),
        SearchEngineOptimisationPanel(),
    ]

    settings_panels = [
        FieldPanel('title_en_gb'),
        FieldPanel('slug'),
    ]
