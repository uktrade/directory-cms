from unittest.mock import patch

from core import storage_backends


def test_settings(settings):
    assert settings.DEFAULT_FILE_STORAGE == (
        'core.storage_backends.ImmutableFilesS3Boto3Storage'
    )


@patch('django.core.files.storage.Storage.delete')
def test_delete_disabled(mock_delete):
    backend = storage_backends.ImmutableFilesS3Boto3Storage()

    backend.delete('some/name.png')

    assert mock_delete.call_count == 0


def test_replace_disabled():
    assert (
        storage_backends.ImmutableFilesS3Boto3Storage.file_overwrite is False
    )


def test_replace_disabled_hardcoded(settings):
    settings.AWS_S3_FILE_OVERWRITE = True

    assert (
        storage_backends.ImmutableFilesS3Boto3Storage.file_overwrite is False
    )
