from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView

from . import views

app_name = 'sso'
urlpatterns = [
    url(
        r'^$',
        login_required(views.SSORequestAccessView.as_view()),
        name="request_access",
    ),
    url(
        r'^thanks/$',
        login_required(TemplateView.as_view(
            template_name="sso/request_access_success.html"
        )),
        name="request_access_success",
    ),
]
