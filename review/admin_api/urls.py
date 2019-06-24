from django.conf.urls import url
from django.views.decorators.csrf import csrf_exempt

from . import views


app_name = 'review_admin_api'
urlpatterns = [
    url(r'^page/(?P<pk>\d+)/shares/$', views.PageShares.as_view(), name='page_shares'),
]
