from wagtail.contrib.modeladmin.options import (
    ModelAdmin, modeladmin_register)
from wagtail.contrib.modeladmin.helpers import PermissionHelper
from .models import GroupInfo


class GroupPermissionHelper(PermissionHelper):
    """
    Creation and deletion is handled automatically, so overriding these
    methods to hide those options in the UI
    """

    def user_can_create(self, user):
        return False

    def user_can_delete_obj(self, user, obj):
        return False


class GroupInfoAdmin(ModelAdmin):
    model = GroupInfo
    menu_icon = 'cog'
    menu_order = 602
    add_to_settings_menu = True
    permission_helper_class = GroupPermissionHelper
    list_display = (
        'group_name',
        'name_singular',
        'visibility',
        'seniority_level',
    )
    ordering = ('group__name',)
    list_filter = (
        'visibility',
        'seniority_level',
    )
    search_fields = (
        'name_singular',
        'permission_summary',
        'role_match_description',
    )
    form_fields_exclude = ('group',)


modeladmin_register(GroupInfoAdmin)
