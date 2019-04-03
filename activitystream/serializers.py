from rest_framework import serializers


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