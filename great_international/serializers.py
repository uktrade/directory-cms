from rest_framework import serializers
from wagtail.images.api import fields as wagtail_fields

from core import fields as core_fields
from core.serializers import BasePageSerializer

from .models import (InternationalArticlePage, InternationalArticleListingPage,
                     InternationalLocalisedFolderPage,
                     InternationalCampaignPage)


class RelatedArticlePageSerializer(BasePageSerializer):
    title = serializers.CharField(max_length=255, source='article_title')
    teaser = serializers.CharField(max_length=255, source='article_teaser')
    thumbnail = wagtail_fields.ImageRenditionField(
        'fill-640x360|jpegquality-60|format-jpeg', source='article_image')


class RelatedCampaignPageSerializer(BasePageSerializer):
    title = serializers.CharField(
        max_length=255, source='campaign_heading')
    teaser = serializers.CharField(
        max_length=255, source='campaign_teaser')
    thumbnail = wagtail_fields.ImageRenditionField(
        'fill-640x360|jpegquality-60|format-jpeg',
        source='campaign_hero_image')


MODEL_TO_SERIALIZER_MAPPING = {
    InternationalArticlePage: RelatedArticlePageSerializer,
    InternationalCampaignPage: RelatedCampaignPageSerializer,
}


class PageWithRelatedPagesSerializer(BasePageSerializer):
    related_pages = serializers.SerializerMethodField()

    def get_related_pages(self, obj):
        serialized = []
        items = [
            obj.related_page_one,
            obj.related_page_two,
            obj.related_page_three
        ]
        for related_page in items:
            if not related_page:
                continue
            # currently only used for articles and campaigns
            serializer_class = MODEL_TO_SERIALIZER_MAPPING[
                related_page.specific.__class__]
            serializer = serializer_class(related_page.specific)
            serialized.append(serializer.data)

        return serialized


class InternationalArticlePageSerializer(PageWithRelatedPagesSerializer):
    article_title = serializers.CharField(max_length=255)
    display_title = serializers.CharField(source='article_title')
    article_teaser = serializers.CharField(max_length=255)
    article_image = wagtail_fields.ImageRenditionField('original')
    article_image_thumbnail = wagtail_fields.ImageRenditionField(
        'fill-640x360|jpegquality-60|format-jpeg', source='article_image')
    article_body_text = core_fields.MarkdownToHTMLField()


class InternationalHomePageSerializer(PageWithRelatedPagesSerializer):
    news_title = serializers.CharField(max_length=255)
    tariffs_title = serializers.CharField(max_length=255)
    tariffs_description = core_fields.MarkdownToHTMLField()
    tariffs_link = serializers.URLField()
    tariffs_image = wagtail_fields.ImageRenditionField(
        'fill-640x360|jpegquality-60|format-jpeg'
    )


class InternationalCampaignPageSerializer(PageWithRelatedPagesSerializer):
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

    cta_box_message = serializers.CharField(max_length=255)
    cta_box_button_url = serializers.CharField(max_length=255)
    cta_box_button_text = serializers.CharField(max_length=255)


class InternationalArticleListingPageSerializer(BasePageSerializer):
    landing_page_title = serializers.CharField(max_length=255)
    display_title = serializers.CharField(source='landing_page_title')
    hero_image = wagtail_fields.ImageRenditionField('original')
    hero_image_thumbnail = wagtail_fields.ImageRenditionField(
        'fill-640x360|jpegquality-60|format-jpeg', source='hero_image')

    articles_count = serializers.IntegerField()
    list_teaser = core_fields.MarkdownToHTMLField(allow_null=True)
    hero_teaser = serializers.CharField(allow_null=True)
    child_pages = serializers.SerializerMethodField()
    localised_child_pages = serializers.SerializerMethodField()

    def get_localised_child_pages(self, obj):
        data = []
        region = self.context['request'].GET.get('region')
        if region:
            slug = f'{obj.slug}-{region}'
            folder = InternationalLocalisedFolderPage.objects.filter(slug=slug)
            if folder.exists():
                articles_queryset = folder[0].get_descendants().type(
                    InternationalArticlePage
                ).live().specific()
                articles = InternationalArticlePageSerializer(
                    articles_queryset,
                    many=True,
                    allow_null=True,
                    context=self.context
                )
                campaigns_queryset = folder[0].get_descendants().type(
                    InternationalCampaignPage
                ).live().specific()

                campaings = RelatedCampaignPageSerializer(
                    campaigns_queryset,
                    many=True,
                    allow_null=True,
                    context=self.context
                )
                data = articles.data + campaings.data
        return data

    def get_child_pages(self, obj):
        articles_queryset = obj.get_descendants().type(
            InternationalArticlePage
        ).live().specific()
        articles = InternationalArticlePageSerializer(
            articles_queryset,
            many=True,
            allow_null=True,
            context=self.context
        )
        campaings_queryset = obj.get_descendants().type(
            InternationalCampaignPage
        ).live().specific()
        campaings = RelatedCampaignPageSerializer(
            campaings_queryset,
            many=True,
            allow_null=True,
            context=self.context
        )
        return articles.data + campaings.data


class InternationalTopicLandingPageSerializer(BasePageSerializer):
    landing_page_title = serializers.CharField(max_length=255)
    display_title = serializers.CharField(source='landing_page_title')
    hero_teaser = serializers.CharField(max_length=255)
    hero_image = wagtail_fields.ImageRenditionField('original')

    hero_image_thumbnail = wagtail_fields.ImageRenditionField(
        'fill-640x360|jpegquality-60|format-jpeg', source='hero_image')

    child_pages = serializers.SerializerMethodField()

    def get_child_pages(self, obj):
        articles_listing_queryset = obj.get_descendants().type(
            InternationalArticleListingPage
        ).live().specific()
        articles_list_serializer = InternationalArticleListingPageSerializer(
            articles_listing_queryset,
            many=True,
            allow_null=True,
            context=self.context
        )
        campaigns_queryset = obj.get_descendants().type(
            InternationalCampaignPage
        ).live().specific()
        campaigns_serializer = RelatedCampaignPageSerializer(
            campaigns_queryset,
            many=True,
            allow_null=True,
            context=self.context
        )
        return articles_list_serializer.data + campaigns_serializer.data
