from urllib.parse import urlparse

import markdown

from django.core.exceptions import ObjectDoesNotExist
from django import forms

from core import constants,  helpers


INCORRECT_SLUG = 'Slug is incorrect.'
ABSOLUTE_INTERNAL_HYPERKINK = (
    'Please use a slug hyperlink. e.g., [%(text)s](slug:the-target-page-slug)'
)


def slug_hyperlinks(value):
    try:
        helpers.render_markdown(value)
    except ObjectDoesNotExist:
        raise forms.ValidationError(INCORRECT_SLUG)


def no_absolute_internal_hyperlinks(value):
    md = markdown.Markdown()
    md.convert(value)
    pattern = markdown.inlinepatterns.LinkPattern(
        markdown.inlinepatterns.LINK_RE, md
    )

    domains = set(
        urlparse(url).netloc for url in constants.APP_URLS.values()
    )
    for match in pattern.getCompiledRegExp().finditer(value):
        element = pattern.handleMatch(match)
        parsed = urlparse(element.get('href') or '')
        if parsed.netloc in domains:
            raise forms.ValidationError(
                ABSOLUTE_INTERNAL_HYPERKINK, params={'text': element.text}
            )
