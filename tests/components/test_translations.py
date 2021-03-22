from modeltranslation.translator import translator
import pytest

from components import models


@pytest.mark.django_db
def test_required_fields_banner_component(en_locale):
    options = translator.get_options_for_model(models.BannerComponent)
    assert options.required_languages == {
        'en-gb': [
            'title',
            'banner_content',
        ]
    }
