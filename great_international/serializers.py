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


class InternationalSectorPageSerializer(PageWithRelatedPagesSerializer):
    heading = serializers.CharField(max_length=255)
    sub_heading = serializers.CharField(max_length=255)
    hero_image = wagtail_fields.ImageRenditionField('original')
    heading_teaser = serializers.CharField()

    section_one_body = core_fields.MarkdownToHTMLField()
    section_one_image = wagtail_fields.ImageRenditionField('fill-640x360')
    section_one_image_caption = serializers.CharField(max_length=255)
    section_one_image_caption_company = serializers.CharField(max_length=255)

    statistic_1_number = serializers.CharField(max_length=255)
    statistic_1_heading = serializers.CharField(max_length=255)
    statistic_1_smallprint = serializers.CharField(max_length=255)

    statistic_2_number = serializers.CharField(max_length=255)
    statistic_2_heading = serializers.CharField(max_length=255)
    statistic_2_smallprint = serializers.CharField(max_length=255)

    statistic_3_number = serializers.CharField(max_length=255)
    statistic_3_heading = serializers.CharField(max_length=255)
    statistic_3_smallprint = serializers.CharField(max_length=255)

    statistic_4_number = serializers.CharField(max_length=255)
    statistic_4_heading = serializers.CharField(max_length=255)
    statistic_4_smallprint = serializers.CharField(max_length=255)

    statistic_5_number = serializers.CharField(max_length=255)
    statistic_5_heading = serializers.CharField(max_length=255)
    statistic_5_smallprint = serializers.CharField(max_length=255)

    statistic_6_number = serializers.CharField(max_length=255)
    statistic_6_heading = serializers.CharField(max_length=255)
    statistic_6_smallprint = serializers.CharField(max_length=255)

    section_two_heading = serializers.CharField(max_length=255)
    section_two_teaser = serializers.CharField()
    section_two_subsection_one_icon = wagtail_fields.ImageRenditionField(
        'original')
    section_two_subsection_one_heading = serializers.CharField(max_length=255)
    section_two_subsection_one_body = serializers.CharField()
    section_two_subsection_two_icon = wagtail_fields.ImageRenditionField(
        'original')
    section_two_subsection_two_heading = serializers.CharField(max_length=255)
    section_two_subsection_two_body = serializers.CharField()
    section_two_subsection_three_icon = wagtail_fields.ImageRenditionField(
        'original')
    section_two_subsection_three_heading = serializers.CharField(
        max_length=255)
    section_two_subsection_three_body = serializers.CharField()

    case_study_title = serializers.CharField(max_length=255)
    case_study_description = serializers.CharField(max_length=255)
    case_study_cta_text = serializers.CharField(max_length=255)
    case_study_cta_page = serializers.SerializerMethodField()
    case_study_image = wagtail_fields.ImageRenditionField('original')

    def get_case_study_cta_page(self, obj):
        if not obj.case_study_cta_page:
            return None
        related_page = obj.case_study_cta_page
        serializer_class = MODEL_TO_SERIALIZER_MAPPING[
            related_page.specific.__class__]
        serializer = serializer_class(related_page.specific)
        return serializer.data

    section_three_heading = serializers.CharField(max_length=255)
    section_three_teaser = serializers.CharField()
    section_three_subsection_one_heading = serializers.CharField(
        max_length=255)
    section_three_subsection_one_teaser = serializers.CharField()
    section_three_subsection_one_body = core_fields.MarkdownToHTMLField()
    section_three_subsection_two_heading = serializers.CharField(
        max_length=255)
    section_three_subsection_two_teaser = serializers.CharField()
    section_three_subsection_two_body = core_fields.MarkdownToHTMLField()


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
        if 'region' in self.context:
            slug = f'{obj.slug}-{self.context["region"]}'
            folder = InternationalLocalisedFolderPage.objects.filter(slug=slug)
            if folder.exists():
                articles_queryset = folder[0].get_descendants().type(
                    InternationalArticlePage
                ).live().specific()
                articles = RelatedArticlePageSerializer(
                    articles_queryset,
                    many=True,
                    allow_null=True,
                    context=self.context
                )
                campaigns_queryset = folder[0].get_descendants().type(
                    InternationalCampaignPage
                ).live().specific()

                campaigns = RelatedCampaignPageSerializer(
                    campaigns_queryset,
                    many=True,
                    allow_null=True,
                    context=self.context
                )
                data = articles.data + campaigns.data
        return data

    def get_child_pages(self, obj):
        articles_queryset = obj.get_descendants().type(
            InternationalArticlePage
        ).live().specific()
        articles = RelatedArticlePageSerializer(
            articles_queryset,
            many=True,
            allow_null=True,
            context=self.context
        )
        campaigns_queryset = obj.get_descendants().type(
            InternationalCampaignPage
        ).live().specific()
        campaigns = RelatedCampaignPageSerializer(
            campaigns_queryset,
            many=True,
            allow_null=True,
            context=self.context
        )
        return articles.data + campaigns.data


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


class FeatureSerializer(serializers.Serializer):
    heading = serializers.CharField()
    content = core_fields.MarkdownToHTMLField()
    image = wagtail_fields.ImageRenditionField('original')
    image_thumbnail = wagtail_fields.ImageRenditionField(
        'fill-640x360|jpegquality-60|format-jpeg', source='image')
    url = serializers.CharField()


class FeatureProxyDataWrapper:

    def __init__(self, instance, position_number):
        self.position_number = position_number
        self.instance = instance

    def get_field_value(self, attribute_name_pattern):
        return getattr(
            self.instance,
            attribute_name_pattern.format(self.position_number),
            None
        )

    @property
    def heading(self):
        return self.get_field_value('feature_{}_heading')

    @property
    def content(self):
        return self.get_field_value('feature_{}_content')

    @property
    def image(self):
        return self.get_field_value('feature_{}_image')

    @property
    def url(self):
        return self.get_field_value('feature_{}_url')


class InternationalCuratedTopicLandingPageSerializer(BasePageSerializer):
    display_title = serializers.CharField()

    hero_image = wagtail_fields.ImageRenditionField('original')
    hero_image_thumbnail = wagtail_fields.ImageRenditionField(
        'fill-640x360|jpegquality-60|format-jpeg', source='hero_image')

    teaser = serializers.CharField()

    feature_section_heading = serializers.CharField()

    features_large = serializers.SerializerMethodField()

    features_small = serializers.SerializerMethodField()

    def get_features(self, instance, *positions):
        data = [
            FeatureProxyDataWrapper(
                instance=instance,
                position_number=num,

            )
            for num in positions
        ]
        serializer = FeatureSerializer(data, many=True)
        return serializer.data

    def get_features_large(self, instance):
        return self.get_features(instance, 'one', 'two')

    def get_features_small(self, instance):
        return self.get_features(instance, 'three', 'four', 'five')
