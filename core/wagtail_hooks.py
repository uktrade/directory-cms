from wagtail.admin.widgets import Button
from wagtail.core import hooks
from wagtail.admin.wagtail_hooks import page_listing_buttons

from django.conf import settings
from django.contrib.staticfiles.templatetags.staticfiles import static
from django.urls import reverse
from django.utils.html import format_html
from core import helpers, models


@hooks.register('register_page_listing_more_buttons')
def add_copy_button(page, page_perms, is_parent=False):
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


@helpers.replace_hook('register_page_listing_buttons', page_listing_buttons)
def update_default_listing_buttons(page, page_perms, is_parent=False):
    buttons = list(page_listing_buttons(page, page_perms, is_parent))
    if isinstance(page, models.BasePage):
        for button in buttons:
            if helpers.get_button_url_name(button) == 'view_draft':
                button.url = page.get_url(is_draft=True)
    else:
        # for non-subclasses-of-BasePage allow only adding children
        allowed_urls = ['add_subpage']
        buttons = [
            button for button in buttons
            if helpers.get_button_url_name(button) in allowed_urls
        ]
    return buttons


@hooks.register('insert_editor_css')
def editor_css():
    return format_html(
        '<link rel="stylesheet" href="{}">',
        static('core/css/main.css')
    )


@hooks.register('insert_global_admin_css')
def global_admin_css():
    if settings.ENVIRONMENT_CSS_THEME_FILE:
        return format_html(
            '<link rel="stylesheet" href="{}">',
            static(settings.ENVIRONMENT_CSS_THEME_FILE)
        )
