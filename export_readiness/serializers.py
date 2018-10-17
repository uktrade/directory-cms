from rest_framework import serializers
from wagtail.images.api import fields as wagtail_fields

from core import fields as core_fields
from core.serializers import BasePageSerializer

from .models import ArticleListingPage, ArticlePage


class NestedArticlePageSerializer(serializers.Serializer):
    article_title = serializers.CharField(max_length=255)
    article_teaser = serializers.CharField(max_length=255)
    last_published_at = serializers.DateTimeField()
    full_url = serializers.CharField(max_length=255)
    full_path = serializers.CharField(max_length=255)


class HomePageSerializer(BasePageSerializer):
    news_title = serializers.CharField(
        max_length=255,
        allow_null=True,
    )
    news_description = core_fields.MarkdownToHTMLField()
    articles = serializers.SerializerMethodField()
    guidance = serializers.SerializerMethodField()

    @staticmethod
    def _get_articles_in_a_listing_page_by_slug(listing_slug):
        queryset = None
        if ArticleListingPage.objects.filter(slug=listing_slug).exists():
            queryset = ArticleListingPage.objects.get(
                slug=listing_slug
            ).get_descendants().type(
                ArticlePage
            ).live().specific()
        serializer = NestedArticlePageSerializer(
            queryset,
            many=True,
            allow_null=True
        )
        return serializer.data

    def get_articles(self, obj):
        return self._get_articles_in_a_listing_page_by_slug(
            listing_slug='news'
        )

    def get_guidance(self, obj):
        return self._get_articles_in_a_listing_page_by_slug(
            listing_slug='guidance'
        )


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
