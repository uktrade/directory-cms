from unittest.mock import patch

import pytest
from wagtail.wagtailimages.models import Image

from django.core.files.storage import default_storage
from django.core.files.uploadedfile import SimpleUploadedFile


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
