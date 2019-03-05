from django.utils.decorators import decorator_from_middleware

from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.generics import ListAPIView

from export_readiness.models import ArticlePage
from activitystream.authentication import ActivityStreamAuthentication, \
    ActivityStreamHawkResponseMiddleware
from activitystream.filters import ArticlePageFilter
from activitystream.serializers import ArticlePageSerializer

MAX_PER_PAGE = 25


class ActivityStreamViewSet(ListAPIView):
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

        article_filter = ArticlePageFilter(
            request.GET,
            queryset=ArticlePage.objects.live()
        )
        articles_qs = article_filter.qs. \
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
