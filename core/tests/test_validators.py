import pytest

from django import forms

from core import validators


@pytest.mark.django_db
def test_slug_hyperlinks_correct_link(page):
    markdown = '[the link](slug:{slug})'.format(slug=page.slug)
    assert validators.slug_hyperlinks(markdown) is None


@pytest.mark.django_db
def test_slug_hyperlinks_incorret_link():
    markdown = '[the link](slug:some-slug)'
    with pytest.raises(forms.ValidationError):
        validators.slug_hyperlinks(markdown)


def test_no_absolute_internal_hyperlinks_correct_link():
    markdown = '[the link](http://www.google.com)'
    assert validators.no_absolute_internal_hyperlinks(markdown) is None


def test_no_absolute_internal_hyperlinks_incorrect_link(settings):
    markdown = '[the link]({url})'.format(url=settings.APP_URL_FIND_A_SUPPLIER)
    with pytest.raises(forms.ValidationError):
        validators.no_absolute_internal_hyperlinks(markdown)
