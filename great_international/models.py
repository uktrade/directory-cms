from directory_constants.constants import cms
from django.forms import Textarea, CheckboxSelectMultiple
from django.utils.text import slugify
from modelcluster.fields import ParentalManyToManyField
from wagtail.admin.edit_handlers import (
    FieldPanel, FieldRowPanel, MultiFieldPanel, PageChooserPanel
)
from wagtail.images.edit_handlers import ImageChooserPanel

from django.db import models

from core.model_fields import MarkdownField

from core.models import (
    BasePage,
    ExclusivePageMixin,
    ServiceMixin,
)
from core.panels import SearchEngineOptimisationPanel
from export_readiness.models import Tag


class GreatInternationalApp(ExclusivePageMixin, ServiceMixin, BasePage):
    slug_identity = 'great-international-app'
    service_name_value = cms.GREAT_INTERNATIONAL

    @classmethod
    def get_required_translatable_fields(cls):
        return []


class InternationalSectorPage(BasePage):
    service_name_value = cms.GREAT_INTERNATIONAL
    subpage_types = ['great_international.InternationalSectorPage']

    heading = models.CharField(max_length=255)
    sub_heading = models.CharField(max_length=255)
    hero_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    heading_teaser = models.CharField(max_length=255)

    section_one_body = models.CharField(max_length=255)
    section_one_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    statistic_number_one = models.CharField(max_length=255)
    statistic_heading_one = models.CharField(max_length=255)
    statistic_smallprint_one = models.CharField(max_length=255)

    statistic_number_two = models.CharField(max_length=255)
    statistic_heading_two = models.CharField(max_length=255)
    statistic_smallprint_two = models.CharField(max_length=255)

    statistic_number_three = models.CharField(max_length=255, blank=True)
    statistic_heading_three = models.CharField(max_length=255, blank=True)
    statistic_smallprint_three = models.CharField(max_length=255, blank=True)

    statistic_number_four = models.CharField(max_length=255, blank=True)
    statistic_heading_four = models.CharField(max_length=255, blank=True)
    statistic_smallprint_four = models.CharField(max_length=255, blank=True)

    statistic_number_five = models.CharField(max_length=255, blank=True)
    statistic_heading_five = models.CharField(max_length=255, blank=True)
    statistic_smallprint_five = models.CharField(max_length=255, blank=True)

    statistic_number_six = models.CharField(max_length=255, blank=True)
    statistic_heading_six = models.CharField(max_length=255, blank=True)
    statistic_smallprint_six = models.CharField(max_length=255, blank=True)

    section_two_heading = models.CharField(max_length=255)
    section_two_teaser = models.CharField(max_length=255)

    section_two_icon_one = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    section_two_heading_one = models.CharField(max_length=255)
    section_two_body_one = models.CharField(max_length=255)

    section_two_icon_two = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    section_two_heading_two = models.CharField(max_length=255)
    section_two_body_two = models.CharField(max_length=255)

    section_two_icon_three = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    section_two_heading_three = models.CharField(max_length=255)
    section_two_body_three = models.CharField(max_length=255)

    case_study_title = models.CharField(max_length=255)
    case_study_description = models.CharField(max_length=255)
    case_study_cta_text = models.CharField(max_length=255)
    case_study_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    section_three_heading = models.CharField(max_length=255)
    section_three_teaser = models.CharField(max_length=255)

    section_three_heading_one = models.CharField(max_length=255)
    section_three_teaser_one = models.CharField(max_length=255)
    section_three_body_one = MarkdownField(blank=True, null=True)

    section_three_heading_two = models.CharField(max_length=255)
    section_three_teaser_two = models.CharField(max_length=255)
    section_three_body_two = MarkdownField(blank=True, null=True)

    next_steps_heading = models.CharField(max_length=255)
    next_steps_description = models.CharField(max_length=255)

    content_panels = [
        MultiFieldPanel(
            [
                FieldPanel('heading'),
                FieldPanel('sub_heading'),
                ImageChooserPanel('hero_image'),
                FieldPanel('heading_teaser')
            ],
            heading='Heading'
        ),
        MultiFieldPanel(
            [
                FieldRowPanel(
                    [
                        FieldPanel('section_one_body'),
                        ImageChooserPanel('section_one_image')
                    ]
                )
            ],
            heading='Section One'
        ),
        MultiFieldPanel(
            [
                FieldRowPanel(
                    [
                        MultiFieldPanel(
                            [
                                FieldPanel('statistic_number_one'),
                                FieldPanel('statistic_heading_one'),
                                FieldPanel('statistic_smallprint_one')
                            ]
                        ),
                        MultiFieldPanel(
                            [
                                FieldPanel('statistic_number_two'),
                                FieldPanel('statistic_heading_two'),
                                FieldPanel('statistic_smallprint_two')
                            ]
                        ),
                        MultiFieldPanel(
                            [
                                FieldPanel('statistic_number_three'),
                                FieldPanel('statistic_heading_three'),
                                FieldPanel('statistic_smallprint_three')
                            ]
                        ),
                        MultiFieldPanel(
                            [
                                FieldPanel('statistic_number_four'),
                                FieldPanel('statistic_heading_four'),
                                FieldPanel('statistic_smallprint_four')
                            ]
                        ),
                        MultiFieldPanel(
                            [
                                FieldPanel('statistic_number_five'),
                                FieldPanel('statistic_heading_five'),
                                FieldPanel('statistic_smallprint_five')
                            ]
                        ),
                        MultiFieldPanel(
                            [
                                FieldPanel('statistic_number_six'),
                                FieldPanel('statistic_heading_six'),
                                FieldPanel('statistic_smallprint_six')
                            ]
                        ),
                    ]
                )
            ],
            heading='Statistics'
        ),
        MultiFieldPanel(
            [
                FieldPanel('section_two_heading'),
                FieldPanel('section_two_teaser'),
                FieldRowPanel(
                    [
                        MultiFieldPanel(
                            [
                                ImageChooserPanel('section_two_icon_one'),
                                FieldPanel('section_two_heading_one'),
                                FieldPanel('section_two_body_one')
                            ]
                        ),
                        MultiFieldPanel(
                            [
                                ImageChooserPanel('section_two_icon_two'),
                                FieldPanel('section_two_heading_two'),
                                FieldPanel('section_two_body_two')
                            ]
                        ),
                        MultiFieldPanel(
                            [
                                ImageChooserPanel('section_two_icon_three'),
                                FieldPanel('section_two_heading_three'),
                                FieldPanel('section_two_body_three')
                            ]
                        )
                    ]
                )
            ],
            heading='Section Two'
        ),
        MultiFieldPanel(
            [
                FieldPanel('case_study_title'),
                FieldPanel('case_study_description'),
                FieldPanel('case_study_cta_text'),
                ImageChooserPanel('case_study_image')
            ],
            heading='Case Study'
        ),
        MultiFieldPanel(
            [
                FieldPanel('section_three_heading'),
                FieldPanel('section_three_teaser'),
                FieldRowPanel(
                    [
                        MultiFieldPanel(
                            [
                                FieldPanel('section_three_heading_one'),
                                FieldPanel('section_three_teaser_one'),
                                FieldPanel('section_three_body_one')
                            ]
                        ),
                        MultiFieldPanel(
                            [
                                FieldPanel('section_three_heading_two'),
                                FieldPanel('section_three_teaser_two'),
                                FieldPanel('section_three_body_two')
                            ]
                        )
                    ]
                )
            ],
            heading='Section Three'
        ),
        MultiFieldPanel(
            [
                FieldPanel('next_steps_heading'),
                FieldPanel('next_steps_description')
            ],
            heading='Next Steps'
        ),
        SearchEngineOptimisationPanel()
    ]

    settings_panels = [
        FieldPanel('title_en_gb'),
        FieldPanel('slug')
    ]


class InternationalHomePage(ExclusivePageMixin, BasePage):
    service_name_value = cms.GREAT_INTERNATIONAL
    slug_identity = cms.GREAT_HOME_INTERNATIONAL_SLUG
    subpage_types = [
        'great_international.InternationalArticleListingPage',
        'great_international.InternationalArticlePage',
        'great_international.InternationalMarketingPages'
    ]

    tariffs_title = models.CharField(max_length=255)
    tariffs_description = MarkdownField()
    tariffs_link = models.URLField()
    tariffs_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    news_title = models.CharField(max_length=255)
    related_page_one = models.ForeignKey(
        'wagtailcore.Page',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
    )
    related_page_two = models.ForeignKey(
        'wagtailcore.Page',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
    )
    related_page_three = models.ForeignKey(
        'wagtailcore.Page',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
    )

    content_panels = [
        MultiFieldPanel(
            heading='Tariffs',
            children=[
                FieldPanel('tariffs_title'),
                FieldPanel('tariffs_description'),
                FieldPanel('tariffs_link'),
                ImageChooserPanel('tariffs_image')
            ]
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
        SearchEngineOptimisationPanel(),
    ]

    settings_panels = [
        FieldPanel('title_en_gb'),
        FieldPanel('slug'),
    ]


class InternationalMarketingPages(ExclusivePageMixin, BasePage):
    service_name_value = cms.GREAT_INTERNATIONAL
    slug_identity = cms.GREAT_INTERNATIONAL_MARKETING_PAGES_SLUG
    tags = ParentalManyToManyField(Tag, blank=True)

    subpage_types = [
        'great_international.InternationalArticlePage',
        'great_international.InternationalCampaignPage'
    ]
    settings_panels = [
        FieldPanel('tags', widget=CheckboxSelectMultiple)
    ]

    def save(self, *args, **kwargs):
        self.title = self.get_verbose_name()
        return super().save(*args, **kwargs)


class InternationalRegionPage(BasePage):
    service_name_value = cms.GREAT_INTERNATIONAL
    subpage_types = [
        'great_international.InternationalRegionalFolderPage'
    ]

    tags = ParentalManyToManyField(Tag, blank=True)

    settings_panels = [
        FieldPanel('title_en_gb'),
        FieldPanel('slug'),
        FieldPanel('tags', widget=CheckboxSelectMultiple)
    ]

    def save(self, *args, **kwargs):
        return super().save(*args, **kwargs)


class InternationalRegionalFolderPage(BasePage):
    service_name_value = cms.GREAT_INTERNATIONAL
    subpage_types = [
        'great_international.InternationalArticlePage',
        'great_international.InternationalCampaignPage'
    ]

    settings_panels = [
        FieldPanel('title_en_gb'),
        FieldPanel('slug'),
    ]

    def save(self, *args, **kwargs):
        if self.pk is None:
            self.slug = slugify(f'{self.slug}-{self.get_parent().slug}')
        return super().save(*args, **kwargs)


class InternationalArticlePage(BasePage):
    service_name_value = cms.GREAT_INTERNATIONAL
    subpage_types = []

    article_title = models.CharField(max_length=255)

    article_teaser = models.CharField(max_length=255)
    article_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    article_body_text = MarkdownField()

    related_page_one = models.ForeignKey(
        'great_international.InternationalArticlePage',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
    )
    related_page_two = models.ForeignKey(
        'great_international.InternationalArticlePage',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
    )
    related_page_three = models.ForeignKey(
        'great_international.InternationalArticlePage',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
    )
    tags = ParentalManyToManyField(Tag, blank=True)

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
        FieldPanel('tags', widget=CheckboxSelectMultiple)
    ]


class InternationalArticleListingPage(BasePage):
    service_name_value = cms.GREAT_INTERNATIONAL
    subpage_types = ['great_international.InternationalArticlePage']

    landing_page_title = models.CharField(max_length=255)
    hero_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    hero_teaser = models.CharField(max_length=255, null=True, blank=True)
    list_teaser = MarkdownField(null=True, blank=True)
    tags = ParentalManyToManyField(Tag, blank=True)

    @property
    def articles_count(self):
        return self.get_descendants().type(
            InternationalArticlePage
        ).live().count()

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
        FieldPanel('tags', widget=CheckboxSelectMultiple)
    ]


class InternationalCampaignPage(BasePage):
    service_name_value = cms.GREAT_INTERNATIONAL
    subpage_types = [
        'great_international.InternationalArticlePage'
    ]
    view_path = 'campaigns/'

    campaign_teaser = models.CharField(max_length=255, null=True, blank=True)
    campaign_heading = models.CharField(max_length=255)
    campaign_hero_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    section_one_heading = models.CharField(max_length=255)
    section_one_intro = MarkdownField()
    section_one_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    selling_point_one_icon = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    selling_point_one_heading = models.CharField(max_length=255)
    selling_point_one_content = MarkdownField()

    selling_point_two_icon = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    selling_point_two_heading = models.CharField(
        max_length=255,
        null=True,
        blank=True,
    )
    selling_point_two_content = MarkdownField(null=True, blank=True)

    selling_point_three_icon = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    selling_point_three_heading = models.CharField(
        max_length=255,
        null=True,
        blank=True
    )
    selling_point_three_content = MarkdownField(null=True, blank=True)

    section_one_contact_button_url = models.CharField(
        max_length=255,
        null=True,
        blank=True
    )
    section_one_contact_button_text = models.CharField(
        max_length=255,
        null=True,
        blank=True
    )

    section_two_heading = models.CharField(max_length=255)
    section_two_intro = MarkdownField()

    section_two_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    section_two_contact_button_url = models.CharField(
        max_length=255,
        null=True,
        blank=True
    )
    section_two_contact_button_text = models.CharField(
        max_length=255,
        null=True,
        blank=True
    )

    related_content_heading = models.CharField(max_length=255)
    related_content_intro = MarkdownField()

    related_page_one = models.ForeignKey(
        'great_international.InternationalArticlePage',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
    )
    related_page_two = models.ForeignKey(
        'great_international.InternationalArticlePage',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
    )
    related_page_three = models.ForeignKey(
        'great_international.InternationalArticlePage',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
    )

    cta_box_message = models.CharField(max_length=255)
    cta_box_button_url = models.CharField(max_length=255)
    cta_box_button_text = models.CharField(max_length=255)

    tags = ParentalManyToManyField(Tag, blank=True)

    content_panels = [
        MultiFieldPanel(
            heading='Hero section',
            children=[
                FieldPanel('campaign_heading'),
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
        FieldPanel('tags', widget=CheckboxSelectMultiple)
    ]


class InternationalTopicLandingPage(BasePage):
    service_name_value = cms.GREAT_INTERNATIONAL
    subpage_types = [
        'great_international.InternationalArticleListingPage',
        'great_international.InternationalCampaignPage'
    ]

    landing_page_title = models.CharField(max_length=255)

    hero_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    hero_teaser = models.CharField(max_length=255, null=True, blank=True)
    tags = ParentalManyToManyField(Tag, blank=True)

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
        FieldPanel('tags', widget=CheckboxSelectMultiple)
    ]
