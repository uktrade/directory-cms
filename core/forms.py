import itertools

from modeltranslation.utils import build_localized_fieldname

from django import forms
from django.conf import settings

from wagtail.admin.forms import WagtailAdminPageForm


class CopyToEnvironmentForm(forms.Form):

    environment = forms.ChoiceField(
        label='Website',
        help_text='The website you would like to copy the page to',
        choices=[(url, url) for url in settings.COPY_DESTINATION_URLS]
    )


class WagtailAdminPageForm(WagtailAdminPageForm):
    def __new__(cls, data=None, *args, **kwargs):
        form_class = super().__new__(cls)
        if not data:
            cls.set_required(form_class)
        return form_class

    @staticmethod
    def set_required(form_class):
        fields = form_class._meta.model.get_required_translatable_fields()
        for name, (code, _) in itertools.product(fields, settings.LANGUAGES):
            field_name = build_localized_fieldname(name, lang=code)
            form_class.base_fields[field_name].required = True
