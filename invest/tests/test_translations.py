from modeltranslation.translator import translator
import pytest

from invest import models


@pytest.mark.django_db
def test_required_fields_invest_home_page():
    options = translator.get_options_for_model(models.InvestHomePage)
    assert options.required_languages == {
        'en-gb': [
            'heading',
            'sub_heading',
            'subsections',
            'sector_title',
            'setup_guide_title',
            'setup_guide_lead_in',
            'how_we_help_title',
            'how_we_help_lead_in',
            'how_we_help',
            'sector_button_text'
        ]
    }


@pytest.mark.django_db
def test_required_fields_sector_page():
    options = translator.get_options_for_model(models.SectorPage)
    assert options.required_languages == {
        'en-gb': [
            'description',
            'heading',
            'pullout',
            'subsections',
        ]
    }


@pytest.mark.django_db
def test_required_fields_sector_landing_page():
    options = translator.get_options_for_model(models.SectorLandingPage)
    assert options.required_languages == {
        'en-gb': [
            'heading',
        ]
    }


@pytest.mark.django_db
def test_required_fields_info_page():
    options = translator.get_options_for_model(models.InfoPage)
    assert options.required_languages == {
        'en-gb': [
            'content',
        ]
    }


@pytest.mark.django_db
def test_required_fields_setup_guide_page():
    options = translator.get_options_for_model(models.SetupGuidePage)
    assert options.required_languages == {
        'en-gb': [
            'description',
            'heading',
            'sub_heading',
            'subsections',
        ]
    }


@pytest.mark.django_db
def test_required_field_setup_guide_landing_page():
    options = translator.get_options_for_model(models.SetupGuideLandingPage)
    assert options.required_languages == {
        'en-gb': [
            'heading',
            'sub_heading',
            'lead_in',
        ]
    }
