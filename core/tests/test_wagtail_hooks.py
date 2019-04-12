from unittest.mock import Mock

import pytest

from django.utils import translation
from django.urls import reverse

from core import wagtail_hooks


@pytest.mark.django_db
def test_update_default_listing_buttons_from_base_page(page_with_reversion):
    buttons = wagtail_hooks.update_default_listing_buttons(
        page=page_with_reversion, page_perms=Mock()
    )

    assert len(buttons) == 5
    assert buttons[1].url == page_with_reversion.get_url(is_draft=True)


@pytest.mark.django_db
def test_update_default_listing_buttons_not_from_base_page(
    settings, root_page, page_without_specific_type
):
    translation.activate(settings.LANGUAGE_CODE)

    # For the root page, only the 'Add child page' button should be present
    buttons = wagtail_hooks.update_default_listing_buttons(
        page=root_page, page_perms=Mock()
    )
    assert len(buttons) == 1
    assert buttons[0].label == 'Add child page'

    # For any other page without a type, there should also be a 'Delete' button
    buttons = wagtail_hooks.update_default_listing_buttons(
        page=page_without_specific_type, page_perms=Mock()
    )
    assert len(buttons) == 2
    assert buttons[0].label == 'Add child page'
    assert buttons[1].label == 'Delete'


@pytest.mark.django_db
def test_add_copy_button(page_with_reversion):
    page = page_with_reversion
    buttons = list(wagtail_hooks.add_copy_button(page=page, page_perms=None))

    assert len(buttons) == 2
    assert buttons[0].label == 'Copy upstream'
    assert buttons[0].url == reverse('copy-upstream', kwargs={'pk': page.id})
    assert buttons[1].label == 'Update upstream'
    assert buttons[1].url == reverse('update-upstream', kwargs={'pk': page.id})


def test_env_css_set(settings):
    settings.ENVIRONMENT_CSS_THEME_FILE = 'wagtailadmin/css/normalize.css'
    assert 'wagtailadmin/css/normalize.css' in wagtail_hooks.global_admin_css()
    assert wagtail_hooks.global_admin_css().count('<link ') == 2


def test_env_css_unset(settings):
    settings.ENVIRONMENT_CSS_THEME_FILE = None

    assert wagtail_hooks.global_admin_css().count('<link ') == 1
