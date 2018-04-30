from unittest.mock import call, patch

import pytest
from wagtail.admin.widgets import PageListingButton

from django.urls import reverse

from core import helpers
from find_a_supplier.models import IndustryPage


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


def test_clean_translated_value_html_entity():
    actual = helpers.clean_translated_value(
        field=IndustryPage._meta.get_field('breadcrumbs_label'),
        value='&pound;682m &#39;',
    )

    assert actual == '£682m \''


def test_clean_translated_value_truncate():
    actual = helpers.clean_translated_value(
        field=IndustryPage._meta.get_field('breadcrumbs_label'),
        value='a'*300,
    )

    assert actual == 'a'*47 + '...'


def test_clean_translated_value_long_text():
    actual = helpers.clean_translated_value(
        field=IndustryPage._meta.get_field('introduction_column_one_text'),
        value='a'*1000,
    )

    assert actual == 'a'*1000


@pytest.mark.django_db
def test_get_or_create_image_existing(image):
    actual = helpers.get_or_create_image(image.file.name)

    assert actual == image


@pytest.mark.django_db
def test_get_or_create_image_new(image, uploaded_file):
    image.delete()

    actual = helpers.get_or_create_image('original_images/test_image.png')

    assert actual.file.name == 'original_images/test_image.png'


@pytest.mark.django_db
def test_get_button_url_name_internal_url(page):
    button = PageListingButton(
        'View draft',
        reverse('wagtailadmin_pages:view_draft', args=[page.id]),
    )

    assert helpers.get_button_url_name(button) == 'view_draft'


def test_get_button_url_name_external_url():
    button = PageListingButton('View draft', 'http://www.example.com')

    assert helpers.get_button_url_name(button) is None
