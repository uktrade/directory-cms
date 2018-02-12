import pytest

from django.urls import reverse

from core import permissions, views
from config.signature import SignatureCheckPermission
from find_a_supplier.tests.factories import CaseStudyPageFactory


@pytest.fixture
def page():
    return CaseStudyPageFactory.create()


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
