from rest_framework import serializers

from core import fields


class BasePageSerializer(serializers.Serializer):
    seo_title = serializers.CharField()
    search_description = serializers.CharField()
    meta = fields.MetaDictField()
