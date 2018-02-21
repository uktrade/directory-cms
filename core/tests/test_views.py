import pytest
from urllib import parse
from unittest.mock import call, patch

from bs4 import BeautifulSoup
from directory_constants.constants import sectors

from django.urls import reverse

from core import constants, permissions, views
from config.signature import SignatureCheckPermission
from find_a_supplier.translation import IndustryPageTranslationOptions


def test_permissions_draft(rf):
    view = views.PagesOptionalDraftAPIEndpoint()
    param = permissions.DraftTokenPermisison.TOKEN_PARAM
    view.request = rf.get('/', {param: 'thing'})

    assert view.permission_classes == [
        SignatureCheckPermission,
        permissions.DraftTokenPermisison
    ]


def test_permissions_published(rf):
    view = views.PagesOptionalDraftAPIEndpoint()
    view.request = rf.get('/')

    assert view.permission_classes == [
        SignatureCheckPermission,
    ]


@pytest.mark.django_db
def test_draft_view(client, translated_page):
    url = reverse('draft-view', kwargs={'pk': translated_page.pk})
    response = client.get(url)

    assert response.status_code == 302
    assert response.url == translated_page.draft_url


@pytest.mark.parametrize('languaue_code,expected', (
    ('en-gb', 'ENGLISH'),
    ('de', 'GERMAN'),
    ('ja', 'JAPANESE'),
    ('zh-hans', 'SIMPLIFIED CHINESE'),
    ('fr', 'FRENCH'),
    ('es', 'SPANISH'),
    ('pt', 'PORTUGUESE'),
    ('pt-br', 'BRAZILIAN'),
    ('ar', 'ARABIC'),
))
@pytest.mark.django_db
def test_api_translations(client, translated_page, languaue_code, expected):
    url = reverse('api:pages:detail', kwargs={'pk': translated_page.pk})
    response = client.get(url, {'lang': languaue_code})

    assert response.status_code == 200
    assert response.json()['title'] == expected


@pytest.mark.django_db
def test_api_draft(client, page_with_reversion):
    url = reverse('api:pages:detail', kwargs={'pk': page_with_reversion.pk})
    param = permissions.DraftTokenPermisison.TOKEN_PARAM

    draft_response = client.get(url, {
        param: page_with_reversion.get_draft_token()
    })
    published_response = client.get(url)

    assert draft_response.status_code == 200
    assert draft_response.json()['title'] == 'draft-title'

    assert published_response.status_code == 200
    assert published_response.json()['title'] == 'published-title'


@pytest.mark.django_db
def test_copy_to_environment_redirect(client, translated_page, settings):
    url = reverse('copy-to-environment', kwargs={'pk': translated_page.pk})
    environment = settings.COPY_DESTINATION_URLS[0]

    response = client.post(url, {'environment': environment})

    assert response.status_code == 302

    params = parse.parse_qs(parse.urlsplit(response.url).query)

    assert params['title_en_gb'] == [translated_page.title_en_gb]
    assert params['title_de'] == [translated_page.title_de]
    assert params['title_ja'] == [translated_page.title_ja]
    assert params['title_zh_hans'] == [translated_page.title_zh_hans]
    assert params['title_fr'] == [translated_page.title_fr]
    assert params['title_es'] == [translated_page.title_es]
    assert params['title_pt'] == [translated_page.title_pt]
    assert params['title_pt_br'] == [translated_page.title_pt_br]
    assert params['title_ar'] == [translated_page.title_ar]


@pytest.mark.django_db
def test_copy_to_environment_prepopulate(
    client, translated_page, settings, admin_client
):
    url = reverse('copy-to-environment', kwargs={'pk': translated_page.pk})
    environment = settings.COPY_DESTINATION_URLS[0]

    response = admin_client.post(url, {'environment': environment})
    params = dict(parse.parse_qsl(parse.urlsplit(response.url).query))
    path = response.url.replace(environment, '')

    response = admin_client.get(path)

    soup = BeautifulSoup(response.content, 'html.parser')

    ignore_fields = IndustryPageTranslationOptions.fields + (
        'content_type',
        'depth',
        'draft_title',
        'expired',
        'id',
        'live',
        'locked',
        'numchild',
        'owner',
        'page_ptr',
        'path',
        'show_in_menus',
        'slug',
        'title',
        'url_path',
        constants.PREOPPULATE_PARAM,
    )

    for name, value in params.items():
        if name in ignore_fields:
            continue
        element = soup.find(id='id_' + name)
        if element.name == 'textarea':
            actual = element.contents[0].strip()
        elif element.name == 'select':
            actual = element.find_all('option', selected=True)[0].get('value')
        else:
            actual = element.get('value')
        assert actual == value


@pytest.mark.django_db
def test_copy_to_environment_not_prepopulate(
    admin_client, translated_page
):
    url = reverse(
        'wagtailadmin_pages:add',
        args=(
            translated_page._meta.app_label,
            translated_page._meta.model_name,
            2
        )
    )

    response = admin_client.get(url)

    assert response.status_code == 200


@pytest.mark.django_db
@patch('core.helpers.auto_populate_translations')
@patch('wagtail.wagtailcore.models.Page.save_revision')
def test_translate_page(
    mock_save_revision, mock_auto_populate_translations, translated_page,
    admin_client, admin_user, settings
):
    settings.LANGUAGES = [
        ['de', 'German'],
        [settings.LANGUAGE_CODE, 'default'],
    ]
    url = reverse('wagtailadmin_pages:edit', args=(translated_page.pk,))

    response = admin_client.post(
        url,
        data={
            'action-translate': True,
            'sector_value': sectors.AUTOMOTIVE,
            'slug_en_gb': 'this-is-great',
            'title_en_gb': 'this-is-great',
        }
    )

    assert response.status_code == 302
    assert response.url == reverse(
        'wagtailadmin_pages:edit', args=(translated_page.pk,)
    )
    assert mock_auto_populate_translations.call_count == 1
    assert mock_auto_populate_translations.call_args == call(
        translated_page, ['de']
    )
    assert mock_save_revision.call_count == 2
    assert mock_save_revision.call_args == call(user=admin_user)


@pytest.mark.django_db
@patch('core.helpers.auto_populate_translations')
def test_translate_page_not_called_always(
     mock_auto_populate_translations, translated_page, admin_client,
     admin_user
):
    url = reverse('wagtailadmin_pages:edit', args=(translated_page.pk,))

    response = admin_client.post(
        url,
        data={
            'sector_value': sectors.AUTOMOTIVE,
            'slug_en_gb': 'this-is-great',
            'title_en_gb': 'this-is-great',
            'lede_en_gb': 'Good',
            'lede_column_three_en_gb': 'get this',
            'lede_column_two_en_gb': 'this good',
            'case_study_en_gb': 'so good',
            'seo_description_en_gb': 'this is good',
            'hero_text_en_gb': 'good times',
            'sector_label_en_gb': 'Good',
            'lede_column_one_en_gb': 'goodies',
        }
    )

    assert response.status_code == 302
    assert response.url == reverse(
        'wagtailadmin_pages:edit', args=(translated_page.pk,)
    )

    assert mock_auto_populate_translations.call_count == 0


@pytest.mark.django_db
def test_page_listing(translated_page, admin_client):
    url = reverse('wagtailadmin_pages:edit', args=(2,))

    response = admin_client.get(url)

    assert response.status_code == 200
