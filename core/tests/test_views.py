import pytest

from django.urls import reverse

from core import permissions, views
from config.signature import SignatureCheckPermission
from find_a_supplier.tests.factories import CaseStudyPageFactory


@pytest.fixture
def page():
    return CaseStudyPageFactory.create()


@pytest.fixture
def translated_page():
    return CaseStudyPageFactory(
        title_en_gb='ENGLISH',
        title_de='GERMAN',
        title_ja='JAPANESE',
        title_zh_hans='SIMPLIFIED CHINESE',
        title_fr='FRENCH',
        title_es='SPANISH',
        title_pt='PORTUGUESE',
        title_pt_br='BRAZILIAN',
        title_ar='ARABIC',
    )


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
def test_draft_view(client, page):
    url = reverse('draft-view', kwargs={'pk': page.pk})
    response = client.get(url)

    assert response.status_code == 302
    assert response.url == page.draft_url


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
def test_translations(client, translated_page, languaue_code, expected):
    url = reverse('api:pages:detail', kwargs={'pk': translated_page.pk})
    response = client.get(url, {'lang': languaue_code})

    assert response.status_code == 200
    assert response.json()['title'] == expected
