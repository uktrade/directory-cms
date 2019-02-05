from directory_constants.constants import cms
from rest_framework import serializers
from wagtail.images.api import fields as wagtail_fields

from core import fields as core_fields
from core.serializers import BasePageSerializer

from .models import (
    InternationalArticlePage, InternationalMarketingPages
)


class PageWithRelatedPagesSerializer(BasePageSerializer):
    related_pages = serializers.SerializerMethodField()

    def get_related_pages(self, obj):
        items = [
            obj.related_page_one,
            obj.related_page_two,
            obj.related_page_three
        ]
        serializer = RelatedArticlePageSerializer(
            [item for item in items if item],
            context=self.context,
            many=True,
        )
        return serializer.data


class RelatedArticlePageSerializer(BasePageSerializer):
    """Separate serializer for related article pages so we don't end up with
    infinite nesting of related pages inside an article page"""

    article_title = serializers.CharField(max_length=255)
    article_teaser = serializers.CharField(max_length=255)
    article_image = wagtail_fields.ImageRenditionField('original')
    article_image_thumbnail = wagtail_fields.ImageRenditionField(
        'fill-640x360|jpegquality-60|format-jpeg', source='article_image')


class ArticlePageSerializer(PageWithRelatedPagesSerializer):
    article_title = serializers.CharField(max_length=255)
    display_title = serializers.CharField(source='article_title')
    article_teaser = serializers.CharField(max_length=255)
    article_image = wagtail_fields.ImageRenditionField('original')
    article_image_thumbnail = wagtail_fields.ImageRenditionField(
        'fill-640x360|jpegquality-60|format-jpeg', source='article_image')
    article_body_text = core_fields.MarkdownToHTMLField()


class InternationalHomePageSerializer(BasePageSerializer):
    news_title = serializers.CharField(max_length=255)
    tariffs_title = serializers.CharField(max_length=255)
    tariffs_description = core_fields.MarkdownToHTMLField()
    tariffs_link = serializers.URLField()
    tariffs_image = wagtail_fields.ImageRenditionField(
        'fill-640x360|jpegquality-60|format-jpeg'
    )

    articles = serializers.SerializerMethodField()

    def get_articles(self, obj):
        queryset = None
        slug = cms.GREAT_INTERNATIONAL_MARKETING_PAGES_SLUG
        if InternationalMarketingPages.objects.filter(slug=slug).exists():
            queryset = InternationalMarketingPages.objects.get(
                slug=slug
            ).get_descendants().type(
                InternationalArticlePage
            ).live().specific()[:3]
        serializer = ArticlePageSerializer(
            queryset,
            many=True,
            allow_null=True,
            context=self.context
        )
        return serializer.data
