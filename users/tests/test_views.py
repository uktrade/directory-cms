import pytest
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
            'email': 'This is not an email address',
            'first_name': 'Test',
            'last_name': 'User',
            'groups': ['1']
        }
    )
    message = response.context['message']
    assert message == 'The user could not be created due to errors.'
    assert response.status_code == status.HTTP_200_OK


@pytest.mark.django_db
def test_get_edit_user_view(admin_client):
    user = UserFactory(username='test', email='test@test.com')
    url = reverse('wagtailusers_users:edit', kwargs={'pk': user.pk})
    response = admin_client.get(url)
    assert response.status_code == status.HTTP_200_OK
    assert response.context['can_delete'] is True


@pytest.mark.django_db
def test_edit_user_view(admin_client):
    user = UserFactory(username='test', email='test@test.com')
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
    assert response.context['message'] == 'User test updated.'
    assert response.status_code == status.HTTP_302_FOUND
    assert response.url == reverse('wagtailusers_users:index')
    user.refresh_from_db()
    group_ids = set(user.groups.values_list('id', flat=True))
    assert group_ids == {1}


@pytest.mark.django_db
def test_edit_user_view_cant_change_basic_details(admin_client):
    user = UserFactory(username='test', email='test@test.com')
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
    assert response.context['message'] == 'User test updated.'
    assert response.status_code == status.HTTP_302_FOUND
    assert response.url == reverse('wagtailusers_users:index')
    user.refresh_from_db()
    assert user.username == 'test'
    assert user.is_active is True


@pytest.mark.django_db
def test_edit_user_view_can_reactivate_disabled_users(admin_client):
    user = UserFactory(username='test', email='test@test.com', is_active=False)
    url = reverse('wagtailusers_users:edit', kwargs={'pk': user.pk})
    response = admin_client.post(
        url,
        data={
            'username': 'foobar',
            'email': 'test@test.com',
            'first_name': 'Test',
            'last_name': 'User',
            'is_active': 'on',
            'groups': ['1']
        }
    )
    assert response.status_code == status.HTTP_302_FOUND
    assert response.url == reverse('wagtailusers_users:index')
    user.refresh_from_db()
    assert user.is_active is True
