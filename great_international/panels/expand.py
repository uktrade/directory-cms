from wagtail.admin.edit_handlers import (
    FieldPanel, FieldRowPanel, MultiFieldPanel, ObjectList, HelpPanel, PageChooserPanel
)
from wagtail.images.edit_handlers import ImageChooserPanel

from core.helpers import make_translated_interface
from core.panels import SearchEngineOptimisationPanel


class ExpandInternationalLandingPagePanels:

    image_panels = [
        ImageChooserPanel('hero_image'),
        ImageChooserPanel('benefits_section_img'),
        ImageChooserPanel('how_to_expand_image'),
        ImageChooserPanel('how_we_help_icon_one'),
        ImageChooserPanel('how_we_help_icon_two'),
        ImageChooserPanel('how_we_help_icon_three'),
        ImageChooserPanel('how_we_help_icon_four'),
        ImageChooserPanel('how_we_help_icon_five'),
    ]

    content_panels = [
        MultiFieldPanel(
            heading='Hero',
            classname='collapsible',
            children=[
                FieldPanel('breadcrumbs_label'),
                FieldPanel('hero_title'),
                FieldPanel('sub_heading'),
                HelpPanel('Cta\'s require both text and a link to show '
                          'on page. '),
                FieldPanel('hero_cta_text'),
                FieldPanel('hero_cta_link'),
            ],
        ),
        MultiFieldPanel(
            heading='Benefits section',
            classname='collapsible',
            children=[
                HelpPanel('Required fields for section to show: Benefits section title and text'),
                FieldPanel('benefits_section_title'),
                FieldPanel('benefits_section_intro'),
                FieldPanel('benefits_section_text'),
                HelpPanel('CTAs require both text and a link to show on page'),
                FieldPanel('benefits_section_cta_text'),
                FieldPanel('benefits_section_cta_link'),
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
                    ],
                ),
                FieldRowPanel(
                    [
                        MultiFieldPanel(
                            [
                                FieldPanel('how_to_expand_title_three'),
                                FieldPanel('how_to_expand_text_three')
                            ],
                        ),
                        MultiFieldPanel(
                            [
                                FieldPanel('how_to_expand_title_four'),
                                FieldPanel('how_to_expand_text_four')
                            ],
                        ),
                    ],
                ),
            ],
        ),
        MultiFieldPanel(
            heading='How we help section',
            classname='collapsible',
            children=[
                HelpPanel('Required fields for section to show: '
                          'How We Help Title, How We Help intro'),
                FieldPanel('how_we_help_title'),
                FieldPanel('how_we_help_intro'),
                HelpPanel('Each icon requires the corresponding text to '
                          'show on the page'),
                FieldRowPanel(
                    [
                        MultiFieldPanel(
                            [
                                FieldPanel('how_we_help_text_one'),
                            ],
                        ),
                        MultiFieldPanel(
                            [
                                FieldPanel('how_we_help_text_two'),
                            ],
                        ),
                        MultiFieldPanel(
                            [
                                FieldPanel('how_we_help_text_three'),
                            ],
                        ),
                    ],
                ),
                FieldRowPanel(
                    [
                        MultiFieldPanel(
                            [
                                FieldPanel('how_we_help_text_four'),
                            ],
                        ),
                        MultiFieldPanel(
                            [
                                FieldPanel('how_we_help_text_five'),
                            ],
                        )
                    ],

                ),
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
                FieldPanel('contact_section_cta_text'),
                FieldPanel('contact_section_cta_link'),
            ],
        ),
        MultiFieldPanel(
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
                          'Industries Title and at least one featured industry '
                          '(choose in \'featured industries\' tab)'),
                FieldPanel('industries_title'),
                FieldPanel('industries_intro'),
                FieldPanel('industries_cta_text'),
                FieldPanel('industries_cta_link'),
            ],

        ),
        SearchEngineOptimisationPanel()
    ]

    settings_panels = [
        FieldPanel('title_en_gb'),
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
