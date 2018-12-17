from django import forms

from wagtail.utils.widgets import WidgetWithScript


class MarkdownTextarea(WidgetWithScript, forms.widgets.Textarea):

    @property
    def media(self):
        return forms.Media(
            css={
                'all': (
                    'https://cdn.jsdelivr.net/simplemde/latest/simplemde.min.css',
                )
            },
            js=(
                'https://cdn.jsdelivr.net/simplemde/latest/simplemde.min.js',
                'core/js/refresh_codemirror.js'
            )
        )
