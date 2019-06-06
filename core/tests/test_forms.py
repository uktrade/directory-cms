import itertools
import pytest

from modeltranslation.utils import build_localized_fieldname

from great_international.models import InternationalHomePage
from core import forms


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
        request=rf.get(path='/')
    )

    assert form.fields['slug'].required is True
    assert form.fields['slug'].disabled is False


@pytest.mark.django_db
def test_wagtailadminexclusivepageform_when_slug_identity_set_on_model(rf):
    edit_handler = InternationalHomePage.get_edit_handler()
    form_class = edit_handler.get_form_class()
    form = form_class()
    assert isinstance(form, forms.WagtailAdminPageExclusivePageForm)

    edit_handler.bind_to_instance(
        instance=InternationalHomePage(),
        form=form,
        request=rf.get(path='/')
    )

    assert form.fields['slug'].required is True
    assert form.fields['slug'].disabled is False
    assert form.initial['slug'] == InternationalHomePage.slug_identity


@pytest.mark.django_db
def test_wagtailadminexclusivepageform_when_slug_identity_not_set_on_model(rf):
    # temporarily remove the slug_identity attribute
    slug_identity = InternationalHomePage.slug_identity
    del InternationalHomePage.slug_identity

    try:
        edit_handler = InternationalHomePage.get_edit_handler()
        form_class = edit_handler.get_form_class()
        form = form_class()
        assert isinstance(form, forms.WagtailAdminPageExclusivePageForm)

        edit_handler.bind_to_instance(
            instance=InternationalHomePage(),
            form=form,
            request=rf.get('/')
        )

        assert form.fields['slug'].required is True
        assert form.fields['slug'].disabled is False
        assert 'slug' not in form.initial
    finally:
        # using finally to ensure slug_identity always restored
        InternationalHomePage.slug_identity = slug_identity
