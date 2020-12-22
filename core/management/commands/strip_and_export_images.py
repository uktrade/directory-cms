import json
import sys
import tempfile

from urllib.parse import urlparse

from operator import attrgetter

import boto3

from django.core.management import BaseCommand
from django.core.serializers.json import DjangoJSONEncoder
from django.db import transaction
from django.utils.timezone import now as tz_now

from storages.backends.s3boto3 import S3Boto3Storage

from wagtail.core.models import Page
from wagtail.images.models import Image
from wagtailmedia.models import Media

# Make an S3 API available to us
s3 = boto3.resource('s3')


class Command(BaseCommand):
    help = ("""This command makes a note of every media object
    (wagtailimages.image or wagtailmedia.video) exports their
    data to a file, copies from one S3 bucket to another and
    then removes them from the page they were found in.""")

    def add_arguments(self, parser):
        parser.add_argument(
            '--target-bucket',
            help='Target S3 bucket name',
        )
        parser.add_argument(
            '--access-key-id',
            help='Access key ID for profile that owns the *target* buceket',
        )
        parser.add_argument(
            '--secret-access-key',
            help='Secret key for profile that owns the *target* buceket',
        )
        parser.add_argument(
            '--commit',
            help='Actually perform the removal of images from the target system',
        )

    _page_fields_cache = {}

    _media_copy_count = 0

    _already_copied = {}

    _media_attrs = [
        # common
        'id',
        'title',
        'width',
        'height',
        'collection.name',
        'created_at',
        'uploaded_by_user.username',
        # wagtail.images only,
        'focal_point_x',
        'focal_point_y',
        'focal_point_width',
        'focal_point_height',
        'file_size',
        'file_hash',
        # wagtailmedia only,
        'type',
        'duration',
        'thumbnail.file.name',
    ]

    def _get_media_fields(self, instance: Page) -> list:
        # Media fields are actually FKs to the relevant media model

        _page = instance.specific
        cached = self._page_fields_cache.get(_page._meta.label_lower)
        if cached:
            return cached

        target_models = [Image, Media]

        field_list = [
            field for field in
            _page._meta.get_fields()
            if field.related_model in target_models
        ]

        self._page_fields_cache[_page._meta.label_lower] = field_list

        return field_list

    def _get_media_meta(self, instance, field_list) -> list:
        output = {}
        for field in field_list:
            fieldname = field.name
            fkeyed_media_instance = getattr(instance.specific, fieldname)
            if fkeyed_media_instance:
                # the FK may be null, after all
                output[fieldname] = {
                    'source_url': fkeyed_media_instance.file.url,
                    'tags': [x for x in fkeyed_media_instance.tags.all().values_list('name', flat=True)],
                }

                for attr in self._media_attrs:
                    try:
                        f = attrgetter(attr)
                        output[fieldname][attr] = f(fkeyed_media_instance)
                    except AttributeError:
                        output[fieldname][attr] = ''
        return output

    def _copy_media(self, target_bucket: str, media_meta: dict):
        # NB: modifies data media_meta structure, alas :-/

        for fieldname, meta in media_meta.items():

            parsed = urlparse(meta['source_url'])

            source_bucket = parsed.netloc.split('.')[0]  # bucket_name.s3.amazonwas.com -> bucket_name
            source_key = parsed.path[1:]  # /path/to/thing.file -> path/to/thing.file

            # NB: This will only work if the source file is publicly readable
            copy_source = {'Bucket': source_bucket, 'Key': source_key}

            _copy_source_cache_key = str(copy_source)
            target_filename = self._already_copied.get(_copy_source_cache_key)

            if not target_filename:
                target_filename = S3Boto3Storage().get_available_name(source_key)
                # s3.meta.client.copy(copy_source, target_bucket, target_filename)

                sys.stdout.write(f'\n{target_filename} copied to s3://{target_bucket}')
                self._media_copy_count += 1
                self._already_copied[_copy_source_cache_key] = target_filename
            else:
                sys.stdout.write(f'\nFile already copied to: {target_filename}')

            # Also update the metadata so we track where the file ended up,
            # in case it's not same filename due to a collision
            meta['target_filename'] = target_filename

    def _nullify_media_fields(self, model):
        # Strike out the FK from the page to the media item, but don't delete the
        # actual Image/Media record.

        field_list = self._page_fields_cache[model._meta.label_lower]

        if field_list:
            update_params = dict(zip([x.name for x in field_list], [None] * len(field_list)))
            # zap them all without needing to re-save
            result = model.objects.all().update(**update_params)
            sys.stdout.write(f'updated {result} records.')
        else:
            sys.stdout.write(f'no relevant fields to update.')

    @transaction.atomic
    def handle(self, *args, **options):
        sys.stdout.write(
            '\nExtracting list of media objects in use, '
            'then removing the FK relations from Pages to them'
        )

        _now = tz_now().isoformat()

        s3_copy_enabled = all([
            options['target_bucket'],
            options['access_key_id'],
            options['secret_access_key'],
        ])

        if not s3_copy_enabled:
            sys.stdout.write('\nAuto copying of S3 files is DISABLED because we lack configuration')

        output = []

        # find all the pages
        # for each, find all its images
        all_pages = Page.objects.all()
        sys.stdout.write(f'\nGathering data for {all_pages.count()} pages')

        for page in all_pages:
            media_fields = self._get_media_fields(instance=page)
            media_meta = self._get_media_meta(instance=page, field_list=media_fields)
            if media_meta:
                # if s3_copy_enabled:
                if s3_copy_enabled:
                    target_bucket = options['target_bucket']
                    self._copy_media(target_bucket=target_bucket, media_meta=media_meta)
                media_meta.update({'page_id': page.id})  # If you add this before _copy_media you'll cause a TypeError
                output.append(media_meta)

        # Zap the links to the images for all instances of the model
        all_models = set([page.specific._meta.model for page in all_pages])
        for count, model in enumerate(all_models):
            sys.stdout.write(
                f'\n{count+1}/{len(all_models)}:\t '
                f'Nullifying FKs from all {model.__name__} instances to their media items: '
            )
            self._nullify_media_fields(model=model)

        total_items = len(output)
        sys.stdout.write(f'\n{total_items} pages had media fields to deal with')
        sys.stdout.write(f'\n{self._media_copy_count} media objects copied')

        # output the JSON file
        with tempfile.NamedTemporaryFile(
            mode='w',
            prefix=_now,
            suffix='.json',
            delete=False
        ) as fp:
            sys.stdout.write(f'\nWriting JSON for {total_items} items')
            fp.write(json.dumps(output, indent=2, cls=DjangoJSONEncoder))

        sys.stdout.write(f'\nDone for {total_items} rows of data\n\n\n')

        sys.stdout.write(f'\nFile output to: {fp.name}\n\n')

        if options['commit']:
            sys.stdout.write(f'Committing changes to the database')
        else:
            assert False, 'Dry run only: rolling back changes'
