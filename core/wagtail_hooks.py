
from wagtail.wagtailadmin.widgets import Button
from wagtail.wagtailcore import hooks

from django.conf import settings
from django.contrib.contenttypes.models import ContentType
from django.shortcuts import render
from django.urls import reverse
from django.shortcuts import redirect

from core import constants, helpers


@hooks.register('before_create_page')
def prepopulate_page(request, parent_page, page_class):
    if constants.PREOPPULATE_PARAM not in request.GET:
        return
    edit_handler_class = page_class.get_edit_handler()
    form_class = edit_handler_class.get_form_class(page_class)
    page = page_class(owner=request.user)
    form = form_class(
        initial=request.GET.dict(),
        instance=page,
        parent_page=parent_page
    )
    return render(request, 'wagtailadmin/pages/create.html', {
        'content_type': ContentType.objects.get_for_model(page),
        'page_class': page_class,
        'parent_page': parent_page,
        'edit_handler': edit_handler_class(instance=page, form=form),
        'preview_modes': page.preview_modes,
        'form': form,
        'has_unsaved_changes': False,
    })


@hooks.register('register_page_listing_buttons')
def add_copy_button(page, page_perms, is_parent=False):
    if hasattr(page, 'build_prepopulate_url'):
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

    page.save_revision(user=request.user,)

    return redirect(reverse('wagtailadmin_pages:edit', args=(page.pk,)))
