from django.db import models
from wagtail.users.views.users import change_user_perm


class GroupInfoQuerySet(models.QuerySet):

    def visibile_to_anyone(self):
        return self.filter(visibility=self.model.VISIBILITY_UNRESTRICTED)

    def visibile_to_managers(self):
        return self.filter(visibility__in=(
            self.model.VISIBILITY_UNRESTRICTED,
            self.model.VISIBILITY_MANAGERS_ONLY,
        ))

    def visible_to_user(self, user):
        if user.is_superuser:
            return self.all()
        if user.has_perm(change_user_perm):
            return self.visibile_to_managers()
        return self.visibile_to_anyone()

    @property
    def team_leaders_group(self):
        """Returns a single object"""
        return self.get(is_team_leaders_group=True)
