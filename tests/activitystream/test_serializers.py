import pytest

from activitystream.serializers import WagtailPageSerializer


from tests.great_international.factories import InternationalArticlePageFactory


@pytest.mark.django_db
def test_wagtail_page_serializer():
    article = InternationalArticlePageFactory()

    serialized_article = WagtailPageSerializer().to_representation(article)

    # serialized_article.object.content.content is None because the page is not available in the Redis cache.
    # Serializing of actual article content / caching is covered by other unit tests.
    assert serialized_article == {
        'id': ('dit:cmsContent:international:' + str(article.id) + ':Update'),
        'type': 'Update',
        'published': article.last_published_at.isoformat(),
        'object': {
            'type': 'dit:cmsContent',
            'id': 'dit:cmsContent:international:' + str(article.id),
            'name': article.title,
            'url': article.url_path,
            'content': {
                'url': article.url_path,
                'seo_title': article.seo_title,
                'search_description': article.search_description,
                'content': None,
                'first_published_at': article.first_published_at.isoformat(),
                'last_published_at': article.last_published_at.isoformat(),
                'content_type_id': article.content_type_id,
            },
        },
    }
