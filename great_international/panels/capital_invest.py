from wagtail.admin.edit_handlers import FieldPanel

from core.helpers import make_translated_interface
from core.panels import SearchEngineOptimisationPanel


class CapitalInvestContactFormPagePanels:
    content_panels = [
        FieldPanel('title'),
        FieldPanel('breadcrumbs_label'),
        FieldPanel('heading'),
        FieldPanel('intro'),
        FieldPanel('comment'),
        FieldPanel('cta_text'),
        SearchEngineOptimisationPanel()
    ]

    settings_panels = [
        FieldPanel('slug'),
    ]

    edit_handler = make_translated_interface(
        content_panels=content_panels,
        settings_panels=settings_panels,
    )


class CapitalInvestContactFormSuccessPagePanels:
    content_panels = [
        FieldPanel('title'),
        FieldPanel('message_box_heading'),
        FieldPanel('message_box_description'),
        FieldPanel('what_happens_next_description')
    ]

    settings_panels = [
        FieldPanel('slug'),
    ]

    edit_handler = make_translated_interface(
        content_panels=content_panels,
        settings_panels=settings_panels,
    )
