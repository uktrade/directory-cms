from django.core.exceptions import ObjectDoesNotExist
from django import forms

from core import helpers


INCORRECT_SLUG = 'Slug is incorrect.'


def slug_hyperlinks(value):
    try:
        helpers.render_markdown(value)
    except ObjectDoesNotExist:
        raise forms.ValidationError(INCORRECT_SLUG)
