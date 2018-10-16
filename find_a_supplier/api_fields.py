from wagtail.api import APIField

from core.api_fields import APIQuerysetSerializer
from find_a_supplier import serializers


class APIIndustriesListField(APIField):
    def __init__(self, name, queryset, field_names=None):
        field_names = field_names or [
            'meta',
            'hero_image',
            'hero_text',
            'breadcrumbs_label',
            'summary_image',
            'show_on_industries_showcase_page',
        ]
        # see explanation of the `fields_config` syntax here:
        # https://github.com/wagtail/wagtail/blob/
        # db6d36845f3f2c5d7009a22421c2efab9968aa24/wagtail/api/v2/utils.py#L68
        serializer = APIQuerysetSerializer(
            name,
            fields_config=[(name, False, None) for name in field_names],
            queryset=queryset,
        )
        super().__init__(name=name, serializer=serializer)


class APIArticleSummariesField(APIField):
    def __init__(self, name):
        serializer = serializers.APIArticleSummariesSerializer(name)
        super().__init__(name=name, serializer=serializer)
