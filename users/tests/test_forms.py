import pytest
from django.contrib.auth.models import Group

from .factories import UserFactory, GroupPagePermissionFactory
from export_readiness.tests.factories import ArticleListingPageFactory
from users.forms import UserCreationForm


@pytest.mark.django_db
def test_super_user_can_see_all_the_groups():
    user = UserFactory(is_superuser=True, is_staff=True)
    form = UserCreationForm(user=user)
    all_groups_count = Group.objects.all().count()
    assert form.fields['groups'].queryset.count() == all_groups_count


@pytest.mark.django_db
def test_user_can_see_same_entry_point_groups(root_page):
    page = ArticleListingPageFactory(parent=root_page)
    group_page_one = GroupPagePermissionFactory(
        page=page
    )
    group_page_two = GroupPagePermissionFactory(
        page=page
    )
    user = UserFactory(
        is_superuser=False,
        is_staff=False,
        groups=[group_page_one.group]
    )
    form = UserCreationForm(user=user)
    assert list(
        form.fields['groups'].queryset.values_list('pk', flat=True)
    ) == [group_page_one.group.pk, group_page_two.group.pk]


@pytest.mark.django_db
def test_normal_user_with_no_group_assigned_sees_no_groups():
    user = UserFactory(is_superuser=False, is_staff=False)
    form = UserCreationForm(user=user)
    assert form.fields['groups'].queryset.count() == 0
