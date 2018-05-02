from wagtailmarkdown.widgets import (
    MarkdownTextarea as OriginalMarkdownTextarea
)


class MarkdownTextarea(OriginalMarkdownTextarea):

    @property
    def media(self):
        media = super().media
        media.add_js(['core/js/refresh_codemirror.js'])
        return media
