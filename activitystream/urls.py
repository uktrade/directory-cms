from django.urls import path

# from great_components.decorators import skip_ga360

import activitystream.views

app_name = 'activitystream'

urlpatterns = [
    path(
        r'cms-content/',
        activitystream.views.CMSContentActivityStreamView.as_view(),
        name='cms-content',
    ),
]
