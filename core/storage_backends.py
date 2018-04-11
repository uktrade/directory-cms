from storages.backends.s3boto3 import S3Boto3Storage


class ImmutableFilesS3Boto3Storage(S3Boto3Storage):
    """Prevent deletion and replacing images from the bucket, as the bucket is
    used across multiple environments in order to facilitate copying of images
    from one environment to another.

    Extends:
        S3Boto3Storage

    """

    # cause the storage backend to prefix the filename if an image already
    # exists in the bucket with the same name.
    file_overwrite = False

    def delete(self, name):
        """Prevent deleting the image.

        The "image" exists as two things:

        1) The wagtai.wagtailImages.Image model in the db, which has the url
           of the actual image on s3.
        2) The actual image on s3.

        The user is allowed to delete 1, but we want to prevent the storage
        backend from actually deleting 2. We do that by preventing storage
        backend's delete from doing anything.

        """

        pass
