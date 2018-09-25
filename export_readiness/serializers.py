from rest_framework import fields

from core.serializers import APIChildrenSerializer


class APIRelatedArticlePageSerializer(fields.DictField):

    def to_representation(self, value):
        import ipdb; ipdb.set_trace()
        return {
            'title': value.article_title,
            'teaser': value.article_teaser,
            'updated': value.last_published_at,
            'url': value.url
        }


class APIChildrenTopicLandingPageListSerializer(APIChildrenSerializer):
    sorting_key = 'last_published_at'

    @staticmethod
    def get_model():
        from .models import ArticleListingPage
        return ArticleListingPage


class APIChildrenArticleListingPageListSerializer(APIChildrenSerializer):
    sorting_key = 'last_published_at'

    @staticmethod
    def get_model():
        from .models import ArticlePage
        return ArticlePage
