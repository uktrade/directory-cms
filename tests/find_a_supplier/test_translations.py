from modeltranslation.translator import translator
import pytest

from find_a_supplier import models


@pytest.mark.django_db
def test_required_fields_industry_page():
    options = translator.get_options_for_model(models.IndustryPage)
    assert options.required_languages == {
        'en-gb': [
            'title',
            'hero_text',
            'introduction_text',
            'introduction_call_to_action_button_text',
            'introduction_title',
            'introduction_column_one_text',
            'introduction_column_two_text',
            'introduction_column_three_text',
            'breadcrumbs_label',
            'company_list_text',
            'company_list_call_to_action_text'
        ]
    }
