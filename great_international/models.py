from directory_constants.constants import cms
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


class GreatInternationalApp(ExclusivePageMixin, ServiceMixin, BasePage):
    slug_identity = 'great-international-app'
    service_name_value = cms.GREAT_INTERNATIONAL

    @classmethod
    def get_required_translatable_fields(cls):
        return []


class InternationalHomePage(ExclusivePageMixin, BasePage):
    service_name_value = cms.GREAT_INTERNATIONAL
    slug_identity = cms.EXPORT_READINESS_HOME_INTERNATIONAL_SLUG
    subpage_types = [
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

    content_panels = [
        MultiFieldPanel(
            heading='Tariffs',
            children=[
                FieldPanel('news_title'),
            ]
        ),
        MultiFieldPanel(
            heading='News and events',
            children=[
                FieldPanel('tariffs_title'),
                FieldPanel('tariffs_description'),
                FieldPanel('tariffs_link'),
                ImageChooserPanel('tariffs_image')
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

    subpage_types = [
        'great_international.InternationalArticlePage',
    ]

    settings_panels = []

    def save(self, *args, **kwargs):
        self.title = self.get_verbose_name()
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
    ]
