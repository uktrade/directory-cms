from modeltranslation.translator import translator
import pytest

from invest import models


@pytest.mark.django_db
def test_required_fields_invest_home_page():
    options = translator.get_options_for_model(models.InvestHomePage)
    assert options.required_languages == {
        'en-gb': [
            'title',
            'slug',
            'heading',
            'sub_heading',
            'sector_title',
            'sector_button_text',
            'setup_guide_title',
            'how_we_help_title'
        ]
    }


@pytest.mark.django_db
def test_required_fields_invest_sector_page():
    options = translator.get_options_for_model(models.SectorPage)
    assert options.required_languages == {
        'en-gb': [
            'title',
            'slug',
            'description',
            'heading',
        ]
    }


@pytest.mark.django_db
def test_required_fields_invest_sector_landing_page():
    options = translator.get_options_for_model(models.SectorLandingPage)
    assert options.required_languages == {
        'en-gb': [
            'title',
            'slug',
            'heading',
        ]
    }


@pytest.mark.django_db
def test_required_fields_invest_info_page():
    options = translator.get_options_for_model(models.InfoPage)
    assert options.required_languages == {
        'en-gb': [
            'title',
            'slug',
            'content',
        ]
    }


@pytest.mark.django_db
def test_required_fields_invest_setup_guide_page():
    options = translator.get_options_for_model(models.SetupGuidePage)
    assert options.required_languages == {
        'en-gb': [
            'title',
            'slug',
            'description',
            'heading',
            'sub_heading',
        ]
    }


@pytest.mark.django_db
def test_required_field_invest_setup_guide_landing_page():
    options = translator.get_options_for_model(models.SetupGuideLandingPage)
    assert options.required_languages == {
        'en-gb': [
            'title',
            'slug',
            'heading',
            'sub_heading',
        ]
    }
