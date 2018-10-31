from rest_framework import serializers
from wagtail.images.api import fields as wagtail_fields

from conf import settings
from core import fields as core_fields
from core.serializers import BasePageSerializer

from .models import ArticleListingPage, ArticlePage, TopicLandingPage


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


class ArticleListingPageSerializer(BasePageSerializer):
    landing_page_title = serializers.CharField(max_length=255)
    hero_image = wagtail_fields.ImageRenditionField('original')
    articles_count = serializers.IntegerField()
    list_teaser = core_fields.MarkdownToHTMLField(allow_null=True)
    hero_teaser = serializers.CharField(allow_null=True)
    articles = serializers.SerializerMethodField()

    def get_articles(self, obj):
        queryset = obj.get_descendants().type(
            ArticlePage
        ).live().specific()
        serializer = ArticlePageSerializer(
            queryset,
            many=True,
            allow_null=True,
            context=self.context
        )
        return serializer.data


class HomePageSerializer(BasePageSerializer):
    news_title = serializers.CharField(
        max_length=255,
        allow_null=True,
    )
    news_description = core_fields.MarkdownToHTMLField()
    articles = serializers.SerializerMethodField()
    guidance = serializers.SerializerMethodField()

    def get_articles(self, obj):
        queryset = None
        slug = settings.EU_EXIT_NEWS_LISTING_PAGE_SLUG
        if ArticleListingPage.objects.filter(slug=slug).exists():
            queryset = ArticleListingPage.objects.get(
                slug=slug
            ).get_descendants().type(
                ArticlePage
            ).live().specific()
        serializer = ArticlePageSerializer(
            queryset,
            many=True,
            allow_null=True,
            context=self.context
        )
        return serializer.data

    def get_guidance(self, obj):
        queryset = None
        if TopicLandingPage.objects.filter(slug='guidance').exists():
            queryset = TopicLandingPage.objects.get(
                slug='guidance'
            ).get_descendants().type(
                ArticleListingPage
            ).live().specific()
        serializer = ArticleListingPageSerializer(
            queryset,
            many=True,
            allow_null=True,
            context=self.context
        )
        return serializer.data


class TopicLandingPageSerializer(BasePageSerializer):
    landing_page_title = serializers.CharField(max_length=255)
    hero_teaser = serializers.CharField(max_length=255)
    hero_image = wagtail_fields.ImageRenditionField('original')
    article_listing = serializers.SerializerMethodField()

    def get_article_listing(self, obj):
        queryset = obj.get_descendants().type(
            ArticleListingPage
        ).live().specific()
        serializer = ArticleListingPageSerializer(
            queryset,
            many=True,
            allow_null=True,
            context=self.context
        )
        return serializer.data


class InternationalLandingPageSerializer(BasePageSerializer):
    pass


class TagSerializer(serializers.Serializer):
    name = serializers.CharField()
    slug = serializers.CharField()
    articles = serializers.SerializerMethodField()

    def get_articles(self, object):
        serializer = ArticlePageSerializer(
            object.articlepage_set.filter(live=True),
            many=True,
            context=self.context
        )
        return serializer.data
