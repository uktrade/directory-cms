from django.core.exceptions import ObjectDoesNotExist
from django import forms

from core import helpers


INCORRECT_SLUG = 'Slug is incorrect.'
ABSOLUTE_INTERNAL_HYPERKINK = (
    'Please use a slug hyperlink. e.g., [%(text)s](slug:the-target-page-slug)'
)


def slug_hyperlinks(value):
    try:
        helpers.render_markdown(value)
    except ObjectDoesNotExist:
        raise forms.ValidationError(INCORRECT_SLUG)
