from wagtail.contrib.modeladmin.options import (
    ModelAdmin, modeladmin_register)
from wagtail.contrib.modeladmin.helpers import PermissionHelper
from .models import GroupInfo


class GroupPermissionHelper(PermissionHelper):

    def user_can_create(self, user):
        """
        Creation is handled automatically, so overriding this to hide the
        create functionality in the UI
        """
        return False


class GroupInfoAdmin(ModelAdmin):
    model = GroupInfo
    menu_icon = 'cog'
    menu_order = 602
    add_to_settings_menu = True
    list_display = (
        'name_singular',
        'get_visibility_display',
        'seniority_level',
    )
    list_filter = (
        'visibility',
        'seniority_level',
    )
    search_fields = (
        'name_singular',
        'permission_summary',
        'role_match_description',
    )

modeladmin_register(GroupInfoAdmin)
