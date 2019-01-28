import pytest
from django.contrib.auth.models import Group

from .factories import UserFactory
from users.forms import UserCreationForm


@pytest.mark.django_db
def test_super_user_can_see_all_the_groups():
    user = UserFactory(is_superuser=True, is_staff=True)
    form = UserCreationForm(user=user)
    assert form.fields['groups'].queryset == Group.objects.all()


@pytest.mark.django_db
def test_user_can_see_same_entry_point_groups():
    pass


@pytest.mark.django_db
def test_normal_user_with_no_group_assigned_sees_no_groups():
    user = UserFactory(is_superuser=True, is_staff=True)
    form = UserCreationForm(user=user)
    assert form.fields['groups'].queryset == Group.objects.none()
