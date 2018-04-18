from modeltranslation.translator import TranslationOptions

from django.conf import settings


class BaseTranslationOptions(TranslationOptions):
    @property
    def required_languages(self):
        required_field_names = [
            field.name for field in self.model._meta.fields
            if not field.blank and field.name in self.fields
        ]
        return {settings.LANGUAGE_CODE: required_field_names}
