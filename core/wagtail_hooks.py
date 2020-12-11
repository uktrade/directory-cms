import logging
import boto3
from urllib.parse import urlparse

from wagtail.admin.widgets import Button, PageListingButton
from wagtail.core import hooks
from wagtail.admin.wagtail_hooks import page_listing_buttons

from wagtail_transfer.field_adapters import FieldAdapter
from wagtail_transfer.files import File as WTFile, FileTransferError
from wagtail_transfer.models import ImportedFile

from django.core.files.storage import DefaultStorage

from django.db import models as django_models
from django.conf import settings
from django.contrib.staticfiles.templatetags.staticfiles import static
from django.urls import reverse
from django.utils.html import format_html
from core import constants, helpers, models

logger = logging.getLogger(__name__)

# Make an S3 API available to us
s3 = boto3.resource('s3')


@hooks.register('register_page_listing_more_buttons')
def add_copy_button(page, page_perms, is_parent=False):
    if isinstance(page, models.BasePage):
        yield Button(
            'Copy upstream',
            reverse('copy-upstream', kwargs={'pk': page.id}),
            attrs={'title': "Copy this page to another environment"},
            priority=80
        )
        yield Button(
            'Update upstream',
            reverse('update-upstream', kwargs={'pk': page.id}),
            attrs={'title': "Update this page on another environment"},
            priority=80
        )


@helpers.replace_hook('register_page_listing_buttons', page_listing_buttons)
def update_default_listing_buttons(page, page_perms, is_parent=False):
    buttons = list(page_listing_buttons(page, page_perms, is_parent))
    if isinstance(page, models.BasePage):
        for button in buttons:
            if helpers.get_button_url_name(button) == 'view_draft':
                button.url = page.get_url(is_draft=True)

    else:
        # limit buttons for non-subclasses-of-BasePage
        allowed_urls = ['add_subpage']
        buttons = [
            button for button in buttons
            if helpers.get_button_url_name(button) in allowed_urls
        ]
        # since the drop-down is removed by the above, add a delete
        # button to this list
        if page_perms.can_delete():
            buttons.append(PageListingButton(
                'Delete',
                reverse('wagtailadmin_pages:delete', args=[page.id]),
                attrs={
                    'title': "Delete '%s'" % page.get_admin_display_title()
                },
            ))
    return buttons


@hooks.register('insert_editor_css')
def editor_css():
    return format_html(
        '<link rel="stylesheet" href="{}">',
        static('core/css/editor.css')
    )


@hooks.register('insert_global_admin_css')
def global_admin_css():
    env_stylesheet = ''

    if settings.ENVIRONMENT_CSS_THEME_FILE:
        env_stylesheet = format_html(
            '<link rel="stylesheet" href="{}">',
            static(settings.ENVIRONMENT_CSS_THEME_FILE)
        )

    return format_html(
        '<link rel="stylesheet" href="{}">',
        static('core/css/global.css')
    ) + env_stylesheet


@hooks.register('insert_editor_js')
def add_sum_required_fields_js():
    return format_html(
        '<script src="{0}"></script>',
        static('core/js/sum_required_localised_fields.js')
    )


class S3WagtailTransferFile(WTFile):
    """Subclass of File that knows how to transfer() using an
    S3 to S3 copy"""

    def __init__(self, local_filename, size, hash_, source_url, **kwargs):
        super().__init__(local_filename=local_filename, size=size, hash=hash_, source_url=source_url)

        self.source_bucket = kwargs['source_bucket']
        self.source_key = kwargs['source_key']

    def transfer(self):

        # NB: This will only work if the source file is publicly readable
        copy_source = {'Bucket': self.source_bucket, 'Key': self.source_key}

        try:
            s3.meta.client.copy(copy_source, settings.AWS_STORAGE_BUCKET_NAME, self.local_filename)
        except (
            boto3.exceptions.RetriesExceededError,
            boto3.exceptions.S3UploadFailedError,
            ValueError,
            # This may not be exhaustive - we'll have to expand as required
            # or just catch Exception
        ) as ex:
            logger.exception(ex)
            raise FileTransferError(ex)

        return ImportedFile.objects.create(
            file=self.local_filename,
            source_url=self.source_url,
            hash=self.hash,
            size=self.size,
        )


class S3FileFieldAdapter(FieldAdapter):
    """Custom adapter that handles file fields when using AWS S3

    NOTE that this will only work for transfers within the same Region
    """

    def _get_relevant_s3_meta(self, field_value) -> dict:
        """Returns relevant metadata from S3 in a single data structure,
        cleaned up and with one network request."""

        # TODO: cache this? NB: the adapter itself is cached/persisted
        # so we can't put state on it

        _object_summary = s3.ObjectSummary(
            field_value.storage.bucket.name,  # bucket
            field_value.name,  # key
        )
        return {'size': _object_summary.size, 'hash': self._get_file_hash(_object_summary)}

    def _get_file_hash(self, object_summary) -> str:
        """Uses the object's eTag as a hash, avoiding the need to
        download and hash the actual file"""

        # IMPORTANT: The ETag from S3 may not be reliable/consistent
        # if the file ended up being multi-part uploaded. If that's the
        # case, we'll get a 'cache miss' and end up doing redundant work
        #
        # * https://boto3.amazonaws.com/v1/documentation/api/latest/
        #       reference/services/s3.html#S3.ObjectSummary.e_tag
        # * https://boto3.amazonaws.com/v1/documentation/api/latest/
        #       reference/services/s3.html#S3.Object.initiate_multipart_upload
        #
        # Also note that the ETags are wrapped in quotes, as per RFC:
        # https://tools.ietf.org/html/rfc2616#section-14.19 but we'll drop
        # them here to avoid noise in our hash

        return object_summary.e_tag.replace('"', '')

    def _get_imported_file_bucket_and_key(self, imported_file_url) -> tuple:
        """From the URL for the imported file, work out what its
        S3 bucket and key are, so we can make an API call to copy it.

        Here, we're trusting that our buckets are consistenty configured to be
        subdomains + constants.AWS_S3_MAIN_HOSTNAME
        """

        source = urlparse(imported_file_url)

        bucket_name = source.netloc

        for _hostname in constants.AWS_S3_MAIN_HOSTNAME_OPTIONS:

            if _hostname in bucket_name:
                _target = f'.{_hostname}'
                bucket_name = bucket_name.replace(_target, '')
                continue

        key_name = source.path[1:] if source.path.startswith('/') else source.path
        return bucket_name, key_name

    def serialize(self, instance):
        value = self.field.value_from_object(instance)
        if not value:
            return None

        # This adapter is only used when files are on S3, so there's no need
        # to prepend MEDIA_URL to `url` (which the default FileAdapter does)
        url = value.url

        _s3_object_metadata = self._get_relevant_s3_meta(field_value=value)

        return {
            'download_url': url,
            'size': _s3_object_metadata['size'],
            'hash': _s3_object_metadata['hash'],
        }

    def populate_field(self, instance, value, context):
        """Check if the field's file needs to be imported, and if so, do so."""

        # `value` is the output of self.serialize() - either a dict or None
        if not value:
            return None

        source_file_url = value['download_url']
        source_file_hash = value['hash']
        source_file_size = value['size']

        imported_file = context.imported_files_by_source_url.get(source_file_url)
        if imported_file is None:
            logger.info('File from %s has not already been imported: reimporting', source_file_url)

            existing_file = self.field.value_from_object(instance)
            if existing_file:
                logger.info('File exists. Comparing hashes with source file and existing file')
                _s3_object_metadata = self._get_relevant_s3_meta(field_value=existing_file)
                existing_file_hash = _s3_object_metadata['hash']
                if existing_file_hash == source_file_hash:
                    # File not changed, so don't bother updating it
                    logger.info('Matching hashes, so no need to import')
                    return

            # Generate a safe, new filename for the destination bucket, so avoid overwrites
            source_bucket, source_key = self._get_imported_file_bucket_and_key(source_file_url)

            target_filename = DefaultStorage().get_available_name(source_key)

            _file = S3WagtailTransferFile(
                local_filename=target_filename,
                size=source_file_size,
                hash_=source_file_hash,
                source_url=source_file_url,
                source_bucket=source_bucket,
                source_key=source_key,
            )
            try:
                logger.info('Attempting to copy file from %s, S3-to-S3', source_file_url)
                imported_file = _file.transfer()
            except FileTransferError as ex:
                logger.exception('Failed to transfer: %s', ex)
                return None

            context.imported_files_by_source_url[_file.source_url] = imported_file

        # This is standard behaviour from the base FileAdapter:
        value = imported_file.file.name
        getattr(instance, self.field.get_attname()).name = value

        logger.info('File copied to destination')


@hooks.register('register_field_adapters')
def register_s3_media_file_adapter():
    """For all FileFields in our application, use our custom S3 one
    to handle transfers
    """

    extra_adapters = {}

    if settings.USER_MEDIA_ON_S3:
        extra_adapters.update(
            {
                django_models.FileField: S3FileFieldAdapter,
            }
        )

    return extra_adapters
