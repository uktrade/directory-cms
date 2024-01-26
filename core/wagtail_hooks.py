from wagtail.admin.widgets import Button
from wagtail import hooks

from django.conf import settings
from django.templatetags.static import static
from django.urls import reverse
from django.utils.html import format_html
from core import models


@hooks.register('register_page_listing_more_buttons')
def add_copy_button(page, user=None, next_url=None):
    if isinstance(page, models.BasePage):
        yield Button(
            'Copy upstream',
            reverse('copy-upstream', kwargs={'pk': page.id}),
            attrs={'title': "Copy this page to another environment"},
            priority=80
        )
        yield Button(
            'Update upstream',
            reverse('update-upstream', kwargs={'pk': page.id}),
            attrs={'title': "Update this page on another environment"},
            priority=80
        )


@hooks.register('insert_editor_css')
def editor_css():
    return format_html(
        '<link rel="stylesheet" href="{}">',
        static('core/css/editor.css')
    )


@hooks.register('insert_global_admin_css')
def global_admin_css():
    env_stylesheet = ''

    if settings.ENVIRONMENT_CSS_THEME_FILE:
        env_stylesheet = format_html(
            '<link rel="stylesheet" href="{}">',
            static(settings.ENVIRONMENT_CSS_THEME_FILE)
        )

    return format_html(
        '<link rel="stylesheet" href="{}">',
        static('core/css/global.css')
    ) + env_stylesheet


@hooks.register('insert_editor_js')
def add_sum_required_fields_js():
    return format_html(
        '<script src="{0}"></script>',
        static('core/js/sum_required_localised_fields.js')
    )
