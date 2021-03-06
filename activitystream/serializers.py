from rest_framework import serializers
from export_readiness.models import (
    ArticlePage,
    MarketingArticlePage,
)


class CountryGuidePageSerializer(serializers.Serializer):

    def to_representation(self, obj):
        return {
            'id': (
                'dit:cms:Article:' + str(obj.id) +
                ':Update'
            ),
            'type': 'Update',
            'published': obj.last_published_at.isoformat('T'),
            'object': {
                'type': 'Article',
                'id': 'dit:cms:Article:' + str(obj.id),
                'name': obj.heading,
                'summary': obj.sub_heading,
                'content': obj.section_one_body,
                'url': obj.get_url(),
                'keywords': " ".join(
                    obj.tags.all().values_list('name', flat=True)
                )
            },
        }


class ArticlePageSerializer(serializers.Serializer):

    def to_representation(self, obj):
        return {
            'id': ('dit:cms:Article:' + str(obj.id) + ':Update'),
            'type': 'Update',
            'published': obj.last_published_at.isoformat('T'),
            'object': {
                'type': 'Article',
                'id': 'dit:cms:Article:' + str(obj.id),
                'name': obj.article_title,
                'summary': obj.article_teaser,
                'content': obj.article_body_text,
                'url': obj.get_url()
            },
        }


class MarketingArticlePageSerializer(ArticlePageSerializer):
    pass


class PageSerializer(serializers.Serializer):

    def to_representation(self, obj):
        if isinstance(obj, ArticlePage):
            return ArticlePageSerializer(obj).data
        elif isinstance(obj, MarketingArticlePage):
            return MarketingArticlePageSerializer(obj).data
        else:  # CountryGuidePage
            return CountryGuidePageSerializer(obj).data
