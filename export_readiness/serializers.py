from rest_framework import serializers
from wagtail.images.api import fields as wagtail_fields

from core import fields as core_fields
from core.serializers import BasePageSerializer


class ArticlePageSerializer(BasePageSerializer):
    article_title = serializers.CharField(max_length=255)
    article_teaser = serializers.CharField(max_length=255)
    article_image = wagtail_fields.ImageRenditionField('original')
    article_body_text = core_fields.MarkdownToHTMLField()
    related_article_one_url = serializers.CharField(
        max_length=255,
        allow_null=True
    )
    related_article_one_title = serializers.CharField(
        max_length=255,
        allow_null=True
    )
    related_article_one_teaser = serializers.CharField(
        max_length=255,
        allow_null=True
    )
    related_article_two_url = serializers.CharField(
        max_length=255,
        allow_null=True
    )
    related_article_two_title = serializers.CharField(
        max_length=255,
        allow_null=True
    )
    related_article_two_teaser = serializers.CharField(
        max_length=255,
        allow_null=True
    )
    related_article_three_url = serializers.CharField(
        max_length=255,
        allow_null=True
    )
    related_article_three_title = serializers.CharField(
        max_length=255,
        allow_null=True
    )
    related_article_three_teaser = serializers.CharField(
        max_length=255,
        allow_null=True
    )
    tags = core_fields.TagsListField()
