from django.forms import CheckboxSelectMultiple, Select, Textarea
from wagtail.admin.panels import (
    FieldPanel,
    FieldRowPanel,
    HelpPanel,
    InlinePanel,
    MultiFieldPanel,
    ObjectList,
    PageChooserPanel,
)

from wagtailmedia.edit_handlers import MediaChooserPanel
from wagtailmedia.widgets import AdminMediaChooser
from core.helpers import make_translated_interface
from core.panels import SearchEngineOptimisationPanel


class InternationalHomePagePanels:

    content_panels = [
        FieldPanel('title'),
        FieldPanel('hero_title'),
        MediaChooserPanel('hero_video'),
        FieldPanel('homepage_link_panels'),
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
                FieldPanel('hero_image'),
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
                                FieldPanel('section_one_image'),
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
                                FieldPanel(
                                    'section_two_subsection_one_icon'),
                                FieldPanel(
                                    'section_two_subsection_one_heading'),
                                FieldPanel(
                                    'section_two_subsection_one_body')
                            ]
                        ),
                        MultiFieldPanel(
                            [
                                FieldPanel(
                                    'section_two_subsection_two_icon'),
                                FieldPanel(
                                    'section_two_subsection_two_heading'),
                                FieldPanel(
                                    'section_two_subsection_two_body')
                            ]
                        ),
                        MultiFieldPanel(
                            [
                                FieldPanel(
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
                FieldPanel('case_study_image')
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
        FieldPanel('type_of_article', widget=Select),
        FieldPanel('hero_image'),
        MediaChooserPanel('hero_video'),
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
        SearchEngineOptimisationPanel(),
    ]

    image_panels = [
        FieldPanel('article_image'),
        FieldPanel('article_video', widget=AdminMediaChooser),
    ]

    settings_panels = [
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
                FieldPanel('hero_image'),
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
                FieldPanel('campaign_hero_image'),
            ]
        ),
        MultiFieldPanel(
            heading='Section one',
            children=[
                FieldPanel('section_one_heading'),
                FieldPanel('section_one_intro'),
                FieldPanel('section_one_image'),
                FieldRowPanel([
                    MultiFieldPanel(
                        children=[
                            FieldPanel('selling_point_one_icon'),
                            FieldPanel('selling_point_one_heading'),
                            FieldPanel('selling_point_one_content'),
                        ]
                    ),
                    MultiFieldPanel(
                        children=[
                            FieldPanel('selling_point_two_icon'),
                            FieldPanel('selling_point_two_heading'),
                            FieldPanel('selling_point_two_content'),
                        ]
                    ),
                    MultiFieldPanel(
                        children=[
                            FieldPanel('selling_point_three_icon'),
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
                FieldPanel('section_two_image'),
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
            heading='Hero content',
            children=[
                FieldPanel('hero_image'),
                MediaChooserPanel('hero_video'),
                FieldPanel('hero_teaser')
            ]
        ),
        MultiFieldPanel(
            heading="Explore more of the Investment Atlas section",
            classname="collapsible",
            children=[
                PageChooserPanel('related_page_one', [
                    'great_international.WhyInvestInTheUKPage',
                    'great_international.AboutUkRegionPage',
                    'great_international.InvestmentOpportunityPage',
                    'great_international.InvestmentGeneralContentPage',
                    'great_international.AboutUkRegionListingPage',
                    'great_international.InvestmentOpportunityListingPage']),
                PageChooserPanel('related_page_two', [
                    'great_international.WhyInvestInTheUKPage',
                    'great_international.AboutUkRegionPage',
                    'great_international.InvestmentOpportunityPage',
                    'great_international.InvestmentGeneralContentPage',
                    'great_international.AboutUkRegionListingPage',
                    'great_international.InvestmentOpportunityListingPage']),
                PageChooserPanel('related_page_three', [
                    'great_international.WhyInvestInTheUKPage',
                    'great_international.AboutUkRegionPage',
                    'great_international.InvestmentOpportunityPage',
                    'great_international.InvestmentGeneralContentPage',
                    'great_international.AboutUkRegionListingPage',
                    'great_international.InvestmentOpportunityListingPage']),
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


class AboutDitServiceFieldPanels:

    panels = [
        MultiFieldPanel([
            FieldPanel('icon'),
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
            ],
        ),
        MultiFieldPanel(
            heading="Teaser",
            children=[
                FieldPanel('teaser'),
            ],
        ),
        MultiFieldPanel(
            heading="EBook section",
            classname='collapsible',
            children=[
                FieldRowPanel([
                    FieldPanel('ebook_section_image_alt_text')
                ]),
                MultiFieldPanel([
                    FieldPanel('ebook_section_body'),
                    HelpPanel('CTAs require both text and a link to show on page. '),
                    FieldPanel('ebook_section_cta_text'),
                    FieldPanel('ebook_section_cta_link'),
                ]),
            ]
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

    image_panels = [
        FieldPanel('hero_image'),
        FieldPanel('ebook_section_image'),
        FieldPanel('case_study_image'),
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


class AboutUkLandingPagePanels:

    image_panels = [
        FieldPanel('hero_image'),
        FieldPanel('why_choose_uk_image'),
        MultiFieldPanel(
            heading="How we help images",
            children=[
                FieldPanel('how_we_help_one_icon'),
                FieldPanel('how_we_help_two_icon'),
                FieldPanel('how_we_help_three_icon'),
                FieldPanel('how_we_help_four_icon'),
                FieldPanel('how_we_help_five_icon'),
                FieldPanel('how_we_help_six_icon'),
            ]),
        FieldPanel('ebook_section_image'),
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
                            ['great_international.AboutUkRegionPage']
                        ),
                        FieldPanel('scotland_text')
                    ]),
                    MultiFieldPanel([
                        PageChooserPanel(
                            'northern_ireland',
                            ['great_international.AboutUkRegionPage']
                        ),
                        FieldPanel('northern_ireland_text')
                    ]),
                    MultiFieldPanel([
                        PageChooserPanel(
                            'north_england',
                            ['great_international.AboutUkRegionPage']
                        ),
                        FieldPanel('north_england_text')
                    ]),
                ]),
                FieldRowPanel([
                    MultiFieldPanel([
                        PageChooserPanel(
                            'wales',
                            ['great_international.AboutUkRegionPage']
                        ),
                        FieldPanel('wales_text')
                    ]),
                    MultiFieldPanel([
                        PageChooserPanel(
                            'midlands',
                            ['great_international.AboutUkRegionPage']
                        ),
                        FieldPanel('midlands_text')
                    ]),
                    MultiFieldPanel([
                        PageChooserPanel(
                            'south_england',
                            ['great_international.AboutUkRegionPage']
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
                    FieldPanel('ebook_section_cta_link'),
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
        FieldPanel('hero_image'),
        MediaChooserPanel('hero_video')
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
        MultiFieldPanel(
            heading="Explore more of the Investment Atlas section",
            classname="collapsible",
            children=[
                PageChooserPanel(
                    'related_page_one', [
                        'great_international.WhyInvestInTheUKPage',
                        'great_international.InternationalTopicLandingPage',
                        'great_international.AboutUkRegionPage',
                        'great_international.InvestmentOpportunityPage']),
                PageChooserPanel('related_page_two', [
                        'great_international.WhyInvestInTheUKPage',
                        'great_international.InternationalTopicLandingPage',
                        'great_international.AboutUkRegionPage',
                        'great_international.InvestmentOpportunityPage']),
                PageChooserPanel('related_page_three', [
                        'great_international.WhyInvestInTheUKPage',
                        'great_international.InternationalTopicLandingPage',
                        'great_international.AboutUkRegionPage',
                        'great_international.InvestmentOpportunityPage']),
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
                FieldPanel('hero_image'),
            ],
        ),
        FieldPanel('featured_description'),
        MultiFieldPanel(
            heading="Region summary",
            classname='collapsible',
            children=[
                HelpPanel('Required fields for section to show: '
                          'Region Summary Section Content'),
                FieldPanel('region_summary_section_image'),
                FieldPanel('region_summary_section_strapline'),
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
                FieldPanel('property_and_infrastructure_section_image'),
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
                        FieldPanel('sub_section_one_icon'),
                        FieldPanel('sub_section_one_content')
                    ]),
                    MultiFieldPanel([
                        FieldPanel('sub_section_two_title'),
                        FieldPanel('sub_section_two_icon'),
                        FieldPanel('sub_section_two_content')
                    ]),
                    MultiFieldPanel([
                        FieldPanel('sub_section_three_title'),
                        FieldPanel('sub_section_three_icon'),
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
                FieldPanel('case_study_image'),
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
            FieldPanel('image'),
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
                FieldPanel('hero_title'),
                FieldPanel('hero_image'),
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
                        FieldPanel('section_one_image'),
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
                    FieldPanel('ebook_section_image'),
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


class InternationalInvestmentSectorPagePanels:
    content_panels = [
        FieldPanel('title'),
        MultiFieldPanel(
            heading='Heading',
            classname='collapsible',
            children=[
                FieldPanel('heading'),
                FieldPanel('hero_image'),
                MediaChooserPanel('hero_video'),
                FieldPanel('standfirst'),
                FieldPanel('featured_description')
            ]
        ),
        MultiFieldPanel(
            heading='Intro',
            classname='collapsible',
            children=[
                FieldPanel('intro_text'),
                FieldPanel('intro_image'),
            ]
        ),
        MultiFieldPanel(
            heading='Contact details',
            classname='collapsible',
            children=[
                FieldPanel('contact_name'),
                FieldPanel('contact_avatar'),
                FieldPanel('contact_job_title'),
                FieldPanel('contact_link'),
                FieldPanel('contact_link_button_preamble'),
                FieldPanel('contact_link_button_label'),
            ]
        ),
        MultiFieldPanel(
            heading='Related opportunities',
            classname='collapsible',
            children=[
                FieldPanel('related_opportunities_header'),
                HelpPanel('See the dedicated tab for selecting the opportunities themselves'),
            ]
        ),
        FieldPanel('downpage_content'),
        MultiFieldPanel(
            heading='Early opportunities',
            classname='collapsible',
            children=[
                FieldPanel('early_opportunities_header'),
                FieldPanel('early_opportunities'),
            ]
        ),
        SearchEngineOptimisationPanel()
    ]

    settings_panels = [
        FieldPanel('slug'),
        FieldPanel('tags'),
    ]

    related_entities_panels = [
        FieldRowPanel(
            heading='Related Opportunities',
            children=[
                FieldPanel('manually_selected_related_opportunities'),
            ]
        ),
    ]

    edit_handler = make_translated_interface(
        content_panels=content_panels,
        other_panels=related_entities_panels,  # These are shown as separate tabs
        settings_panels=settings_panels
    )


class InternationalInvestmentSubSectorPagePanels:

    content_panels = [
        FieldPanel('title'),
        FieldPanel('heading'),
    ]

    settings_panels = [
        FieldPanel('slug'),
    ]

    edit_handler = make_translated_interface(
        content_panels=content_panels,
        settings_panels=settings_panels
    )


class WhyInvestInTheUKPagePanels:

    content_panels = [
        MultiFieldPanel(
            heading="Hero and Intro",
            classname='collapsible',
            children=[
                FieldPanel('title'),
                FieldPanel('hero_image'),
                MediaChooserPanel('hero_video'),
                FieldPanel('strapline'),
                FieldPanel('introduction'),
                FieldPanel('intro_image'),
            ],
        ),
        MultiFieldPanel(
            heading="UK Strengths",
            classname='collapsible',
            children=[
                FieldPanel('uk_strength_title'),
                FieldPanel('uk_strength_intro'),
                FieldPanel('uk_strength_panels'),
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
