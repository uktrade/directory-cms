from rest_framework import serializers
from wagtail.images.api import fields as wagtail_fields

from conf import settings
from core import fields as core_fields
from core.serializers import BasePageSerializer

from .models import ArticleListingPage, ArticlePage, TopicLandingPage


class GenericBodyOnlyPageSerializer(BasePageSerializer):
    body = core_fields.MarkdownToHTMLField()


class GetFinancePageSerializer(BasePageSerializer):
    breadcrumbs_label = serializers.CharField()
    hero_text = core_fields.MarkdownToHTMLField()
    hero_image = wagtail_fields.ImageRenditionField('original')
    ukef_logo = wagtail_fields.ImageRenditionField('original')
    contact_proposition = core_fields.MarkdownToHTMLField()
    contact_button = serializers.CharField()
    advantages_title = serializers.CharField()
    advantages_one = core_fields.MarkdownToHTMLField()
    advantages_one_icon = wagtail_fields.ImageRenditionField('original')
    advantages_two = core_fields.MarkdownToHTMLField()
    advantages_two_icon = wagtail_fields.ImageRenditionField('original')
    advantages_three = core_fields.MarkdownToHTMLField()
    advantages_three_icon = wagtail_fields.ImageRenditionField('original')
    evidence = core_fields.MarkdownToHTMLField()
    evidence_video = core_fields.VideoField()


class PerformanceDashboardPageSerializer(BasePageSerializer):
    heading = serializers.CharField()
    description = core_fields.MarkdownToHTMLField()
    product_link = serializers.URLField()
    data_title_row_one = serializers.CharField()
    data_number_row_one = serializers.CharField()
    data_period_row_one = serializers.CharField()
    data_description_row_one = core_fields.MarkdownToHTMLField()
    data_title_row_two = serializers.CharField()
    data_number_row_two = serializers.CharField()
    data_period_row_two = serializers.CharField()
    data_description_row_two = core_fields.MarkdownToHTMLField()
    data_title_row_three = serializers.CharField()
    data_number_row_three = serializers.CharField()
    data_period_row_three = serializers.CharField()
    data_description_row_three = core_fields.MarkdownToHTMLField()
    data_title_row_four = serializers.CharField()
    data_number_row_four = serializers.CharField()
    data_period_row_four = serializers.CharField()
    data_description_row_four = core_fields.MarkdownToHTMLField()
    guidance_notes = core_fields.MarkdownToHTMLField()
    landing_dashboard = serializers.BooleanField()


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
    articles_count = serializers.IntegerField()


class TagSerializer(serializers.Serializer):
    """This is not a Page model."""
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


class CampaignPageSerializer(BasePageSerializer):
    campaign_heading = serializers.CharField(max_length=255)

    section_one_heading = serializers.CharField(max_length=255)
    campaign_hero_image = wagtail_fields.ImageRenditionField('original')

    section_one_intro = core_fields.MarkdownToHTMLField(allow_null=True)

    section_one_image = wagtail_fields.ImageRenditionField('fill-600x800')

    selling_point_one_icon = wagtail_fields.ImageRenditionField('original')
    selling_point_one_heading = serializers.CharField(max_length=255)
    selling_point_one_content = core_fields.MarkdownToHTMLField(
        allow_null=True)

    selling_point_two_icon = wagtail_fields.ImageRenditionField('original')
    selling_point_two_heading = serializers.CharField(max_length=255)
    selling_point_two_content = core_fields.MarkdownToHTMLField(
        allow_null=True)

    selling_point_three_icon = wagtail_fields.ImageRenditionField('original')
    selling_point_three_heading = serializers.CharField(max_length=255)
    selling_point_three_content = core_fields.MarkdownToHTMLField(
        allow_null=True)

    section_one_contact_button_url = serializers.CharField(max_length=255)
    section_one_contact_button_text = serializers.CharField(max_length=255)

    section_two_heading = serializers.CharField(max_length=255)
    section_two_intro = core_fields.MarkdownToHTMLField(allow_null=True)

    section_two_image = wagtail_fields.ImageRenditionField('fill-640x360')

    section_two_contact_button_url = serializers.CharField(max_length=255)
    section_two_contact_button_text = serializers.CharField(max_length=255)

    related_content_heading = serializers.CharField(max_length=255)
    related_content_intro = core_fields.MarkdownToHTMLField(allow_null=True)

    related_page_one_url = serializers.CharField(max_length=255)
    related_page_one_heading = serializers.CharField(max_length=255)
    related_page_one_description = serializers.CharField(max_length=255)
    related_page_one_image = wagtail_fields.ImageRenditionField('fill-640x360')

    related_page_two_url = serializers.CharField(max_length=255)
    related_page_two_heading = serializers.CharField(max_length=255)
    related_page_two_description = serializers.CharField(max_length=255)
    related_page_two_image = wagtail_fields.ImageRenditionField('fill-640x360')

    related_page_three_url = serializers.CharField(max_length=255)
    related_page_three_heading = serializers.CharField(max_length=255)
    related_page_three_description = serializers.CharField(max_length=255)
    related_page_three_image = wagtail_fields.ImageRenditionField(
        'fill-640x360')

    cta_box_message = serializers.CharField(max_length=255)
    cta_box_button_url = serializers.CharField(max_length=255)
    cta_box_button_text = serializers.CharField(max_length=255)
