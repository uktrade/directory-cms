import pytest

from core import permissions
from find_a_supplier.tests.factories import IndustryPageFactory


@pytest.fixture
def page():
    return IndustryPageFactory(pk=2, title='3')


@pytest.mark.django_db
def test_valid_draft_token(rf, page):
    request = rf.get('/', {'draft_token': page.get_draft_token()})
    permission = permissions.DraftTokenPermisison()

    assert permission.has_object_permission(request, None, page) is True


@pytest.mark.django_db
def test_invalid_draft_token(rf, page):
    request = rf.get('/', {'draft_token': 'thing'})
    permission = permissions.DraftTokenPermisison()

    assert permission.has_object_permission(request, None, page) is False


@pytest.mark.django_db
def test_no_draft_token(rf, page):
    request = rf.get('/')
    permission = permissions.DraftTokenPermisison()

    assert permission.has_object_permission(request, None, page) is False
