from django.apps import AppConfig
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save


class UsersConfig(AppConfig):
    name = 'users'

    def ready(self):
        from wagtail.core import hooks
        from wagtail.admin.wagtail_hooks import register_account_change_email
        from users import signals

        # HACK: Unregister "change email" account menu item hook
        hooks.search_for_hooks()
        registered_hooks = hooks._hooks.get('register_account_menu_item')
        if registered_hooks:
            registered_hooks.remove((register_account_change_email, 0))
            hooks._hooks['register_account_menu_item'] = registered_hooks

        post_save.connect(
            receiver=signals.set_status_for_new_users,
            sender=get_user_model()
        )
