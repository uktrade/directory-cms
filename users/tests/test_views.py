import sys
import pytest
from importlib import import_module, reload
from django.conf import settings
from django.core.urlresolvers import clear_url_caches
from django.urls import reverse
from rest_framework import status

from .factories import UserFactory

USER_DETAILS = {
    'username': 'test',
    'email': 'test@test.com',
    'first_name': 'Foo',
    'last_name': 'Bar',
}

USER_DETAILS_CREATE = USER_DETAILS.copy()
USER_DETAILS_CREATE.update(password1='pass', password2='pass')

USER_DETAILS_CHANGING = {
    'username': 'johnsmith',
    'email': 'john@smiths.com',
    'first_name': 'John',
    'last_name': 'Smith',
}


def test_create_user_view_get(admin_client):
    url = reverse('wagtailusers_users:add')
    response = admin_client.get(url)
    assert response.status_code == status.HTTP_200_OK


@pytest.mark.django_db
def test_create_user_view(admin_client):
    url = reverse('wagtailusers_users:add')

    response = admin_client.post(url, data=USER_DETAILS_CREATE)

    assert response.context['message'] == 'User test created.'
    assert response.status_code == status.HTTP_302_FOUND
    assert response.url == reverse('wagtailusers_users:index')


@pytest.mark.django_db
def test_create_user_view_invalid_form(admin_client):
    url = reverse('wagtailusers_users:add')

    post_data = USER_DETAILS.copy()
    post_data.update(email='This is not an email address')
    response = admin_client.post(url, post_data)

    message = response.context['message']
    assert message == 'The user could not be created due to errors.'
    assert response.status_code == status.HTTP_200_OK


@pytest.mark.django_db
def test_get_edit_user_view(admin_client):
    user = UserFactory(**USER_DETAILS)
    url = reverse('wagtailusers_users:edit', kwargs={'pk': user.pk})
    response = admin_client.get(url)
    assert response.status_code == status.HTTP_200_OK
    assert response.context['can_delete'] is True


@pytest.mark.django_db
def test_edit_user_view(admin_client):
    user = UserFactory(**USER_DETAILS)
    url = reverse('wagtailusers_users:edit', kwargs={'pk': user.pk})

    # We'll add the user to a group, as well as changing their details
    post_data = USER_DETAILS_CHANGING.copy()
    post_data['groups'] = ['1']
    response = admin_client.post(url, data=post_data)

    assert response.context['message'] == 'User johnsmith updated.'
    assert response.status_code == status.HTTP_302_FOUND
    assert response.url == reverse('wagtailusers_users:index')

    user.refresh_from_db()
    # The user's details should have changed to reflect the posted values
    user.refresh_from_db()
    for field_name, changed_value in USER_DETAILS_CHANGING.items():
        assert getattr(user, field_name) == changed_value
    # And they should have been added to a group
    group_ids = set(user.groups.values_list('id', flat=True))
    assert group_ids == {1}


@pytest.mark.django_db
def test_edit_user_view_cannot_change_personal_details_when_sso_enforced(
    admin_client
):
    # Set this flag to True and actions if previous test
    settings.FEATURE_FLAGS['ENFORCE_STAFF_SSO_ON'] = True

    user = UserFactory(**USER_DETAILS)

    # Post changes to the view
    url = reverse('wagtailusers_users:edit', kwargs={'pk': user.pk})
    admin_client.post(url, data=USER_DETAILS_CHANGING)

    # The users details should remain unchanged, because the
    # personal detail fields should all be disabled
    user.refresh_from_db()
    for field_name, original_value in USER_DETAILS.items():
        assert getattr(user, field_name) == original_value

    # Change this back to avoid cross-test pollution
    settings.FEATURE_FLAGS['ENFORCE_STAFF_SSO_ON'] = False


@pytest.mark.django_db
def test_edit_user_view_preserves_ability_to_update_is_active(admin_client):
    # Set this flag to True and actions if previous test
    settings.FEATURE_FLAGS['ENFORCE_STAFF_SSO_ON'] = True

    # Create an 'inactive' user to test with
    user = UserFactory(**USER_DETAILS)
    user.is_active = False
    user.save()

    # Post using the same details + 'is_active=on'
    post_data = USER_DETAILS.copy()
    post_data.update(is_active='on')
    url = reverse('wagtailusers_users:edit', kwargs={'pk': user.pk})
    admin_client.post(url, data=post_data)

    # The change to 'is_active' should have been applied, because that field
    # is not disabled along with the personal detail ones
    user.refresh_from_db()
    assert user.is_active is True

    # Change this back to avoid cross-test pollution
    settings.FEATURE_FLAGS['ENFORCE_STAFF_SSO_ON'] = False


def reload_urlconf(urlconf=None):
    clear_url_caches()
    if urlconf is None:
        urlconf = settings.ROOT_URLCONF
    if urlconf in sys.modules:
        reload(sys.modules[urlconf])
    else:
        import_module(urlconf)


def test_force_staff_sso(client):
    """Test that URLs and redirects are in place."""
    settings.FEATURE_FLAGS['ENFORCE_STAFF_SSO_ON'] = True
    settings.AUTHBROKER_CLIENT_ID = 'debug'
    settings.AUTHBROKER_CLIENT_SECRET = 'debug'
    settings.AUTHBROKER_URL = 'https://test.com'
    reload_urlconf()

    assert reverse('authbroker:login') == '/auth/login/'
    assert reverse('authbroker:callback') == '/auth/callback/'
    response = client.get('/admin/login/')
    assert response.status_code == 302
    assert response.url == '/auth/login/'

    settings.FEATURE_FLAGS['ENFORCE_STAFF_SSO_ON'] = False
    reload_urlconf()
