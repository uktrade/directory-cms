from directory_constants.constants import cms
from rest_framework import serializers

from core import fields as core_fields
from core.serializers import BasePageSerializer
from wagtail.images.api import fields as wagtail_fields

from find_a_supplier.models import IndustryPage


class ArticleSummarySerializer(serializers.Serializer):
    industry_name = serializers.CharField()
    title = serializers.CharField()
    body = core_fields.MarkdownToHTMLField()
    image = wagtail_fields.ImageRenditionField('original')
    video_media = core_fields.VideoField()


class IndustryPageSerializer(BasePageSerializer):
    hero_image = wagtail_fields.ImageRenditionField('original')
    mobile_hero_image = wagtail_fields.ImageRenditionField('original')
    hero_image_caption = serializers.CharField()
    summary_image = wagtail_fields.ImageRenditionField('original')
    hero_text = core_fields.MarkdownToHTMLField()
    introduction_text = serializers.CharField()
    introduction_call_to_action_button_text = serializers.CharField()
    introduction_title = serializers.CharField()
    introduction_column_one_text = core_fields.MarkdownToHTMLField()
    introduction_column_two_text = core_fields.MarkdownToHTMLField()
    introduction_column_three_text = core_fields.MarkdownToHTMLField()
    introduction_column_one_icon = wagtail_fields.ImageRenditionField(
        'original'
    )
    introduction_column_two_icon = wagtail_fields.ImageRenditionField(
        'original'
    )
    introduction_column_three_icon = wagtail_fields.ImageRenditionField(
        'original'
    )
    breadcrumbs_label = serializers.CharField()
    breadcrumbs = core_fields.BreadcrumbsField(
        service_name=cms.FIND_A_SUPPLIER
    )
    search_filter_sector = serializers.ListField()
    search_filter_text = serializers.CharField()
    search_filter_showcase_only = serializers.BooleanField()
    company_list_text = core_fields.MarkdownToHTMLField()
    company_list_search_input_placeholder_text = serializers.CharField()
    company_list_call_to_action_text = serializers.CharField()
    show_on_homepage = serializers.BooleanField()
    show_on_industries_showcase_page = serializers.BooleanField()
    article_summaries = serializers.SerializerMethodField()

    def get_article_summaries(self, instance):
        serializer = ArticleSummarySerializer(
            instance.article_summaries.all(),
            many=True,
            allow_null=True,
            context=self.context
        )
        return serializer.data


class IndustryLandingPageSerializer(BasePageSerializer):
    hero_image = wagtail_fields.ImageRenditionField('original')
    mobile_hero_image = wagtail_fields.ImageRenditionField('original')
    hero_image_caption = serializers.CharField()
    breadcrumbs_label = serializers.CharField()
    breadcrumbs = core_fields.BreadcrumbsField(
        service_name=cms.FIND_A_SUPPLIER
    )
    hero_title = serializers.CharField()
    proposition_text = serializers.CharField()
    call_to_action_text = serializers.CharField()
    more_industries_title = serializers.CharField()
    industries = serializers.SerializerMethodField()

    def get_industries(self, instance):
        queryset = instance.get_descendants().type(
            IndustryPage
        ).live().specific()
        serializer = IndustryPageSerializer(
            queryset,
            many=True,
            allow_null=True,
            context=self.context
        )
        return serializer.data


class IndustryArticlePageSerializer(BasePageSerializer):
    breadcrumbs_label = serializers.CharField()
    introduction_title = serializers.CharField()
    body = core_fields.MarkdownToHTMLField()
    author_name = serializers.CharField()
    job_title = serializers.CharField()
    proposition_text = serializers.CharField()
    call_to_action_text = serializers.CharField()
    show_table_of_content = serializers.BooleanField()
    back_to_home_link_text = serializers.CharField()
    social_share_title = serializers.CharField()
    date = serializers.DateField()
    breadcrumbs = core_fields.BreadcrumbsField(
        service_name=cms.FIND_A_SUPPLIER
    )


class LandingPageSerializer(BasePageSerializer):
    hero_image = wagtail_fields.ImageRenditionField('original')
    mobile_hero_image = wagtail_fields.ImageRenditionField('original')
    hero_image_caption = serializers.CharField()
    breadcrumbs_label = serializers.CharField()
    breadcrumbs = core_fields.BreadcrumbsField(
        service_name=cms.FIND_A_SUPPLIER
    )
    hero_text = core_fields.MarkdownToHTMLField()
    search_field_placeholder = serializers.CharField()
    search_button_text = serializers.CharField()
    proposition_text = core_fields.MarkdownToHTMLField()
    call_to_action_text = serializers.CharField()
    industries_list_text = core_fields.MarkdownToHTMLField()
    industries_list_call_to_action_text = serializers.CharField()
    services_list_text = core_fields.MarkdownToHTMLField()
    services_column_one = core_fields.MarkdownToHTMLField()
    services_column_two = core_fields.MarkdownToHTMLField()
    services_column_three = core_fields.MarkdownToHTMLField()
    services_column_four = core_fields.MarkdownToHTMLField()
    services_column_one_icon = wagtail_fields.ImageRenditionField('original')
    services_column_two_icon = wagtail_fields.ImageRenditionField('original')
    services_column_three_icon = wagtail_fields.ImageRenditionField('original')
    services_column_four_icon = wagtail_fields.ImageRenditionField('original')
    article_summaries = serializers.SerializerMethodField()
    industries = serializers.SerializerMethodField()

    def get_article_summaries(self, instance):
        serializer = ArticleSummarySerializer(
            instance.article_summaries.all(),
            many=True,
            allow_null=True,
            context=self.context
        )
        return serializer.data

    def get_industries(self, instance):
        queryset = IndustryPage.objects.filter(
            show_on_homepage=True, live=True
        ).order_by('slug')[:3]
        serializer = IndustryPageSerializer(
            queryset,
            many=True,
            allow_null=True,
            context=self.context
        )
        return serializer.data


class IndustryContactPageSerializer(BasePageSerializer):
    breadcrumbs_label = serializers.CharField()
    breadcrumbs = core_fields.BreadcrumbsField(
        service_name=cms.FIND_A_SUPPLIER
    )
    introduction_text = core_fields.MarkdownToHTMLField()
    submit_button_text = serializers.CharField()
    success_message_text = core_fields.MarkdownToHTMLField()
    success_back_link_text = serializers.CharField()
    industry_options = serializers.SerializerMethodField()

    def get_industry_options(self, instance):
        queryset = IndustryPage.objects.filter(live=True)
        serializer = IndustryPageSerializer(
            queryset,
            many=True,
            allow_null=True,
            context=self.context
        )
        return serializer.data
