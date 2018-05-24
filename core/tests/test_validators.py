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
