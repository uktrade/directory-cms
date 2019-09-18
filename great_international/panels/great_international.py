from django.forms import Textarea, CheckboxSelectMultiple, Select

from wagtail.admin.edit_handlers import (
    InlinePanel, HelpPanel, FieldPanel, FieldRowPanel, MultiFieldPanel,
    PageChooserPanel, ObjectList
)
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.documents.edit_handlers import DocumentChooserPanel
from wagtailmedia.widgets import AdminMediaChooser

from core.helpers import make_translated_interface
from core.panels import SearchEngineOptimisationPanel


class InternationalHomePagePanels:

    content_panels = [
        FieldPanel('title'),
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
        FieldPanel('brexit_banner_text'),
        MultiFieldPanel(
            heading="Old International Home Page",
            classname="collapsible collapsed",
            children=[
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
                        ]),
                        FieldRowPanel([
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
            ]
        ),
        FieldPanel('is_new_page_ready'),
        MultiFieldPanel(
            heading="Ready to trade stories",
            children=[
                HelpPanel('At least one ready to trade story is required for this section to show'),
                FieldPanel('ready_to_trade_story_one'),
                FieldPanel('ready_to_trade_story_two'),
                FieldPanel('ready_to_trade_story_three'),
            ],
        ),
        MultiFieldPanel(
            heading="Benefits of the UK section",
            children=[
                HelpPanel('A title and at least one benefit text is required for this section to show'),
                FieldPanel('benefits_of_uk_title'),
                FieldPanel('benefits_of_uk_intro'),
                FieldRowPanel([
                    FieldPanel('benefits_of_uk_one'),
                    FieldPanel('benefits_of_uk_two'),
                    FieldPanel('benefits_of_uk_three'),
                ]),
                FieldRowPanel([
                    FieldPanel('benefits_of_uk_four'),
                    FieldPanel('benefits_of_uk_five'),
                    FieldPanel('benefits_of_uk_six'),
                ]),
            ],
        ),

        MultiFieldPanel(
            heading="Ready for brexit section",
            children=[
                HelpPanel('A title, cta text and cta link are required for this section to show'),
                FieldPanel('ready_for_brexit_title'),
                ImageChooserPanel('ready_for_brexit_image'),
                FieldPanel('ready_for_brexit_cta_text'),
                FieldPanel('ready_for_brexit_cta_link'),
            ]
        ),
        MultiFieldPanel(
            heading="How we help",
            children=[
                HelpPanel('A title and at least one how we help with an icon and text is required for this section to show'),  # NOQA
                FieldPanel('how_we_help_title'),
                FieldPanel('how_we_help_intro'),
                FieldRowPanel([
                    MultiFieldPanel([
                        ImageChooserPanel('how_we_help_one_icon'),
                        FieldPanel('how_we_help_one_text')
                    ]),
                    MultiFieldPanel([
                        ImageChooserPanel('how_we_help_two_icon'),
                        FieldPanel('how_we_help_two_text')
                    ]),
                    MultiFieldPanel([
                        ImageChooserPanel('how_we_help_three_icon'),
                        FieldPanel('how_we_help_three_text')
                    ]),
                ])
            ]
        ),
        MultiFieldPanel(
            heading="Ways of doing business section",
            children=[
                HelpPanel('A title and at least one related page is required for this section to show'),
                FieldPanel('ways_of_doing_business_title'),
                FieldRowPanel([
                    MultiFieldPanel([
                        PageChooserPanel(
                            'related_page_expand',
                            'great_international.InvestInternationalHomePage'
                        ),
                        FieldPanel('related_page_expand_description')
                    ]),
                    MultiFieldPanel([
                        PageChooserPanel(
                            'related_page_invest_capital',
                            'great_international.InternationalCapitalInvestLandingPage'
                        ),
                        FieldPanel('related_page_invest_capital_description')
                    ]),
                    MultiFieldPanel([
                        PageChooserPanel(
                            'related_page_buy',
                            'great_international.InternationalTradeHomePage'
                        ),
                        FieldPanel('related_page_buy_description')
                    ]),
                ])
            ],
        ),
        MultiFieldPanel(
            heading="Case study",
            children=[
                HelpPanel('Required fields for section to show: Case Study Image, Case Study Title'),
                ImageChooserPanel('case_study_image'),
                FieldPanel('case_study_title'),
                FieldPanel('case_study_text'),
                FieldPanel('case_study_cta_text'),
                FieldPanel('case_study_cta_link'),
            ]
        ),
        MultiFieldPanel(
            heading="Industries section",
            children=[
                HelpPanel('A title and a sector in the active language with a featured description '
                          'is required for this section to show'),
                FieldPanel('industries_section_title'),
                FieldPanel('industries_section_intro'),
                FieldPanel('industries_section_industry_label'),
                FieldPanel('industries_section_cta_text'),
                FieldPanel('industries_section_cta_link'),
            ]
        ),
        MultiFieldPanel(
            heading="Link to section",
            children=[
                HelpPanel('A title and at least one link to section is required for this section to show'),
                FieldPanel('link_to_section_title'),
                FieldPanel('link_to_section_intro'),
                FieldRowPanel([
                    MultiFieldPanel([
                        FieldPanel('link_to_section_one'),
                        FieldPanel('link_to_section_one_cta_text'),
                        FieldPanel('link_to_section_one_cta_link'),
                    ]),
                    MultiFieldPanel([
                        FieldPanel('link_to_section_two'),
                        FieldPanel('link_to_section_two_cta_text'),
                        FieldPanel('link_to_section_two_cta_link'),
                    ]),
                    MultiFieldPanel([
                        FieldPanel('link_to_section_three'),
                        FieldPanel('link_to_section_three_cta_text'),
                        FieldPanel('link_to_section_three_cta_link'),
                    ]),
                ])
            ]
        ),
        SearchEngineOptimisationPanel(),
    ]

    settings_panels = [
        FieldPanel('slug'),
    ]

    edit_handler = make_translated_interface(
        content_panels=content_panels,
        settings_panels=settings_panels
    )


class BaseInternationalSectorPagePanels:

    content_panels = [
        FieldPanel('title'),
        MultiFieldPanel(
            heading='Heading',
            children=[
                FieldPanel('heading'),
                FieldPanel('sub_heading'),
                ImageChooserPanel('hero_image'),
                FieldPanel('heading_teaser'),
                FieldPanel('featured_description')
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
                HelpPanel('Up to 3 random opportunities that are related '
                          'to this sector will appear here.'),
                FieldPanel('related_opportunities_cta_text'),
                FieldPanel('related_opportunities_cta_link')
            ]
        ),
        SearchEngineOptimisationPanel()
    ]

    settings_panels = [
        FieldPanel('slug'),
        FieldPanel('tags', widget=CheckboxSelectMultiple)
    ]

    edit_handler = make_translated_interface(
        content_panels=content_panels,
        settings_panels=settings_panels
    )


class InternationalArticlePagePanels:

    content_panels = [
        FieldPanel('title'),
        FieldPanel('article_title'),
        MultiFieldPanel(
            heading='Article content',
            children=[
                FieldPanel('article_subheading'),
                FieldPanel('article_teaser'),
                FieldPanel('article_body_text')
            ]
        ),
        MultiFieldPanel(
            heading='CTA fields',
            children=[
                FieldPanel('cta_title'),
                FieldPanel('cta_teaser'),
                FieldPanel('cta_link_label'),
                FieldPanel('cta_link'),
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

    image_panels = [
        ImageChooserPanel('article_image'),
        FieldPanel('article_video', widget=AdminMediaChooser),
    ]

    settings_panels = [
        FieldPanel('type_of_article', widget=Select),
        FieldPanel('slug'),
        FieldPanel('tags', widget=CheckboxSelectMultiple)
    ]

    edit_handler = make_translated_interface(
        content_panels=content_panels,
        settings_panels=settings_panels,
        other_panels=[
            ObjectList(image_panels, heading='Images')
        ],
    )


class InternationalArticleListingPagePanels:

    content_panels = [
        FieldPanel('title'),
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
        FieldPanel('slug'),
        FieldPanel('tags', widget=CheckboxSelectMultiple)
    ]

    edit_handler = make_translated_interface(
        content_panels=content_panels,
        settings_panels=settings_panels
    )


class InternationalCampaignPagePanels:

    content_panels = [
        FieldPanel('title'),
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
        FieldPanel('slug'),
        FieldPanel('tags', widget=CheckboxSelectMultiple)
    ]

    edit_handler = make_translated_interface(
        content_panels=content_panels,
        settings_panels=settings_panels
    )


class InternationalTopicLandingPagePanels:

    content_panels = [
        FieldPanel('title'),
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
        FieldPanel('slug'),
        FieldPanel('tags', widget=CheckboxSelectMultiple)
    ]

    edit_handler = make_translated_interface(
        content_panels=content_panels,
        settings_panels=settings_panels
    )


class InternationalCuratedTopicLandingPagePanels:

    content_panels = [
        FieldPanel('title'),
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
        ),
        SearchEngineOptimisationPanel()
    ]

    settings_panels = [
        SearchEngineOptimisationPanel(),
        FieldPanel('slug'),
        FieldPanel('tags', widget=CheckboxSelectMultiple)
    ]

    edit_handler = make_translated_interface(
        content_panels=content_panels,
        settings_panels=settings_panels
    )


class InternationalGuideLandingPagePanels:

    content_panels = [
        FieldPanel('title'),
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
        ),
        SearchEngineOptimisationPanel()
    ]

    settings_panels = [
        SearchEngineOptimisationPanel(),
        FieldPanel('slug'),
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


class AboutDitLandingPagePanels:

    content_panels = [
        FieldPanel('breadcrumbs_label'),
        MultiFieldPanel(
            heading="Hero",
            children=[
                FieldPanel('title'),
                FieldPanel('hero_title'),
                ImageChooserPanel('hero_image'),
            ],
        ),
        MultiFieldPanel(
            heading="Intro",
            classname='collapsible',
            children=[
                FieldPanel('intro')
            ],
        ),
        MultiFieldPanel(
            heading="Section one",
            classname='collapsible',
            children=[
                HelpPanel('Required for section to show: Section one content'),
                FieldPanel('section_one_content'),
                ImageChooserPanel('section_one_image'),
            ],
        ),
        MultiFieldPanel(
            heading="Related pages",
            classname='collapsible',
            children=[
                HelpPanel('Required for section to show: title and at least one related page'),
                FieldPanel('how_dit_help_title'),
                FieldRowPanel([
                    MultiFieldPanel([
                        PageChooserPanel(
                            'related_page_one',
                            'great_international.AboutDitServicesPage'
                        ),
                    ]),
                    MultiFieldPanel([
                        PageChooserPanel(
                            'related_page_two',
                            'great_international.AboutDitServicesPage'
                        ),
                    ]),
                    MultiFieldPanel([
                       PageChooserPanel(
                           'related_page_three',
                           'great_international.AboutDitServicesPage'
                       ),
                    ]),
                ]),
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
                HelpPanel('CTAs require both text and a link to show '
                          'on page. '),
                FieldPanel('case_study_cta_text'),
                FieldPanel('case_study_cta_link'),
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


class AboutDitServiceFieldPanels:

    panels = [
        MultiFieldPanel([
            ImageChooserPanel('icon'),
            FieldPanel('title'),
            FieldPanel('summary'),
            FieldPanel('link_text'),
            FieldPanel('link_url'),
        ]),
    ]


class AboutDitServicesPagePanels:

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
        MultiFieldPanel(
            heading="Teaser",
            children=[
                HelpPanel('At least one field required for section to show'),
                FieldPanel('teaser'),
                ImageChooserPanel('teaser_image'),
            ],
        ),
        FieldPanel('featured_description'),
        MultiFieldPanel(
            heading="Services section",
            classname='collapsible',
            children=[
                InlinePanel(
                    'about_dit_services_fields',
                    label="About DIT services"
                )
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
                HelpPanel('CTAs require both text and a link to show '
                          'on page. '),
                FieldPanel('case_study_cta_text'),
                FieldPanel('case_study_cta_link'),
            ],
        ),
        MultiFieldPanel(
            heading="Contact Section",
            classname='collapsible',
            children=[
                HelpPanel('Required fields for section to show: '
                          'Title, Summary'),
                FieldPanel('contact_us_section_title'),
                FieldPanel('contact_us_section_summary'),
                HelpPanel('CTAs require both text and a link to show '
                          'on page. '),
                FieldPanel('contact_us_section_cta_text'),
                FieldPanel('contact_us_section_cta_link'),
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


class AboutUkLandingPagePanels:

    image_panels = [
        ImageChooserPanel('hero_image'),
        ImageChooserPanel('why_choose_uk_image'),
        MultiFieldPanel(
            heading="How we help images",
            children=[
                ImageChooserPanel('how_we_help_one_icon'),
                ImageChooserPanel('how_we_help_two_icon'),
                ImageChooserPanel('how_we_help_three_icon'),
                ImageChooserPanel('how_we_help_four_icon'),
                ImageChooserPanel('how_we_help_five_icon'),
                ImageChooserPanel('how_we_help_six_icon'),
            ]),
        ImageChooserPanel('ebook_section_image'),
    ]

    content_panels = [
        FieldPanel('title'),
        FieldPanel('breadcrumbs_label'),
        MultiFieldPanel(
            heading="Hero",
            children=[
                FieldPanel('hero_title'),
            ],
        ),
        FieldPanel('intro'),
        MultiFieldPanel(
            heading="Why choose the UK section",
            classname="collapsible",
            children=[
                FieldPanel('why_choose_uk_title'),
                FieldPanel('why_choose_uk_content'),
                FieldPanel('why_choose_uk_cta_text'),
                FieldPanel('why_choose_uk_cta_link'),
            ]
        ),
        MultiFieldPanel(
            heading="Key Industries section",
            classname="collapsible",
            children=[
                FieldPanel('industries_section_title'),
                FieldPanel('industries_section_intro'),
                FieldPanel('industries_section_cta_text'),
                FieldPanel('industries_section_cta_link')
            ]
        ),
        MultiFieldPanel(
            heading="UK's regions section",
            classname="collapsible",
            children=[
                FieldPanel('regions_section_title'),
                FieldPanel('regions_section_intro'),
                FieldRowPanel([
                    MultiFieldPanel([
                        PageChooserPanel(
                            'scotland',
                            ['great_international.AboutUkRegionPage', 'great_international.InvestRegionPage']
                        ),
                        FieldPanel('scotland_text')
                    ]),
                    MultiFieldPanel([
                        PageChooserPanel(
                            'northern_ireland',
                            ['great_international.AboutUkRegionPage', 'great_international.InvestRegionPage']
                        ),
                        FieldPanel('northern_ireland_text')
                    ]),
                    MultiFieldPanel([
                        PageChooserPanel(
                            'north_england',
                            ['great_international.AboutUkRegionPage', 'great_international.InvestRegionPage']
                        ),
                        FieldPanel('north_england_text')
                    ]),
                ]),
                FieldRowPanel([
                    MultiFieldPanel([
                        PageChooserPanel(
                            'wales',
                            ['great_international.AboutUkRegionPage', 'great_international.InvestRegionPage']
                        ),
                        FieldPanel('wales_text')
                    ]),
                    MultiFieldPanel([
                        PageChooserPanel(
                            'midlands',
                            ['great_international.AboutUkRegionPage', 'great_international.InvestRegionPage']
                        ),
                        FieldPanel('midlands_text')
                    ]),
                    MultiFieldPanel([
                        PageChooserPanel(
                            'south_england',
                            ['great_international.AboutUkRegionPage', 'great_international.InvestRegionPage']
                        ),
                        FieldPanel('south_england_text')
                    ]),
                ]),
                FieldPanel('regions_section_cta_text'),
                FieldPanel('regions_section_cta_link'),
            ]
        ),
        MultiFieldPanel(
            heading="How we help section",
            classname="collapsible",
            children=[
                FieldPanel('how_we_help_title'),
                FieldPanel('how_we_help_intro'),
                FieldRowPanel([
                    MultiFieldPanel([
                        FieldPanel('how_we_help_one_title'),
                        FieldPanel('how_we_help_one_text')
                    ]),
                    MultiFieldPanel([
                        FieldPanel('how_we_help_two_title'),
                        FieldPanel('how_we_help_two_text')
                    ]),
                    MultiFieldPanel([
                        FieldPanel('how_we_help_three_title'),
                        FieldPanel('how_we_help_three_text')
                    ]),
                ]),
                FieldRowPanel([
                    MultiFieldPanel([
                        FieldPanel('how_we_help_four_title'),
                        FieldPanel('how_we_help_four_text')
                    ]),
                    MultiFieldPanel([
                        FieldPanel('how_we_help_five_title'),
                        FieldPanel('how_we_help_five_text')
                    ]),
                    MultiFieldPanel([
                        FieldPanel('how_we_help_six_title'),
                        FieldPanel('how_we_help_six_text')
                    ]),
                ]),
                FieldPanel('how_we_help_cta_text'),
                FieldPanel('how_we_help_cta_link')
            ]
        ),
        MultiFieldPanel(
            heading="EBook section",
            classname='collapsible',
            children=[
                HelpPanel('Required fields for section to show: title, body'),
                FieldRowPanel([
                    FieldPanel('ebook_section_image_alt_text')
                ]),
                MultiFieldPanel([
                    FieldPanel('ebook_section_title'),
                    FieldPanel('ebook_section_body'),
                    HelpPanel('CTAs require both text and a link to show '
                              'on page. '),
                    FieldPanel('ebook_section_cta_text'),
                    DocumentChooserPanel('ebook_section_cta_link'),
                ]),
            ]
        ),
        MultiFieldPanel(
            heading="Contact us section",
            classname="collapsible",
            children=[
                FieldPanel('contact_title'),
                FieldPanel('contact_text'),
                FieldPanel('contact_cta_text'),
                FieldPanel('contact_cta_link'),
            ]
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


class AboutUkRegionListingPagePanels:
    image_panels = [
        ImageChooserPanel('hero_image'),
    ]

    content_panels = [
        FieldPanel('title'),
        FieldPanel('breadcrumbs_label'),
        MultiFieldPanel(
            heading="Hero",
            children=[
                FieldPanel('hero_title'),
            ],
        ),
        FieldPanel('intro'),
        MultiFieldPanel(
            heading="Contact us section",
            classname="collapsible",
            children=[
                FieldPanel('contact_title'),
                FieldPanel('contact_text'),
                FieldPanel('contact_cta_text'),
                FieldPanel('contact_cta_link'),
            ]
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


class AboutUkRegionPagePanels:

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


class AboutUkArticleFieldPanels:

    panels = [
        MultiFieldPanel([
            ImageChooserPanel('image'),
            FieldPanel('title'),
            FieldPanel('summary'),
            HelpPanel('Both link text and link URL required for link to show'),
            FieldPanel('link_text'),
            FieldPanel('link_url'),
        ]),
    ]


class AboutUkWhyChooseTheUkPagePanels:

    content_panels = [
        FieldPanel('title'),
        FieldPanel('breadcrumbs_label'),
        MultiFieldPanel(
            heading="Hero",
            children=[
                HelpPanel('The hero title no longer shows, use this as alt text for the hero image which includes '
                          'the text heading'),
                FieldPanel('hero_title'),
                ImageChooserPanel('hero_image'),
            ],
        ),
        MultiFieldPanel(
            heading="Teaser",
            children=[
                FieldPanel('teaser'),
                FieldPanel('primary_contact_cta_text'),
                FieldPanel('primary_contact_cta_link')
            ],
        ),
        MultiFieldPanel(
            heading="Section 1",
            classname='collapsible',
            children=[
                HelpPanel('At least one field required for section to show'),
                FieldRowPanel([
                    FieldPanel('section_one_body'),
                    MultiFieldPanel([
                        ImageChooserPanel('section_one_image'),
                        FieldPanel('section_one_video', widget=AdminMediaChooser)
                    ])
                ])
            ],
        ),
        MultiFieldPanel(
            heading='Statistics',
            classname='collapsible',
            children=[
                FieldRowPanel(
                    [
                        MultiFieldPanel(
                            [
                                FieldPanel('statistic_1_heading'),
                                FieldPanel('statistic_1_number'),
                                FieldPanel('statistic_1_smallprint')
                            ]
                        ),
                        MultiFieldPanel(
                            [
                                FieldPanel('statistic_2_heading'),
                                FieldPanel('statistic_2_number'),
                                FieldPanel('statistic_2_smallprint')
                            ]
                        ),
                        MultiFieldPanel(
                            [
                                FieldPanel('statistic_3_heading'),
                                FieldPanel('statistic_3_number'),
                                FieldPanel('statistic_3_smallprint')
                            ]
                        ),
                        MultiFieldPanel(
                            [
                                FieldPanel('statistic_4_heading'),
                                FieldPanel('statistic_4_number'),
                                FieldPanel('statistic_4_smallprint')
                            ]
                        ),
                        MultiFieldPanel(
                            [
                                FieldPanel('statistic_5_heading'),
                                FieldPanel('statistic_5_number'),
                                FieldPanel('statistic_5_smallprint')
                            ]
                        ),
                        MultiFieldPanel(
                            [
                                FieldPanel('statistic_6_heading'),
                                FieldPanel('statistic_6_number'),
                                FieldPanel('statistic_6_smallprint')
                            ]
                        ),
                    ]
                )
            ]
        ),
        MultiFieldPanel(
            heading="Articles section",
            classname='collapsible',
            children=[
                InlinePanel(
                    'about_uk_articles_fields',
                    label="About UK articles"
                )
            ]
        ),
        MultiFieldPanel(
            heading="EBook section",
            classname='collapsible',
            children=[
                HelpPanel('Required fields for section to show: title, body'),
                FieldRowPanel([
                    ImageChooserPanel('ebook_section_image'),
                    FieldPanel('ebook_section_image_alt_text')
                ]),
                MultiFieldPanel([
                    FieldPanel('ebook_section_title'),
                    FieldPanel('ebook_section_body'),
                    HelpPanel('CTAs require both text and a link to show on page.'),
                    FieldPanel('ebook_section_cta_text'),
                    FieldPanel('ebook_section_cta_link'),
                ]),
            ]
        ),
        MultiFieldPanel(
            heading="Related pages",
            classname='collapsible',
            children=[
                HelpPanel('Required for section to show: title and at least one related page'),
                FieldPanel('how_dit_help_title'),
                FieldRowPanel([
                    MultiFieldPanel([
                        PageChooserPanel(
                            'related_page_one',
                            'great_international.AboutDitServicesPage'
                        ),
                    ]),
                    MultiFieldPanel([
                        PageChooserPanel(
                            'related_page_two',
                            'great_international.AboutDitServicesPage'
                        ),
                    ]),
                    MultiFieldPanel([
                       PageChooserPanel(
                           'related_page_three',
                           'great_international.AboutDitServicesPage'
                       ),
                    ]),
                ]),
            ],
        ),
        MultiFieldPanel(
            heading="Contact Section",
            classname='collapsible',
            children=[
                HelpPanel('Required fields for section to show: '
                          'Title, Summary'),
                FieldPanel('contact_us_section_title'),
                FieldPanel('contact_us_section_summary'),
                HelpPanel('CTAs require both text and a link to show '
                          'on page. '),
                FieldPanel('contact_us_section_cta_text'),
                FieldPanel('contact_us_section_cta_link'),
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
