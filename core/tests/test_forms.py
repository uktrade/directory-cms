import itertools

from modeltranslation.utils import build_localized_fieldname
import pytest


@pytest.mark.django_db
def test_required_for_language(translated_page, settings, rf):

    edit_handler = translated_page.get_edit_handler()
    form_class = edit_handler.get_form_class()
    form = form_class()
    edit_handler.bind_to_instance(
        instance=translated_page,
        form=form,
        request=rf
    )

    fields = translated_page.get_required_translatable_fields()

    for name, (code, _) in itertools.product(fields, settings.LANGUAGES):
        field_name = build_localized_fieldname(name, lang=code)
        field = form_class.base_fields[field_name]

        if code == settings.LANGUAGE_CODE:
            assert field.required is True
        else:
            assert field.required is False
            assert field.widget.attrs['required_for_language'] is True
            assert field.widget.attrs['class'] == ' required-for-language'


@pytest.mark.django_db
def test_slug_read_only_when_editing_a_page(translated_page, rf):

    edit_handler = translated_page.get_edit_handler()
    form_class = edit_handler.get_form_class()
    form = form_class(instance=translated_page)
    edit_handler.bind_to_instance(
        instance=translated_page,
        form=form,
        request=rf
    )

    assert form.fields['slug'].required is False
    assert form.fields['slug'].disabled is True


@pytest.mark.django_db
def test_slug_editable_when_creating_a_page(translated_page, rf):

    edit_handler = translated_page.get_edit_handler()
    form_class = edit_handler.get_form_class()
    form = form_class()
    edit_handler.bind_to_instance(
        instance=translated_page,
        form=form,
        request=rf
    )

    assert form.fields['slug'].required is True
    assert form.fields['slug'].disabled is False
