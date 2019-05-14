import pytest

from groups.wagtail_hooks import GroupInfoAdmin


@pytest.mark.django_db
def test_groupinfomodeladmin_indexview_does_not_error(
    admin_client, admin_user, groups_with_info
):
    modeladmin = GroupInfoAdmin()
    response = admin_client.get(modeladmin.url_helper.index_url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_groupinfomodeladmin_permissionhelper(admin_user, groups_with_info):
    modeladmin = GroupInfoAdmin()
    helper = modeladmin.permission_helper
    assert admin_user.is_superuser is True
    # regardless of the above, creation is not permitted
    assert helper.user_can_create(admin_user) is False
    for group in groups_with_info:
        # neither is deletion
        assert helper.user_can_delete_obj(admin_user, group.info) is False
        # but editing is okay
        assert helper.user_can_edit_obj(admin_user, group.info) is True
