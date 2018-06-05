from wagtail.api import APIField

from core.serializers import APIQuerysetSerializer


class APISectorPageListField(APIField):
    def __init__(self, name, queryset, field_names=None):
        field_names = field_names or [
            'meta',
            'featured',
            'description',
            'heading',
            'hero_image',
            'pullout',
            'subsections',
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


class APISetupGuidePageListField(APIField):
    def __init__(self, name, queryset, field_names=None):
        field_names = field_names or [
            'meta',
            'description',
            'heading',
            'sub_heading',
            'sections',
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
