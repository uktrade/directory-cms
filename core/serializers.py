from rest_framework import serializers

from core import fields


class BasePageSerializer(serializers.Serializer):
    seo_title = serializers.CharField()
    search_description = serializers.CharField()
    meta = fields.MetaDictField()
    full_url = serializers.CharField(max_length=255)
    full_path = serializers.CharField(max_length=255)
    last_published_at = serializers.DateTimeField()
    title = serializers.CharField()
