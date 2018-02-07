import pytest

from core import constants
from demo.models import DemoPage


@pytest.fixture
def page():
    return DemoPage(
        view_app=constants.FIND_A_SUPPLIER,
        view_path='/things/',
        pk=2,
    )


@pytest.mark.django_db
def test_base_model_check_valid_draft_token(page):
    draft_token = page.get_draft_token()

    assert page.is_draft_token_valid(draft_token) is True


@pytest.mark.django_db
def test_base_model_check_invalid_draft_token(page):
    assert page.is_draft_token_valid('asdf') is False


@pytest.mark.django_db
def test_base_model_redirect_published_url(rf, page):
    request = rf.get('/')
    request.is_preview = False

    response = page.serve(request)

    assert response.status_code == 302
    assert response.url == page.published_url


@pytest.mark.django_db
def test_base_model_redirect_preview_url(rf, page):
    request = rf.get('/')
    request.is_preview = True

    response = page.serve(request)

    assert response.status_code == 302
    assert response.url == page.preview_url
