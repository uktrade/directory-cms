from django.conf.urls import url

from wagtail.users.views import users as original_users_views

from . import views

app_name = 'wagtailusers_users'
urlpatterns = [
    url(r'^$', original_users_views.index, name='index'),
    url(r'^add/$', views.create, name='add'),
    url(r'^([^\/]+)/$', views.edit, name='edit'),
    url(r'^([^\/]+)/delete/$', original_users_views.delete, name='delete'),
]
