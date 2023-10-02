from django.urls import path

import activitystream.views

app_name = 'activitystream'

urlpatterns = [
    path(
        r'cms-content/',
        activitystream.views.CMSContentActivityStreamView.as_view(),
        name='cms-content',
    ),
]
