from rest_framework import serializers
from core.cache import PageCache


def get_cms_content_for_obj(obj):
    result = {}
    try:
        result = dict(
            url=obj.url_path,
            seo_title=obj.seo_title,
            search_description=obj.search_description,
            content=PageCache.get(obj.id, lang='en-gb'),
            first_published_at=obj.first_published_at.isoformat(),
            last_published_at=obj.last_published_at.isoformat(),
            content_type_id=obj.content_type_id,
        )
    except Exception as e:
        result = {f"Could not parse content for class {obj.specific_class}. Error: {e}"}

    return result


class WagtailPageSerializer(serializers.Serializer):
    def to_representation(self, obj):
        return {
            'id': ('dit:cmsContent:international:' + str(obj.id) + ':Update'),
            'type': 'Update',
            'published': obj.last_published_at.isoformat(),
            'object': {
                'type': 'dit:cmsContent',
                'id': 'dit:cmsContent:international:' + str(obj.id),
                'name': obj.title,
                'url': obj.url_path,
                'content': get_cms_content_for_obj(obj),
            },
        }
