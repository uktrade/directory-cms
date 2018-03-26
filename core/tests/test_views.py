import pytest
from unittest.mock import call, patch

from bs4 import BeautifulSoup
from directory_constants.constants import sectors
import wagtail_factories

from django.forms.models import model_to_dict
from django.urls import reverse

from core import permissions, views
from config.signature import SignatureCheckPermission


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


@pytest.mark.parametrize('languaue_code', (
    'en-gb' 'de' 'ja', 'zh-hans', 'fr', 'es', 'pt', 'pt-br', 'ar',
))
@pytest.mark.django_db
def test_api_translations_not_populated(
    client, untranslated_page, languaue_code
):
    url = reverse('api:pages:detail', kwargs={'pk': untranslated_page.pk})
    response = client.get(url, {'lang': languaue_code})

    assert response.status_code == 200
    assert response.json()['title'] == 'ENGLISH'


@pytest.mark.django_db
def test_api_draft(client, page_with_reversion):
    url = reverse('api:pages:detail', kwargs={'pk': page_with_reversion.pk})
    param = permissions.DraftTokenPermisison.TOKEN_PARAM

    draft_response = client.get(url, {
        param: page_with_reversion.get_draft_token()
    })
    draft_data = draft_response.json()
    published_response = client.get(url)
    published_data = published_response.json()

    assert draft_response.status_code == 200
    assert draft_data['title'] == 'draft-title'
    assert draft_data['url'] == page_with_reversion.draft_url

    assert published_response.status_code == 200
    assert published_data['title'] == 'published-title'
    assert published_data['url'] == page_with_reversion.published_url


@pytest.mark.django_db
def test_copy_to_environment(client, translated_page, settings, image):
    translated_page.hero_image = image
    translated_page.save()

    url = reverse('copy-to-environment', kwargs={'pk': translated_page.pk})

    response = client.get(url)

    assert response.context['page'] == translated_page


@pytest.mark.django_db
def test_add_page_prepopulate(
    client, translated_page, settings, admin_client, image
):
    url = reverse(
        'preload-add-page',
        kwargs={
            'app_name': translated_page._meta.app_label,
            'model_name': translated_page._meta.model_name,
            'parent_pk': 1,
        }
    )

    model_as_dict = model_to_dict(translated_page, exclude=[
        'go_live_at',
        'expire_at',
    ])
    model_as_dict = {key: val for key, val in model_as_dict.items() if val}
    post_data = {
        **model_as_dict,
        'hero_image': image.file.name,
        'introduction_column_one_icon_en_gb': image.file.name,
        'introduction_column_two_icon_en_gb': image.file.name,
        'introduction_column_three_icon_en_gb': image.file.name,
    }
    expected_data = {
        **model_as_dict,
        'hero_image': str(image.pk),
        'introduction_column_one_icon_en_gb': str(image.pk),
        'introduction_column_two_icon_en_gb': str(image.pk),
        'introduction_column_three_icon_en_gb': str(image.pk),
    }

    response = admin_client.post(url, post_data)

    soup = BeautifulSoup(response.content, 'html.parser')

    for name, value in expected_data.items():
        element = soup.find(id='id_' + name)
        if not element or not value:
            continue
        if element.name == 'textarea':
            actual = element.contents[0].strip()
        elif element.name == 'select':
            actual = element.find_all('option', selected=True)[0].get('value')
        else:
            actual = element.get('value')
        assert actual == value


@pytest.mark.django_db
def test_add_page_prepopulate_missing_content_type(
    client, translated_page, settings, admin_client
):
    url = reverse(
        'preload-add-page',
        kwargs={
            'app_name': translated_page._meta.app_label,
            'model_name': 'doesnotexist',
            'parent_pk': 1,
        }
    )

    data = model_to_dict(translated_page, exclude=[
        'go_live_at',
        'expire_at',
        'hero_image',
    ])
    response = admin_client.post(url, data)

    assert response.status_code == 404


@pytest.mark.django_db
@patch('core.helpers.auto_populate_translations')
@patch('wagtail.wagtailcore.models.Page.save_revision')
def test_translate_page(
    mock_save_revision, mock_auto_populate_translations, translated_page,
    admin_client, admin_user, settings, image
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
            'sector_label_en_gb': 'Mining',
            'introduction_text_en_gb': 'introduction',
            'introduction_column_one_text_en_gb': 'column one',
            'introduction_column_two_text_en_gb': 'column two',
            'hero_text_en_gb': 'hero',
            'introduction_column_three_text_en_gb': 'column three',
            'company_list_text_en_gb': 'companies',
            'company_list_call_to_action_text_en_gb': 'view all',
            'introduction_column_two_icon_en_gb': image.pk,
            'introduction_column_one_icon_en_gb': image.pk,
            'introduction_column_two_icon_en_gb': image.pk,
            'introduction_column_three_icon_en_gb': image.pk,
            'seo_description_en_gb': 'description',
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
def test_list_page(
    admin_client, translated_page
):
    url = reverse('wagtailadmin_explore', args=(2,))

    response = admin_client.get(url)

    assert response.status_code == 200


@pytest.mark.django_db
@patch('core.helpers.auto_populate_translations')
def test_translate_page_not_called_always(
     mock_auto_populate_translations, translated_page, admin_client,
     admin_user,
):
    url = reverse('wagtailadmin_pages:edit', args=(translated_page.pk,))
    image = wagtail_factories.ImageFactory()

    response = admin_client.post(
        url,
        data={
            'sector_value': sectors.AUTOMOTIVE,
            'slug_en_gb': 'this-is-great',
            'title_en_gb': 'this-is-great',
            'introduction_text_en_gb': 'Good',
            'introduction_column_three_text_en_gb': 'get this',
            'introduction_column_two_text_en_gb': 'this good',
            'seo_description_en_gb': 'this is good',
            'hero_text_en_gb': 'good times',
            'sector_label_en_gb': 'Good',
            'introduction_column_one_text_en_gb': 'goodies',
            'company_list_text_en_gb': 'companies',
            'company_list_call_to_action_text_en_gb': 'view all',
            'introduction_column_two_icon_en_gb': image.pk,
            'introduction_column_three_icon_en_gb': image.pk,
            'introduction_column_one_icon_en_gb': image.pk,
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


@pytest.mark.django_db
def test_lookup_by_page_type(translated_page, admin_client):
    url = reverse(
        'lookup-by-page-type',
        kwargs={'page_type': 'find_a_supplier.IndustryPage'}
    )

    response = admin_client.get(url)

    assert response.status_code == 200
    assert response.json()['id'] == translated_page.id


@pytest.mark.django_db
def test_lookup_by_page_type_misisng_page(admin_client):
    url = reverse(
        'lookup-by-page-type',
        kwargs={'page_type': 'find_a_supplier.IndustryPage'}
    )

    response = admin_client.get(url)

    assert response.status_code == 404


@pytest.mark.django_db
def test_lookup_by_page_type_invalid_page_name(admin_client):
    url = reverse(
        'lookup-by-page-type',
        kwargs={'page_type': 'find_a_supplier.IstryPage'}
    )

    response = admin_client.get(url)

    assert response.status_code == 400


@pytest.mark.django_db
def test_lookup_by_page_type_draft(page_with_reversion, client):
    url = reverse(
        'lookup-by-page-type',
        kwargs={'page_type': 'find_a_supplier.IndustryPage'}
    )

    param = permissions.DraftTokenPermisison.TOKEN_PARAM

    draft_response = client.get(url, {
        param: page_with_reversion.get_draft_token()
    })
    draft_data = draft_response.json()
    published_response = client.get(url)
    published_data = published_response.json()

    assert draft_response.status_code == 200
    assert draft_data['title'] == 'draft-title'
    assert draft_data['url'] == page_with_reversion.draft_url

    assert published_response.status_code == 200
    assert published_data['title'] == 'published-title'
    assert published_data['url'] == page_with_reversion.published_url


@pytest.mark.django_db
def test_translations_exposed(page, translated_page, settings, client):
    url = reverse('api:pages:detail', kwargs={'pk': translated_page.pk})

    response = client.get(url)

    expected = [[code, label] for code, label in settings.LANGUAGES_LOCALIZED]

    assert response.json()['languages'] == expected


@pytest.mark.parametrize('languaue_code', (
    'en-gb' 'de' 'ja', 'zh-hans', 'fr', 'es', 'pt', 'pt-br', 'ar',
))
@pytest.mark.django_db
def test_lookup_by_page_type_translations_not_populated(
    client, untranslated_page, languaue_code
):
    url = reverse(
        'lookup-by-page-type',
        kwargs={'page_type': 'find_a_supplier.IndustryPage'}
    )
    response = client.get(url, {'lang': languaue_code})

    assert response.status_code == 200
    assert response.json()['title'] == 'ENGLISH'


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
def test_lookup_by_page_type_translations(
    client, translated_page, languaue_code, expected
):
    url = reverse(
        'lookup-by-page-type',
        kwargs={'page_type': 'find_a_supplier.IndustryPage'}
    )
    response = client.get(url, {'lang': languaue_code})

    assert response.status_code == 200
    assert response.json()['title'] == expected
