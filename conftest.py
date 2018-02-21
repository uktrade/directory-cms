from unittest.mock import patch

import pytest


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
