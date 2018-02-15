from modeltranslation.utils import build_localized_fieldname
from wagtail.wagtailadmin.edit_handlers import (
    FieldPanel, ObjectList, TabbedInterface
)

from django.conf import settings
from django.utils import translation


def build_translated_fieldname(field_name):
    return 'translated_' + field_name


def make_language_panel(content_panels, language_code=None):
    return [
        FieldPanel(
            build_localized_fieldname(content_panel.field_name, language_code),
            classname=content_panel.classname
        ) for content_panel in content_panels
    ]


def make_language_panels(content_panels):
    return [
        ObjectList(make_language_panel(content_panels, code), heading=name)
        for code, name in settings.LANGUAGES
    ]


def make_translated_interface(content_panels, settings_panels):
    return TabbedInterface(
        make_language_panels(content_panels) +
        [ObjectList(settings_panels, heading='Settings', classname='settings')]
    )


def get_language_from_querystring(request):
    language_code = request.GET.get('lang')
    language_codes = translation.trans_real.get_languages()
    if language_code and language_code in language_codes:
        return language_code
