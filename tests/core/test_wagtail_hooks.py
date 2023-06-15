from unittest.mock import Mock

import pytest
import re

from django.utils import translation
from django.urls import reverse

from core import wagtail_hooks


@pytest.mark.django_db
def test_update_default_listing_buttons_from_base_page(page_with_reversion):
    buttons = wagtail_hooks.update_default_listing_buttons(
        page=page_with_reversion, page_perms=Mock()
    )

    expected_url = 'http://great.gov.uk/international/content/123-555-207/'
    assert len(buttons) == 4
    assert buttons[1].url == expected_url


@pytest.mark.django_db
def test_update_default_listing_buttons_from_base_page_button_url_name_view_draft(
    page_with_reversion
):
    import pdb
    button_url_name = 'view_draft'
    buttons = wagtail_hooks.update_default_listing_buttons(
        page=page_with_reversion, page_perms=Mock(), button_url_name=button_url_name,
    )

    expected_url = r'http://great[.]gov[.]uk/international/content/123-555-209/[?]draft_token=\w+'
    assert len(buttons) == 4
    pdb;pdb.set_trace()
    assert re.match(expected_url, buttons[1].url)


@pytest.mark.django_db
def test_update_default_listing_buttons_not_from_base_page(
    settings, page_without_specific_type
):
    translation.activate(settings.LANGUAGE_CODE)

    # For a page without a type, there should also be an 'Add child page'
    # and 'Delete' button
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


@pytest.mark.django_db
def test_env_css_set(settings):
    settings.ENVIRONMENT_CSS_THEME_FILE = 'wagtailadmin/css/normalize.css'
    assert 'wagtailadmin/css/normalize.css' in wagtail_hooks.global_admin_css()
    assert wagtail_hooks.global_admin_css().count('<link ') == 2


@pytest.mark.django_db
def test_env_css_unset(settings):
    settings.ENVIRONMENT_CSS_THEME_FILE = None

    assert wagtail_hooks.global_admin_css().count('<link ') == 1
