from django.urls import reverse
from wagtail.admin.menu import MenuItem
from wagtail.core import hooks


@hooks.register('register_admin_menu_item')
def add_moderation_queue_to_menu():
    return MenuItem(
        'Moderation Queue',
        reverse('moderation-queue'),
        classnames='icon icon-folder-inverse',
        order=600,
    )
