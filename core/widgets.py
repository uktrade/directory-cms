from wagtailmarkdown.widgets import (
    MarkdownTextarea as OriginalMarkdownTextarea
)

from django import forms


class MarkdownTextarea(OriginalMarkdownTextarea):

    @property
    def media(self):
        media = super().media
        return forms.Media(
            css=media._css,
            js=['core/js/refresh_codemirror.js'] + media._js
        )
