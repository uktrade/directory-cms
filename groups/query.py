from django.db import models


class GroupInfoQuerySet(models.QuerySet):

    def visibility(self, visibility):
        return self.filter(visibility=visibility)

    def visibile_to_anyone(self):
        return self.visibility(self.model.VISIBILITY_UNRESTRICTED)

    def visibile_to_managers(self):
        return self.visibility(self.model.VISIBILITY_MANAGERS_ONLY)

    def visible_to_superusers(self):
        return self.visibility(self.model.VISIBILITY_SUPERUSERS_ONLY)

    def team_leaders_group(self):
        """Returns a single object"""
        return self.get(is_team_leaders_group=True)
