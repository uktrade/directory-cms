from wagtail.wagtailadmin.widgets import Button
from wagtail.wagtailcore import hooks

from django.conf import settings
from django.urls import reverse
from django.shortcuts import redirect

from core import helpers


@hooks.register('register_page_listing_buttons')
def add_copy_button(page, page_perms, is_parent=False):
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
