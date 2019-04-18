import pytest
from unittest.mock import ANY, call, patch

from bs4 import BeautifulSoup
from directory_constants.constants import cms
from modeltranslation.utils import build_localized_fieldname
from wagtail.core.models import Page

from django.forms.models import model_to_dict
from django.urls import reverse

from core import helpers, permissions, views
from core.helpers import CachedResponse
from conf.signature import SignatureCheckPermission
from invest.tests.factories import InfoPageFactory


@pytest.fixture
def cluster_data(settings):
    data = {}
    for code, _ in settings.LANGUAGES:
        field_name = build_localized_fieldname('article_summaries', lang=code)
        data.update(
            helpers.nested_form_data({
                field_name: helpers.inline_formset([])
            })
        )
    return data


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


@pytest.mark.parametrize('language_code,expected', (
    ('en-gb', 'ENGLISH'),
    ('de', 'GERMAN'),
    ('ja', 'JAPANESE'),
    ('zh-hans', 'SIMPLIFIED CHINESE'),
    ('fr', 'FRENCH'),
    ('es', 'SPANISH'),
    ('pt', 'PORTUGUESE'),
    ('ar', 'ARABIC'),
))
@pytest.mark.django_db
def test_api_translations(client, translated_page, language_code, expected):
    url = reverse('api:api:pages:detail', kwargs={'pk': translated_page.pk})
    response = client.get(url, {'lang': language_code})

    assert response.status_code == 200
    assert response.json()['title'] == expected


@pytest.mark.parametrize('language_code', (
    'en-gb' 'de' 'ja', 'zh-hans', 'fr', 'es', 'pt', 'ar',
))
@pytest.mark.django_db
def test_api_translations_not_populated(
    client, untranslated_page, language_code
):
    url = reverse('api:api:pages:detail', kwargs={'pk': untranslated_page.pk})
    response = client.get(url, {'lang': language_code})

    assert response.status_code == 200
    assert response.json()['title'] == 'ENGLISH'


@pytest.mark.django_db
def test_api_draft(client, page_with_reversion):
    url = reverse(
        'api:api:pages:detail', kwargs={'pk': page_with_reversion.pk}
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
    assert draft_data['meta']['url'] == page_with_reversion.get_url(
        is_draft=True
    )

    assert published_response.status_code == 200
    assert published_data['title'] == 'published-title'
    assert published_data['meta']['url'] == page_with_reversion.get_url()


@pytest.mark.django_db
def test_copy_upsteam(admin_client, translated_page, settings, image):
    translated_page.hero_image = image
    translated_page.save()

    url = reverse('copy-upstream', kwargs={'pk': translated_page.pk})

    response = admin_client.get(url)

    assert response.status_code == 200
    assert response.context['page'] == translated_page


@pytest.mark.django_db
def test_update_upstream(admin_client, translated_page, settings, image):
    translated_page.hero_image = image
    translated_page.save()

    url = reverse('update-upstream', kwargs={'pk': translated_page.pk})

    response = admin_client.get(url)

    assert response.status_code == 200
    assert response.context['page'] == translated_page


@pytest.mark.django_db
@pytest.mark.parametrize('url_name', ('copy-upstream', 'update-upstream'))
def test_upstream_anon(client, translated_page, settings, image, url_name):
    translated_page.hero_image = image
    translated_page.save()

    url = reverse(url_name, kwargs={'pk': translated_page.pk})

    response = client.get(url)

    assert response.status_code == 302


@pytest.mark.django_db
@pytest.mark.parametrize('include_slug, expected_template', (
    (True, 'wagtailadmin/pages/edit.html'),
    (False, 'wagtailadmin/pages/create.html'),
))
def test_add_page_prepopulate(
    translated_fas_industry_page, settings, admin_client, image, cluster_data,
    include_slug, expected_template, fas_industry_landing_page
):
    url = reverse(
        'preload-add-page',
        kwargs={
            'service_name': translated_fas_industry_page._meta.app_label,
            'model_name': translated_fas_industry_page._meta.model_name,
            'parent_slug': fas_industry_landing_page.slug,
        }
    )
    model_as_dict = model_to_dict(translated_fas_industry_page, exclude=[
        'go_live_at',
        'expire_at',
        'slug',
    ])
    model_as_dict = {key: val for key, val in model_as_dict.items() if val}
    post_data = {
        **model_as_dict,
        'hero_image': image.file.name,
        'introduction_column_one_icon': image.file.name,
        'introduction_column_two_icon': image.file.name,
        'introduction_column_three_icon': image.file.name,
        **cluster_data,
    }

    expected_data = {
        **model_as_dict,
        'hero_image': str(image.pk),
        'introduction_column_one_icon': str(image.pk),
        'introduction_column_two_icon': str(image.pk),
        'introduction_column_three_icon': str(image.pk),
        'search_filter_sector': model_as_dict['search_filter_sector'][0],
    }
    if include_slug:
        post_data['slug'] = expected_data['slug'] = (
            translated_fas_industry_page.slug
        )

    response = admin_client.post(url, post_data)

    assert response.template_name == [expected_template]
    assert response.status_code == 200

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
    translated_fas_industry_page, settings, admin_client,
    fas_industry_landing_page, cluster_data
):
    url = reverse(
        'preload-add-page',
        kwargs={
            'service_name': translated_fas_industry_page._meta.app_label,
            'model_name': 'doesnotexist',
            'parent_slug': fas_industry_landing_page.slug,
        }
    )

    data = model_to_dict(translated_fas_industry_page, exclude=[
        'go_live_at',
        'expire_at',
        'hero_image',
    ])
    response = admin_client.post(url, {**data, **cluster_data})

    assert response.status_code == 404


@pytest.mark.django_db
def test_add_page_prepopulate_get(
    translated_fas_industry_page, settings, admin_client,
    fas_industry_landing_page, cluster_data
):
    url = reverse(
        'preload-add-page',
        kwargs={
            'service_name': translated_fas_industry_page._meta.app_label,
            'model_name': translated_fas_industry_page._meta.model_name,
            'parent_slug': fas_industry_landing_page.slug,
        }
    )

    response = admin_client.get(url)

    assert response.status_code == 405


@pytest.mark.django_db
def test_list_page(admin_client, translated_page, root_page):
    url = reverse('wagtailadmin_explore', args=(root_page.pk,))

    response = admin_client.get(url)

    assert response.status_code == 200


@pytest.mark.django_db
def test_page_listing(translated_page, admin_client):
    url = reverse('wagtailadmin_pages:edit', args=(translated_page.pk,))

    response = admin_client.get(url)

    assert response.status_code == 200


@pytest.mark.django_db
def test_translations_exposed(page, translated_page, settings, client):
    url = reverse('api:api:pages:detail', kwargs={'pk': translated_page.pk})

    response = client.get(url)

    expected = [[code, label] for code, label in settings.LANGUAGES_LOCALIZED]

    assert response.json()['meta']['languages'] == expected


@pytest.mark.django_db
def test_lookup_by_slug(translated_page, admin_client):
    url = reverse(
        'api:lookup-by-slug',
        kwargs={
            'slug': translated_page.slug,
        }
    )

    response = admin_client.get(url, {'service_name': cms.FIND_A_SUPPLIER})

    assert response.status_code == 200
    assert response.json()['id'] == translated_page.id


@pytest.mark.django_db
def test_lookup_by_slug_missing_required_query_param(translated_page,
                                                     admin_client):
    url = reverse(
        'api:lookup-by-slug',
        kwargs={
            'slug': translated_page.slug,
        }
    )

    response = admin_client.get(url)

    assert response.status_code == 400
    assert response.json() == {'service_name': 'This parameter is required'}


@pytest.mark.django_db
def test_lookup_by_slug_missing_page(admin_client):
    url = reverse('api:lookup-by-slug', kwargs={'slug': 'thing'})

    response = admin_client.get(url, {'service_name': cms.FIND_A_SUPPLIER})

    assert response.status_code == 404


@pytest.mark.django_db
def test_lookup_by_slug_draft(page_with_reversion, client):
    url = reverse(
        'api:lookup-by-slug', kwargs={'slug': page_with_reversion.slug}
    )

    param = permissions.DraftTokenPermisison.TOKEN_PARAM

    draft_response = client.get(url, {
        param: page_with_reversion.get_draft_token(),
        'service_name': cms.FIND_A_SUPPLIER
    })
    draft_data = draft_response.json()
    published_response = client.get(url, {'service_name': cms.FIND_A_SUPPLIER})
    published_data = published_response.json()

    assert draft_response.status_code == 200
    assert draft_data['title'] == 'draft-title'
    assert draft_data['meta']['url'] == page_with_reversion.get_url(
        is_draft=True
    )

    assert published_response.status_code == 200
    assert published_data['title'] == 'published-title'
    assert published_data['meta']['url'] == page_with_reversion.get_url()


@pytest.mark.django_db
def test_lookup_by_full_path(translated_page, admin_client):
    url = reverse('api:lookup-by-full-path')
    response = admin_client.get(
        url,
        {'full_path': translated_page.full_path}
    )
    assert response.status_code == 200
    assert response.json()['id'] == translated_page.id


@pytest.mark.django_db
def test_lookup_by_full_path_missing_param(admin_client):
    url = reverse('api:lookup-by-full-path')
    response = admin_client.get(url)
    assert response.status_code == 400
    assert response.json() == {'full_path': 'This parameter is required'}


@pytest.mark.django_db
def test_lookup_by_full_path_not_found(admin_client):
    url = reverse('api:lookup-by-full-path')
    response = admin_client.get(
        url,
        {'full_path': 'foo'}
    )
    assert response.status_code == 404


def test_cache_etags_match(admin_client):
    service_name = cms.INVEST
    # given there exists a page that is cached
    page = InfoPageFactory.create(live=True)
    url = reverse('api:lookup-by-slug', kwargs={'slug': page.slug})

    # and the page is cached
    admin_client.get(url, {'service_name': service_name})

    # and the cached page is retrieved
    response_two = admin_client.get(url, {'service_name': service_name})

    # then exposing the same etag in subsequent responses results in 304
    response_three = admin_client.get(
        url,
        {'service_name': service_name},
        HTTP_IF_NONE_MATCH=response_two['ETag'],
    )
    assert response_three.status_code == 304
    assert response_three.content == b''


def test_cache_etags_mismatch(admin_client):
    service_name = cms.INVEST
    # given there exists a page that is cached
    page = InfoPageFactory.create(live=True)

    # when the page is retrieved
    url = reverse('api:lookup-by-slug', kwargs={'slug': page.slug})
    admin_client.get(url, {'service_name': service_name})

    # then exposing the same etag in subsequent responses results in 304
    response_two = admin_client.get(
        url,
        {'service_name': service_name},
        HTTP_IF_NONE_MATCH='something-123',
    )

    assert isinstance(response_two, CachedResponse)
    assert response_two.status_code == 200
    assert response_two.content


def test_pages_types_view(admin_client):
    url = reverse('api:pages-types-list')
    response = admin_client.get(url)
    assert response.status_code == 200
    assert 'types' in response.json()


def test_pages_view(admin_client):
    response = admin_client.get('/api/pages/')
    assert response.status_code == 200
