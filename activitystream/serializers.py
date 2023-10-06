from rest_framework import serializers
from core.cache import PageCache
from django.conf import settings


class WagtailPageSerializer(serializers.Serializer):
    prefix = 'dit:cmsContent'
    subtype = 'international'
    operation = 'Update'

    def to_representation(self, obj):
        return {
            'id': f'{self.prefix}:{self.subtype}:{obj.id}:{self.operation}',
            'type': self.operation,
            'published': obj.last_published_at.isoformat(),
            'object': {
                'id': f'{self.prefix}:{self.subtype}:{obj.id}',
                'type': self.prefix,
                'title': obj.title,
                'seoTitle': obj.seo_title,
                'url': f"{settings.APP_URL_GREAT_INTERNATIONAL}content{obj.url}",
                'searchDescription': obj.search_description,
                'firstPublishedAt': obj.first_published_at.isoformat(),
                'lastPublishedAt': obj.last_published_at.isoformat(),
                'contentTypeId': obj.content_type_id,
                'content': f"{PageCache.get(obj.id, lang='en-gb')}",
            },
        }