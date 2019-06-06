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

    @property
    def media(self):
        media = super().media
        media.add_js(['core/js/sum_required_localised_fields.js'])
        return media

    def __new__(cls, data=None, *args, **kwargs):
        form_class = super().__new__(cls)
        cls.set_required_for_language(form_class)
        cls.set_read_only(form_class)
        return form_class

    def __init__(self, *args, **kwargs):
        """Set slug to read only if editing an existing page."""
        instance = kwargs.get('instance')
        if instance and instance.pk:
            field = self.base_fields.get('slug')  # App pages don't have slug
            if field:
                field.disabled = True
                field.required = False
        super().__init__(*args, **kwargs)

    @staticmethod
    def set_read_only(form_class):
        for field_name in form_class._meta.model.read_only_fields:
            if field_name in form_class.base_fields:
                field = form_class.base_fields[field_name]
                field.disabled = True
                field.required = False

    @staticmethod
    def set_required_for_language(form_class):
        """Mark fields that must be populated for a language to be available.

        Some fields are optional, but for their language to be available the
        field must be populated e.g., for German to be available for a page
        then the fields title_de and description_de must must be populated.

        `required_for_language` is used by templates to style the page and hint
        the user which fields they need to populate.

        Arguments:
            form_class {WagtailAdminPageForm}

        """

        css_classname = 'required-for-language'
        fields = form_class._meta.model.get_required_translatable_fields()
        for name, (code, _) in itertools.product(fields, settings.LANGUAGES):
            field_name = build_localized_fieldname(name, lang=code)
            field = form_class.base_fields[field_name]
            if field.required is False:
                attrs = field.widget.attrs
                attrs['required_for_language'] = True
                attrs['class'] = attrs.get('class', '') + ' ' + css_classname


class WagtailAdminPageExclusivePageForm(WagtailAdminPageForm):

    def __init__(self, *args, **kwargs):
        if(
            hasattr(self._meta.model, 'slug_identity')
            and 'initial' not in kwargs
        ):
            kwargs['initial'] = {
                'slug': self._meta.model.slug_identity
            }
        super().__init__(*args, **kwargs)


class BaseAppAdminPageForm(WagtailAdminPageExclusivePageForm):

    @staticmethod
    def set_required_for_language(form_class):
        pass
