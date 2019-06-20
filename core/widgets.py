import json
from django import forms

from django.utils.safestring import mark_safe
from wagtail.utils.widgets import WidgetWithScript


class MarkdownTextarea(WidgetWithScript, forms.widgets.Textarea):
    def __init__(self, **kwargs):
        super(MarkdownTextarea, self).__init__(**kwargs)

    def render_js_init(self, id_, name, value):
        return 'simplemdeAttach("{0}");'.format(id_)

    @property
    def media(self):
        return forms.Media(
            css={
                'all': (
                    'https://cdn.jsdelivr.net/simplemde/latest/simplemde.min.css',  # NOQA
                )
            },
            js=(
                'https://cdn.jsdelivr.net/simplemde/latest/simplemde.min.js',
                'core/js/refresh_codemirror.js',
                'wagtailadmin/js/page-chooser-modal.js',
            )
        )


class Select2WidgetMediaMixin:
    class Media:
        css = {
            'all': (
                'core/js/select2/select2.css',
                'core/js/select2/select2-wagtailadmin.css'
            )
        }
        js = ('core/js/select2/select2.min.js',)


class Select2RenderWithOptionsMixin:

    def __init__(self, *args, select2_options={}, **kwargs):
        super().__init__(*args, **kwargs)
        self.select2_options = select2_options

    def render(self, name, value, attrs=None, renderer=None):
        html = super().render(name, value, attrs, renderer)
        extra = mark_safe('\n'.join((
            "<script>$(function () {",
            "   $('select[name=\"{field_name}\"]').select2({options});".format(
                    field_name=name, options=json.dumps(self.select2_options)
                ),
            "});</script>"
        )))
        return html + extra


class Select2Widget(
    Select2WidgetMediaMixin,
    Select2RenderWithOptionsMixin,
    forms.Select
):
    pass


class Select2MultipleWidget(
    Select2WidgetMediaMixin,
    Select2RenderWithOptionsMixin,
    forms.SelectMultiple
):
    pass
