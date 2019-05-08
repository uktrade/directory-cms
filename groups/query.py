from django.db import models
from wagtail.users.views.users import change_user_perm


class GroupInfoQuerySet(models.QuerySet):

    def visible_to_anyone(self):
        return self.filter(visibility=self.model.VISIBILITY_UNRESTRICTED)

    def with_groups(self):
        return self.select_related('group')

    @property
    def team_leaders_group(self):
        """Returns a single object"""
        return self.with_groups().get(is_team_leaders_group=True)
