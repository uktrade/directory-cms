from rest_framework import serializers
from wagtail.images.api import fields as wagtail_fields

from core.blocks_serializers import StreamChildBaseSerializer
from core import fields as core_fields


class CampaignBlockStreamChildSerializer(StreamChildBaseSerializer):
    heading = serializers.CharField()
    subheading = serializers.CharField()
    related_link_text = serializers.CharField()
    related_link_url = serializers.CharField()
    image = wagtail_fields.ImageRenditionField('original')
    video = core_fields.VideoField()
    video_transcript = serializers.CharField()
