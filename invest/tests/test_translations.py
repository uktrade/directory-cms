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
            'subsection_title_one',
            'subsection_content_one',
            'subsection_title_two',
            'subsection_content_two',
            'subsection_title_three',
            'subsection_content_three',
            'subsection_title_four',
            'subsection_content_four',
            'subsection_title_five',
            'subsection_content_five',
            'subsection_title_six',
            'subsection_content_six',
            'subsection_title_seven',
            'subsection_content_seven',
            'sector_title',
            'sector_button_text',
            'setup_guide_title',
            'how_we_help_title',
            'how_we_help_text_one',
            'how_we_help_icon_one',
            'how_we_help_text_two',
            'how_we_help_icon_two',
            'how_we_help_text_three',
            'how_we_help_icon_three',
            'how_we_help_text_four',
            'how_we_help_icon_four',
            'how_we_help_text_five',
            'how_we_help_icon_five',
            'how_we_help_text_six',
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
            'pullout',
            'pullout_text',
            'pullout_stat',
            'pullout_stat_text',
            'subsection_title_one',
            'subsection_content_one',
            'subsection_info_one',
            'subsection_map_one',
            'subsection_title_two',
            'subsection_content_two',
            'subsection_info_two',
            'subsection_map_two',
            'subsection_title_three',
            'subsection_content_three',
            'subsection_info_three',
            'subsection_map_three',
            'subsection_title_four',
            'subsection_content_four',
            'subsection_info_four',
            'subsection_map_four',
            'subsection_title_five',
            'subsection_content_five',
            'subsection_info_five',
            'subsection_map_five',
            'subsection_title_six',
            'subsection_content_six',
            'subsection_info_six',
            'subsection_map_six',
            'subsection_title_seven',
            'subsection_content_seven',
            'subsection_info_seven',
            'subsection_map_seven'
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
            'subsection_title_one',
            'subsection_content_one',
            'subsection_title_two',
            'subsection_content_two',
            'subsection_title_three',
            'subsection_content_three',
            'subsection_title_four',
            'subsection_content_four',
            'subsection_title_five',
            'subsection_content_five',
            'subsection_title_six',
            'subsection_content_six',
            'subsection_title_seven',
            'subsection_content_seven',
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
