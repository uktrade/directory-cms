from rest_framework.generics import ListAPIView

from activitystream.authentication import (
    ActivityStreamAuthentication,
    ActivityStreamHawkResponseMiddleware,
)
from django.utils.decorators import decorator_from_middleware
from wagtail.models import Page
import django_filters.rest_framework
from activitystream.serializers import WagtailPageSerializer
from activitystream.pagination import ActivityStreamCMSContentPagination
from activitystream.filters import ActivityStreamCMSContentFilter


class ActivityStreamBaseView(ListAPIView):
    authentication_classes = (ActivityStreamAuthentication,)
    permission_classes = ()
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]

    @decorator_from_middleware(ActivityStreamHawkResponseMiddleware)
    def list(self, request, *args, **kwargs):
        """A single page of activities to be consumed by activity stream."""
        return super().list(request, *args, **kwargs)


class CMSContentActivityStreamView(ActivityStreamBaseView):
    queryset = Page.objects.all().filter(live=True)
    serializer_class = WagtailPageSerializer
    pagination_class = ActivityStreamCMSContentPagination
    filterset_class = ActivityStreamCMSContentFilter

    def get_queryset(self):
        return self.queryset.order_by('id')
