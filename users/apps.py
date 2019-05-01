from django.apps import AppConfig


class UsersConfig(AppConfig):
    name = 'users'

    def ready(self):
        # HACK: Unregister "change email" account menu item hook
        from wagtail.core import hooks
        from wagtail.admin.wagtail_hooks import register_account_change_email
        hooks.search_for_hooks()
        registered_hooks = hooks._hooks.get('register_account_menu_item')
        if registered_hooks:
            registered_hooks.remove((register_account_change_email, 0))
            hooks._hooks['register_account_menu_item'] = registered_hooks
