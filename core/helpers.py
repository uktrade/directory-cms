import copy
import functools
import os

import gevent
from google.cloud import translate
from modeltranslation.utils import build_localized_fieldname
from wagtail.wagtailadmin.edit_handlers import ObjectList, TabbedInterface
from wagtail.wagtailimages.models import Image

from django.conf import settings
from django.core.files.storage import default_storage
from django.core.files.images import get_image_dimensions
from django.utils.translation import trans_real
from django.utils.text import slugify, Truncator

from core import models, permissions


def build_translated_fieldname(field_name):
    return 'translated_' + field_name


def make_language_panel(untranslated_panel, language_code):
    """Convert an English admin editor field ("panel") to e.g, French.

    That is achieved by cloning the English panel and then changing the
    field_name property of the clone.

    Some panels are not fields, but really are fieldsets (which have no name)
    so we just clone then without trying to set the name.

    Arguments:
        untranslated_panel {Panel} -- English panel to convert
        language_code {str} -- Target conversion language

    Returns:
        Panel -- Translated panel

    """

    panel = copy.deepcopy(untranslated_panel)
    if hasattr(panel, 'field_name'):
        panel.field_name = build_localized_fieldname(
            field_name=untranslated_panel.field_name, lang=language_code
        )
    return panel


def make_language_panels(content_panels, language_code):
    """Convert English admin editor fields ("panels") to e.g, French.

    Given a list of panels with names such as "intro" and "image"
    return a new list of panels with names such as "intro_fr" and "image_fr".

    Arguments:
        content_panels {Panel[]} -- English panels to convert
        language_code {str} -- Target conversion language

    Returns:
        Panel[] -- Translated panels

    """

    translated_panel_builder = functools.partial(
        make_language_panel, language_code=language_code
    )
    panels = []
    for untranslated_panel in content_panels:
        panel = translated_panel_builder(untranslated_panel)
        if hasattr(panel, 'children'):
            panel.children = map(translated_panel_builder, panel.children)
        panels.append(panel)
    return panels


def make_translated_interface(content_panels, other_panels):
    translated_panels = [
        ObjectList(make_language_panels(content_panels, code), heading=name)
        for code, name in settings.LANGUAGES
    ]
    return TabbedInterface(translated_panels + other_panels)


def get_language_from_querystring(request):
    language_code = request.GET.get('lang')
    language_codes = trans_real.get_languages()
    if language_code and language_code in language_codes:
        return language_code


def auto_populate_translations(page, language_codes):
    translate_client = translate.Client()
    field_names = page.get_translatable_fields()
    language_codes = [
        {'django': code, 'google': language_code_django_to_google(code)}
        for code in language_codes
    ]
    translator = functools.partial(
        gevent.Greenlet.spawn,
        translate_client.translate,
        values=[getattr(page, name) for name in field_names],
        source_language='en',
    )
    gevent_threads = [
        translator(target_language=language_code['google'])
        for language_code in language_codes
    ]
    gevent.joinall(gevent_threads)

    for gevent_thread, language_code in zip(gevent_threads, language_codes):
        for translation, field_name in zip(gevent_thread.value, field_names):
            field = page._meta.get_field(field_name)
            setattr(
                page,
                build_localized_fieldname(field_name, language_code['django']),
                clean_translated_value(field, translation['translatedText']),
            )


def clean_translated_value(field, value):
    if field.name == 'slug':
        value = slugify(value)
    elif field.max_length:
        value = Truncator(text=value).chars(num=field.max_length)
    return value


def language_code_django_to_google(code):
    return {
        'zh-hans': 'zh-CN',
    }.get(code, code)


def get_or_create_image(image_path):
    object_summary = default_storage.connection.ObjectSummary(
        bucket_name=default_storage.bucket_name,
        key=image_path
    )
    queryset = models.ImageHash.objects.filter(
        content_hash=object_summary.e_tag[1:-1]
    )
    if queryset.exists():
        image = queryset.first().image
    else:
        image_file = default_storage.open(image_path)
        width, height = get_image_dimensions(image_file)
        image = Image.objects.create(
            title=os.path.basename(image_path),
            width=width,
            height=height,
            file=image_path,
        )
    return image


def is_draft_requested(request):
    return permissions.DraftTokenPermisison.TOKEN_PARAM in request.GET
