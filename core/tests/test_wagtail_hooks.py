from unittest.mock import Mock

import pytest
from wagtail.wagtailcore.models import Page

from core import wagtail_hooks


@pytest.mark.django_db
def test_update_default_listing_buttons_from_base_page(page_with_reversion):
    buttons = wagtail_hooks.update_default_listing_buttons(
        page=page_with_reversion, page_perms=Mock()
    )

    assert len(buttons) == 5
    assert buttons[1].url == page_with_reversion.get_url(is_draft=True)


@pytest.mark.django_db
def test_update_default_listing_buttons_not_from_base_page():
    page = Page.objects.get(pk=1)

    buttons = wagtail_hooks.update_default_listing_buttons(
        page=page, page_perms=Mock()
    )

    assert len(buttons) == 1
    assert buttons[0].label == 'Add child page'
