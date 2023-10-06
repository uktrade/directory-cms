import pytest
from wagtail.models import Page
from django.conf import settings

from activitystream.serializers import WagtailPageSerializer


from tests.great_international.factories import InternationalArticlePageFactory


@pytest.mark.django_db
def test_wagtail_page_serializer(international_site):
    article = InternationalArticlePageFactory(parent=international_site.root_page)

    serialized_article = WagtailPageSerializer().to_representation(article)
    # serialized_article.object.content is "None" because the page is not available in the Redis cache.
    # Serializing of actual article content / caching is covered by other unit tests.
    assert serialized_article == {
        'id': ('dit:cmsContent:international:' + str(article.id) + ':Update'),
        'type': 'Update',
        'published': article.last_published_at.isoformat(),
        'object': {
            'id': 'dit:cmsContent:international:' + str(article.id),
            'type': 'dit:cmsContent',
            'title': article.title,
            'url': settings.APP_URL_GREAT_INTERNATIONAL+'content'+article.url,
            'seoTitle': article.seo_title,
            'searchDescription': article.search_description,
            'firstPublishedAt': article.first_published_at.isoformat(),
            'lastPublishedAt': article.last_published_at.isoformat(),
            'contentTypeId': article.content_type_id,
            'content': "None",
        },
    }
