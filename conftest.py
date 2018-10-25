import os
from unittest.mock import patch

import pytest
from wagtail.images.models import Image
from wagtail.core.models import Page
import wagtail_factories

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
    Page.objects.all().delete()
    return wagtail_factories.PageFactory(parent=None)


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


@pytest.fixture(autouse=True)
def reset_language(settings):
    translation.activate(settings.LANGUAGE_CODE)


@pytest.fixture()
def migration(transactional_db):
    """
    This fixture returns a helper object to test Django data migrations.
    The fixture returns an object with two methods;
     - `before` to initialize db to the state before the migration under test
     - `after` to execute the migration and bring db to the state after the
    migration. The methods return `old_apps` and `new_apps` respectively; these
    can be used to initiate the ORM models as in the migrations themselves.
    For example:
        def test_foo_set_to_bar(migration):
            old_apps = migration.before([('my_app', '0001_inital')])
            Foo = old_apps.get_model('my_app', 'foo')
            Foo.objects.create(bar=False)
            assert Foo.objects.count() == 1
            assert Foo.objects.filter(bar=False).count() == Foo.objects.count()
            # executing migration
            new_apps = migration.apply('my_app', '0002_set_foo_bar')
            Foo = new_apps.get_model('my_app', 'foo')
            assert Foo.objects.filter(bar=False).count() == 0
            assert Foo.objects.filter(bar=True).count() == Foo.objects.count()
    From: https://gist.github.com/asfaltboy/b3e6f9b5d95af8ba2cc46f2ba6eae5e2
    """
    class Migrator:
        def before(self, migrate_from):
            """ Specify app and starting migration name as in:
                before(['app', '0001_before']) => app/migrations/0001_before.py
            """

            self.migrate_from = migrate_from
            self.executor = MigrationExecutor(db.connection)
            self.executor.migrate(self.migrate_from)
            self._old_apps = self.executor.loader.project_state(
                self.migrate_from).apps
            return self._old_apps

        def apply(self, app, migrate_to):
            """ Migrate forwards to the "migrate_to" migration """
            self.migrate_to = [(app, migrate_to)]
            self.executor.loader.build_graph()  # reload.
            self.executor.migrate(self.migrate_to)
            self._new_apps = self.executor.loader.project_state(
                self.migrate_to).apps
            return self._new_apps

    yield Migrator()
    call_command('migrate')


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
        os.system('PGPASSWORD=debug createdb -h localhost -U debug test_directory_cms_debug')  # NOQA
        os.system('PGPASSWORD=debug psql -h localhost -U debug -d test_directory_cms_debug -f db_template.sql')  # NOQA
        call_command('migrate') # if the template is old we might need to migrate  # NOQA
        yield

        for connection in db.connections.all():
            connection.close()
