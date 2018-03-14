from wagtail.api import APIField

from core import serializers


class APIHyperlinkField(APIField):
    def __init__(self, name):
        serializer = serializers.URLHyperlinkSerializer(
            draft_url_attribute='draft_url',
            published_url_attribute='published_url',
        )
        super().__init__(name=name, serializer=serializer)


class APIRichTextField(APIField):
    def __init__(self, name):
        serializer = serializers.APIRichTextSerializer()
        super().__init__(name=name, serializer=serializer)
