from unittest.mock import patch

import pytest
from wagtail.admin.widgets import PageListingButton
from django.urls import reverse

from core import helpers


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
