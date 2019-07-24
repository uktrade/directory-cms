import os
from unittest.mock import patch

import pytest
from six import b
from wagtail.documents.models import Document
from wagtail.images.models import Image
from wagtail.core.models import Page, Site

from django import db
from django.core.cache import cache
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
from django.core.files.uploadedfile import SimpleUploadedFile
from django.core.management import call_command
from django.utils import translation

from conf import settings
from core.models import RoutingSettings
from groups.models import GroupInfo
from users.models import UserProfile
from .great_international.factories import InternationalHomePageFactory
from .find_a_supplier.factories import IndustryPageFactory
from .users.factories import UserFactory


@pytest.fixture()
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


@pytest.fixture
def document():
    fake_file = ContentFile(b('A boring example document'))
    fake_file.name = 'test.pdf'
    yield Document.objects.create(title='Test document', file=fake_file)


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


@pytest.fixture
def groups_with_info():
    from django.contrib.auth.models import Group
    groups = []
    for i, group in enumerate(Group.objects.select_related('info').all(), 1):
        try:
            info = group.info
        except GroupInfo.DoesNotExist:
            info = GroupInfo(group=group)
        info.name_singular = group.name[:-1]
        info.permission_summary = 'For managers'
        info.role_match_description = 'For content admins'
        info.visibility = GroupInfo.VISIBILITY_UNRESTRICTED
        info.seniority_level = i  # determines order in choices etc
        info.save()
        group.info = info
        groups.append(group)
    return groups


@pytest.fixture
def team_leaders_group(groups_with_info):
    group = list(groups_with_info).pop()
    group.info.is_team_leaders_group = True
    group.info.save()
    return group


@pytest.fixture
def team_leaders(team_leaders_group):
    user_1 = UserFactory(username='user1', first_name='Adam')
    user_2 = UserFactory(username='user2', first_name='Zac')
    team_leaders_group.user_set.set([user_1, user_2])
    return (user_1, user_2)


@pytest.fixture
def approved_user():
    user = UserFactory(username='approved-user')
    profile = user.userprofile
    profile.assignment_status = UserProfile.STATUS_APPROVED
    profile.save()
    return user


@pytest.fixture
def user_awaiting_approval(groups_with_info):
    user = UserFactory(username='awaiting-approval-user')
    profile = user.userprofile
    profile.assignment_status = UserProfile.STATUS_AWAITING_APPROVAL
    profile.self_assigned_group_id = groups_with_info[0].id
    profile.save()
    return user


@pytest.fixture()
def international_root_page(root_page):
    return InternationalHomePageFactory.create(
        parent=root_page,
        slug='home',
        title_en_gb='home',
        hero_title_en_gb='foo',
        invest_title_en_gb='foo',
        trade_title_en_gb='foo',
        tariffs_title_en_gb='foo',
        tariffs_description_en_gb='foo',
        tariffs_link_en_gb='http://foo.com',
        tariffs_call_to_action_text_en_gb='foo',
        news_title_en_gb='foo',
        study_in_uk_cta_text_en_gb='foo',
        visit_uk_cta_text_en_gb='foo'
    )


@pytest.fixture(autouse=True)
def international_site(international_root_page):
    site, created = Site.objects.get_or_create(
        port=80,
        hostname='great.gov.uk',
        defaults={
            'root_page': international_root_page,
            'site_name': 'international'
        }
    )
    RoutingSettings.objects.get_or_create(
        site=site,
        defaults={'root_path_prefix': '/international/content/'}
    )
    return site
