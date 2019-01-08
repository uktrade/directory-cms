from django.db import models
from directory_constants.constants import cms
from core.models import (
    BasePage,
    ExclusivePageMixin,
    ServiceMixin,
)
from wagtail.admin.edit_handlers import (
    FieldPanel, MultiFieldPanel
)
from core.helpers import make_translated_interface
from core.model_fields import MarkdownField


class ComponentsApp(ExclusivePageMixin, ServiceMixin, BasePage):
    slug_identity = 'components-app'
    service_name_value = cms.COMPONENTS

    @classmethod
    def get_required_translatable_fields(cls):
        return []


class BannerComponent(BasePage):
    service_name_value = cms.COMPONENTS
    view_path = ''

    banner_content = MarkdownField()
    banner_label = models.CharField(max_length=50, null=True, blank=True)

    content_panels = [
        MultiFieldPanel(
            heading='Banner component',
            children=[
                FieldPanel('banner_label'),
                FieldPanel('banner_content'),
            ]
        ),
    ]

    settings_panels = [
        FieldPanel('title_en_gb'),
        FieldPanel('slug'),
    ]

    edit_handler = make_translated_interface(
        content_panels=content_panels,
        settings_panels=settings_panels,
    )
