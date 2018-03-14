from wagtail.api import APIField

from core import serializers


class APIHyperlinkField(APIField):
    def __init__(self, name):
        serializer = serializers.URLHyperlinkField(
            draft_url_attribute='draft_url',
            published_url_attribute='published_url',
        )
        super().__init__(name=name, serializer=serializer)
