import os
from unittest.mock import patch

import pytest
from wagtail.images.models import Image
from wagtail.core.models import Page, Site

from django.core.cache import cache
from django.core.files.storage import default_storage
from django.core.files.uploadedfile import SimpleUploadedFile
from django.core.management import call_command
from django.utils import translation
from django import db
from django.db.migrations.executor import MigrationExecutor

from conf import settings
from find_a_supplier.tests.factories import IndustryPageFactory


@pytest.fixture
def root_page():
    """
    On start Wagtail provides one page with ID=1 and it's called "Root page"
    """
    return Page.objects.get(pk=1)


@pytest.fixture
def untranslated_page(root_page):
    return IndustryPageFactory(
        parent=root_page,
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


@pytest.fixture
def site_with_untranslated_page_as_root(untranslated_page):
    return Site.objects.create(
        site_name='Test',
        hostname='example.com',
        port=8096,
        root_page=untranslated_page,
    )


@pytest.fixture(autouse=True)
def mock_signature_check():
    stub = patch('conf.signature.SignatureCheckPermission.has_permission')
    stub.start()
    yield stub
    stub.stop()


@pytest.fixture
def enable_signature_check(mock_signature_check):
    mock_signature_check.stop()
    yield
    mock_signature_check.start()


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


@pytest.fixture(autouse=True)
def reset_language(settings):
    translation.activate(settings.LANGUAGE_CODE)


@pytest.fixture(autouse=True)
def clear_django_cache():
    cache.clear()


@pytest.fixture(scope='session')
def django_db_createdb():
    """Never let Django create the test db.
    django_db_setup will take care of it"""
    return False


@pytest.fixture(scope='session')
def django_db_setup(django_db_blocker):
    """Load db schema from template."""
    with django_db_blocker.unblock():
        settings.DATABASES['default']['NAME'] = 'test_directory_cms_debug'
        os.system('PGPASSWORD=debug dropdb  test_directory_cms_debug')
        os.system('PGPASSWORD=debug createdb -h localhost -U debug test_directory_cms_debug')  # NOQA
        os.system('PGPASSWORD=debug psql -h localhost -U debug -d test_directory_cms_debug -f db_template.sql >/dev/null 2>&1')  # NOQA
        call_command('migrate')  # if the template is old we need to migrate
        yield

        for connection in db.connections.all():
            connection.close()


@pytest.fixture(autouse=True)
def feature_flags(settings):
    # solves this issue: https://github.com/pytest-dev/pytest-django/issues/601
    settings.FEATURE_FLAGS = {**settings.FEATURE_FLAGS}
    yield settings.FEATURE_FLAGS
