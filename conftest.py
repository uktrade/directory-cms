from unittest.mock import patch

import pytest
from wagtail.wagtailcore.models import Page
from wagtail.wagtailimages.models import Image

from django.core.files.storage import default_storage
from django.core.files.uploadedfile import SimpleUploadedFile

from find_a_supplier.tests.factories import IndustryPageFactory


@pytest.fixture
def untranslated_page():
    return IndustryPageFactory(
        parent=Page.objects.get(pk=1),
        title_en_gb='ENGLISH',
        breadcrumbs_label_en_gb='label',
        introduction_text_en_gb='lede',
        search_description_en_gb='description',
        hero_text_en_gb='hero text',
        introduction_column_one_text_en_gb='lede column one',
        introduction_column_two_text_en_gb='lede column two',
        introduction_column_three_text_en_gb='lede column three',
        company_list_text_en_gb='companies',
        company_list_call_to_action_text_en_gb='view all',
    )


@pytest.fixture(autouse=True)
def mock_signature_check():
    stub = patch('config.signature.SignatureCheckPermission.has_permission')
    stub.start()
    yield stub
    stub.stop()


@pytest.fixture
def enable_signature_check(mock_signature_check):
    mock_signature_check.stop()
    yield
    mock_signature_check.start()


@pytest.fixture(autouse=True)
def mock_auth():
    stub = patch('google.auth.default', return_value=[None, None])
    stub.start()
    yield stub
    stub.stop()


@pytest.fixture
def uploaded_file():
    return SimpleUploadedFile(
        name='test_image.png',
        content=open('core/static/core/logo.png', 'rb').read(),
        content_type='image/png'
    )


@pytest.fixture
def image(uploaded_file):
    image = Image.objects.create(
        file=uploaded_file,
        title='test',
        width=100,
        height=100,
    )
    yield image
    default_storage.delete(image.file.name)
