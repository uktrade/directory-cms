from django.urls import re_path

from wagtail.users.views import users as original_users_views

from . import views

app_name = 'great_users'
urlpatterns = [
    re_path(r'^$', original_users_views.Index, name='index'),
    re_path(r'^add/$', views.CreateUserView.as_view(), name='add'),
    re_path(r'^(?P<pk>\d+)/$', views.EditUserView.as_view(), name='edit'),
    re_path(r'^([^\/]+)/delete/$', original_users_views.Delete, name='delete'),
]
