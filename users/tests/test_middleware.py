import pytest

from django.urls import reverse

from users.models import UserProfile
from users.middleware import SSORedirectUsersToRequestAccessViews


class MockProfile:
    def __init__(self, assignment_status):
        if assignment_status is None:
            assignment_status = UserProfile.STATUS_APPROVED
        self.assignment_status = assignment_status


class MockUser:
    def __init__(
        self, authenticated=False, superuser=False,
        assignment_status=None
    ):
        self.authenticated = authenticated
        self.is_superuser = superuser
        self.userprofile = MockProfile(assignment_status)

    def is_authenticated(self):
        return self.authenticated


def test_process_request_returns_none_if_user_is_not_authenticated(rf):
    request = rf.get('/admin/')
    request.user = MockUser(authenticated=False)
    result = SSORedirectUsersToRequestAccessViews().process_request(request)
    assert result is None


def test_process_request_returns_none_if_user_is_a_superuser(rf):
    request = rf.get('/admin/')
    request.user = MockUser(authenticated=True, superuser=True)
    result = SSORedirectUsersToRequestAccessViews().process_request(request)
    assert result is None


@pytest.mark.parametrize('url', (
    '/',
    '/healthcheck/',
    '/activity-stream/v1/',
))
def test_process_request_returns_none_if_url_not_in_admin(rf, url):
    request = rf.get(url)
    request.user = MockUser(authenticated=True, superuser=False)
    result = SSORedirectUsersToRequestAccessViews().process_request(request)
    assert result is None


@pytest.mark.parametrize('url', (
    reverse('wagtailusers_users:sso_request_access'),
    reverse('wagtailusers_users:sso_request_access_success'),
))
def test_process_request_returns_none_if_user_requesting_access(rf, url):
    request = rf.get(url)
    request.user = MockUser(authenticated=True, superuser=False)
    result = SSORedirectUsersToRequestAccessViews().process_request(request)
    assert result is None


@pytest.mark.parametrize('assignment_status, redirects_to', (
    (
        UserProfile.STATUS_CREATED,
        reverse('wagtailusers_users:sso_request_access')
    ),
    (
        UserProfile.STATUS_AWAITING_APPROVAL,
        reverse('wagtailusers_users:sso_request_access_success')
    ),
))
def test_process_request_redirects_for_assignment_status(
    rf, assignment_status, redirects_to
):
    request = rf.get('/admin/')
    request.user = MockUser(
        authenticated=True,
        superuser=False,
        assignment_status=assignment_status,
    )
    result = SSORedirectUsersToRequestAccessViews().process_request(request)
    assert result.status_code == 302
    assert result['Location'] == redirects_to
