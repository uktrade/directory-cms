from datetime import datetime
from os import environ

from django.db.models import Q
from django.utils.decorators import decorator_from_middleware


from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.generics import ListAPIView

from export_readiness.models import ArticlePage
from activitystream.authentication import ActivityStreamAuthentication, \
    ActivityStreamHawkResponseMiddleware

MAX_PER_PAGE = 250


class ActivityStreamViewSet(ListAPIView):
    """List-only view set for the activity stream"""

    authentication_classes = (ActivityStreamAuthentication,)
    permission_classes = ()

    @staticmethod
    def _parse_after(request):
        after = request.GET.get('after', '0.000000_0')
        after_ts_str, after_id_str = after.split('_')
        after_ts = datetime.fromtimestamp(float(after_ts_str))
        after_id = int(after_id_str)
        return after_ts, after_id

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

    @staticmethod
    def _build_article_objects(request, articles):
        article_objects = []
        for article in articles:
            article_objects.append({
                'id': (
                    'dit:cms:Article:' + str(article.id) +
                    ':Update'
                ),
                'type': 'Update',
                'published': article.last_published_at.isoformat('T'),
                'object': {
                    'type': ['Document', 'dit:cms:Article'],
                    'id': 'dit:cms:Article:' + str(article.id),
                    'name': article.article_title,
                    'summary': article.article_teaser,
                    'content': article.article_body_text,
                    'url':
                    f'{environ["APP_URL_EXPORT_READINESS"]}/{article.slug}/'
                },
            })
        return article_objects

    @decorator_from_middleware(ActivityStreamHawkResponseMiddleware)
    def list(self, request):
        """A single page of activities"""

        after_ts, after_id = self._parse_after(request)
        article_qs_all = ArticlePage.objects.live().filter(
            Q(last_published_at=after_ts, id__gt=after_id) |
            Q(last_published_at__gt=after_ts)
        ).order_by('last_published_at', 'id')

        article_qs = article_qs_all[:MAX_PER_PAGE]
        articles = list(article_qs)
        article_objects = self._build_article_objects(request, articles)

        items = {
            '@context': 'https://www.w3.org/ns/activitystreams',
            'type': 'Collection',
            'orderedItems': article_objects
        }

        if articles:
            next_article = {
                'next': self._build_after(
                    request, articles[-1].last_published_at, articles[-1].id)
            }
        else:
            next_article = {}

        return Response({
            **items,
            **next_article,
        })
