from django.utils.decorators import decorator_from_middleware

from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.generics import ListAPIView
from wagtail.core.models import Page

from export_readiness.models import ArticlePage, CountryGuidePage
from activitystream.authentication import ActivityStreamAuthentication, \
    ActivityStreamHawkResponseMiddleware
from activitystream.filters import ArticlePageFilter, PageFilter
from activitystream.serializers import ArticlePageSerializer

MAX_PER_PAGE = 25


class ActivityStreamView(ListAPIView):
    """List-only view set for the activity stream"""

    authentication_classes = (ActivityStreamAuthentication,)
    permission_classes = ()

    @staticmethod
    def _build_after(request, after_ts, after_id):
        return (
            request.build_absolute_uri(
                reverse('activity-stream')
            ) +
            '?after={}_{}'.format(
                str(after_ts.timestamp()),
                str(after_id)
            )
        )

    @decorator_from_middleware(ActivityStreamHawkResponseMiddleware)
    def list(self, request):
        """A single page of activities"""

        # Consider https://stackoverflow.com/questions/18776221/django-querying-multiple-types-of-objects
        # Or chaining multiple queries?

        # Or inheriting from page and then doing a sub-search in serializer to get the actual details?

        filter = PageFilter(
            request.GET,
            queryset=Page.objects.type((ArticlePage, CountryGuidePage))
        )
        articles_qs = filter.qs.specific(). \
            order_by('last_published_at', 'id')[:MAX_PER_PAGE]


        items = {
            '@context': 'https://www.w3.org/ns/activitystreams',
            'type': 'Collection',
            'orderedItems': ArticlePageSerializer(articles_qs, many=True).data
        }

        if not articles_qs:
            next_page = {}
        else:
            last_article = articles_qs[len(articles_qs)-1]
            next_page = {
                'next': self._build_after(
                    request, last_article.last_published_at, last_article.id)
            }

        return Response({
            **items,
            **next_page,
        })
