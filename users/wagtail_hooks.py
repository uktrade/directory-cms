from django.conf.urls import include
from django.urls import re_path
from wagtail import hooks

from . import urls as users_urls


@hooks.register('register_admin_urls', order=-1)
# This will run before every hook in the wagtail core
def register_admin_urls():
    return [re_path(r'^dit_users/', include(users_urls, namespace='great_users'))]
