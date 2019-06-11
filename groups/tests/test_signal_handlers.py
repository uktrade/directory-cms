import pytest
from django.contrib.auth.models import Group

from groups.models import GroupInfo


@pytest.mark.django_db
def test_groupinfo_created_automatically_for_new_groups():
    group = Group.objects.create(name='test')
    info = group.info
    assert info.name_singular == 'test'
    assert info.visibility == GroupInfo.VISIBILITY_SUPERUSERS_ONLY
    assert info.seniority_level == 5
