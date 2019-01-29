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
            'password1': 'password',
            'password2': 'password',
            'groups': ['1']
        }
    )
    assert response.status_code == status.HTTP_302_FOUND
    assert response.url == reverse('wagtailusers_users:index')


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
            'password1': 'password',
            'password2': 'password',
            'groups': ['1']
        }
    )
    assert response.status_code == status.HTTP_302_FOUND
    assert response.url == reverse('wagtailusers_users:index')
    user.refresh_from_db()
    assert user.username == 'foobar'
