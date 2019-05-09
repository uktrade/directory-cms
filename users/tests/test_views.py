import sys
import pytest
from importlib import import_module, reload
from django.conf import settings
from django.core.urlresolvers import clear_url_caches
from django.urls import reverse
from rest_framework import status

from .factories import UserFactory


def test_create_user_view_get(admin_client):
    url = reverse('wagtailusers_users:add')
    response = admin_client.get(url)
    assert response.status_code == status.HTTP_200_OK


@pytest.mark.django_db
def test_create_user_view(admin_client):
    url = reverse('wagtailusers_users:add')
    response = admin_client.post(
        url,
        data={
            'username': 'test',
            'email': 'test@test.com',
            'first_name': 'Test',
            'last_name': 'User',
            'password1': 'password',
            'password2': 'password',
            'groups': ['1']
        }
    )
    assert response.context['message'] == 'User test created.'
    assert response.status_code == status.HTTP_302_FOUND
    assert response.url == reverse('wagtailusers_users:index')


@pytest.mark.django_db
def test_create_user_view_invalid_form(admin_client):
    url = reverse('wagtailusers_users:add')
    response = admin_client.post(
        url,
        data={
            'username': 'test',
            'email': 'test@test.com',
            'first_name': 'Test',
            'last_name': 'User',
            'password1': 'password',
            'password2': 'passwords',
            'groups': ['1']
        }
    )
    message = response.context['message']
    assert message == 'The user could not be created due to errors.'
    assert response.status_code == status.HTTP_200_OK


@pytest.mark.django_db
def test_edit_user_view(admin_client):
    user = UserFactory(username='test')
    url = reverse('wagtailusers_users:edit', kwargs={'pk': user.pk})
    response = admin_client.post(
        url,
        data={
            'username': 'foobar',
            'email': 'test@test.com',
            'first_name': 'Test',
            'last_name': 'User',
            'groups': ['1']
        }
    )
    assert response.context['message'] == 'User foobar updated.'
    assert response.status_code == status.HTTP_302_FOUND
    assert response.url == reverse('wagtailusers_users:index')
    user.refresh_from_db()
    assert user.username == 'foobar'


@pytest.mark.django_db
def test_edit_user_view_invalid(admin_client):
    user = UserFactory(username='test')
    url = reverse('wagtailusers_users:edit', kwargs={'pk': user.pk})
    response = admin_client.post(
        url,
        data={
            'username': 'foobar',
            'email': 'test@test.com',
            'last_name': 'User',
            'groups': ['1']
        }
    )
    message = response.context['message']
    assert message == 'The user could not be saved due to errors.'
    assert response.status_code == status.HTTP_200_OK


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
