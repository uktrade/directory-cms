from itertools import product
from unittest.mock import patch

import pytest
from modeltranslation.utils import build_localized_fieldname
from six import b
from wagtail.documents.models import Document
from wagtail.images.models import Image
from wagtail.core.models import GroupPagePermission, Locale, Page, Site

from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from django.core.cache import cache
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
from django.core.files.uploadedfile import SimpleUploadedFile
from django.utils import translation

from core.models import RoutingSettings
from groups.models import GroupInfo
from users.models import UserProfile
from .great_international.factories import InternationalHomePageFactory, InternationalArticlePageFactory, \
    InvestHighPotentialOpportunityDetailPageFactory
from .users.factories import UserFactory


@pytest.mark.django_db
@pytest.fixture()
def en_locale():
    # Equivalent for unittest is in tests.core.helpers.SetUpLocaleMixin
    return Locale.objects.get_or_create(language_code='en-gb')



@pytest.fixture
def wagtail_initial_data(request, en_locale):
    if not request.node.get_closest_marker('django_db'):
        return
    page_content_type, _ = ContentType.objects.get_or_create(
        model='page',
        app_label='wagtailcore'
    )
    locale = Locale.objects.get(language_code='en-gb')

    root, _ = Page.objects.get_or_create(
        slug='root',
        defaults=dict(
            title='Root',
            title_en_gb='Root',
            content_type=page_content_type,
            path='0001',
            depth=1,
            numchild=1,
            locale=locale,
            url_path='/',
        )
    )
    Page.objects.get_or_create(
        slug='home',
        defaults=dict(
            title="Welcome to your new Wagtail site!",
            title_en_gb="Welcome to your new Wagtail site!",
            content_type=page_content_type,
            path='00010001',
            depth=2,
            numchild=0,
            url_path='/home/',
            locale=locale,
        )
    )

    wagtailadmin_content_type, _ = ContentType.objects.get_or_create(
        app_label='wagtailadmin',
        model='admin'
    )
    admin_permission, created = Permission.objects.get_or_create(
        content_type=wagtailadmin_content_type,
        codename='access_admin',
        name='Can access Wagtail admin'
    )

    moderators_group = Group.objects.create(name='Moderators')
    editors_group = Group.objects.create(name='Editors')

    GroupPagePermission.objects.create(
        group=moderators_group,
        page=root,
        permission_type='add',
    )
    GroupPagePermission.objects.create(
        group=moderators_group,
        page=root,
        permission_type='edit',
    )
    GroupPagePermission.objects.create(
        group=moderators_group,
        page=root,
        permission_type='publish',
    )

    GroupPagePermission.objects.create(
        group=editors_group,
        page=root,
        permission_type='add',
    )
    GroupPagePermission.objects.create(
        group=editors_group,
        page=root,
        permission_type='edit',
    )

    return root


@pytest.fixture
def root_page(wagtail_initial_data):
    """
    On start Wagtail provides one page with ID=1 and it's called "Root page"
    """
    return wagtail_initial_data


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
    return user_1, user_2


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


@pytest.fixture
def international_root_page(root_page, request):
    if not request.node.get_closest_marker('django_db'):
        return

    return InternationalHomePageFactory.create(
        parent=root_page,
        slug='international-home',
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
def international_site(international_root_page, request):
    if not request.node.get_closest_marker('django_db'):
        return

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


@pytest.fixture
def page_without_specific_type(root_page):
    page = Page(title="No specific type", slug='no-specific-type')
    root_page.add_child(instance=page)
    return page


@pytest.fixture
def translated_page(settings, international_root_page):
    page = InternationalArticlePageFactory(
        parent=international_root_page,
        title_en_gb='ENGLISH',
        title_de='GERMAN',
        title_ja='JAPANESE',
        title_zh_hans='SIMPLIFIED CHINESE',
        title_fr='FRENCH',
        title_es='SPANISH',
        title_pt='PORTUGUESE',
        title_ar='ARABIC',
    )
    field_names = page.get_required_translatable_fields()
    language_codes = settings.LANGUAGES
    for field_name, (language_code, _) in product(field_names, language_codes):
        localized_name = build_localized_fieldname(field_name, language_code)
        if not getattr(page, localized_name):
            setattr(page, localized_name, localized_name + '-v')
    page.save()
    return page


@pytest.fixture
def site_with_translated_page_as_root(translated_page):
    return Site.objects.create(
        site_name='Test',
        hostname='example.com',
        port=8097,
        root_page=translated_page,
    )


@pytest.fixture
def page_with_reversion(admin_user, translated_page):
    translated_page.title = 'published-title',
    translated_page.title_en_gb = 'published-title'
    translated_page.save()

    translated_page.title_en_gb = 'draft-title'
    translated_page.save_revision(
        user=admin_user,
        submitted_for_moderation=False,
    )
    return translated_page


@pytest.fixture
def site_with_revised_page_as_root(page_with_reversion):
    return Site.objects.create(
        site_name='Test',
        hostname='example.com',
        port=8098,
        root_page=page_with_reversion,
    )


@pytest.fixture
def page(international_root_page):
    return InternationalArticlePageFactory(
        parent=international_root_page,
        slug='the-slug'
    )


@pytest.fixture
def high_potential_opportunity_page(page):
    pdf_document = Document.objects.create(
        title='document.pdf',
        file=page.article_image.file  # not really pdf
    )
    return InvestHighPotentialOpportunityDetailPageFactory(pdf_document=pdf_document)


@pytest.fixture()
def untranslated_page(international_root_page):
    return InternationalArticlePageFactory(
        parent=international_root_page,
        slug='the-slug',
        title_en_gb='ENGLISH',
    )
