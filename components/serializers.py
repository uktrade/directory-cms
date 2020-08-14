from rest_framework import serializers

from core.serializers import BasePageSerializer
from core import fields as core_fields


class BannerComponentPageSerializer(BasePageSerializer):
    banner_content = core_fields.MarkdownToHTMLField()
    banner_label = serializers.CharField()


class ComponentsAppSerializer(BasePageSerializer):
    pass