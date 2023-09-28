import pytest
from wagtail.models import Page
from django.conf import settings

from activitystream.serializers import WagtailPageSerializer


from tests.great_international.factories import InternationalArticlePageFactory


@pytest.mark.django_db
def test_wagtail_page_serializer(international_site):
    article = InternationalArticlePageFactory(parent=international_site.root_page)

    serialized_article = WagtailPageSerializer().to_representation(article)
    # serialized_article.object.content is None because the page is not available in the Redis cache.
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
            'seo_title': article.seo_title,
            'search_description': article.search_description,
            'first_published_at': article.first_published_at.isoformat(),
            'last_published_at': article.last_published_at.isoformat(),
            'content_type_id': article.content_type_id,
            'content': None,
        },
    }


@pytest.mark.django_db
def test_error_thrown_for_invalid_page(international_site):
    page = Page.objects.get(id=3)
    invalid_page = page.copy()
    invalid_page.id = None
    invalid_page.title = None
    invalid_page.first_published_at = None

    serialized_article = WagtailPageSerializer().to_representation(invalid_page)

    assert 'Could not parse content for class' in serialized_article['object']['error']
