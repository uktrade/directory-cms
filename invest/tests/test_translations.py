from modeltranslation.translator import translator
import pytest

from invest import models


@pytest.mark.django_db
def test_required_fields_invest_home_page():
    options = translator.get_options_for_model(models.InvestHomePage)
    assert options.required_languages == {
        'en-gb': [
            'title',
            'breadcrumbs_label',
            'heading',
            'sub_heading',
            'benefits_section_title',
            'capital_invest_section_title',
            'sector_title',
            'sector_button_text',
            'hpo_title',
            'setup_guide_title',
            'setup_guide_call_to_action_text',
            'how_we_help_title',
            'how_we_help_text_one',
            'how_we_help_text_two',
            'how_we_help_text_three',
            'how_we_help_text_four',
            'how_we_help_text_five',
            'contact_section_title',
            'contact_section_call_to_action_text'
        ]
    }


@pytest.mark.django_db
def test_required_fields_invest_sector_page():
    options = translator.get_options_for_model(models.SectorPage)
    assert options.required_languages == {
        'en-gb': [
            'title',
            'description',
            'heading',
            'subsection_title_one',
            'subsection_content_one',
            'subsection_title_two',
            'subsection_content_two'
        ]
    }


@pytest.mark.django_db
def test_required_fields_invest_sector_landing_page():
    options = translator.get_options_for_model(models.SectorLandingPage)
    assert options.required_languages == {
        'en-gb': [
            'title',
            'heading',
        ]
    }


@pytest.mark.django_db
def test_required_fields_invest_info_page():
    options = translator.get_options_for_model(models.InfoPage)
    assert options.required_languages == {
        'en-gb': [
            'title',
            'content',
        ]
    }


@pytest.mark.django_db
def test_required_fields_invest_setup_guide_page():
    options = translator.get_options_for_model(models.SetupGuidePage)
    assert options.required_languages == {
        'en-gb': [
            'title',
            'description',
            'heading',
            'sub_heading',
            'subsection_title_one',
            'subsection_content_one',
            'subsection_title_two',
            'subsection_content_two'
        ]
    }


@pytest.mark.django_db
def test_required_field_invest_setup_guide_landing_page():
    options = translator.get_options_for_model(models.SetupGuideLandingPage)
    assert options.required_languages == {
        'en-gb': [
            'title',
            'heading',
            'sub_heading',
        ]
    }
