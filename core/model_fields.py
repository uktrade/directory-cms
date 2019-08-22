from django.db.models import TextField

from core import widgets


class MarkdownField(TextField):
    def formfield(self, **kwargs):
        defaults = {
            'widget': widgets.MarkdownTextarea
        }
        defaults.update(kwargs)
        return super(MarkdownField, self).formfield(**defaults)
