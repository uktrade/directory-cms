import time
from unittest import mock

from bs4 import BeautifulSoup
from directory_constants import cms
from modeltranslation.utils import build_localized_fieldname
import pytest
from rest_framework.serializers import Serializer

from django.forms.models import model_to_dict
from django.urls import reverse

from core import cache, helpers, permissions, serializer_mapping, views
from core.helpers import CachedResponse
from conf.signature import SignatureCheckPermission
from components.models import ComponentsApp
from tests.great_international.factories import InternationalArticlePageFactory
from tests.core.helpers import make_test_video


from .helpers import clean_post_data


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


@pytest.mark.django_db
def test_permissions_draft(rf):
    view = views.PagesOptionalDraftAPIEndpoint()
    param = permissions.DraftTokenPermisison.TOKEN_PARAM
    view.request = rf.get('/', {param: 'thing'})

    assert view.permission_classes == [
        SignatureCheckPermission,
        permissions.DraftTokenPermisison
    ]


@pytest.mark.django_db
def test_permissions_published(rf):
    view = views.PagesOptionalDraftAPIEndpoint()
    view.request = rf.get('/')

    assert view.permission_classes == [
        SignatureCheckPermission,
    ]


@pytest.mark.parametrize('language_code,expected_title', (
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
def test_api_translations_are_loaded_when_available(
    client, translated_page, site_with_translated_page_as_root, language_code, expected_title
):
    cache.rebuild_all_cache()

    # to be added as a query params to all requests
    languge_query_params = {'lang': language_code}

    # looking up by id
    url = reverse('api:api:pages:detail', kwargs={'pk': translated_page.pk})
    response = client.get(url, languge_query_params)
    assert response.status_code == 200
    assert response.json()['title'] == expected_title

    # looking up by path and site_id
    # NOTE: path should be blank when you want a site root page
    url = reverse('api:lookup-by-path', kwargs={
        'path': '', 'site_id': site_with_translated_page_as_root.id,
    })
    response = client.get(url, languge_query_params)
    assert response.status_code == 200
    assert response.json()['title'] == expected_title

    # looking up by slug and service_name
    url = reverse('api:lookup-by-slug', kwargs={'slug': translated_page.slug})
    query_params = {'service_name': cms.GREAT_INTERNATIONAL}
    query_params.update(languge_query_params)
    response = client.get(url, query_params)
    assert response.status_code == 200
    assert response.json()['title'] == expected_title


@pytest.mark.parametrize('language_code', (
    'en-gb', 'de', 'ja', 'zh-hans', 'fr', 'es', 'pt', 'ar',
))
@pytest.mark.django_db
def test_api_falls_back_to_english_when_translations_unavailable(
    client, untranslated_page, site_with_untranslated_page_as_root, language_code
):
    cache.rebuild_all_cache()
    # to be added as a query params to all requests
    languge_query_params = {'lang': language_code}

    # looking up by id
    url = reverse(
        'api:api:pages:detail',
        kwargs={'pk': untranslated_page.pk}
    )
    response = client.get(url, languge_query_params)
    assert response.status_code == 200
    assert response.json()['title'] == 'ENGLISH'

    # looking up by site_id + path
    # NOTE: path should be blank when you want a site root page
    url = reverse(
        'api:lookup-by-path',
        kwargs={'path': '', 'site_id': site_with_untranslated_page_as_root.id}
    )
    response = client.get(url, languge_query_params)
    assert response.status_code == 200
    assert response.json()['title'] == 'ENGLISH'

    # looking up by service_name + slug
    url = reverse(
        'api:lookup-by-slug',
        kwargs={'slug': untranslated_page.slug}
    )
    query_params = {'service_name': 'GREAT_INTERNATIONAL'}
    query_params.update(languge_query_params)
    response = client.get(url, query_params)
    assert response.status_code == 200
    assert response.json()['title'] == 'ENGLISH'


@pytest.mark.django_db
def test_api_serves_drafts(client, page_with_reversion, site_with_revised_page_as_root):
    cache.rebuild_all_cache()
    # For applying the draft token as a query param for each request
    param_name = permissions.DraftTokenPermisison.TOKEN_PARAM
    draft_query_params = {
        param_name: page_with_reversion.get_draft_token()
    }

    # first we'll get a non-draft response for comparison
    url = reverse(
        'api:api:pages:detail', kwargs={'pk': page_with_reversion.pk}
    )
    response = client.get(url)
    assert response.status_code == 200
    data = response.json()
    assert data['title'] == 'published-title'
    assert data['meta']['url'] == page_with_reversion.get_url()

    # get draft version, looking up by id
    response = client.get(url, draft_query_params)
    assert response.status_code == 200
    data = response.json()
    assert data['title'] == 'draft-title'
    assert data['meta']['url'] == page_with_reversion.get_url(is_draft=True)

    # get draft version, looking up by site_id + path
    # NOTE: path should be blank when you want a site root page
    url = reverse(
        'api:lookup-by-path',
        kwargs={'path': '', 'site_id': site_with_revised_page_as_root.id}
    )
    response = client.get(url, draft_query_params)
    assert response.status_code == 200
    data = response.json()
    assert data['title'] == 'draft-title'
    assert data['meta']['url'] == page_with_reversion.get_url(is_draft=True)

    # get draft version, looking up by service_name + slug
    url = reverse(
        'api:lookup-by-slug', kwargs={'slug': page_with_reversion.slug}
    )
    query_params = {'service_name': cms.GREAT_INTERNATIONAL}
    query_params.update(draft_query_params)
    response = client.get(url, query_params)
    assert response.status_code == 200
    data = response.json()
    assert data['title'] == 'draft-title'
    assert data['meta']['url'] == page_with_reversion.get_url(is_draft=True)


@pytest.mark.django_db
def test_copy_upsteam(admin_client, translated_page, image):
    translated_page.hero_image = image
    translated_page.save()

    url = reverse('copy-upstream', kwargs={'pk': translated_page.pk})

    response = admin_client.get(url)

    assert response.status_code == 200
    assert response.context['page'] == translated_page


@pytest.mark.django_db
def test_update_upstream(admin_client, translated_page, image):
    translated_page.hero_image = image
    translated_page.save()

    url = reverse('update-upstream', kwargs={'pk': translated_page.pk})

    response = admin_client.get(url)

    assert response.status_code == 200
    assert response.context['page'] == translated_page


@pytest.mark.django_db
@pytest.mark.parametrize('url_name', ('copy-upstream', 'update-upstream'))
def test_upstream_anon(client, translated_page, image, url_name):
    translated_page.hero_image = image
    translated_page.save()

    url = reverse(url_name, kwargs={'pk': translated_page.pk})

    response = client.get(url)

    assert response.status_code == 302


@pytest.mark.django_db
@pytest.mark.parametrize('is_edit, expected_template', (
    (True, 'wagtailadmin/pages/edit.html'),
    (False, 'wagtailadmin/pages/create.html'),
))
def test_add_page_prepopulate(
    is_edit, expected_template, international_root_page, translated_page, admin_client, image, cluster_data
):
    cache.rebuild_all_cache()
    cache.PageIDCache.populate()
    url = reverse('preload-add-page')
    model_as_dict = model_to_dict(translated_page, exclude=[
        'go_live_at',
        'expire_at',
        'slug',
    ])
    model_as_dict = {key: val for key, val in model_as_dict.items() if val}
    post_data = {
        **model_as_dict,
        '(image)hero_image': image.file.name,
        '(image)introduction_column_one_icon': image.file.name,
        '(image)introduction_column_two_icon': image.file.name,
        '(image)introduction_column_three_icon': image.file.name,
        'management-app_label': translated_page._meta.app_label,
        'management-model_name': translated_page._meta.model_name,
        'management-parent_path': international_root_page.get_url_parts()[2],
        'management-site_name': international_root_page.get_site().site_name,
        **cluster_data,
    }
    expected_data = {
        **model_as_dict,
        'hero_image': str(image.pk),
        'introduction_column_one_icon': str(image.pk),
        'introduction_column_two_icon': str(image.pk),
        'introduction_column_three_icon': str(image.pk),
    }
    if is_edit:
        post_data['management-path'] = expected_data['path'] = translated_page.get_url_parts()[2]

    response = admin_client.post(url, clean_post_data(post_data))

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
        assert str(actual) == str(value)


@pytest.mark.django_db
def test_add_page_prepopulate_missing_content_type(
    translated_page, admin_client, international_root_page, cluster_data
):
    url = reverse('preload-add-page')

    post_data = model_to_dict(
        international_root_page,
        exclude=['go_live_at', 'expire_at', 'hero_image']
    )
    post_data.update(cluster_data)
    post_data.update({
        'management-app_label': translated_page._meta.app_label,
        'management-model_name': 'doesnotexist',
        'management-parent_path': international_root_page.get_url_parts()[2],
        'management-site_name': translated_page.get_site().site_name,
    })

    response = admin_client.post(url, clean_post_data(post_data))

    assert response.status_code == 404


@pytest.mark.django_db
def test_list_page(admin_client, root_page):
    url = reverse('wagtailadmin_explore', args=(root_page.pk,))

    response = admin_client.get(url)

    assert response.status_code == 200


@pytest.mark.django_db
def test_page_listing(translated_page, admin_client):
    url = reverse('wagtailadmin_pages:edit', args=(translated_page.pk,))

    response = admin_client.get(url)

    assert response.status_code == 200


@pytest.mark.django_db
def test_translations_exposed(translated_page, settings, client):
    cache.rebuild_all_cache()

    url = reverse('api:api:pages:detail', kwargs={'pk': translated_page.pk})

    response = client.get(url)

    expected = [[code, label] for code, label in settings.LANGUAGES_LOCALIZED]

    assert response.json()['meta']['languages'] == expected


@pytest.mark.django_db
def test_unserializable_page_requested(settings, client):
    page = ComponentsApp.objects.create(
        title_en_gb='the app',
        depth=2,
        path='/thing',
    )
    cache.rebuild_all_cache()

    url = reverse('api:api:pages:detail', kwargs={'pk': page.pk})

    response = client.get(url)

    assert response.status_code == 204


@pytest.mark.django_db
def test_lookup_by_path(international_root_page, page, admin_client):
    # Creating a semi-realistic page structure and moving page into it
    parent_page = InternationalArticlePageFactory(parent=international_root_page)
    page.move(target=parent_page, pos='last-child')

    cache.rebuild_all_cache()

    # to lookup page, the path should include the parent's slug and
    # the page's slug, but NOT that of app_root_page
    path = '/'.join([parent_page.slug, page.slug])
    response = admin_client.get(reverse(
        'api:lookup-by-path', kwargs={'site_id': '1', 'path': path}
    ))

    assert response.status_code == 200
    assert response.json()['id'] == page.id

    # paths are normalised by the view, so the presence of extra '/'
    # characters on either end of the value shouldn't hinder matching
    dodgy_path = '///' + path + '///'
    response = admin_client.get(reverse(
        'api:lookup-by-path', kwargs={'site_id': '1', 'path': dodgy_path}
    ))
    assert response.status_code == 200
    assert response.json()['id'] == page.id


@pytest.mark.django_db
def test_lookup_by_path_for_non_existent_page(client):
    site_id = 52
    path = 'xyz'
    response = client.get(reverse(
        'api:lookup-by-path', kwargs={'site_id': site_id, 'path': path}
    ))
    assert response.status_code == 404

    expected_msg = f"No page found matching site_id '{site_id}' and path '{path}'"
    assert response.json() == {'message': expected_msg}


@pytest.mark.django_db
def test_lookup_by_slug(translated_page, admin_client):
    cache.rebuild_all_cache()

    url = reverse(
        'api:lookup-by-slug',
        kwargs={
            'slug': translated_page.slug,
        }
    )

    response = admin_client.get(url, {'service_name': cms.GREAT_INTERNATIONAL})

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
    service_name = cms.FIND_A_SUPPLIER
    slug = 'thing'

    url = reverse('api:lookup-by-slug', kwargs={'slug': slug})

    response = admin_client.get(url, {'service_name': service_name})

    assert response.status_code == 404

    expected_msg = f"No page could be found matching service_name '{service_name}' and slug '{slug}'"
    assert response.json() == {'message': expected_msg}


@pytest.mark.django_db
def test_cache_etags_match(admin_client, international_root_page):
    service_name = cms.GREAT_INTERNATIONAL

    # given there exists a page that is cached
    page = InternationalArticlePageFactory.create(parent=international_root_page, live=True)
    url = reverse('api:lookup-by-slug', kwargs={'slug': page.slug})
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


@pytest.mark.django_db
def test_cache_miss_slow_database_read(admin_client, international_root_page):

    class SlowSerializer(Serializer):
        def to_representation(self, instance):
            time.sleep(3)
            return {}

    service_name = cms.GREAT_INTERNATIONAL

    page = InternationalArticlePageFactory.create(parent=international_root_page, live=True)

    url = reverse('api:lookup-by-slug', kwargs={'slug': page.slug})

    # given the page  is very slow to read
    with mock.patch.dict(serializer_mapping.MODELS_SERIALIZERS_MAPPING, {page.__class__: SlowSerializer}):
        response = admin_client.get(url, {'service_name': service_name})

    # then the response results in 501
    assert response.status_code == 501


@pytest.mark.django_db
def test_cache_etags_mismatch(admin_client, international_root_page):
    service_name = cms.GREAT_INTERNATIONAL
    # given there exists a page that is cached
    page = InternationalArticlePageFactory.create(parent=international_root_page, live=True)

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


@pytest.mark.django_db
def test_pages_types_view(admin_client):
    url = reverse('api:pages-types-list')
    response = admin_client.get(url)
    assert response.status_code == 200
    assert 'types' in response.json()


@pytest.mark.django_db
def test_pages_view(admin_client):
    response = admin_client.get('/api/pages/')
    assert response.status_code == 200


@pytest.mark.django_db
def test_robots_txt(client):
    response = client.get('/robots.txt')
    assert response.content == b'User-agent: * \nDisallow: /'
    assert response.headers['Content-Type'] == 'text/plain'


@pytest.mark.django_db
def test_serve_subtitles(client):
    media = make_test_video()

    media.subtitles_en = 'Dummy subtitles content'
    media.save()

    dest = reverse('subtitles-serve', args=[media.id, 'en'])

    resp = client.get(dest, follow=False)

    assert resp.status_code == 200
    assert resp.content == b'Dummy subtitles content'


@pytest.mark.django_db
def test_serve_subtitles__missing_media(client):

    dest = reverse('subtitles-serve', args=[99999, 'en'])
    resp = client.get(dest, follow=False)

    assert resp.status_code == 404


@pytest.mark.django_db
def test_serve_subtitles__none_available(client):
    media = make_test_video()
    media.save()

    dest = reverse('subtitles-serve', args=[media.id, 'en'])

    resp = client.get(dest, follow=False)

    assert resp.status_code == 404
