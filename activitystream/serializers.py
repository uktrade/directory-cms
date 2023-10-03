from rest_framework import serializers
from core.cache import PageCache
from django.conf import settings


class WagtailPageSerializer(serializers.Serializer):
    prefix = 'dit:cmsContent'
    subtype = 'international'
    operation = 'Update'

    def get_cms_content_for_obj(self, obj):
        try:
            result = dict(
                id=f'{self.prefix}:{self.subtype}:{obj.id}',
                type=self.prefix,
                title=obj.title,
                url=settings.APP_URL_GREAT_INTERNATIONAL+'content'+obj.url,
                seoTitle=obj.seo_title,
                searchDescription=obj.search_description,
                firstPublishedAt=obj.first_published_at.isoformat(),
                lastPublishedAt=obj.last_published_at.isoformat(),
                contentTypeId=obj.content_type_id,
                content=f"{PageCache.get(obj.id, lang='en-gb')}",
            )
        except Exception as e:
            result = {"error": f"Could not parse content for class {obj.specific_class}. Error: {e}"}

        return result

    def to_representation(self, obj):
        return {
            'id': f'{self.prefix}:{self.subtype}:{obj.id}:{self.operation}',
            'type': self.operation,
            'published': obj.last_published_at.isoformat(),
            'object': self.get_cms_content_for_obj(obj),
        }
