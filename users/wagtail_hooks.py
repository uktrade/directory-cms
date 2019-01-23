from django.conf.urls import url, include
from wagtail.core import hooks

from . import urls as users_urls


@hooks.register('register_admin_urls', order=-1)  # This will run before every hook in the wagtail core
def register_admin_urls():
    return [
        url(r'^users/', include(users_urls, namespace='wagtailusers_users')),
    ]
