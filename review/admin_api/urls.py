from django.conf.urls import url
from django.views.decorators.csrf import csrf_exempt

from . import views


urlpatterns = [
    url(r'^page/(?P<pk>\d+)/shares/$', views.PageShares.as_view(), name='page_shares'),
    url(r'^page/(?P<pk>\d+)/share/$', views.SharePage.as_view(), name='share_page'),
    url(r'^page/(?P<page_pk>\d+)/share/(?P<pk>\d+)/$', views.RevokeShare.as_view(), name='revoke_share'),
]
