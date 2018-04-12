from wagtail.api import APIField
from wagtail.wagtailimages.api.fields import ImageRenditionField

from core import serializers


class APIRichTextField(APIField):
    def __init__(self, name):
        serializer = serializers.APIRichTextSerializer()
        super().__init__(name=name, serializer=serializer)


class APIImageField(APIField):
    def __init__(self, name):
        serializer = ImageRenditionField('original')
        super().__init__(name=name, serializer=serializer)


class APIMetaField(APIField):
    def __init__(self, name):
        serializer = serializers.APIMetaSerializer(name)
        super().__init__(name=name, serializer=serializer)


class APIBreadcrumbsField(APIField):
    def __init__(self, name, app_label):
        serializer = serializers.APIBreadcrumsSerializer(
            app_label
        )
        super().__init__(name=name, serializer=serializer)


class APIVideoField(APIField):
    def __init__(self, name):
        serializer = serializers.APIVideoSerializer()
        super().__init__(name=name, serializer=serializer)
