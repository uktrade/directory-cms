from django.apps import AppConfig
from django.db.models.signals import post_save


class GroupsConfig(AppConfig):
    name = 'groups'

    def ready(self):
        from groups import signal_handlers
        post_save.connect(
            sender='auth.Group',
            receiver=signal_handlers.create_groupinfo_for_new_group,
        )
