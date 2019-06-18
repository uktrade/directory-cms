from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^moderation/lock/$', views.ModerationLock.as_view(), name='lock'),
    url(r'^moderation/respond/$', views.ModerationRespond.as_view(), name='respond'),
]
