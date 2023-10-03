from rest_framework import serializers
from core.cache import PageCache
from django.conf import settings


class WagtailPageSerializer(serializers.Serializer):
    def get_cms_content_for_obj(self, obj):
        try:
            result = dict(
                id='dit:cmsContent:international:' + str(obj.id),
                type='dit:cmsContent',
                title=obj.title,
                url=settings.APP_URL_GREAT_INTERNATIONAL+'content'+obj.url,
                seo_title=obj.seo_title,
                search_description=obj.search_description,
                first_published_at=obj.first_published_at.isoformat(),
                last_published_at=obj.last_published_at.isoformat(),
                content_type_id=obj.content_type_id,
                content=f"{PageCache.get(obj.id, lang='en-gb')}",
            )
        except Exception as e:
            result = {"error": f"Could not parse content for class {obj.specific_class}. Error: {e}"}

        return result

    def to_representation(self, obj):
        return {
            'id': ('dit:cmsContent:international:' + str(obj.id) + ':Update'),
            'type': 'Update',
            'published': obj.last_published_at.isoformat(),
            'object': self.get_cms_content_for_obj(obj),
        }
