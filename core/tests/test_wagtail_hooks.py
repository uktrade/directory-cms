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
    settings, root_page
):
    translation.activate(settings.LANGUAGE_CODE)

    buttons = wagtail_hooks.update_default_listing_buttons(
        page=root_page, page_perms=Mock()
    )

    assert len(buttons) == 1
    assert buttons[0].label == 'Add child page'


@pytest.mark.django_db
def test_add_copy_button(page_with_reversion):
    page = page_with_reversion
    buttons = list(wagtail_hooks.add_copy_button(page=page, page_perms=None))

    assert len(buttons) == 2
    assert buttons[0].label == 'Copy upstream'
    assert buttons[0].url == reverse('copy-upstream', kwargs={'pk': page.id})
    assert buttons[1].label == 'Update upstream'
    assert buttons[1].url == reverse('update-upstream', kwargs={'pk': page.id})


def test_env_dependent_global_admin_css_set(settings):
    settings.ENVIRONMENT_CSS_THEME_FILE = 'wagtailadmin/css/normalize.css'
    assert (
        'wagtailadmin/css/normalize.css'
    ) in wagtail_hooks.env_dependent_global_admin_css()


def test_env_dependent_global_admin_css_unset(settings):
    settings.ENVIRONMENT_CSS_THEME_FILE = None

    assert wagtail_hooks.env_dependent_global_admin_css() == ''
