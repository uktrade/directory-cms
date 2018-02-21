from unittest.mock import call, patch
import pytest

from find_a_supplier.models import IndustryPage

from core import helpers


@pytest.fixture(autouse=True)
def mock_google_translate():
    stub = patch('google.cloud.translate.Client.translate', side_effect=[
        [{'input': 'this-is-greater', 'translatedText': 'das ist größer'}],
        [{'input': 'this-is-greater', 'translatedText': 'これほど大きい'}],
    ])
    stub.start()
    yield stub
    stub.stop()


@pytest.fixture(autouse=True)
def mock_translated_fields():
    stub = patch(
        'find_a_supplier.models.IndustryPage.get_translatable_fields',
        return_value=['title']
    )
    stub.start()
    yield stub
    stub.stop()


@pytest.mark.django_db
def test_auto_populate_translations(page):
    helpers.auto_populate_translations(page=page, language_codes=['de', 'ja'])

    assert page.title_de == 'das ist größer'
    assert page.title_ja == 'これほど大きい'


@pytest.mark.django_db
@patch('core.helpers.clean_translated_value')
def test_auto_populate_translations_calls_clean_method(
    mock_clean_translated_value, page
):
    helpers.auto_populate_translations(page=page, language_codes=['de', 'ja'])

    assert mock_clean_translated_value.call_count == 2
    assert mock_clean_translated_value.call_args_list == [
        call(page._meta.get_field('title'), 'das ist größer'),
        call(page._meta.get_field('title'), 'これほど大きい'),
    ]


def test_language_code_django_to_google_chinese():
    assert helpers.language_code_django_to_google('zh-hans') == 'zh-CN'


def test_clean_translated_value_slug():
    actual = helpers.clean_translated_value(
        field=IndustryPage._meta.get_field('slug'),
        value='this is great'
    )

    assert actual == 'this-is-great'


def test_clean_translated_value_truncate():
    actual = helpers.clean_translated_value(
        field=IndustryPage._meta.get_field('sector_label'),
        value='a'*300,
    )

    assert actual == 'a'*252 + '...'


def test_clean_translated_value_long_text():
    actual = helpers.clean_translated_value(
        field=IndustryPage._meta.get_field('lede_column_one'),
        value='a'*1000,
    )

    assert actual == 'a'*1000
