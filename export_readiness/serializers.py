from rest_framework import serializers
from wagtail.images.api import fields as wagtail_fields

from core import fields as core_fields
from core.serializers import (
    BasePageSerializer, FormPageSerializerMetaclass, ChildPagesSerializerHelper, HeroSerializer
)
from core.blocks_serializers import StreamChildBaseSerializer, LinkWithImageAndContentBlockStreamChildSerializer, \
    LinkBlockStreamChildSerializer
from export_readiness import blocks_serializers

from great_international.serializers import StatisticProxyDataWrapper, StatisticSerializer

from .models import (
    ArticleListingPage, ArticlePage, CampaignPage, SuperregionPage, EUExitDomesticFormPage, CountryGuidePage
)


class RelatedArticlePageSerializer(BasePageSerializer):
    """Separate serializer for related article pages so we don't end up with
    infinite nesting of related pages inside an article page"""

    type_of_article = serializers.CharField()
    article_title = serializers.CharField(max_length=255)
    article_teaser = serializers.CharField(max_length=255)
    article_image = wagtail_fields.ImageRenditionField('original')
    article_image_thumbnail = wagtail_fields.ImageRenditionField(
        'fill-640x360', source='article_image')


class RelatedCampaignPageSerializer(BasePageSerializer):
    title = serializers.CharField(max_length=255, source='campaign_heading')
    thumbnail = wagtail_fields.ImageRenditionField('fill-640x360', source='campaign_hero_image')


class RelatedArticleListingPageSerializer(BasePageSerializer):
    title = serializers.CharField(source='landing_page_title')
    thumbnail = wagtail_fields.ImageRenditionField('fill-640x360', source='hero_image')
    teaser = serializers.CharField(max_length=255, source='list_teaser')


MODEL_TO_SERIALIZER_MAPPING = {
    ArticlePage: RelatedArticlePageSerializer,
    CampaignPage: RelatedCampaignPageSerializer,
    ArticleListingPage: RelatedArticleListingPageSerializer
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


class GenericBodyOnlyPageSerializer(BasePageSerializer):
    body = core_fields.MarkdownToHTMLField()


class GetFinancePageSerializer(BasePageSerializer, HeroSerializer):
    breadcrumbs_label = serializers.CharField()
    hero_text = core_fields.MarkdownToHTMLField()
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


class BaseArticlePageSerializer(PageWithRelatedPagesSerializer):

    display_title = serializers.CharField(source='article_title')
    article_title = serializers.CharField()
    article_teaser = serializers.CharField()

    article_image = wagtail_fields.ImageRenditionField('original')
    article_image_thumbnail = wagtail_fields.ImageRenditionField('fill-640x360', source='article_image')

    article_body_text = core_fields.MarkdownToHTMLField()

    cta_title = serializers.CharField()
    cta_teaser = serializers.CharField()
    cta_link_label = serializers.CharField()
    cta_link = serializers.CharField()

    tags = core_fields.TagsListField()


class ArticlePageSerializer(BaseArticlePageSerializer):
    type_of_article = serializers.CharField()
    article_subheading = serializers.CharField()
    article_video = core_fields.VideoField()
    article_video_transcript = core_fields.MarkdownToHTMLField()


class MarketingArticlePageSerializer(BaseArticlePageSerializer):
    pass


class ArticleListingPageSerializer(
    BasePageSerializer, ChildPagesSerializerHelper, HeroSerializer
):
    landing_page_title = serializers.CharField(max_length=255)
    display_title = serializers.CharField(source='landing_page_title')

    articles_count = serializers.IntegerField()
    list_teaser = core_fields.MarkdownToHTMLField(allow_null=True)
    hero_teaser = serializers.CharField(allow_null=True)
    articles = serializers.SerializerMethodField()

    def get_articles(self, obj):
        return self.get_child_pages_data_for(
            obj,
            ArticlePage,
            ArticlePageSerializer
        )


class AccordionStatisticProxyDataWrapper:
    def __init__(self, instance, accordion, position_number):
        self.accordion = accordion
        self.position_number = position_number
        self.instance = instance

    @property
    def number(self):
        return getattr(
            self.instance,
            f'{self.accordion}_statistic_{self.position_number}_number'
        )

    @property
    def heading(self):
        return getattr(
            self.instance,
            f'{self.accordion}_statistic_{self.position_number}_heading'
        )

    @property
    def smallprint(self):
        return getattr(
            self.instance,
            f'{self.accordion}_statistic_{self.position_number}_smallprint'
        )


class AccordionSubsectionProxyDataWrapper:
    def __init__(self, instance, accordion, position_number):
        self.accordion = accordion
        self.position_number = position_number
        self.instance = instance

    @property
    def icon(self):
        return getattr(
            self.instance,
            f'{self.accordion}_subsection_{self.position_number}_icon'
        )

    @property
    def heading(self):
        return getattr(
            self.instance,
            f'{self.accordion}_subsection_{self.position_number}_heading'
        )

    @property
    def body(self):
        return getattr(
            self.instance,
            f'{self.accordion}_subsection_{self.position_number}_body'
        )


class IntroCTAProxyDataWrapper:
    def __init__(self, instance, position_number):
        self.position_number = position_number
        self.instance = instance

    @property
    def link(self):
        return getattr(
            self.instance,
            f'intro_cta_{self.position_number}_link'
        )

    @property
    def title(self):
        return getattr(
            self.instance,
            f'intro_cta_{self.position_number}_title'
        )


class AccordionProxyDataWrapper:

    def __init__(self, instance, position_number):
        self.position_number = position_number
        self.instance = instance

    @property
    def icon(self):
        return getattr(
            self.instance,
            f'accordion_{self.position_number}_icon'
        )

    @property
    def title(self):
        return getattr(
            self.instance,
            f'accordion_{self.position_number}_title'
        )

    @property
    def teaser(self):
        return getattr(
            self.instance,
            f'accordion_{self.position_number}_teaser'
        )

    @property
    def subsections(self):
        return [
            AccordionSubsectionProxyDataWrapper(
                instance=self.instance,
                accordion=f'accordion_{self.position_number}',
                position_number=num
            )
            for num in ('1', '2', '3')
        ]

    @property
    def statistics(self):
        return [
            AccordionStatisticProxyDataWrapper(
                instance=self.instance,
                accordion=f'accordion_{self.position_number}',
                position_number=num
            )
            for num in ('1', '2', '3', '4', '5', '6')
        ]

    def case_study_field_value(self, field_name):
        return getattr(
            self.instance,
            field_name
        )

    @property
    def case_study(self):
        image = self.case_study_field_value(
            f'accordion_{self.position_number}_case_study_hero_image'
        )
        button_text = self.case_study_field_value(
            f'accordion_{self.position_number}_case_study_button_text'
        )
        button_link = self.case_study_field_value(
            f'accordion_{self.position_number}_case_study_button_link'
        )
        title = self.case_study_field_value(
            f'accordion_{self.position_number}_case_study_title'
        )
        description = self.case_study_field_value(
            f'accordion_{self.position_number}_case_study_description'
        )
        return {
            'image': image,
            'button_text': button_text,
            'button_link': button_link,
            'title': title,
            'description': description,
        }


class FactSheetColumnProxyDataWrapper:

    def __init__(self, instance, position_number):
        self.position_number = position_number
        self.instance = instance

    @property
    def title(self):
        return getattr(
            self.instance,
            f'fact_sheet_column_{self.position_number}_title'
        )

    @property
    def teaser(self):
        return getattr(
            self.instance,
            f'fact_sheet_column_{self.position_number}_teaser'
        )

    @property
    def body(self):
        return getattr(
            self.instance,
            f'fact_sheet_column_{self.position_number}_body'
        )


class AccordionCaseStudySerializer(serializers.Serializer):
    image = wagtail_fields.ImageRenditionField('original')
    button_text = serializers.CharField()
    button_link = serializers.CharField()
    title = serializers.CharField()
    description = serializers.CharField()


class AccordionSubsectionSerializer(serializers.Serializer):
    icon = wagtail_fields.ImageRenditionField('original')
    heading = serializers.CharField()
    body = serializers.CharField()


class StatisticSubsectionSerializer(serializers.Serializer):
    number = serializers.CharField()
    heading = serializers.CharField()
    smallprint = serializers.CharField()


class AccordionSerializer(serializers.Serializer):
    icon = wagtail_fields.ImageRenditionField('original')
    title = serializers.CharField()
    teaser = serializers.CharField()
    case_study = AccordionCaseStudySerializer()
    subsections = AccordionSubsectionSerializer(many=True)
    statistics = StatisticSubsectionSerializer(many=True)


class FactSheetColumnSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=255)
    teaser = serializers.CharField(max_length=255)
    body = core_fields.MarkdownToHTMLField(allow_null=True)


class FactSheetSerializer(serializers.Serializer):
    fact_sheet_title = serializers.CharField(max_length=255)
    fact_sheet_teaser = serializers.CharField(max_length=255)
    columns = FactSheetColumnSerializer(many=True)


class IntroCTAsSerializer(serializers.Serializer):
    link = serializers.CharField()
    title = serializers.CharField()


class CountryGuideListingPageSerializer(serializers.Serializer):
    hero_image_thumbnail = wagtail_fields.ImageRenditionField('fill-640x360', source='hero_image')
    full_path = serializers.CharField(max_length=255, source='specific.full_path')
    last_published_at = serializers.DateTimeField()
    title = serializers.CharField()


class CountryGuidePageSerializer(PageWithRelatedPagesSerializer, HeroSerializer):
    heading = serializers.CharField(max_length=255)
    sub_heading = serializers.CharField(max_length=255)
    heading_teaser = serializers.CharField()
    intro_ctas = serializers.SerializerMethodField()

    section_one_body = core_fields.MarkdownToHTMLField()
    section_one_image = wagtail_fields.ImageRenditionField('fill-640x360')
    section_one_image_caption = serializers.CharField(max_length=255)
    section_one_image_caption_company = serializers.CharField(
        max_length=255)

    section_two_heading = serializers.CharField(max_length=255, allow_null=True)
    section_two_teaser = serializers.CharField(allow_null=True)

    statistics = serializers.SerializerMethodField()
    accordions = serializers.SerializerMethodField()
    fact_sheet = serializers.SerializerMethodField()

    duties_and_custom_procedures_cta_link = serializers.CharField(max_length=255)

    tags = core_fields.TagsListField()
    region = serializers.CharField(allow_null=True, source='country.region.name')

    def get_intro_ctas(self, instance):
        data = [
            IntroCTAProxyDataWrapper(instance=instance, position_number=num)
            for num in ['one', 'two', 'three']
        ]
        serialized = IntroCTAsSerializer(data, many=True).data
        return [cta for cta in serialized if cta['link'] and cta['title']]

    def get_fact_sheet(self, instance):
        data = {
            'fact_sheet_title': instance.fact_sheet_title,
            'fact_sheet_teaser': instance.fact_sheet_teaser,
            'columns': [
                FactSheetColumnProxyDataWrapper(
                    instance=instance, position_number=num)
                for num in ['1', '2']
            ]
        }
        return FactSheetSerializer(data).data

    def get_statistics(self, instance):
        data = [
            StatisticProxyDataWrapper(instance=instance, position_number=num)
            for num in ['1', '2', '3', '4', '5', '6']
        ]
        serializer = StatisticSerializer(data, many=True)
        return serializer.data

    def get_accordions(self, instance):
        data = [
            AccordionProxyDataWrapper(instance=instance, position_number=num)
            for num in ['1', '2', '3', '4', '5', '6']
        ]
        serializer = AccordionSerializer(data, many=True)
        return serializer.data


class RelatedArticlePageStreamChildSerializer(RelatedArticlePageSerializer, StreamChildBaseSerializer):
    pass


class HomePageSerializer(BasePageSerializer):
    hero_image = wagtail_fields.ImageRenditionField('original')
    hero_image_thumbnail = wagtail_fields.ImageRenditionField('fill-640x360', source='hero_image')
    hero_text = serializers.CharField(required=False)
    hero_cta_text = serializers.CharField(required=False)
    hero_cta_url = serializers.CharField(required=False)

    chevron_url = serializers.CharField(required=False)
    chevron_text = serializers.CharField(required=False)
    chevron_links = LinkBlockStreamChildSerializer(many=True, required=False)

    how_dit_helps_title = serializers.CharField(required=False)
    how_dit_helps_columns = LinkWithImageAndContentBlockStreamChildSerializer(many=True, required=False)

    madb_title = serializers.CharField(required=False)
    madb_image = wagtail_fields.ImageRenditionField('original', required=False)
    madb_image_alt = serializers.CharField(required=False)
    madb_content = core_fields.MarkdownToHTMLField(required=False)
    madb_cta_text = serializers.CharField(required=False)
    madb_cta_url = serializers.CharField(required=False)

    what_is_new_title = serializers.CharField(required=False)
    what_is_new_pages = LinkWithImageAndContentBlockStreamChildSerializer(many=True, required=False)

    campaign = blocks_serializers.CampaignBlockStreamChildSerializer(required=False, many=True)


class ChildSuperregionPageSerializer(BasePageSerializer):
    hero_image_thumbnail = wagtail_fields.ImageRenditionField('fill-640x360', source='article_image')
    teaser = serializers.CharField()


class ChildArticlePageSerializer(BasePageSerializer):
    hero_image_thumbnail = wagtail_fields.ImageRenditionField('fill-640x360', source='article_image')
    teaser = serializers.CharField(source='article_teaser')
    sub_heading = serializers.CharField(source='article_subheading')


class ChildArticleListPageSerializer(BasePageSerializer):
    hero_image_thumbnail = wagtail_fields.ImageRenditionField('fill-640x360', source='hero_image')
    teaser = serializers.CharField(source='list_teaser')


class ChildCountryGuidePageSerializer(BasePageSerializer):
    hero_image_thumbnail = wagtail_fields.ImageRenditionField('fill-640x360', source='hero_image')
    heading = serializers.CharField()
    sub_heading = serializers.CharField()


class TopicLandingPageSerializer(BasePageSerializer, ChildPagesSerializerHelper, HeroSerializer):
    landing_page_title = serializers.CharField(max_length=255)
    display_title = serializers.CharField(source='landing_page_title')
    hero_teaser = serializers.CharField(max_length=255)
    banner_text = core_fields.MarkdownToHTMLField()

    teaser = serializers.CharField()

    child_pages = serializers.SerializerMethodField()

    def get_child_pages(self, obj):
        articles = self.get_child_pages_data_for(
            obj,
            ArticlePage,
            ChildArticlePageSerializer
        )
        article_lists = self.get_child_pages_data_for(
            obj,
            ArticleListingPage,
            ChildArticleListPageSerializer
        )
        superregions = self.get_child_pages_data_for(
            obj,
            SuperregionPage,
            ChildSuperregionPageSerializer
        )
        country_guides = self.get_child_pages_data_for(
            obj,
            CountryGuidePage,
            ChildCountryGuidePageSerializer
        )
        country_guides = sorted(country_guides, key=lambda x: x['heading'])

        return article_lists + articles + superregions + country_guides


class SuperregionPageSerializer(TopicLandingPageSerializer):
    pass
    """
    Superregions are unused but will be used in the future

    articles_count = serializers.IntegerField()
        def get_child_pages(self, obj):
        articles = self.get_child_pages_data_for(
            obj,
            ArticleListingPage,
            ArticleListingPageSerializer
        )
        country_guides = self.get_child_pages_data_for(
            obj,
            CountryGuidePage,
            CountryGuidePageSerializer
        )
        return articles + country_guides
    """


class TagCountryPageSerializer(serializers.Serializer):
    name = serializers.CharField()
    countries = serializers.SerializerMethodField()

    def get_countries(self, object):
        serializer = CountryGuidePageSerializer(
            object.countryguidepage_set.filter(live=True),
            many=True,
            context=self.context
        )
        return serializer.data


class IDNameSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()


class IndustryTagSerializer(IDNameSerializer):
    icon = wagtail_fields.ImageRenditionField('original')
    pages_count = serializers.SerializerMethodField()

    def get_pages_count(self, tag):
        return tag.countryguidepage_set.all().live().count()


class CampaignPageSerializer(PageWithRelatedPagesSerializer):
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


class EUExitGenericFormPageSerializer(BasePageSerializer):
    breadcrumbs_label = serializers.CharField()
    heading = serializers.CharField()
    body_text = core_fields.MarkdownToHTMLField()
    submit_button_text = serializers.CharField()
    disclaimer = core_fields.MarkdownToHTMLField()


class EUExitDomesticFormPageSerializer(
    EUExitGenericFormPageSerializer,
    metaclass=FormPageSerializerMetaclass
):
    class Meta:
        model_class = EUExitDomesticFormPage


class EUExitFormSuccessPageSerializer(BasePageSerializer):
    breadcrumbs_label = serializers.CharField()
    heading = serializers.CharField()
    body_text = serializers.CharField()
    next_title = serializers.CharField()
    next_body_text = serializers.CharField()


class ContactUsGuidancePageSerializer(BasePageSerializer):
    topic = core_fields.MarkdownToHTMLField()
    body = core_fields.MarkdownToHTMLField()


class ContactSuccessPageSerializer(BasePageSerializer):
    topic = core_fields.MarkdownToHTMLField()
    heading = serializers.CharField()
    body_text = serializers.CharField()
    next_title = serializers.CharField()
    next_body_text = serializers.CharField()


class SellingOnlineOverseasHomePageSerializer(BasePageSerializer):
    featured_case_studies = serializers.SerializerMethodField()

    def get_featured_case_studies(self, instance):
        pages = [
            instance.featured_case_study_one,
            instance.featured_case_study_two,
            instance.featured_case_study_three
        ]

        return [
            ChildArticlePageSerializer(page.specific).data
            for page in pages if page
        ]
