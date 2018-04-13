from wagtail.wagtailadmin.widgets import Button
from wagtail.wagtailcore import hooks
from wagtail.wagtailadmin.wagtail_hooks import page_listing_buttons

from django.conf import settings
from django.contrib.staticfiles.templatetags.staticfiles import static
from django.shortcuts import redirect
from django.urls import reverse
from django.utils.html import format_html
from core import helpers, models


@hooks.register('register_page_listing_buttons')
def add_copy_button(page, page_perms, is_parent=False):
    if isinstance(page, models.BasePage):
        yield Button(
            'Copy upstream',
            reverse('copy-to-environment', kwargs={'pk': page.id}),
            attrs={'title': "Copy this page to another environment"},
            classes={
                'button', 'button-small', 'bicolor', 'icon', 'white',
                'icon-site'
            },
            priority=40
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


@hooks.register('after_edit_page')
def translate_page(request, page):
    if 'action-translate' not in request.POST:
        return

    page = page.get_latest_revision_as_page()
    language_codes = [
        code for code, name in settings.LANGUAGES
        if code != settings.LANGUAGE_CODE
    ]
    helpers.auto_populate_translations(page, language_codes)

    page.save_revision(user=request.user)

    return redirect(reverse('wagtailadmin_pages:edit', args=(page.pk,)))


@hooks.register('insert_editor_css')
def editor_css():
    return format_html(
        '<link rel="stylesheet" href="{}">',
        static('core/css/main.css')
    )
