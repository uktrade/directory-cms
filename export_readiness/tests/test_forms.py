import pytest

from export_readiness import models


@pytest.mark.django_db
@pytest.mark.parametrize('model_class', (
    models.TermsAndConditionsPage, models.PrivacyAndCookiesPage
))
def test_terms_slug(model_class):
    instance = model_class()
    edit_handler = model_class.get_edit_handler()
    form_class = edit_handler.get_form_class()
    form = form_class()
    edit_handler.bind_to_instance(instance=instance, form=form)

    assert form.initial == {'slug_en_gb': model_class.slug_identity}
