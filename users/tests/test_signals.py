from unittest import mock

import pytest
from django.contrib.auth import get_user_model

from users.models import UserProfile, CREATED


@pytest.mark.django_db
def test_new_user_profile_status_created():
    User = get_user_model()
    user = User.objects.create_user('test')
    profile = UserProfile.objects.get(user=user)
    assert profile.assignment_status == CREATED


@pytest.mark.django_db
def test_user_profile_status_user_updated():
    User = get_user_model()
    user = User.objects.create_user('test')
    with mock.patch('users.signals.UserProfile') as mocked_profile:
        user.first_name = 'Testo'
        user.save()
        assert mocked_profile.called is False
