from rest_framework import serializers
from wagtail.images.api import fields as wagtail_fields

from core import fields as core_fields
from core.serializers import (
    BasePageSerializer,
    ChildPagesSerializerHelper,
    FormPageSerializerMetaclass,
)

from .models import (
    InternationalArticlePage,
    InternationalArticleListingPage,
    InternationalLocalisedFolderPage,
    InternationalCampaignPage,
    InternationalGuideLandingPage,
    InternationalSectorPage,
    InternationalEUExitFormPage,
    CapitalInvestSectorPage)


class SectionThreeSubsectionProxyDataWrapper:

    def __init__(self, instance, position_number):
        self.position_number = position_number
        self.instance = instance

    @property
    def heading(self):
        return getattr(
            self.instance,
            f'section_three_subsection_{self.position_number}_heading'
        )

    @property
    def teaser(self):
        return getattr(
            self.instance,
            f'section_three_subsection_{self.position_number}_teaser'
        )

    @property
    def body(self):
        return getattr(
            self.instance,
            f'section_three_subsection_{self.position_number}_body'
        )


class FeaturedLinkProxyDataWrapper:
    def __init__(self, instance, position_number):
        self.position_number = position_number
        self.instance = instance

    @property
    def image(self):
        return getattr(
            self.instance,
            f'featured_link_{self.position_number}_image'
        )

    @property
    def heading(self):
        return getattr(
            self.instance,
            f'featured_link_{self.position_number}_heading'
        )


class SectionTwoSubsectionProxyDataWrapper:

    def __init__(self, instance, position_number):
        self.position_number = position_number
        self.instance = instance

    @property
    def icon(self):
        return getattr(
            self.instance,
            f'section_two_subsection_{self.position_number}_icon'
        )

    @property
    def heading(self):
        return getattr(
            self.instance,
            f'section_two_subsection_{self.position_number}_heading'
        )

    @property
    def body(self):
        return getattr(
            self.instance,
            f'section_two_subsection_{self.position_number}_body'
        )


class StatisticProxyDataWrapper:

    def __init__(self, instance, position_number):
        self.position_number = position_number
        self.instance = instance

    @property
    def number(self):
        return getattr(
            self.instance,
            f'statistic_{self.position_number}_number'
        )

    @property
    def heading(self):
        return getattr(
            self.instance,
            f'statistic_{self.position_number}_heading'
        )

    @property
    def smallprint(self):
        return getattr(
            self.instance,
            f'statistic_{self.position_number}_smallprint'
        )


class EconomicsStatisticProxyDataWrapper:

    def __init__(self, instance, position_number):
        self.position_number = position_number
        self.instance = instance

    @property
    def number(self):
        return getattr(
            self.instance,
            f'economics_stat_{self.position_number}_number'
        )

    @property
    def heading(self):
        return getattr(
            self.instance,
            f'economics_stat_{self.position_number}_heading'
        )

    @property
    def smallprint(self):
        return getattr(
            self.instance,
            f'economics_stat_{self.position_number}_smallprint'
        )


class LocationStatisticProxyDataWrapper:

    def __init__(self, instance, position_number):
        self.position_number = position_number
        self.instance = instance

    @property
    def number(self):
        return getattr(
            self.instance,
            f'location_stat_{self.position_number}_number'
        )

    @property
    def heading(self):
        return getattr(
            self.instance,
            f'location_stat_{self.position_number}_heading'
        )

    @property
    def smallprint(self):
        return getattr(
            self.instance,
            f'location_stat_{self.position_number}_smallprint'
        )


class SectionThreeSubsectionSerializer(serializers.Serializer):
    heading = serializers.CharField(max_length=255)
    teaser = serializers.CharField()
    body = core_fields.MarkdownToHTMLField()


class SectionTwoSubsectionSerializer(serializers.Serializer):
    icon = wagtail_fields.ImageRenditionField('original')
    heading = serializers.CharField(max_length=255)
    body = serializers.CharField()


class StatisticSerializer(serializers.Serializer):
    number = serializers.CharField(max_length=255)
    heading = serializers.CharField(max_length=255)
    smallprint = serializers.CharField(max_length=255)


class FeaturedLinkSerializer(serializers.Serializer):
    image = wagtail_fields.ImageRenditionField('original')
    heading = serializers.CharField(max_length=255)


class EconomicStatSerializer(serializers.Serializer):
    number = serializers.CharField(max_length=255)
    heading = serializers.CharField(max_length=255)
    smallprint = serializers.CharField(max_length=255)


class LocationStatSerializer(serializers.Serializer):
    number = serializers.CharField(max_length=255)
    heading = serializers.CharField(max_length=255)
    smallprint = serializers.CharField(max_length=255)


class RelatedArticlePageSerializer(BasePageSerializer):
    title = serializers.CharField(source='article_title')
    subheading = serializers.CharField(source='article_subheading')
    teaser = serializers.CharField(source='article_teaser')
    thumbnail = wagtail_fields.ImageRenditionField(
        'fill-640x360', source='article_image')


class RelatedCampaignPageSerializer(BasePageSerializer):
    title = serializers.CharField(
        max_length=255, source='campaign_heading')
    subheading = serializers.CharField(
        max_length=255, source='campaign_subheading'
    )
    teaser = serializers.CharField(
        max_length=255, source='campaign_teaser')
    thumbnail = wagtail_fields.ImageRenditionField(
        'fill-640x360',
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
    sub_heading = serializers.CharField()
    hero_image = wagtail_fields.ImageRenditionField('original')
    hero_image_thumbnail = wagtail_fields.ImageRenditionField(
        'fill-640x360', source='hero_image')
    heading_teaser = serializers.CharField()

    section_one_body = core_fields.MarkdownToHTMLField()
    section_one_image = wagtail_fields.ImageRenditionField('fill-640x360')
    section_one_image_caption = serializers.CharField(max_length=255)
    section_one_image_caption_company = serializers.CharField(max_length=255)

    statistics = serializers.SerializerMethodField()

    def get_statistics(self, instance):
        data = [
            StatisticProxyDataWrapper(instance=instance, position_number=num)
            for num in ['1', '2', '3', '4', '5', '6']
        ]
        serializer = StatisticSerializer(data, many=True)
        return serializer.data

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
    section_two_subsections = serializers.SerializerMethodField()

    def get_section_two_subsections(self, instance):
        data = [
            SectionTwoSubsectionProxyDataWrapper(
                instance=instance,
                position_number=num
            )
            for num in ['one', 'two', 'three']
        ]
        serializer = SectionTwoSubsectionSerializer(data, many=True)
        return serializer.data

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
    section_three_subsections = serializers.SerializerMethodField()

    def get_section_three_subsections(self, instance):
        data = [
            SectionThreeSubsectionProxyDataWrapper(
                instance=instance,
                position_number=num
            )
            for num in ['one', 'two']
        ]
        serializer = SectionThreeSubsectionSerializer(data, many=True)
        return serializer.data

    section_three_subsection_one_heading = serializers.CharField(
        max_length=255)
    section_three_subsection_one_teaser = serializers.CharField()
    section_three_subsection_one_body = core_fields.MarkdownToHTMLField()
    section_three_subsection_two_heading = serializers.CharField(
        max_length=255)
    section_three_subsection_two_teaser = serializers.CharField()
    section_three_subsection_two_body = core_fields.MarkdownToHTMLField()


class InternationalArticlePageSerializer(PageWithRelatedPagesSerializer):
    article_title = serializers.CharField()
    article_subheading = serializers.CharField()
    display_title = serializers.CharField(source='article_title')
    article_teaser = serializers.CharField()
    article_image = wagtail_fields.ImageRenditionField('original')
    article_image_thumbnail = wagtail_fields.ImageRenditionField(
        'fill-640x360', source='article_image')
    article_body_text = core_fields.MarkdownToHTMLField()


class InternationalHomePageSerializer(PageWithRelatedPagesSerializer):
    hero_title = serializers.CharField(max_length=255)
    hero_subtitle = serializers.CharField(max_length=255)
    hero_cta_text = serializers.CharField(max_length=255)
    hero_cta_link = serializers.CharField(max_length=255)
    hero_image = wagtail_fields.ImageRenditionField('original')

    invest_title = serializers.CharField(max_length=255)
    invest_content = core_fields.MarkdownToHTMLField()
    invest_image = wagtail_fields.ImageRenditionField(
        'fill-640x360'
    )

    section_two_heading = serializers.CharField()
    section_two_teaser = serializers.CharField()
    section_two_subsections = serializers.SerializerMethodField()

    def get_section_two_subsections(self, instance):
        data = [
            SectionTwoSubsectionProxyDataWrapper(
                instance=instance,
                position_number=num
            )
            for num in ['one', 'two', 'three', 'four', 'five', 'six']
        ]
        serializer = SectionTwoSubsectionSerializer(data, many=True)
        return serializer.data

    featured_links_title = serializers.CharField()
    featured_links_summary = serializers.CharField()
    featured_links = serializers.SerializerMethodField()

    def get_featured_links(self, instance):
        data = [
            FeaturedLinkProxyDataWrapper(
                instance=instance,
                position_number=num
            )
            for num in ['one', 'two', 'three']
        ]
        serializer = FeaturedLinkSerializer(data, many=True)
        return serializer.data

    trade_title = serializers.CharField(max_length=255)
    trade_content = core_fields.MarkdownToHTMLField()
    trade_image = wagtail_fields.ImageRenditionField(
        'fill-640x360'
    )

    news_title = serializers.CharField(max_length=255)

    tariffs_title = serializers.CharField(max_length=255)
    tariffs_description = core_fields.MarkdownToHTMLField()
    tariffs_link = serializers.URLField()
    tariffs_image = wagtail_fields.ImageRenditionField(
        'fill-640x360'
    )
    tariffs_call_to_action_text = serializers.CharField(max_length=255)
    study_in_uk_cta_text = serializers.CharField(max_length=255)
    visit_uk_cta_text = serializers.CharField(max_length=255)


class InternationalCampaignPageSerializer(PageWithRelatedPagesSerializer):
    campaign_heading = serializers.CharField(max_length=255)
    campaign_subheading = serializers.CharField(max_length=255)

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


class InternationalArticleListingPageSerializer(
    BasePageSerializer,
    ChildPagesSerializerHelper
):
    landing_page_title = serializers.CharField(max_length=255)
    display_title = serializers.CharField(source='landing_page_title')
    hero_image = wagtail_fields.ImageRenditionField('original')
    hero_image_thumbnail = wagtail_fields.ImageRenditionField(
        'fill-640x360', source='hero_image')

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
                articles = self.get_child_pages_data_for(
                    folder[0],
                    InternationalArticlePage,
                    RelatedArticlePageSerializer
                )
                campaigns = self.get_child_pages_data_for(
                    folder[0],
                    InternationalCampaignPage,
                    InternationalCampaignPageSerializer
                )
                data = articles + campaigns
        return data

    def get_child_pages(self, obj):
        articles = self.get_child_pages_data_for(
            obj,
            InternationalArticlePage,
            RelatedArticlePageSerializer
        )
        campaigns = self.get_child_pages_data_for(
            obj,
            InternationalCampaignPage,
            RelatedCampaignPageSerializer
        )
        return articles + campaigns


class InternationalTopicLandingPageSerializer(
    BasePageSerializer,
    ChildPagesSerializerHelper
):
    landing_page_title = serializers.CharField(max_length=255)
    display_title = serializers.CharField(source='landing_page_title')
    hero_teaser = serializers.CharField(max_length=255)
    hero_image = wagtail_fields.ImageRenditionField('original')

    hero_image_thumbnail = wagtail_fields.ImageRenditionField(
        'fill-640x360', source='hero_image')

    child_pages = serializers.SerializerMethodField()

    def get_child_pages(self, obj):
        articles = self.get_child_pages_data_for(
            obj,
            InternationalArticleListingPage,
            InternationalArticleListingPageSerializer
        )
        campaigns = self.get_child_pages_data_for(
            obj,
            InternationalCampaignPage,
            RelatedCampaignPageSerializer
        )
        guides = self.get_child_pages_data_for(
            obj,
            InternationalGuideLandingPage,
            InternationalGuideLandingPageSerializer
        )
        sectors = self.get_child_pages_data_for(
            obj,
            InternationalSectorPage,
            InternationalSectorPageSerializer
        )
        sectors = sorted(sectors, key=lambda x: x['heading'])
        return articles + campaigns + guides + sectors


class FeatureSerializer(serializers.Serializer):
    heading = serializers.CharField()
    content = core_fields.MarkdownToHTMLField()
    image = wagtail_fields.ImageRenditionField(
        'fill-640x360')
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
        'fill-640x360', source='hero_image')

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


class InternationalGuideLandingPageSerializer(BasePageSerializer):

    display_title = serializers.CharField()

    hero_image = wagtail_fields.ImageRenditionField('original')
    hero_image_thumbnail = wagtail_fields.ImageRenditionField(
        'fill-640x360', source='hero_image')

    teaser = serializers.CharField()

    section_one_content = core_fields.MarkdownToHTMLField()
    section_one_image = wagtail_fields.ImageRenditionField(
        'fill-640x360')
    section_one_image_caption = serializers.CharField()

    section_two_heading = serializers.CharField()
    section_two_teaser = serializers.CharField()
    section_two_button_text = serializers.CharField()
    section_two_button_url = serializers.CharField()
    section_two_image = wagtail_fields.ImageRenditionField(
        'fill-640x360')

    guides_section_heading = serializers.CharField()
    guides = serializers.SerializerMethodField()

    def get_guides(self, obj):
        article_list = (
            InternationalArticlePage.objects
            .descendant_of(obj)
            .live()
            .order_by('-first_published_at')
        )[:9]
        serializer = RelatedArticlePageSerializer(article_list, many=True)
        return serializer.data


class EUExitGenericFormPageSerializer(BasePageSerializer):
    breadcrumbs_label = serializers.CharField()
    heading = serializers.CharField()
    body_text = core_fields.MarkdownToHTMLField()
    submit_button_text = serializers.CharField()
    disclaimer = core_fields.MarkdownToHTMLField()


class InternationalEUExitFormPageSerializer(
    EUExitGenericFormPageSerializer,
    metaclass=FormPageSerializerMetaclass
):
    class Meta:
        model_class = InternationalEUExitFormPage


class InternationalEUExitFormSuccessPageSerializer(BasePageSerializer):
    breadcrumbs_label = serializers.CharField()
    heading = serializers.CharField()
    body_text = serializers.CharField()
    next_title = serializers.CharField()
    next_body_text = serializers.CharField()


class InternationalCapitalInvestLandingPageSerializer(BasePageSerializer):

    hero_title = serializers.CharField(max_length=255)
    hero_image = wagtail_fields.ImageRenditionField('original')
    hero_subheading = serializers.CharField(max_length=255)
    hero_subtitle = serializers.CharField(max_length=255)
    hero_cta_text = serializers.CharField(max_length=255)

    reason_to_invest_section_title = serializers.CharField(max_length=255)
    reason_to_invest_section_intro = serializers.CharField(max_length=255)
    reason_to_invest_section_content = core_fields.MarkdownToHTMLField()
    reason_to_invest_section_image = wagtail_fields.ImageRenditionField('original')
    reason_to_invest_section_image_caption = serializers.CharField(
        max_length=255
    )

    region_ops_section_title = serializers.CharField(max_length=255)
    region_ops_section_intro = serializers.CharField(max_length=255)

    region_card_one_image = wagtail_fields.ImageRenditionField('original')
    region_card_one_title = serializers.CharField(max_length=255)
    region_card_one_description = serializers.CharField(max_length=255)
    region_card_one_cta_text = serializers.CharField(max_length=255)
    region_card_one_pdf_document = core_fields.DocumentURLField()

    region_card_two_image = wagtail_fields.ImageRenditionField('original')
    region_card_two_title = serializers.CharField(max_length=255)
    region_card_two_description = serializers.CharField(max_length=255)
    region_card_two_cta_text = serializers.CharField(max_length=255)
    region_card_two_pdf_document = core_fields.DocumentURLField()

    region_card_three_image = wagtail_fields.ImageRenditionField('original')
    region_card_three_title = serializers.CharField(max_length=255)
    region_card_three_description = serializers.CharField(max_length=255)
    region_card_three_cta_text = serializers.CharField(max_length=255)
    region_card_three_pdf_document = core_fields.DocumentURLField()

    region_card_four_image = wagtail_fields.ImageRenditionField('original')
    region_card_four_title = serializers.CharField(max_length=255)
    region_card_four_description = serializers.CharField(max_length=255)
    region_card_four_cta_text = serializers.CharField(max_length=255)
    region_card_four_pdf_document = core_fields.DocumentURLField()

    region_card_five_image = wagtail_fields.ImageRenditionField('original')
    region_card_five_title = serializers.CharField(max_length=255)
    region_card_five_description = serializers.CharField(max_length=255)
    region_card_five_cta_text = serializers.CharField(max_length=255)
    region_card_five_pdf_document = core_fields.DocumentURLField()

    region_card_six_image = wagtail_fields.ImageRenditionField('original')
    region_card_six_title = serializers.CharField(max_length=255)
    region_card_six_description = serializers.CharField(max_length=255)
    region_card_six_cta_text = serializers.CharField(max_length=255)
    region_card_six_pdf_document = core_fields.DocumentURLField()

    energy_sector_title = serializers.CharField(max_length=255)
    energy_sector_content = core_fields.MarkdownToHTMLField()
    energy_sector_image = wagtail_fields.ImageRenditionField('original')
    energy_sector_image_caption = serializers.CharField(max_length=255)
    energy_sector_cta_text = serializers.CharField(max_length=255)
    energy_sector_pdf_document = core_fields.DocumentURLField()

    how_we_help_title = serializers.CharField(max_length=255)
    how_we_help_intro = serializers.CharField(max_length=255)
    how_we_help_one_icon = wagtail_fields.ImageRenditionField('original')
    how_we_help_one_text = serializers.CharField(max_length=255)
    how_we_help_two_icon = wagtail_fields.ImageRenditionField('original')
    how_we_help_two_text = serializers.CharField(max_length=255)
    how_we_help_three_icon = wagtail_fields.ImageRenditionField('original')
    how_we_help_three_text = serializers.CharField(max_length=255)
    how_we_help_four_icon = wagtail_fields.ImageRenditionField('original')
    how_we_help_four_text = serializers.CharField(max_length=255)

    contact_section_title = serializers.CharField(max_length=255)
    contact_section_text = serializers.CharField(max_length=255)
    contact_section_cta_text = serializers.CharField(max_length=255)


class CapitalInvestRegionPageSerializer(PageWithRelatedPagesSerializer):

    hero_title = serializers.CharField(max_length=255)
    breadcrumbs_label = serializers.CharField(max_length=255)
    hero_image = wagtail_fields.ImageRenditionField('original')

    region_summary_section_image = wagtail_fields.ImageRenditionField(
        'original')
    region_summary_section_intro = serializers.CharField(max_length=255)
    region_summary_section_content = core_fields.MarkdownToHTMLField(
        max_length=255
    )

    investment_opps_title = serializers.CharField(max_length=255)
    investment_opps_intro = serializers.CharField(max_length=255)

    economics_stats = serializers.SerializerMethodField()

    def get_economics_stats(self, instance):
        data = [
            EconomicsStatisticProxyDataWrapper(
                instance=instance,
                position_number=num
            )
            for num in ['1', '2', '3', '4']
        ]
        serializer = EconomicStatSerializer(data, many=True)
        return serializer.data

    economics_data_title = serializers.CharField(max_length=255)
    economics_stat_1_number = serializers.CharField(max_length=255)
    economics_stat_1_heading = serializers.CharField(max_length=255)
    economics_stat_1_smallprint = serializers.CharField(max_length=255)

    economics_stat_2_number = serializers.CharField(max_length=255)
    economics_stat_2_heading = serializers.CharField(max_length=255)
    economics_stat_2_smallprint = serializers.CharField(max_length=255)

    economics_stat_3_number = serializers.CharField(max_length=255)
    economics_stat_3_heading = serializers.CharField(max_length=255)
    economics_stat_3_smallprint = serializers.CharField(max_length=255)

    economics_stat_4_number = serializers.CharField(max_length=255)
    economics_stat_4_heading = serializers.CharField(max_length=255)
    economics_stat_4_smallprint = serializers.CharField(max_length=255)

    location_stats = serializers.SerializerMethodField()

    def get_location_stats(self, instance):
        data = [
            LocationStatisticProxyDataWrapper(
                instance=instance,
                position_number=num
            )
            for num in ['1', '2', '3', '4']
        ]
        serializer = LocationStatSerializer(data, many=True)
        return serializer.data

    location_data_title = serializers.CharField(max_length=255)
    location_stat_1_number = serializers.CharField(max_length=255)
    location_stat_1_heading = serializers.CharField(max_length=255)
    location_stat_1_smallprint = serializers.CharField(max_length=255)

    location_stat_2_number = serializers.CharField(max_length=255)
    location_stat_2_heading = serializers.CharField(max_length=255)
    location_stat_2_smallprint = serializers.CharField(max_length=255)

    location_stat_3_number = serializers.CharField(max_length=255)
    location_stat_3_heading = serializers.CharField(max_length=255)
    location_stat_3_smallprint = serializers.CharField(max_length=255)

    location_stat_4_number = serializers.CharField(max_length=255)
    location_stat_4_heading = serializers.CharField(max_length=255)
    location_stat_4_smallprint = serializers.CharField(max_length=255)

    section_title = serializers.CharField(max_length=255)
    section_image = wagtail_fields.ImageRenditionField('original')
    section_content = core_fields.MarkdownToHTMLField(max_length=255)

    case_study_image = wagtail_fields.ImageRenditionField('original')
    case_study_title = serializers.CharField(max_length=255)
    case_study_text = serializers.CharField(max_length=255)
    case_study_cta_text = serializers.CharField(max_length=255)
    case_study_cta_link = serializers.CharField(max_length=255)

    next_steps_title = serializers.CharField(max_length=255)
    next_steps_intro = serializers.CharField(max_length=255)
    invest_cta_text = serializers.CharField(max_length=255)
    invest_cta_link = serializers.CharField(max_length=255)
    buy_cta_text = serializers.CharField(max_length=255)
    buy_cta_link = serializers.CharField(max_length=255)


class CapitalInvestSectorPageSerializer(
        PageWithRelatedPagesSerializer):

    breadcrumbs_label = serializers.CharField(max_length=255)
    hero_image = wagtail_fields.ImageRenditionField(
        'original')
    hero_title = serializers.CharField(max_length=255)
    featured_description = serializers.CharField(max_length=255)

    sector_summary_intro = serializers.CharField(max_length=255)
    sector_summary_content = core_fields.MarkdownToHTMLField(max_length=255)
    sector_summary_image = wagtail_fields.ImageRenditionField(
        'original')

    investment_opportunities_title = serializers.CharField(max_length=255)

    next_steps_title = serializers.CharField(max_length=255)
    next_steps_intro = serializers.CharField(max_length=255)

    invest_cta_text = serializers.CharField(max_length=255)
    invest_cta_link = serializers.CharField(max_length=255)
    buy_cta_text = serializers.CharField(max_length=255)
    buy_cta_link = serializers.CharField(max_length=255)


class CapitalInvestOpportunityPageSerializer(BasePageSerializer):

    breadcrumbs_label = serializers.CharField(max_length=255)
    hero_image = wagtail_fields.ImageRenditionField(
        'original')
    hero_title = serializers.CharField(max_length=255)

    opportunity_summary_intro = serializers.CharField(max_length=255)
    opportunity_summary_content = core_fields.MarkdownToHTMLField(
        max_length=255
    )
    opportunity_summary_image = wagtail_fields.ImageRenditionField(
        'original')

    location = serializers.CharField(max_length=255)
    project_promoter = serializers.CharField(max_length=255)
    scale = serializers.CharField(max_length=255)
    programme = serializers.CharField(max_length=255)
    investment_type = serializers.CharField(max_length=255)
    planning_status = serializers.CharField(max_length=255)

    project_background_title = serializers.CharField(max_length=255)
    project_background_intro = serializers.CharField(max_length=255)
    project_description_title = serializers.CharField(max_length=255)
    project_description_content = core_fields.MarkdownToHTMLField(
        max_length=255
    )
    project_promoter_title = serializers.CharField(max_length=255)
    project_promoter_content = core_fields.MarkdownToHTMLField(
        max_length=255
    )
    project_image = wagtail_fields.ImageRenditionField(
        'original')

    case_study_image = wagtail_fields.ImageRenditionField('original')
    case_study_title = serializers.CharField(max_length=255)
    case_study_text = serializers.CharField(max_length=255)
    case_study_cta_text = serializers.CharField(max_length=255)
    case_study_cta_link = serializers.CharField(max_length=255)

    similar_projects_title = serializers.CharField(max_length=255)
    similar_projects_cta_text = serializers.CharField(max_length=255)
    similar_projects_cta_link = serializers.CharField(max_length=255)

    next_steps_title = serializers.CharField(max_length=255)
    next_steps_intro = serializers.CharField(max_length=255)

    invest_cta_text = serializers.CharField(max_length=255)
    invest_cta_link = serializers.CharField(max_length=255)
    buy_cta_text = serializers.CharField(max_length=255)
    buy_cta_link = serializers.CharField(max_length=255)

