from unittest.mock import patch, Mock

from botocore.exceptions import EndpointConnectionError
import pytest

from core import models, storage_backends


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


@pytest.mark.django_db
def test_immutable_file_storage_get_image_by_path_exists(page):

    image_hash = models.ImageHash.objects.all().first()

    backend = storage_backends.ImmutableFilesS3Boto3Storage()
    with patch.object(backend.connection, 'ObjectSummary') as mock:
        mock.return_value = Mock(e_tag='"{}"'.format(image_hash.content_hash))
        image_path = image_hash.image.file.url
        image = backend.get_image_by_path(image_path)

    assert image == image_hash.image


@pytest.mark.django_db
def test_immutable_file_storage_get_image_by_path_not_exist_in_bucket():
    backend = storage_backends.ImmutableFilesS3Boto3Storage()
    with patch.object(backend.connection, 'ObjectSummary') as mock:
        mock.side_effect = EndpointConnectionError(endpoint_url='/')
        image = backend.get_image_by_path('/thing.png')

    assert image is None


@pytest.mark.django_db
def test_immutable_file_storage_get_image_by_path_not_exist_in_database():
    backend = storage_backends.ImmutableFilesS3Boto3Storage()
    with patch.object(backend.connection, 'ObjectSummary') as mock:
        mock.return_value = Mock(e_tag='"123455"')
        image = backend.get_image_by_path('/thing.png')

    assert image is None


@pytest.mark.django_db
def test_immutable_file_storage_get_document_by_path_exists(
    high_potential_opportunity_page
):
    document_hash = models.DocumentHash.objects.all().first()

    backend = storage_backends.ImmutableFilesS3Boto3Storage()
    with patch.object(backend.connection, 'ObjectSummary') as mock:
        mock.return_value = Mock(
            e_tag='"{}"'.format(document_hash.content_hash)
        )
        document_path = document_hash.document.file.url
        document = backend.get_document_by_path(document_path)

    assert document == document_hash.document


@pytest.mark.django_db
def test_immutable_file_storage_get_document_by_path_not_exist_in_bucket():
    backend = storage_backends.ImmutableFilesS3Boto3Storage()
    with patch.object(backend.connection, 'ObjectSummary') as mock:
        mock.side_effect = EndpointConnectionError(endpoint_url='/')
        document = backend.get_document_by_path('/thing.png')

    assert document is None


@pytest.mark.django_db
def test_immutable_file_storage_get_document_by_path_not_exist_in_database():
    backend = storage_backends.ImmutableFilesS3Boto3Storage()
    with patch.object(backend.connection, 'ObjectSummary') as mock:
        mock.return_value = Mock(e_tag='"123455"')
        document = backend.get_document_by_path('/thing.png')

    assert document is None
