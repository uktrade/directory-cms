import copy
import os

import bleach
import markdown

from bleach_whitelist import markdown_tags, markdown_attrs
from markdown.extensions.tables import TableExtension
from modeltranslation.utils import build_localized_fieldname
from wagtail.admin.edit_handlers import ObjectList, TabbedInterface
from wagtail.core import hooks
from wagtail.core.models import Page
from wagtail.documents.models import Document
from wagtail.images.models import Image

from django.conf import settings
from django.core.files.storage import default_storage
from django.core.files.images import get_image_dimensions
from django.http import JsonResponse
from django.utils.safestring import mark_safe
from django.utils.translation import trans_real
from django.urls import resolve, Resolver404

from core import permissions


class CachedResponse(JsonResponse):
    pass


def translate_panel(panel, language_code):
    """Convert an English admin editor field ("panel") to e.g, French.

    That is achieved by cloning the English panel and then changing the
    field_name property of the clone.

    Some panels are not fields, but really are fieldsets (which have no name)
    so we just clone then without trying to set the name.

    Some panels have child panels, so those child panels are translated too.

    Arguments:
        panel {Panel} -- English panel to convert
        language_code {str} -- Target conversion language

    Returns:
        Panel -- Translated panel

    """

    panel = copy.deepcopy(panel)
    if hasattr(panel, 'field_name'):
        panel.field_name = build_localized_fieldname(
            field_name=panel.field_name, lang=language_code
        )
    if hasattr(panel, 'relation_name'):
        panel.relation_name = build_localized_fieldname(
            field_name=panel.relation_name, lang=language_code
        )
    if hasattr(panel, 'children'):
        panel.children = [
            translate_panel(child, language_code) for child in panel.children
        ]
    return panel


def make_translated_interface(
    content_panels, settings_panels=None, other_panels=None
):
    panels = []
    for code, name in settings.LANGUAGES:
        panels.append(
            ObjectList(
                [translate_panel(panel, code) for panel in content_panels],
                heading=name
            )
        )
    if settings_panels:
        panels.append(
            ObjectList(
                settings_panels, classname='settings', heading='Settings'
            )
        )
    if other_panels:
        panels += other_panels
    return TabbedInterface(panels)


def get_language_from_querystring(request):
    language_code = request.GET.get('lang')
    language_codes = trans_real.get_languages()
    if language_code and language_code in language_codes:
        return language_code


def get_or_create_document(document_path):
    document = default_storage.get_document_by_path(document_path)
    if not document:
        document_file = default_storage.open(document_path)
        document = Document.objects.create(
            title=os.path.basename(document_path),
            file=document_file,
        )
    return document


def get_or_create_image(image_path):
    image = default_storage.get_image_by_path(image_path)
    if not image:
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


# from https://github.com/wagtail/wagtail/wagtail/tests/utils/form_data.py
def _nested_form_data(data):
    if isinstance(data, dict):
        items = data.items()
    elif isinstance(data, list):
        items = enumerate(data)

    for key, value in items:
        key = str(key)
        if isinstance(value, (dict, list)):
            for child_keys, child_value in _nested_form_data(value):
                yield [key] + child_keys, child_value
        else:
            yield [key], value


# from https://github.com/wagtail/wagtail/wagtail/tests/utils/form_data.py
def nested_form_data(data):
    return {'-'.join(key): value for key, value in _nested_form_data(data)}


# from https://github.com/wagtail/wagtail/wagtail/tests/utils/form_data.py
def inline_formset(items, initial=0, min=0, max=1000):
    def to_form(index, item):
        defaults = {
            'ORDER': str(index),
            'DELETE': '',
        }
        defaults.update(item)
        return defaults

    data_dict = {str(index): to_form(index, item)
                 for index, item in enumerate(items)}

    data_dict.update({
        'TOTAL_FORMS': str(len(data_dict)),
        'INITIAL_FORMS': str(initial),
        'MIN_NUM_FORMS': str(min),
        'MAX_NUM_FORMS': str(max),
    })
    return data_dict


def replace_hook(hook_name, original_fn):
    hooks._hooks[hook_name].remove((original_fn, 0))

    def inner(fn):
        hooks.register('register_page_listing_buttons', fn)
        return fn
    return inner


def get_button_url_name(button):
    try:
        return resolve(button.url).url_name
    except Resolver404:
        return None


def render_markdown(text, context=None):
    html = markdown.markdown(
        text,
        extensions=[
            'markdown.extensions.extra',
            'markdown.extensions.codehilite',
            TableExtension(),
            LinkerExtension()
        ],
        extension_configs={
            'codehilite': [
                ('guess_lang', False),
            ]
        },
        output_format='html5'
    )
    sanitised_html = bleach.clean(html, markdown_tags, markdown_attrs)
    return mark_safe(sanitised_html)


class LinkPattern(markdown.inlinepatterns.LinkPattern):
    def sanitize_url(self, url):
        if url.startswith('slug:'):
            slug = url.split(':')[1]
            page = Page.objects.get(slug=slug).specific
            url = page.url
        return super().sanitize_url(url)


class LinkerExtension(markdown.Extension):
    def extendMarkdown(self, md, md_globals):
        md.inlinePatterns['link'] = LinkPattern(
            markdown.inlinepatterns.LINK_RE, md
        )
