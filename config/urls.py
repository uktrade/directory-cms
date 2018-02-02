from django.conf.urls import url

import healthcheck.views
import core.views


urlpatterns = [
    url(
        r'^$',
        core.views.HelloWorldView.as_view(),
        name='hello-world'
    ),
    url(
        r'^healthcheck/database/$',
        healthcheck.views.DatabaseAPIView.as_view(),
        name='health-check-database'
    ),
    url(
        r'^healthcheck/ping/$',
        healthcheck.views.PingAPIView.as_view(),
        name='health-check-ping'
    ),
]
