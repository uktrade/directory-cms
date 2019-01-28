import pytest
from django.urls import reverse
from rest_framework import status


def test_create_user_view_get(admin_client):
    url = reverse('wagtailusers_users:add')
    response = admin_client.get(url)
    assert response.status_code == status.HTTP_200_OK


@pytest.mark.django_db
def test_create_user_view(admin_client):
    url = reverse('wagtailusers_users:add')
    response = admin_client.post(url,
        data={}
    )
    assert response.status_code == status.HTTP_201_CREATED


@pytest.mark.django_db
def test_edit_user_view(admin_client):
    url = reverse('wagtailusers_users:edit')

