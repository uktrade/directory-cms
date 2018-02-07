import pytest

from core import constants, permissions
from demo.models import DemoPage


@pytest.fixture
def page():
    return DemoPage(
        view_app=constants.FIND_A_SUPPLIER,
        view_path='/things/',
        pk=2,
    )


def test_valid_draft_token(rf, page):
    request = rf.get('/', {'draft_token': page.get_draft_token()})
    permission = permissions.DraftTokenPermisison()

    assert permission.has_object_permission(request, None, page) is True


def test_invalid_draft_token(rf, page):
    request = rf.get('/', {'draft_token': 'thing'})
    permission = permissions.DraftTokenPermisison()

    assert permission.has_object_permission(request, None, page) is False


def test_no_draft_token(rf, page):
    request = rf.get('/')
    permission = permissions.DraftTokenPermisison()

    assert permission.has_object_permission(request, None, page) is False
