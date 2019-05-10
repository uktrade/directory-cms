from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView

from wagtail.users.views import users as original_users_views

from . import views

app_name = 'wagtailusers_users'
urlpatterns = [
    url(r'^$', original_users_views.index, name='index'),
    url(r'^add/$', views.CreateUserView.as_view(), name='add'),
    url(
        r'^request-access/$',
        login_required(views.SSORequestAccessView.as_view()),
        name="sso_request_access",
    ),
    url(
        r'^request-access/thanks/$',
        login_required(TemplateView.as_view(
            template_name="sso/request_access_success.html"
        )),
        name="sso_request_access_success",
    ),
    url(r'^(?P<pk>\d+)/$', views.EditUserView.as_view(), name='edit'),
    url(r'^([^\/]+)/delete/$', original_users_views.delete, name='delete'),
]
