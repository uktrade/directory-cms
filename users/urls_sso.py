from django.contrib.auth.decorators import login_required
from django.urls import re_path
from django.views.generic import TemplateView

from . import views

app_name = 'great_sso'
urlpatterns = [
    re_path(
        r'^$',
        login_required(views.SSORequestAccessView.as_view()),
        name="request_access",
    ),
    re_path(
        r'^thanks/$',
        login_required(TemplateView.as_view(template_name="sso/request_access_success.html")),
        name="request_access_success",
    ),
]
