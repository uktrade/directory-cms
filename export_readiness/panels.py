from django.forms import CheckboxSelectMultiple, Textarea, Select

from wagtail.admin.edit_handlers import (
    FieldPanel, FieldRowPanel, MultiFieldPanel, PageChooserPanel, HelpPanel, StreamFieldPanel)
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtailmedia.widgets import AdminMediaChooser

from core.panels import SearchEngineOptimisationPanel

ACCORDION_FIELDS_HELP_TEXT = (
    'To be displayed, this industry needs at least: a title, a teaser, '
    '2 bullet points, and 2 calls to action (CTAs).')


class TermsAndConditionsPagePanels:

    content_panels = [
        MultiFieldPanel(
            heading='Terms and conditions',
            children=[
                FieldPanel('body'),
            ]
        ),
        SearchEngineOptimisationPanel(),
    ]

    settings_panels = [
        FieldPanel('title_en_gb'),
        FieldPanel('slug'),
    ]


class PrivacyAndCookiesPagePanels:

    content_panels = [
        MultiFieldPanel(
            heading='Privacy and cookies',
            children=[
                FieldPanel('body'),
            ]
        ),
        SearchEngineOptimisationPanel(),
    ]

    settings_panels = [
        FieldPanel('title_en_gb'),
        FieldPanel('slug'),
    ]

    promote_panels = []


class GetFinancePagePanels:

    content_panels = [
        FieldPanel('breadcrumbs_label'),
        MultiFieldPanel(
            heading='Banner',
            children=[
                ImageChooserPanel('hero_image'),
                FieldPanel('hero_text'),
                ImageChooserPanel('ukef_logo'),
            ]
        ),
        MultiFieldPanel(
            heading='Contact us',
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
            heading='Advantages',
            children=[
                FieldPanel('advantages_title'),
                FieldRowPanel(
                    children=[
                        ImageChooserPanel('advantages_one_icon'),
                        ImageChooserPanel('advantages_two_icon'),
                        ImageChooserPanel('advantages_three_icon'),
                    ]
                ),
                FieldRowPanel(
                    children=[
                        FieldPanel('advantages_one'),
                        FieldPanel('advantages_two'),
                        FieldPanel('advantages_three'),
                    ]
                )
            ]
        ),
        MultiFieldPanel(
            heading='Evidence',
            children=[
                FieldRowPanel(
                    children=[
                        FieldPanel('evidence'),
                        FieldPanel(
                            'evidence_video',
                            widget=AdminMediaChooser,
                        ),
                    ]
                )
            ]
        ),
        SearchEngineOptimisationPanel(),
    ]

    settings_panels = [
        FieldPanel('title_en_gb'),
        FieldPanel('slug'),
    ]


class PerformanceDashboardPagePanels:

    content_panels = [
        MultiFieldPanel(
            heading='Heading and description',
            children=[
                FieldPanel('description'),
                FieldPanel('product_link', widget=Select),
            ]
        ),
        FieldRowPanel(
            heading='Data columns',
            children=[
                MultiFieldPanel(
                    heading='Data row 1',
                    children=[
                        FieldPanel('data_title_row_one'),
                        FieldPanel('data_number_row_one'),
                        FieldPanel('data_period_row_one'),
                        FieldPanel('data_description_row_one'),
                    ]
                ),
                MultiFieldPanel(
                    heading='Data row 2',
                    children=[
                        FieldPanel('data_title_row_two'),
                        FieldPanel('data_number_row_two'),
                        FieldPanel('data_period_row_two'),
                        FieldPanel('data_description_row_two'),
                    ]
                ),
                MultiFieldPanel(
                    heading='Data row 3',
                    children=[
                        FieldPanel('data_title_row_three'),
                        FieldPanel('data_number_row_three'),
                        FieldPanel('data_period_row_three'),
                        FieldPanel('data_description_row_three'),
                    ]
                ),
                MultiFieldPanel(
                    heading='Data row 4',
                    children=[
                        FieldPanel('data_title_row_four'),
                        FieldPanel('data_number_row_four'),
                        FieldPanel('data_period_row_four'),
                        FieldPanel('data_description_row_four'),
                    ]
                ),
            ]
        ),
        FieldPanel('guidance_notes'),
    ]


class PerformanceDashboardNotesPagePanels:

    content_panels = [
        MultiFieldPanel(
            heading='Performance dashboard notes',
            children=[
                FieldPanel('body'),
            ]
        ),
        SearchEngineOptimisationPanel(),
    ]

    settings_panels = [
        FieldPanel('title_en_gb'),
        FieldPanel('slug'),
    ]

    promote_panels = []


class TopicLandingPagePanels:

    content_panels = [
        FieldPanel('landing_page_title'),
        MultiFieldPanel(
            heading='Hero',
            children=[
                ImageChooserPanel('hero_image'),
                FieldPanel('hero_teaser')
            ]
        ),
        FieldPanel('banner_text',
                   help_text='Use this field to change the text displayed in '
                             'the banner, if the page has one.'),
        FieldPanel('teaser'),
        SearchEngineOptimisationPanel(),
    ]

    settings_panels = [
        FieldPanel('title_en_gb'),
        FieldPanel('slug'),
    ]


class ArticleListingPagePanels:

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
    ]


class CountryGuidePagePanels:

    content_panels = [
        MultiFieldPanel(
            heading='Heading and introduction',
            children=[
                FieldPanel('heading'),
                FieldPanel('sub_heading'),
                ImageChooserPanel('hero_image'),
                FieldPanel('heading_teaser'),
                FieldRowPanel([
                    MultiFieldPanel([
                        FieldPanel('intro_cta_one_link'),
                        FieldPanel('intro_cta_one_title'),
                    ]),
                    MultiFieldPanel([
                        FieldPanel('intro_cta_two_link'),
                        FieldPanel('intro_cta_two_title'),
                    ]),
                    MultiFieldPanel([
                        FieldPanel('intro_cta_three_link'),
                        FieldPanel('intro_cta_three_title'),
                    ])
                ]),
            ]

        ),
        MultiFieldPanel(
            heading='Unique selling points of the market for UK exporters',
            children=[
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
            classname='collapsible',
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
            heading='Highlights',
            children=[
                FieldPanel('section_two_heading'),
                FieldPanel('section_two_teaser')
            ]
        ),
        MultiFieldPanel(
            heading='Industry one',
            classname='collapsible collapsed',
            children=[
                HelpPanel(
                    content=ACCORDION_FIELDS_HELP_TEXT,
                    classname='help-panel-font-large'
                ),
                ImageChooserPanel('accordion_1_icon'),
                FieldPanel('accordion_1_title'),
                FieldPanel('accordion_1_teaser'),
                FieldRowPanel([
                    MultiFieldPanel(
                        [
                            ImageChooserPanel('accordion_1_subsection_1_icon'),
                            FieldPanel('accordion_1_subsection_1_heading'),
                            FieldPanel('accordion_1_subsection_1_body'),
                        ]
                    ),
                    MultiFieldPanel(
                        [
                            ImageChooserPanel('accordion_1_subsection_2_icon'),
                            FieldPanel('accordion_1_subsection_2_heading'),
                            FieldPanel('accordion_1_subsection_2_body'),
                        ]
                    ),
                    MultiFieldPanel(
                        [
                            ImageChooserPanel('accordion_1_subsection_3_icon'),
                            FieldPanel('accordion_1_subsection_3_heading'),
                            FieldPanel('accordion_1_subsection_3_body'),
                        ]
                    )
                ]),
                MultiFieldPanel([
                    ImageChooserPanel('accordion_1_case_study_hero_image'),
                    FieldPanel('accordion_1_case_study_button_text'),
                    FieldPanel('accordion_1_case_study_button_link'),
                    FieldPanel('accordion_1_case_study_title'),
                    FieldPanel('accordion_1_case_study_description')
                ]),
                FieldRowPanel([
                    MultiFieldPanel(
                        [
                            FieldPanel('accordion_1_statistic_1_number'),
                            FieldPanel('accordion_1_statistic_1_heading'),
                            FieldPanel('accordion_1_statistic_1_smallprint')
                        ]
                    ),
                    MultiFieldPanel(
                        [
                            FieldPanel('accordion_1_statistic_2_number'),
                            FieldPanel('accordion_1_statistic_2_heading'),
                            FieldPanel('accordion_1_statistic_2_smallprint')
                        ]
                    ),
                    MultiFieldPanel(
                        [
                            FieldPanel('accordion_1_statistic_3_number'),
                            FieldPanel('accordion_1_statistic_3_heading'),
                            FieldPanel('accordion_1_statistic_3_smallprint')
                        ]
                    ),
                    MultiFieldPanel(
                        [
                            FieldPanel('accordion_1_statistic_4_number'),
                            FieldPanel('accordion_1_statistic_4_heading'),
                            FieldPanel('accordion_1_statistic_4_smallprint'),
                        ]
                    ),
                    MultiFieldPanel(
                        [

                            FieldPanel('accordion_1_statistic_5_number'),
                            FieldPanel('accordion_1_statistic_5_heading'),
                            FieldPanel('accordion_1_statistic_5_smallprint')
                        ]
                    ),
                    MultiFieldPanel(
                        [
                            FieldPanel('accordion_1_statistic_6_number'),
                            FieldPanel('accordion_1_statistic_6_heading'),
                            FieldPanel('accordion_1_statistic_6_smallprint')
                        ]
                    )
                ]),
            ]
        ),
        MultiFieldPanel(
            heading='Industry two',
            classname='collapsible collapsed',
            children=[
                HelpPanel(
                    content=ACCORDION_FIELDS_HELP_TEXT,
                    classname='help-panel-font-large'
                ),
                ImageChooserPanel('accordion_2_icon'),
                FieldPanel('accordion_2_title'),
                FieldPanel('accordion_2_teaser'),
                FieldRowPanel([
                    MultiFieldPanel(
                        [
                            ImageChooserPanel('accordion_2_subsection_1_icon'),
                            FieldPanel('accordion_2_subsection_1_heading'),
                            FieldPanel('accordion_2_subsection_1_body'),
                        ]
                    ),
                    MultiFieldPanel(
                        [
                            ImageChooserPanel('accordion_2_subsection_2_icon'),
                            FieldPanel('accordion_2_subsection_2_heading'),
                            FieldPanel('accordion_2_subsection_2_body'),
                        ]
                    ),
                    MultiFieldPanel(
                        [
                            ImageChooserPanel('accordion_2_subsection_3_icon'),
                            FieldPanel('accordion_2_subsection_3_heading'),
                            FieldPanel('accordion_2_subsection_3_body'),
                        ]
                    )
                ]),
                MultiFieldPanel([
                    ImageChooserPanel('accordion_2_case_study_hero_image'),
                    FieldPanel('accordion_2_case_study_button_text'),
                    FieldPanel('accordion_2_case_study_button_link'),
                    FieldPanel('accordion_2_case_study_title'),
                    FieldPanel('accordion_2_case_study_description')
                ]),
                FieldRowPanel([
                    MultiFieldPanel(
                        [
                            FieldPanel('accordion_2_statistic_1_number'),
                            FieldPanel('accordion_2_statistic_1_heading'),
                            FieldPanel('accordion_2_statistic_1_smallprint')
                        ]
                    ),
                    MultiFieldPanel(
                        [
                            FieldPanel('accordion_2_statistic_2_number'),
                            FieldPanel('accordion_2_statistic_2_heading'),
                            FieldPanel('accordion_2_statistic_2_smallprint')
                        ]
                    ),
                    MultiFieldPanel(
                        [
                            FieldPanel('accordion_2_statistic_3_number'),
                            FieldPanel('accordion_2_statistic_3_heading'),
                            FieldPanel('accordion_2_statistic_3_smallprint')
                        ]
                    ),
                    MultiFieldPanel(
                        [
                            FieldPanel('accordion_2_statistic_4_number'),
                            FieldPanel('accordion_2_statistic_4_heading'),
                            FieldPanel('accordion_2_statistic_4_smallprint'),
                        ]
                    ),
                    MultiFieldPanel(
                        [

                            FieldPanel('accordion_2_statistic_5_number'),
                            FieldPanel('accordion_2_statistic_5_heading'),
                            FieldPanel('accordion_2_statistic_5_smallprint')
                        ]
                    ),
                    MultiFieldPanel(
                        [
                            FieldPanel('accordion_2_statistic_6_number'),
                            FieldPanel('accordion_2_statistic_6_heading'),
                            FieldPanel('accordion_2_statistic_6_smallprint')
                        ]
                    )
                ]),
            ]
        ),
        MultiFieldPanel(
            heading='Industry three',
            classname='collapsible collapsed',
            children=[
                HelpPanel(
                    content=ACCORDION_FIELDS_HELP_TEXT,
                    classname='help-panel-font-large'
                ),
                ImageChooserPanel('accordion_3_icon'),
                FieldPanel('accordion_3_title'),
                FieldPanel('accordion_3_teaser'),
                FieldRowPanel([
                    MultiFieldPanel(
                        [
                            ImageChooserPanel('accordion_3_subsection_1_icon'),
                            FieldPanel('accordion_3_subsection_1_heading'),
                            FieldPanel('accordion_3_subsection_1_body'),
                        ]
                    ),
                    MultiFieldPanel(
                        [
                            ImageChooserPanel('accordion_3_subsection_2_icon'),
                            FieldPanel('accordion_3_subsection_2_heading'),
                            FieldPanel('accordion_3_subsection_2_body'),
                        ]
                    ),
                    MultiFieldPanel(
                        [
                            ImageChooserPanel('accordion_3_subsection_3_icon'),
                            FieldPanel('accordion_3_subsection_3_heading'),
                            FieldPanel('accordion_3_subsection_3_body'),
                        ]
                    )
                ]),
                MultiFieldPanel([
                    ImageChooserPanel('accordion_3_case_study_hero_image'),
                    FieldPanel('accordion_3_case_study_button_text'),
                    FieldPanel('accordion_3_case_study_button_link'),
                    FieldPanel('accordion_3_case_study_title'),
                    FieldPanel('accordion_3_case_study_description')
                ]),
                FieldRowPanel([
                    MultiFieldPanel(
                        [
                            FieldPanel('accordion_3_statistic_1_number'),
                            FieldPanel('accordion_3_statistic_1_heading'),
                            FieldPanel('accordion_3_statistic_1_smallprint')
                        ]
                    ),
                    MultiFieldPanel(
                        [
                            FieldPanel('accordion_3_statistic_2_number'),
                            FieldPanel('accordion_3_statistic_2_heading'),
                            FieldPanel('accordion_3_statistic_2_smallprint')
                        ]
                    ),
                    MultiFieldPanel(
                        [
                            FieldPanel('accordion_3_statistic_3_number'),
                            FieldPanel('accordion_3_statistic_3_heading'),
                            FieldPanel('accordion_3_statistic_3_smallprint')
                        ]
                    ),
                    MultiFieldPanel(
                        [
                            FieldPanel('accordion_3_statistic_4_number'),
                            FieldPanel('accordion_3_statistic_4_heading'),
                            FieldPanel('accordion_3_statistic_4_smallprint'),
                        ]
                    ),
                    MultiFieldPanel(
                        [

                            FieldPanel('accordion_3_statistic_5_number'),
                            FieldPanel('accordion_3_statistic_5_heading'),
                            FieldPanel('accordion_3_statistic_5_smallprint')
                        ]
                    ),
                    MultiFieldPanel(
                        [
                            FieldPanel('accordion_3_statistic_6_number'),
                            FieldPanel('accordion_3_statistic_6_heading'),
                            FieldPanel('accordion_3_statistic_6_smallprint')
                        ]
                    )
                ]),
            ]
        ),
        MultiFieldPanel(
            heading='Industry four',
            classname='collapsible collapsed',
            children=[
                HelpPanel(
                    content=ACCORDION_FIELDS_HELP_TEXT,
                    classname='help-panel-font-large'
                ),
                ImageChooserPanel('accordion_4_icon'),
                FieldPanel('accordion_4_title'),
                FieldPanel('accordion_4_teaser'),
                FieldRowPanel([
                    MultiFieldPanel(
                        [
                            ImageChooserPanel('accordion_4_subsection_1_icon'),
                            FieldPanel('accordion_4_subsection_1_heading'),
                            FieldPanel('accordion_4_subsection_1_body'),
                        ]
                    ),
                    MultiFieldPanel(
                        [
                            ImageChooserPanel('accordion_4_subsection_2_icon'),
                            FieldPanel('accordion_4_subsection_2_heading'),
                            FieldPanel('accordion_4_subsection_2_body'),
                        ]
                    ),
                    MultiFieldPanel(
                        [
                            ImageChooserPanel('accordion_4_subsection_3_icon'),
                            FieldPanel('accordion_4_subsection_3_heading'),
                            FieldPanel('accordion_4_subsection_3_body'),
                        ]
                    )
                ]),
                MultiFieldPanel([
                    ImageChooserPanel('accordion_4_case_study_hero_image'),
                    FieldPanel('accordion_4_case_study_button_text'),
                    FieldPanel('accordion_4_case_study_button_link'),
                    FieldPanel('accordion_4_case_study_title'),
                    FieldPanel('accordion_4_case_study_description')
                ]),
                FieldRowPanel([
                    MultiFieldPanel(
                        [
                            FieldPanel('accordion_4_statistic_1_number'),
                            FieldPanel('accordion_4_statistic_1_heading'),
                            FieldPanel('accordion_4_statistic_1_smallprint')
                        ]
                    ),
                    MultiFieldPanel(
                        [
                            FieldPanel('accordion_4_statistic_2_number'),
                            FieldPanel('accordion_4_statistic_2_heading'),
                            FieldPanel('accordion_4_statistic_2_smallprint')
                        ]
                    ),
                    MultiFieldPanel(
                        [
                            FieldPanel('accordion_4_statistic_3_number'),
                            FieldPanel('accordion_4_statistic_3_heading'),
                            FieldPanel('accordion_4_statistic_3_smallprint')
                        ]
                    ),
                    MultiFieldPanel(
                        [
                            FieldPanel('accordion_4_statistic_4_number'),
                            FieldPanel('accordion_4_statistic_4_heading'),
                            FieldPanel('accordion_4_statistic_4_smallprint'),
                        ]
                    ),
                    MultiFieldPanel(
                        [

                            FieldPanel('accordion_4_statistic_5_number'),
                            FieldPanel('accordion_4_statistic_5_heading'),
                            FieldPanel('accordion_4_statistic_5_smallprint')
                        ]
                    ),
                    MultiFieldPanel(
                        [
                            FieldPanel('accordion_4_statistic_6_number'),
                            FieldPanel('accordion_4_statistic_6_heading'),
                            FieldPanel('accordion_4_statistic_6_smallprint')
                        ]
                    )
                ]),
            ]
        ),
        MultiFieldPanel(
            heading='Industry five',
            classname='collapsible collapsed',
            children=[
                HelpPanel(
                    content=ACCORDION_FIELDS_HELP_TEXT,
                    classname='help-panel-font-large'
                ),
                ImageChooserPanel('accordion_5_icon'),
                FieldPanel('accordion_5_title'),
                FieldPanel('accordion_5_teaser'),
                FieldRowPanel([
                    MultiFieldPanel(
                        [
                            ImageChooserPanel('accordion_5_subsection_1_icon'),
                            FieldPanel('accordion_5_subsection_1_heading'),
                            FieldPanel('accordion_5_subsection_1_body'),
                        ]
                    ),
                    MultiFieldPanel(
                        [
                            ImageChooserPanel('accordion_5_subsection_2_icon'),
                            FieldPanel('accordion_5_subsection_2_heading'),
                            FieldPanel('accordion_5_subsection_2_body'),
                        ]
                    ),
                    MultiFieldPanel(
                        [
                            ImageChooserPanel('accordion_5_subsection_3_icon'),
                            FieldPanel('accordion_5_subsection_3_heading'),
                            FieldPanel('accordion_5_subsection_3_body'),
                        ]
                    )
                ]),
                MultiFieldPanel([
                    ImageChooserPanel('accordion_4_case_study_hero_image'),
                    FieldPanel('accordion_5_case_study_button_text'),
                    FieldPanel('accordion_5_case_study_button_link'),
                    FieldPanel('accordion_5_case_study_title'),
                    FieldPanel('accordion_5_case_study_description')
                ]),
                FieldRowPanel([
                    MultiFieldPanel(
                        [
                            FieldPanel('accordion_5_statistic_1_number'),
                            FieldPanel('accordion_5_statistic_1_heading'),
                            FieldPanel('accordion_5_statistic_1_smallprint')
                        ]
                    ),
                    MultiFieldPanel(
                        [
                            FieldPanel('accordion_5_statistic_2_number'),
                            FieldPanel('accordion_5_statistic_2_heading'),
                            FieldPanel('accordion_5_statistic_2_smallprint')
                        ]
                    ),
                    MultiFieldPanel(
                        [
                            FieldPanel('accordion_5_statistic_3_number'),
                            FieldPanel('accordion_5_statistic_3_heading'),
                            FieldPanel('accordion_5_statistic_3_smallprint')
                        ]
                    ),
                    MultiFieldPanel(
                        [
                            FieldPanel('accordion_5_statistic_4_number'),
                            FieldPanel('accordion_5_statistic_4_heading'),
                            FieldPanel('accordion_5_statistic_4_smallprint'),
                        ]
                    ),
                    MultiFieldPanel(
                        [

                            FieldPanel('accordion_5_statistic_5_number'),
                            FieldPanel('accordion_5_statistic_5_heading'),
                            FieldPanel('accordion_5_statistic_5_smallprint')
                        ]
                    ),
                    MultiFieldPanel(
                        [
                            FieldPanel('accordion_5_statistic_6_number'),
                            FieldPanel('accordion_5_statistic_6_heading'),
                            FieldPanel('accordion_5_statistic_6_smallprint')
                        ]
                    )
                ]),
            ]
        ),
        MultiFieldPanel(
            heading='Industry six',
            classname='collapsible collapsed',
            children=[
                HelpPanel(
                    content=ACCORDION_FIELDS_HELP_TEXT,
                    classname='help-panel-font-large'
                ),
                ImageChooserPanel('accordion_6_icon'),
                FieldPanel('accordion_6_title'),
                FieldPanel('accordion_6_teaser'),
                FieldRowPanel([
                    MultiFieldPanel(
                        [
                            ImageChooserPanel('accordion_6_subsection_1_icon'),
                            FieldPanel('accordion_6_subsection_1_heading'),
                            FieldPanel('accordion_6_subsection_1_body'),
                        ]
                    ),
                    MultiFieldPanel(
                        [
                            ImageChooserPanel('accordion_6_subsection_2_icon'),
                            FieldPanel('accordion_6_subsection_2_heading'),
                            FieldPanel('accordion_6_subsection_2_body'),
                        ]
                    ),
                    MultiFieldPanel(
                        [
                            ImageChooserPanel('accordion_6_subsection_3_icon'),
                            FieldPanel('accordion_6_subsection_3_heading'),
                            FieldPanel('accordion_6_subsection_3_body'),
                        ]
                    )
                ]),
                MultiFieldPanel([
                    ImageChooserPanel('accordion_6_case_study_hero_image'),
                    FieldPanel('accordion_6_case_study_button_text'),
                    FieldPanel('accordion_6_case_study_button_link'),
                    FieldPanel('accordion_6_case_study_title'),
                    FieldPanel('accordion_6_case_study_description')
                ]),
                FieldRowPanel([
                    MultiFieldPanel(
                        [
                            FieldPanel('accordion_6_statistic_1_number'),
                            FieldPanel('accordion_6_statistic_1_heading'),
                            FieldPanel('accordion_6_statistic_1_smallprint')
                        ]
                    ),
                    MultiFieldPanel(
                        [
                            FieldPanel('accordion_6_statistic_2_number'),
                            FieldPanel('accordion_6_statistic_2_heading'),
                            FieldPanel('accordion_6_statistic_2_smallprint')
                        ]
                    ),
                    MultiFieldPanel(
                        [
                            FieldPanel('accordion_6_statistic_3_number'),
                            FieldPanel('accordion_6_statistic_3_heading'),
                            FieldPanel('accordion_6_statistic_3_smallprint')
                        ]
                    ),
                    MultiFieldPanel(
                        [
                            FieldPanel('accordion_6_statistic_4_number'),
                            FieldPanel('accordion_6_statistic_4_heading'),
                            FieldPanel('accordion_6_statistic_4_smallprint'),
                        ]
                    ),
                    MultiFieldPanel(
                        [

                            FieldPanel('accordion_6_statistic_5_number'),
                            FieldPanel('accordion_6_statistic_5_heading'),
                            FieldPanel('accordion_6_statistic_5_smallprint')
                        ]
                    ),
                    MultiFieldPanel(
                        [
                            FieldPanel('accordion_6_statistic_6_number'),
                            FieldPanel('accordion_6_statistic_6_heading'),
                            FieldPanel('accordion_6_statistic_6_smallprint')
                        ]
                    )
                ]),
            ]
        ),
        MultiFieldPanel(
            heading='Fact sheet',
            classname='collapsible',
            children=[
                FieldPanel('fact_sheet_title'),
                FieldPanel('fact_sheet_teaser'),
                FieldRowPanel([
                    FieldPanel('fact_sheet_column_1_title'),
                    FieldPanel('fact_sheet_column_1_teaser'),
                    FieldPanel('fact_sheet_column_1_body')
                ]),
                FieldRowPanel([
                    FieldPanel('fact_sheet_column_2_title'),
                    FieldPanel('fact_sheet_column_2_teaser'),
                    FieldPanel('fact_sheet_column_2_body')
                ]),
            ]
        ),
        MultiFieldPanel(
            heading='Need help',
            classname='collapsible',
            children=[
                FieldPanel('help_market_guide_cta_link')
            ]
        ),
        MultiFieldPanel(
            heading='News and events',
            children=[
                FieldRowPanel([
                    PageChooserPanel(
                        'related_page_one',
                        [
                            'export_readiness.ArticlePage',
                            'export_readiness.CampaignPage',
                            'export_readiness.ArticleListingPage'
                        ]),
                    PageChooserPanel(
                        'related_page_two',
                        [
                            'export_readiness.ArticlePage',
                            'export_readiness.CampaignPage',
                            'export_readiness.ArticleListingPage'
                        ]),
                    PageChooserPanel(
                        'related_page_three',
                        [
                            'export_readiness.ArticlePage',
                            'export_readiness.CampaignPage',
                            'export_readiness.ArticleListingPage'
                        ]),
                ])
            ]
        ),
        SearchEngineOptimisationPanel(),
    ]

    settings_panels = [
        FieldPanel('title_en_gb'),
        FieldPanel('slug'),
        FieldPanel('tags', widget=CheckboxSelectMultiple)
    ]


class CampaignPagePanels:

    content_panels = [
        MultiFieldPanel(
            heading='Hero section',
            children=[
                FieldPanel('campaign_heading'),
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
                        'export_readiness.ArticlePage'),
                    PageChooserPanel(
                        'related_page_two',
                        'export_readiness.ArticlePage'),
                    PageChooserPanel(
                        'related_page_three',
                        'export_readiness.ArticlePage'),
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
    ]


class ArticlePagePanels:

    content_panels = [
        FieldPanel('article_title'),
        MultiFieldPanel(
            heading='Article content',
            children=[
                FieldPanel('article_subheading'),
                FieldPanel('article_teaser'),
                ImageChooserPanel('article_image'),
                FieldPanel('article_video', widget=AdminMediaChooser),
                FieldPanel('article_video_transcript'),
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
                        'export_readiness.ArticlePage'),
                    PageChooserPanel(
                        'related_page_two',
                        'export_readiness.ArticlePage'),
                    PageChooserPanel(
                        'related_page_three',
                        'export_readiness.ArticlePage'),
                ]),
            ]
        ),
        SearchEngineOptimisationPanel(),
    ]

    settings_panels = [
        FieldPanel('title_en_gb'),
        FieldPanel('type_of_article', widget=Select),
        FieldPanel('slug'),
        FieldPanel('tags', widget=CheckboxSelectMultiple)
    ]


class MarketingArticlePagePanels:

    content_panels = [
        FieldPanel('article_title'),
        MultiFieldPanel(
            heading='Article content',
            children=[
                FieldPanel('article_teaser'),
                ImageChooserPanel('article_image'),
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
                        'export_readiness.ArticlePage'),
                    PageChooserPanel(
                        'related_page_two',
                        'export_readiness.ArticlePage'),
                    PageChooserPanel(
                        'related_page_three',
                        'export_readiness.ArticlePage'),
                ]),
            ]
        ),
        SearchEngineOptimisationPanel(),
    ]

    settings_panels = [
        FieldPanel('title_en_gb'),
        FieldPanel('slug'),
        FieldPanel('tags', widget=CheckboxSelectMultiple),
    ]


class HomePagePanels:

    content_panels = [
        MultiFieldPanel(
            heading='EU Exit banner',
            classname='collapsible',
            children=[
                FieldPanel('banner_label'),
                FieldPanel('banner_content'),
            ]
        ),
        MultiFieldPanel(
            heading='EU exit news',
            classname='collapsible',
            children=[
                FieldPanel('news_title'),
                FieldPanel('news_description')
            ]
        ),
        MultiFieldPanel(
            heading='Hero',
            classname='collapsible',
            children=[
                ImageChooserPanel('hero_image'),
                FieldPanel('hero_text'),
                FieldPanel('hero_cta_text'),
                FieldPanel('hero_cta_url')
            ],
        ),
        MultiFieldPanel(
            heading='Prepare for Brexit',
            classname='collapsible',
            children=[
                FieldPanel('chevron_url'),
                FieldPanel('chevron_text'),
                StreamFieldPanel('chevron_links')
            ]
        ),
        MultiFieldPanel(
            heading='How DIT helps',
            classname='collapsible',
            children=[
                FieldPanel('how_dit_helps_title'),
                StreamFieldPanel('how_dit_helps_columns')
            ],
        ),
        MultiFieldPanel(
            heading='Export good from the UK',
            classname='collapsible',
            children=[
                FieldPanel('madb_title'),
                ImageChooserPanel('madb_image'),
                FieldPanel('madb_image_alt'),
                FieldPanel('madb_content'),
                FieldPanel('madb_cta_text'),
                FieldPanel('madb_cta_url')
            ]
        ),
        MultiFieldPanel(
            heading='What\'s new',
            classname='collapsible',
            children=[
                FieldPanel('what_is_new_title'),
                StreamFieldPanel('what_is_new_pages')
            ]
        ),
        StreamFieldPanel('campaign'),

        SearchEngineOptimisationPanel(),
    ]

    settings_panels = [
        FieldPanel('title_en_gb'),
        FieldPanel('slug'),
    ]


class EUExitDomesticFormPagePanels:

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
        SearchEngineOptimisationPanel()
    ]

    settings_panels = [
        FieldPanel('title_en_gb'),
        FieldPanel('slug'),
    ]


class EUExitFormSuccessPagePanels:

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


class ContactUsGuidancePagePanels:

    content_panels = [
        MultiFieldPanel(
            heading='Topic',
            children=[
                FieldPanel('topic', widget=Select),
            ]
        ),
        MultiFieldPanel(
            heading='Guidance',
            children=[
                FieldPanel('body'),
            ]
        ),
        SearchEngineOptimisationPanel(),
    ]

    settings_panels = []


class ContactSuccessPagePanels:

    content_panels = [
        MultiFieldPanel(
            heading='Topic',
            children=[
                FieldPanel('topic', widget=Select),
            ]
        ),
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

    settings_panels = []
