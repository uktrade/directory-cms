import functools
import os

import gevent
from google.cloud import translate
from modeltranslation.utils import build_localized_fieldname
from wagtail.wagtailadmin.edit_handlers import (
    FieldPanel, ObjectList, TabbedInterface
)
from wagtail.wagtailimages.models import Image

from django.conf import settings
from django.core.files.storage import default_storage
from django.core.files.images import get_image_dimensions
from django.utils.translation import trans_real
from django.utils.text import slugify, Truncator

from core import models


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


def make_translated_interface(content_panels, other_panels):
    return TabbedInterface(make_language_panels(content_panels) + other_panels)


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
