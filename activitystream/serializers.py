from rest_framework import serializers
from export_readiness.models import ArticlePage


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
                'url': obj.get_url()
            },
        }


class ArticlePageSerializer(serializers.Serializer):

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
                'name': obj.article_title,
                'summary': obj.article_teaser,
                'content': obj.article_body_text,
                'url': obj.get_url()
            },
        }


class PageSerializer(serializers.Serializer):

    def to_representation(self, obj):
        if isinstance(obj, ArticlePage):
            return ArticlePageSerializer(obj).data
        else:  # CountryGuidePage
            return CountryGuidePageSerializer(obj).data
