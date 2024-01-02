import pytest

from django.urls import reverse

from core import wagtail_hooks


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
