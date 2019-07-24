import pytest
from django.core.exceptions import ValidationError
from django.contrib.auth.models import Group

from groups.models import GroupInfo


@pytest.mark.django_db
def test_groupinfo_uses_name_singular_for_str(groups_with_info):
    for group in groups_with_info:
        assert str(group.info) == group.info.name_singular


@pytest.mark.django_db
def test_groupinfo_clean_fields_allows_one_team_leaders_group():
    group = Group.objects.create(name='team leaders')
    group.info.is_team_leaders_group = True
    group.info.clean_fields()  # No error raised here!
    group.info.save()

    new_group = Group.objects.create(name='new')
    new_group.info.is_team_leaders_group = True
    with pytest.raises(ValidationError):
        new_group.info.clean_fields()

    GroupInfo.objects.all().update(is_team_leaders_group=True)
    newer_group = Group.objects.create(name='newer')
    newer_group.info.is_team_leaders_group = True
    with pytest.raises(GroupInfo.MultipleObjectsReturned):
        newer_group.info.clean_fields()
