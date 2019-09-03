import pytest

from core import permissions


@pytest.mark.django_db
def test_valid_draft_token(rf, international_root_page):
    request = rf.get('/', {'draft_token': international_root_page.get_draft_token()})
    permission = permissions.DraftTokenPermisison()

    assert permission.has_object_permission(request, None, international_root_page) is True


@pytest.mark.django_db
def test_invalid_draft_token(rf, international_root_page):
    request = rf.get('/', {'draft_token': 'thing'})
    permission = permissions.DraftTokenPermisison()

    assert permission.has_object_permission(request, None, international_root_page) is False


@pytest.mark.django_db
def test_no_draft_token(rf, international_root_page):
    request = rf.get('/')
    permission = permissions.DraftTokenPermisison()

    assert permission.has_object_permission(request, None, international_root_page) is False
