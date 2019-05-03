import pytest

from bs4 import BeautifulSoup
from directory_constants.constants import cms
from modeltranslation.utils import build_localized_fieldname
from wagtail.core.models import Site

from django.forms.models import model_to_dict
from django.urls import reverse

from core import helpers, permissions, views
from core.helpers import CachedResponse
from conf.signature import SignatureCheckPermission
from find_a_supplier.tests.factories import (
    FindASupplierAppFactory, IndustryLandingPageFactory
)
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
    client, translated_page, site_with_translated_page_as_root, language_code,
    expected_title
):
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
    query_params = {'service_name': 'FIND_A_SUPPLIER'}
    query_params.update(languge_query_params)
    response = client.get(url, query_params)
    assert response.status_code == 200
    assert response.json()['title'] == expected_title


@pytest.mark.parametrize('language_code', (
    'en-gb' 'de' 'ja', 'zh-hans', 'fr', 'es', 'pt', 'ar',
))
@pytest.mark.django_db
def test_api_falls_back_to_english_when_translations_unavailable(
    client, untranslated_page, site_with_untranslated_page_as_root,
    language_code
):
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
    query_params = {'service_name': 'FIND_A_SUPPLIER'}
    query_params.update(languge_query_params)
    response = client.get(url, query_params)
    assert response.status_code == 200
    assert response.json()['title'] == 'ENGLISH'


@pytest.mark.django_db
def test_api_serves_drafts(
    client, page_with_reversion, site_with_revised_page_as_root
):
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
    query_params = {'service_name': 'FIND_A_SUPPLIER'}
    query_params.update(draft_query_params)
    response = client.get(url, query_params)
    assert response.status_code == 200
    data = response.json()
    assert data['title'] == 'draft-title'
    assert data['meta']['url'] == page_with_reversion.get_url(is_draft=True)


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
def test_lookup_by_path(root_page, page, admin_client):
    # Creating a semi-realistic page structure and moving page into it
    app_root_page = FindASupplierAppFactory(parent=root_page)
    parent_page = IndustryLandingPageFactory(parent=app_root_page)
    page.move(target=parent_page, pos='last-child')

    # Creating a site with app_root_page as the root
    site = Site.objects.create(
        site_name='Test',
        hostname='example.com',
        root_page=app_root_page,
    )

    # to lookup page, the path should include the parent's slug and
    # the page's slug, but NOT that of app_root_page
    path = '/'.join([parent_page.slug, page.slug])
    response = admin_client.get(reverse(
        'api:lookup-by-path', kwargs={'site_id': site.id, 'path': path}
    ))
    assert response.status_code == 200
    assert response.json()['id'] == page.id

    # paths are normalised by the view, so the presence of extra '/'
    # characters on either end of the value shouldn't hinder matching
    dodgy_path = '///' + path + '///'
    response = admin_client.get(reverse(
        'api:lookup-by-path', kwargs={'site_id': site.id, 'path': dodgy_path}
    ))
    assert response.status_code == 200
    assert response.json()['id'] == page.id


@pytest.mark.django_db
def test_lookup_for_path_for_non_existent_page(client):
    site_id = 52
    path = 'xyz'
    response = client.get(reverse(
        'api:lookup-by-path', kwargs={'site_id': site_id, 'path': path}
    ))
    assert response.status_code == 404

    expected_msg = f"No page could be found matching site_id '{site_id}' and path '{path}'" # noqa
    assert response.json() == {'message': expected_msg}


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
    service_name = cms.FIND_A_SUPPLIER
    slug = 'thing'

    url = reverse('api:lookup-by-slug', kwargs={'slug': slug})

    response = admin_client.get(url, {'service_name': service_name})

    assert response.status_code == 404

    expected_msg = f"No page could be found matching service_name '{service_name}' and slug '{slug}'" # noqa
    assert response.json() == {'message': expected_msg}


def test_cache_etags_match(admin_client, root_page):
    service_name = cms.INVEST

    # given there exists a page that is cached
    page = InfoPageFactory.create(parent=root_page, live=True)
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


def test_cache_etags_mismatch(admin_client, root_page):
    service_name = cms.INVEST
    # given there exists a page that is cached
    page = InfoPageFactory.create(parent=root_page, live=True)

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
