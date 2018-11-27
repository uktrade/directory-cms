from wagtailmarkdown.fields import MarkdownField as OriginalMarkdownField

from core import validators as core_validators, widgets


class MarkdownField(OriginalMarkdownField):
    def __init__(self, validators=None, *args, **kwargs):
        validators = validators or []
        if core_validators.slug_hyperlinks not in validators:
            validators.append(core_validators.slug_hyperlinks)
        super().__init__(validators=validators, *args, **kwargs)

    def formfield(self, **kwargs):
        kwargs['widget'] = widgets.MarkdownTextarea
        return super().formfield(**kwargs)
