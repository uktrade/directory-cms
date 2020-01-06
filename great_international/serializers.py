from directory_constants import cms
from rest_framework import serializers
from wagtail.images.api import fields as wagtail_fields

from core import fields as core_fields
from core.serializers import (
    BasePageSerializer,
    ChildPagesSerializerHelper,
    FormPageSerializerMetaclass,
    SameSectorOpportunitiesHelper,
    HeroSerializer,
)

from .models.great_international import (
    InternationalArticlePage,
    InternationalArticleListingPage,
    InternationalCampaignPage,
    InternationalGuideLandingPage,
    InternationalSectorPage,
    InternationalEUExitFormPage,
    InternationalSubSectorPage, AboutDitServicesPage, AboutUkLandingPage)
from .models.invest import (
    InvestHighPotentialOpportunityFormPage,
    InvestHighPotentialOpportunityDetailPage,
    InvestRegionPage
)

from .models.capital_invest import CapitalInvestOpportunityPage


ONE_TO_SIX_WORDS = ['one', 'two', 'three', 'four', 'five', 'six']
ONE_TO_SEVEN_WORDS = ONE_TO_SIX_WORDS + ['seven']
REGIONS = ['scotland', 'northern_ireland', 'north_england', 'wales', 'midlands', 'south_england']


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


class RegionSubsectionProxyDataWrapper:
    def __init__(self, instance, position_number):
        self.position_number = position_number
        self.instance = instance

    @property
    def title(self):
        return getattr(
            self.instance,
            f'sub_section_{self.position_number}_title'
        )

    @property
    def icon(self):
        return getattr(
            self.instance,
            f'sub_section_{self.position_number}_icon'
        )

    @property
    def content(self):
        return getattr(
            self.instance,
            f'sub_section_{self.position_number}_content'
        )


class InvestHowWeHelpProxyDataWrapper:

    def __init__(self, instance, position_number):
        self.position_number = position_number
        self.instance = instance

    @property
    def text(self):
        return getattr(
            self.instance,
            f'how_we_help_text_{self.position_number}'
        )

    @property
    def icon(self):
        return getattr(
            self.instance,
            f'how_we_help_icon_{self.position_number}'
        )


class ExpandHowToExpandProxyDataWrapper:

    def __init__(self, instance, position_number):
        self.position_number = position_number
        self.instance = instance

    @property
    def title(self):
        return getattr(
            self.instance,
            f'how_to_expand_title_{self.position_number}'
        )

    @property
    def text(self):
        return getattr(
            self.instance,
            f'how_to_expand_text_{self.position_number}'
        )


class HowWeHelpProxyDataWrapper:

    def __init__(self, instance, position_number):
        self.position_number = position_number
        self.instance = instance

    @property
    def text(self):
        return getattr(
            self.instance,
            f'how_we_help_{self.position_number}_text'
        )

    @property
    def icon(self):
        return getattr(
            self.instance,
            f'how_we_help_{self.position_number}_icon'
        )


class HowWeHelpWithTitleProxyDataWrapper:

    def __init__(self, instance, position_number):
        self.position_number = position_number
        self.instance = instance

    @property
    def title(self):
        return getattr(
            self.instance,
            f'how_we_help_{self.position_number}_title'
        )

    @property
    def icon(self):
        return getattr(
            self.instance,
            f'how_we_help_{self.position_number}_icon'
        )

    @property
    def text(self):
        return getattr(
            self.instance,
            f'how_we_help_{self.position_number}_text'
        )


class AboutUkRegionsProxyDataWrapper:

    def __init__(self, instance, region_title):
        self.region_title = region_title
        self.instance = instance

    @property
    def region(self):
        return getattr(
            self.instance,
            f'{self.region_title}'
        )

    @property
    def text(self):
        return getattr(
            self.instance,
            f'{self.region_title}_text'
        )


class ReadyToTradeStoryProxyDataWrapper:
    def __init__(self, instance, position):
        self.position = position
        self.instance = instance

    @property
    def story(self):
        return getattr(
            self.instance,
            f'ready_to_trade_story_{self.position}'
        )


class LinkToSectionLinksProxyDataWrapper:
    def __init__(self, instance, position):
        self.position = position
        self.instance = instance

    @property
    def text(self):
        return getattr(
            self.instance,
            f'link_to_section_{self.position}'
        )

    @property
    def cta_text(self):
        return getattr(
            self.instance,
            f'link_to_section_{self.position}_cta_text'
        )

    @property
    def cta_link(self):
        return getattr(
            self.instance,
            f'link_to_section_{self.position}_cta_link'
        )


class BenefitsOfUkProxyDataWrapper:
    def __init__(self, instance, position):
        self.position = position
        self.instance = instance

    @property
    def benefits_of_uk_text(self):
        return getattr(
            self.instance,
            f'benefits_of_uk_{self.position}'
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


class HowWeHelpSerializer(serializers.Serializer):
    text = serializers.CharField(max_length=255)
    icon = wagtail_fields.ImageRenditionField('original')


class HowWeHelpMarkDownTextSerializer(serializers.Serializer):
    text = core_fields.MarkdownToHTMLField()
    icon = wagtail_fields.ImageRenditionField('original')


class HowWeHelpWithTitleSerializer(serializers.Serializer):
    icon = wagtail_fields.ImageRenditionField('original')
    title = serializers.CharField(max_length=255)
    text = serializers.CharField(max_length=255)


class LinkToSectionLinksSerializer(serializers.Serializer):
    text = core_fields.MarkdownToHTMLField()
    cta_text = serializers.CharField(max_length=255)
    cta_link = serializers.CharField(max_length=255)


class HowToExpandSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=255)
    text = core_fields.MarkdownToHTMLField()


class AboutUkRegionSerializer(serializers.Serializer):
    region = serializers.SerializerMethodField()
    text = serializers.CharField(max_length=255)

    def get_region(self, obj):
        region = obj.region

        if not region:
            return []

        if hasattr(region.specific, 'heading'):
            serializer = MinimalPageSerializer(region.specific)
        else:
            serializer = MinimalPageWithHeroTitleSerializer(
                region.specific)

        return serializer.data


class RelatedArticlePageSerializer(BasePageSerializer):
    title = serializers.CharField(source='article_title')
    subheading = serializers.CharField(source='article_subheading')
    teaser = serializers.CharField(source='article_teaser')
    thumbnail = wagtail_fields.ImageRenditionField(
        'fill-640x360', source='article_image')


class RelatedCampaignPageSerializer(BasePageSerializer):
    title = serializers.CharField(max_length=255, source='campaign_heading')
    subheading = serializers.CharField(max_length=255, source='campaign_subheading')
    teaser = serializers.CharField(max_length=255, source='campaign_teaser')
    thumbnail = wagtail_fields.ImageRenditionField('fill-640x360', source='campaign_hero_image')


class RelatedCapitalInvestPageSerializer(BasePageSerializer):

    title = serializers.CharField(max_length=255, source='hero_title')
    image = wagtail_fields.ImageRenditionField('fill-640x360', source='hero_image')
    featured_description = serializers.CharField(max_length=255)


class RelatedInvestHomePageSerializer(BasePageSerializer):

    title = serializers.CharField(
        max_length=255, source='heading')
    image = wagtail_fields.ImageRenditionField(
        'fill-640x360',
        source='hero_image')
    teaser = serializers.CharField(max_length=255)


class RelatedTradeHomePageSerializer(BasePageSerializer):

    title = serializers.CharField(max_length=255)
    image = wagtail_fields.ImageRenditionField(
        'fill-640x360',
        source='hero_image')


class RelatedCapitalInvestOpportunityPageSerializer(BasePageSerializer):
    title = serializers.CharField(max_length=255, source='hero_title')
    hero_image = wagtail_fields.ImageRenditionField('fill-640x360')
    sector = serializers.CharField(max_length=255)
    scale = serializers.CharField(max_length=255)

    related_sectors = serializers.SerializerMethodField()

    def get_related_sectors(self, instance):
        serializer = RelatedSectorSerializer(
            instance.related_sectors.all(),
            many=True,
            allow_null=True,
            context=self.context
        )
        return serializer.data

    sub_sectors = serializers.SerializerMethodField()

    def get_sub_sectors(self, instance):
        serializer = RelatedSubSectorSerializer(
            instance.related_sub_sectors.all(),
            many=True,
            allow_null=True,
            context=self.context
        )
        sub_sectors_list = [sub_sector['related_sub_sector']
                            for sub_sector in serializer.data]
        return sub_sectors_list


class RelatedSectorPageSerializer(BasePageSerializer):

    title = serializers.CharField(
        max_length=255, source='heading')
    image = wagtail_fields.ImageRenditionField(
        'fill-640x360',
        source='hero_image')
    featured_description = serializers.CharField(max_length=255)


class RegionCardFieldSerializer(serializers.Serializer):
    region_card_image = wagtail_fields.ImageRenditionField('fill-640x360')
    region_card_title = serializers.CharField(max_length=255)
    region_card_summary = core_fields.MarkdownToHTMLField()


class HomesInEnglandCardFieldSerializer(serializers.Serializer):
    homes_in_england_card_image = wagtail_fields.ImageRenditionField(
        'fill-640x360'
    )
    homes_in_england_card_title = serializers.CharField(max_length=255)
    homes_in_england_card_pdf_document = core_fields.DocumentURLField()


class RelatedRegionSerializer(serializers.Serializer):
    related_region = serializers.SerializerMethodField()

    def get_related_region(self, obj):
        region = obj.related_region

        if not region:
            return []
        serializer = RelatedCapitalInvestPageSerializer(
            region.specific)
        return serializer.data


class RelatedSectorSerializer(serializers.Serializer):
    related_sector = serializers.SerializerMethodField()

    def get_related_sector(self, obj):
        sector = obj.related_sector

        if not sector:
            return []
        serializer = MinimalPageSerializer(
            sector.specific)
        return serializer.data


class RelatedSubSectorSerializer(serializers.Serializer):
    related_sub_sector = serializers.SerializerMethodField()

    def get_related_sub_sector(self, obj):
        sector = obj.related_sub_sector

        if not sector:
            return ''
        serializer = MinimalPageSerializer(
            sector.specific)
        return serializer.data['heading']


class BenefitsOfUkTextSerializer(serializers.Serializer):
    benefits_of_uk_text = core_fields.MarkdownToHTMLField()


class ReadyToTradeStorySerializer(serializers.Serializer):
    story = core_fields.MarkdownToHTMLField()


class RelatedOpportunitySerializer(serializers.Serializer):
    opportunities = serializers.SerializerMethodField()

    def get_opportunities(self, opportunity_pages):

        serializer = RelatedCapitalInvestOpportunityPageSerializer(
            opportunity_pages,
            many=True,
            allow_null=True,
            context=self.context
        )

        return serializer.data


class RelatedDitServicesPageSerializer(BasePageSerializer):
    hero_title = serializers.CharField()
    hero_image = wagtail_fields.ImageRenditionField('fill-640x360')
    teaser = core_fields.MarkdownToHTMLField()
    featured_description = serializers.CharField()


MODEL_TO_SERIALIZER_MAPPING = {
    InternationalArticlePage: RelatedArticlePageSerializer,
    InternationalCampaignPage: RelatedCampaignPageSerializer,
    CapitalInvestOpportunityPage:
    RelatedCapitalInvestOpportunityPageSerializer,
    AboutDitServicesPage: RelatedDitServicesPageSerializer,
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
            serializer_class = MODEL_TO_SERIALIZER_MAPPING[
                related_page.specific.__class__]
            serializer = serializer_class(related_page.specific)
            serialized.append(serializer.data)
        return serialized


class BaseInternationalSectorPageSerializer(PageWithRelatedPagesSerializer, HeroSerializer):

    heading = serializers.CharField(max_length=255)
    sub_heading = serializers.CharField()
    heading_teaser = serializers.CharField()
    featured_description = serializers.CharField()

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

    project_opportunities_title = serializers.CharField(max_length=255)
    related_opportunities_cta_text = serializers.CharField(max_length=255)
    related_opportunities_cta_link = serializers.CharField(max_length=255)

    related_opportunities = serializers.SerializerMethodField()

    def get_related_opportunities(self, instance):

        queryset = []
        all_opp_pages = CapitalInvestOpportunityPage.objects.live().public()

        for page in all_opp_pages:
            for related_sectors in page.related_sectors.all():
                if not related_sectors.related_sector:
                    continue
                elif related_sectors.related_sector.title == instance.title:
                    queryset.append(page)

        if not queryset:
            return []

        serializer = RelatedOpportunitySerializer(
            queryset,
            allow_null=True,
            context=self.context
        )
        return serializer.data['opportunities']


class InternationalSectorPageSerializer(
    BaseInternationalSectorPageSerializer,
    ChildPagesSerializerHelper
):
    child_sub_sectors = serializers.SerializerMethodField()
    child_articles = serializers.SerializerMethodField()

    def get_child_sub_sectors(self, obj):
        return self.get_child_pages_data_for(
            obj,
            InternationalSubSectorPage,
            MinimalPageSerializer
        )

    def get_child_articles(self, obj):
        return self.get_child_pages_data_for(
            obj,
            InternationalArticlePage,
            RelatedArticlePageSerializer
        )


class InternationalSubSectorPageSerializer(BaseInternationalSectorPageSerializer):
    pass


class InternationalArticlePageSerializer(PageWithRelatedPagesSerializer):
    type_of_article = serializers.CharField()

    display_title = serializers.CharField(source='article_title')
    article_title = serializers.CharField()
    article_teaser = serializers.CharField()
    article_subheading = serializers.CharField()

    article_image = wagtail_fields.ImageRenditionField('original')
    article_image_thumbnail = wagtail_fields.ImageRenditionField('fill-640x360', source='article_image')
    article_video = core_fields.VideoField()

    article_body_text = core_fields.MarkdownToHTMLField()

    cta_title = serializers.CharField()
    cta_teaser = serializers.CharField()
    cta_link_label = serializers.CharField()
    cta_link = serializers.CharField()

    tags = core_fields.TagsListField()


class InternationalHomePageSerializer(PageWithRelatedPagesSerializer, HeroSerializer):
    hero_title = serializers.CharField(max_length=255)
    hero_subtitle = serializers.CharField(max_length=255)
    hero_cta_text = serializers.CharField(max_length=255)
    hero_cta_link = serializers.CharField(max_length=255)

    brexit_banner_text = core_fields.MarkdownToHTMLField()

    # Old International Home Page fields
    invest_title = serializers.CharField(max_length=255)
    invest_content = core_fields.MarkdownToHTMLField()
    invest_image = wagtail_fields.ImageRenditionField(
        'fill-640x360'
    )

    how_dit_help_title = serializers.CharField(max_length=255)

    related_how_dit_help_pages = serializers.SerializerMethodField()

    def get_related_how_dit_help_pages(self, instance):
        serialized = []
        items = [
            instance.related_how_dit_help_page_one,
            instance.related_how_dit_help_page_two,
            instance.related_how_dit_help_page_three
        ]
        for related_page in items:
            if not related_page:
                continue
            serializer = RelatedDitServicesPageSerializer(related_page.specific)
            serialized.append(serializer.data)
        return serialized

    section_two_heading = serializers.CharField()
    section_two_teaser = serializers.CharField()
    section_two_subsections = serializers.SerializerMethodField()

    def get_page_type(self, instance):
        """
        Overrides BasePageSerializer.get_page_type() so that `page_type`
        is the same whether serialising an `InternationalHomePage` or
        `InternationalHomePageOld` instance. This will prevent front-ends
        from falling over while still requesting the old page.
        """
        return 'InternationalHomePage'

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

    # New International Home Page fields
    is_new_page_ready = serializers.BooleanField()

    ready_to_trade_stories = serializers.SerializerMethodField()

    benefits_of_uk_title = serializers.CharField(max_length=255)
    benefits_of_uk_intro = serializers.CharField()

    benefits_of_uk = serializers.SerializerMethodField()

    ready_for_brexit_title = serializers.CharField(max_length=255)
    ready_for_brexit_image = wagtail_fields.ImageRenditionField('fill-640x360')
    ready_for_brexit_cta_text = serializers.CharField(max_length=255)
    ready_for_brexit_cta_link = serializers.CharField(max_length=255)

    how_we_help_title = serializers.CharField(max_length=255)
    how_we_help_intro = serializers.CharField()

    how_we_help = serializers.SerializerMethodField()

    how_we_help_one_icon = wagtail_fields.ImageRenditionField('original')
    how_we_help_one_text = core_fields.MarkdownToHTMLField()
    how_we_help_two_icon = wagtail_fields.ImageRenditionField('original')
    how_we_help_two_text = core_fields.MarkdownToHTMLField()
    how_we_help_three_icon = wagtail_fields.ImageRenditionField('original')
    how_we_help_three_text = core_fields.MarkdownToHTMLField()

    ways_of_doing_business_title = serializers.CharField(max_length=255)
    related_page_expand = serializers.SerializerMethodField()
    related_page_expand_description = serializers.CharField()
    related_page_invest_capital = serializers.SerializerMethodField()
    related_page_invest_capital_description = serializers.CharField()
    related_page_buy = serializers.SerializerMethodField()
    related_page_buy_description = serializers.CharField()

    case_study_image = wagtail_fields.ImageRenditionField('original')
    case_study_title = serializers.CharField(max_length=255)
    case_study_text = core_fields.MarkdownToHTMLField()
    case_study_cta_text = serializers.CharField(max_length=255)
    case_study_cta_link = serializers.CharField(max_length=255)

    industries_section_title = serializers.CharField(max_length=255)
    industries_section_intro = serializers.CharField()
    all_sectors = serializers.SerializerMethodField()
    industries_section_industry_label = serializers.CharField(max_length=255)
    industries_section_cta_text = serializers.CharField(max_length=255)
    industries_section_cta_link = serializers.CharField(max_length=255)

    link_to_section_title = serializers.CharField(max_length=255)
    link_to_section_intro = serializers.CharField()

    link_to_section_links = serializers.SerializerMethodField()

    link_to_section_one = core_fields.MarkdownToHTMLField()
    link_to_section_one_cta_text = serializers.CharField(max_length=255)
    link_to_section_one_cta_link = serializers.CharField(max_length=255)
    link_to_section_two = core_fields.MarkdownToHTMLField()
    link_to_section_two_cta_text = serializers.CharField(max_length=255)
    link_to_section_two_cta_link = serializers.CharField(max_length=255)
    link_to_section_three = core_fields.MarkdownToHTMLField()
    link_to_section_three_cta_text = serializers.CharField(max_length=255)
    link_to_section_three_cta_link = serializers.CharField(max_length=255)

    def get_ready_to_trade_stories(self, instance):
        data = [
            ReadyToTradeStoryProxyDataWrapper(
                instance=instance,
                position=num,
            )
            for num in ['one', 'two', 'three']
        ]
        serializer = ReadyToTradeStorySerializer(data, many=True)
        return [story for story in serializer.data if story['story']]

    def get_benefits_of_uk(self, instance):
        data = [
            BenefitsOfUkProxyDataWrapper(
                instance=instance,
                position=num,
            )
            for num in ONE_TO_SIX_WORDS
        ]
        serializer = BenefitsOfUkTextSerializer(data, many=True)
        return [benefit for benefit in serializer.data if benefit['benefits_of_uk_text']]

    def get_how_we_help(self, instance):
        data = [
            HowWeHelpProxyDataWrapper(
                instance=instance,
                position_number=num,
            )
            for num in ['one', 'two', 'three']
        ]
        serializer = HowWeHelpMarkDownTextSerializer(data, many=True)
        return [how_we_help for how_we_help in serializer.data if how_we_help['icon'] and how_we_help['text']]

    def get_link_to_section_links(self, instance):
        data = [
            LinkToSectionLinksProxyDataWrapper(
                instance=instance,
                position=num,
            )
            for num in ['one', 'two', 'three']
        ]
        serializer = LinkToSectionLinksSerializer(data, many=True)
        return [link for link in serializer.data if link['text'] and link['cta_text'] and link['cta_link']]

    def get_all_sectors(self, instance):
        queryset = InternationalSectorPage.objects.live().public().all()
        serialized = RelatedSectorPageSerializer(
            queryset,
            many=True,
            allow_null=True,
            context=self.context
        ).data
        return [sector for sector in serialized if sector['title'] and sector['featured_description']]

    def get_related_page_expand(self, instance):
        serialized = []
        if not instance.related_page_expand:
            return serialized
        expand_page = RelatedInvestHomePageSerializer(instance.related_page_expand.specific).data
        if 'image' in expand_page and 'title' in expand_page and expand_page['image'] and expand_page['title']:
            serialized = expand_page
        return serialized

    def get_related_page_invest_capital(self, instance):
        serialized = []
        if not instance.related_page_invest_capital:
            return serialized
        invest_capital_page = RelatedCapitalInvestPageSerializer(instance.related_page_invest_capital.specific).data
        if 'image' in invest_capital_page and 'title' in invest_capital_page and invest_capital_page['image'] \
                and invest_capital_page['title']:
            serialized = invest_capital_page
        return serialized

    def get_related_page_buy(self, instance):
        serialized = []
        if not instance.related_page_buy:
            return serialized
        trade_page = RelatedTradeHomePageSerializer(instance.related_page_buy.specific).data
        if 'image' in trade_page and 'title' in trade_page and trade_page['image'] and trade_page['title']:
            serialized = trade_page
        return serialized


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


class InternationalArticleListingPageSerializer(BasePageSerializer, ChildPagesSerializerHelper, HeroSerializer):
    landing_page_title = serializers.CharField(max_length=255)
    display_title = serializers.CharField(source='landing_page_title')

    articles_count = serializers.IntegerField()
    list_teaser = core_fields.MarkdownToHTMLField(allow_null=True)
    hero_teaser = serializers.CharField(allow_null=True)
    child_pages = serializers.SerializerMethodField()

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


class InternationalTopicLandingPageSerializer(BasePageSerializer, ChildPagesSerializerHelper, HeroSerializer):
    landing_page_title = serializers.CharField(max_length=255)
    display_title = serializers.CharField(source='landing_page_title')
    hero_teaser = serializers.CharField(max_length=255)

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
            BaseInternationalSectorPageSerializer
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


class InternationalCuratedTopicLandingPageSerializer(BasePageSerializer, HeroSerializer):
    display_title = serializers.CharField()

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


class InternationalGuideLandingPageSerializer(BasePageSerializer, HeroSerializer):

    display_title = serializers.CharField()

    teaser = serializers.CharField()

    section_one_content = core_fields.MarkdownToHTMLField()
    section_one_image = wagtail_fields.ImageRenditionField('fill-640x360')
    section_one_image_caption = serializers.CharField()

    section_two_heading = serializers.CharField()
    section_two_teaser = serializers.CharField()
    section_two_button_text = serializers.CharField()
    section_two_button_url = serializers.CharField()
    section_two_image = wagtail_fields.ImageRenditionField('fill-640x360')

    guides_section_heading = serializers.CharField()
    guides = serializers.SerializerMethodField()

    section_three_title = serializers.CharField(max_length=255)
    section_three_text = serializers.CharField()
    section_three_cta_text = serializers.CharField(max_length=255)
    section_three_cta_link = serializers.CharField(max_length=255)

    def get_guides(self, obj):
        article_list = InternationalArticlePage.objects.child_of(obj).live().order_by('-first_published_at')
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


class InternationalCapitalInvestLandingPageSerializer(BasePageSerializer, HeroSerializer):

    breadcrumbs_label = serializers.CharField(max_length=255)
    hero_title = serializers.CharField(max_length=255)
    hero_subheading = serializers.CharField(max_length=255)
    hero_subtitle = serializers.CharField(max_length=255)
    hero_cta_text = serializers.CharField(max_length=255)

    reason_to_invest_section_title = serializers.CharField(max_length=255)
    reason_to_invest_section_intro = serializers.CharField(max_length=255)
    reason_to_invest_section_content = core_fields.MarkdownToHTMLField()
    reason_to_invest_section_image = wagtail_fields.ImageRenditionField(
        'fill-640x360')

    region_ops_section_title = serializers.CharField(max_length=255)
    region_ops_section_intro = serializers.CharField(max_length=255)

    banner_information = core_fields.MarkdownToHTMLField()

    energy_sector_title = serializers.CharField(max_length=255)
    energy_sector_content = core_fields.MarkdownToHTMLField()
    energy_sector_image = wagtail_fields.ImageRenditionField('fill-640x360')
    energy_sector_cta_text = serializers.CharField(max_length=255)
    energy_sector_pdf_document = core_fields.DocumentURLField()

    homes_in_england_section_title = serializers.CharField(max_length=255)

    how_we_help_title = serializers.CharField(max_length=255)
    how_we_help_intro = serializers.CharField(max_length=255)
    how_we_help_icon_and_text = serializers.SerializerMethodField()

    how_we_help_cta_text = serializers.CharField(max_length=255)
    how_we_help_cta_link = serializers.CharField(max_length=255)

    contact_section_title = serializers.CharField(max_length=255)
    contact_section_text = serializers.CharField(max_length=255)
    contact_section_cta_text = serializers.CharField(max_length=255)
    added_homes_in_england_card_fields = serializers.SerializerMethodField()
    added_region_card_fields = serializers.SerializerMethodField()
    added_regions = serializers.SerializerMethodField()

    def get_how_we_help_icon_and_text(self, instance):
        data = [
            HowWeHelpProxyDataWrapper(
                instance=instance,
                position_number=num
            )
            for num in ['one', 'two', 'three', 'four']
        ]
        serializer = HowWeHelpSerializer(data, many=True)
        return serializer.data

    def get_added_homes_in_england_card_fields(self, instance):
        serializer = HomesInEnglandCardFieldSerializer(
            instance.added_homes_in_england_card_fields.all(),
            many=True,
            allow_null=True,
            context=self.context
        )
        return serializer.data

    def get_added_region_card_fields(self, instance):
        serializer = RegionCardFieldSerializer(
            instance.added_region_card_fields.all(),
            many=True,
            allow_null=True,
            context=self.context
        )
        return serializer.data

    def get_added_regions(self, instance):
        serializer = RelatedRegionSerializer(
            instance.added_regions.all(),
            many=True,
            allow_null=True,
            context=self.context
        )
        return serializer.data


class CapitalInvestRegionPageSerializer(BasePageSerializer, HeroSerializer):

    hero_title = serializers.CharField(max_length=255)
    breadcrumbs_label = serializers.CharField(max_length=255)

    featured_description = serializers.CharField(max_length=255)

    region_summary_section_image = wagtail_fields.ImageRenditionField(
        'original')
    region_summary_section_intro = serializers.CharField(max_length=255)
    region_summary_section_content = core_fields.MarkdownToHTMLField(
        max_length=255
    )

    investment_opps_title = serializers.CharField(max_length=255)
    investment_opps_intro = serializers.CharField(max_length=255)
    economics_stats = serializers.SerializerMethodField()
    location_stats = serializers.SerializerMethodField()

    subsections_title = serializers.CharField(max_length=255)
    subsections = serializers.SerializerMethodField()

    property_and_infrastructure_section_title = serializers.CharField(
        max_length=255
    )
    property_and_infrastructure_section_image = \
        wagtail_fields.ImageRenditionField('original')
    property_and_infrastructure_section_content = \
        core_fields.MarkdownToHTMLField(max_length=255)

    case_study_image = wagtail_fields.ImageRenditionField('original')
    case_study_title = serializers.CharField(max_length=255)
    case_study_text = serializers.CharField(max_length=255)
    case_study_cta_text = serializers.CharField(max_length=255)

    case_study_cta_link = serializers.CharField(max_length=255)

    contact_title = serializers.CharField(max_length=255)
    contact_text = core_fields.MarkdownToHTMLField()
    contact_cta_link = serializers.CharField(max_length=255)
    contact_cta_text = serializers.CharField(max_length=255)

    def get_economics_stats(self, instance):
        data = [
            EconomicsStatisticProxyDataWrapper(
                instance=instance,
                position_number=num
            )
            for num in ['1', '2', '3', '4', '5', '6']
        ]
        serializer = EconomicStatSerializer(data, many=True)
        return serializer.data

    def get_location_stats(self, instance):
        data = [
            LocationStatisticProxyDataWrapper(
                instance=instance,
                position_number=num
            )
            for num in ['1', '2', '3', '4', '5', '6']
        ]
        serializer = LocationStatSerializer(data, many=True)
        return serializer.data

    def get_subsections(self, instance):
        data = [
            RegionSubsectionProxyDataWrapper(
                instance=instance,
                position_number=num
            )
            for num in ['one', 'two', 'three']
        ]
        serializer = RegionSubsectionSerializer(data, many=True)
        return serializer.data


class OpportunityListSerializer(BasePageSerializer, RelatedRegionSerializer):
    title = serializers.CharField(max_length=255, source='hero_title')
    hero_image = wagtail_fields.ImageRenditionField('fill-640x360')
    sector = serializers.CharField(max_length=255)
    scale = serializers.CharField(max_length=255)
    scale_value = serializers.DecimalField(max_digits=10, decimal_places=2)
    related_sectors = serializers.SerializerMethodField()

    def get_related_sectors(self, instance):
        serializer = RelatedSectorSerializer(
            instance.related_sectors.all(),
            many=True,
            allow_null=True,
            context=self.context
        )
        return serializer.data

    sub_sectors = serializers.SerializerMethodField()

    def get_sub_sectors(self, instance):
        serializer = RelatedSubSectorSerializer(
            instance.related_sub_sectors.all(),
            many=True,
            allow_null=True,
            context=self.context
        )
        sub_sectors_list = [sub_sector['related_sub_sector']
                            for sub_sector in serializer.data]
        return sub_sectors_list


class CapitalInvestOpportunityListingSerializer(BasePageSerializer):
    breadcrumbs_label = serializers.CharField(max_length=255)
    search_results_title = serializers.CharField(max_length=255)

    opportunity_list = serializers.SerializerMethodField()

    def get_opportunity_list(self, instance):

        queryset = CapitalInvestOpportunityPage.objects.live().public()

        if not queryset:
            return []

        serializer = OpportunityListSerializer(
            queryset,
            many=True,
            allow_null=True,
            context=self.context
        )
        return serializer.data

    sector_with_sub_sectors = serializers.SerializerMethodField()

    def get_sub_sector_headings(self, sector):
        return [sub_sector['heading'] for sub_sector
                in sector['child_sub_sectors']]

    def get_sector_with_sub_sectors(self, instance):

        all_sectors = InternationalSectorPage.objects.live().public()
        sectors = InternationalSectorPageSerializer(
            all_sectors,
            many=True,
            allow_null=True,
            context=self.context
        ).data

        return {sector['heading']: self.get_sub_sector_headings(sector)
                for sector in sectors}


class CapitalInvestOpportunityPageSerializer(
    RelatedRegionSerializer, SameSectorOpportunitiesHelper, BasePageSerializer, HeroSerializer
):

    breadcrumbs_label = serializers.CharField(max_length=255)
    hero_title = serializers.CharField(max_length=255)

    opportunity_summary_intro = serializers.CharField(max_length=255)
    opportunity_summary_content = core_fields.MarkdownToHTMLField(
        max_length=255
    )
    opportunity_summary_image = wagtail_fields.ImageRenditionField(
        'original')

    location_icon = wagtail_fields.ImageRenditionField(
        'original'
    )
    location = serializers.CharField(max_length=255)
    location_heading = serializers.CharField(max_length=255)

    project_promoter_icon = wagtail_fields.ImageRenditionField(
        'original'
    )
    project_promoter = serializers.CharField(max_length=255)
    project_promoter_heading = serializers.CharField(max_length=255)

    scale_icon = wagtail_fields.ImageRenditionField(
        'original'
    )
    scale = serializers.CharField(max_length=255)
    scale_heading = serializers.CharField(max_length=255)
    scale_value = serializers.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    sector_icon = wagtail_fields.ImageRenditionField(
        'original'
    )
    sector = serializers.CharField(max_length=255)
    sector_heading = serializers.CharField(max_length=255)

    investment_type_icon = wagtail_fields.ImageRenditionField(
        'original'
    )
    investment_type = serializers.CharField(max_length=255)
    investment_type_heading = serializers.CharField(max_length=255)

    planning_status_icon = wagtail_fields.ImageRenditionField(
        'original'
    )
    planning_status = serializers.CharField(max_length=255)
    planning_status_heading = serializers.CharField(max_length=255)

    project_background_title = serializers.CharField(max_length=255)
    project_background_intro = core_fields.MarkdownToHTMLField()
    project_description_title = serializers.CharField(max_length=255)
    project_description_content = core_fields.MarkdownToHTMLField()
    project_promoter_title = serializers.CharField(max_length=255)
    project_promoter_content = core_fields.MarkdownToHTMLField()
    project_image = wagtail_fields.ImageRenditionField(
        'original')

    case_study_image = wagtail_fields.ImageRenditionField('original')
    case_study_title = serializers.CharField(max_length=255)
    case_study_text = serializers.CharField(max_length=255)
    case_study_cta_text = serializers.CharField(max_length=255)
    case_study_cta_link = serializers.CharField(max_length=255)

    similar_projects_cta_text = serializers.CharField(max_length=255)
    similar_projects_cta_link = serializers.CharField(max_length=255)

    contact_title = serializers.CharField(max_length=255)
    contact_text = core_fields.MarkdownToHTMLField()

    related_sectors = serializers.SerializerMethodField()

    def get_related_sectors(self, instance):
        serializer = RelatedSectorSerializer(
            instance.related_sectors.all(),
            many=True,
            allow_null=True,
            context=self.context
        )
        return serializer.data

    sub_sectors = serializers.SerializerMethodField()

    def get_sub_sectors(self, instance):
        serializer = RelatedSubSectorSerializer(
            instance.related_sub_sectors.all(),
            many=True,
            allow_null=True,
            context=self.context
        )
        sub_sectors_list = [sub_sector['related_sub_sector']
                            for sub_sector in serializer.data]
        return sub_sectors_list

    related_sector_with_opportunities = serializers.SerializerMethodField()

    def get_related_sector_with_opportunities(self, instance):
        return self.get_same_sector_opportunity_pages_data_for(
            instance,
            RelatedCapitalInvestOpportunityPageSerializer,
            self.get_related_sectors(instance)
        )


class MinimalPageSerializer(BasePageSerializer):
    heading = serializers.CharField(max_length=255)


class MinimalPageWithHeroTitleSerializer(BasePageSerializer):
    hero_title = serializers.CharField(max_length=255)


# Invest seralizers

class SubsectionProxyDataWrapper:

    def __init__(self, instance, suffix):
        self.suffix = suffix
        self.instance = instance

    @property
    def title(self):
        return getattr(self.instance, f'subsection_title_{self.suffix}')

    @property
    def content(self):
        return getattr(self.instance, f'subsection_content_{self.suffix}')

    @property
    def map(self):
        return getattr(self.instance, f'subsection_map_{self.suffix}', None)


class SubsectionSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=255)
    content = core_fields.MarkdownToHTMLField()
    map = wagtail_fields.ImageRenditionField(
        'original',
        allow_null=True
    )


class RegionSubsectionSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=255)
    content = core_fields.MarkdownToHTMLField()
    icon = wagtail_fields.ImageRenditionField(
        'original',
        allow_null=True
    )


class FeaturedCardsDataWrapper:

    def __init__(self, instance, position_number):
        self.position_number = position_number
        self.instance = instance

    @property
    def image(self):
        return getattr(
            self.instance,
            f'featured_card_{self.position_number}_image'
        )

    @property
    def title(self):
        return getattr(
            self.instance,
            f'featured_card_{self.position_number}_title'
        )

    @property
    def summary(self):
        return getattr(
            self.instance,
            f'featured_card_{self.position_number}_summary'
        )

    @property
    def cta_link(self):
        return getattr(
            self.instance,
            f'featured_card_{self.position_number}_cta_link'
        )


class FeaturedCardsSerializer(serializers.Serializer):
    image = wagtail_fields.ImageRenditionField(
        'fill-640x360'
    )
    title = serializers.CharField(max_length=255)
    summary = core_fields.MarkdownToHTMLField(max_length=255)
    cta_link = serializers.CharField(max_length=255)


class FeaturedInternationalSectorPageSerializer(BasePageSerializer, HeroSerializer):
    heading = serializers.CharField(max_length=255)
    featured_description = serializers.CharField(max_length=255)


class InvestInternationalHomePageSerializer(BasePageSerializer, HeroSerializer):
    breadcrumbs_label = serializers.CharField(max_length=50)
    heading = serializers.CharField(max_length=255)
    sub_heading = serializers.CharField(max_length=255)
    hero_call_to_action_text = serializers.CharField(max_length=255)
    hero_call_to_action_url = serializers.CharField(max_length=255)
    teaser = serializers.CharField()
    benefits_section_title = serializers.CharField(max_length=255)
    benefits_section_intro = serializers.CharField(max_length=255)
    benefits_section_content = core_fields.MarkdownToHTMLField()
    benefits_section_cta_text = serializers.CharField(max_length=255)
    benefits_section_cta_url = serializers.CharField(max_length=255)
    benefits_section_img = wagtail_fields.ImageRenditionField('fill-640x360')
    eu_exit_section_title = serializers.CharField(max_length=255)
    eu_exit_section_content = core_fields.MarkdownToHTMLField()
    eu_exit_section_call_to_action_text = serializers.CharField(max_length=255)
    eu_exit_section_call_to_action_url = serializers.CharField(max_length=255)
    eu_exit_section_img = wagtail_fields.ImageRenditionField('original')
    sector_title = serializers.CharField(max_length=255)
    sector_intro = serializers.CharField(max_length=255)
    hpo_title = serializers.CharField(max_length=255)
    hpo_intro = serializers.CharField(max_length=255)
    sector_button_text = serializers.CharField(max_length=255)
    sector_button_url = serializers.CharField(max_length=255)
    how_we_help_title = serializers.CharField(max_length=255)
    how_we_help_lead_in = serializers.CharField(max_length=255)
    how_we_help = serializers.SerializerMethodField()
    how_we_help_cta_text = serializers.CharField(max_length=255)
    how_we_help_cta_link = serializers.CharField(max_length=255)
    contact_section_title = serializers.CharField(max_length=255)
    contact_section_content = serializers.CharField(max_length=255)
    contact_section_call_to_action_text = serializers.CharField(max_length=255)
    contact_section_call_to_action_url = serializers.CharField(max_length=255)
    sectors = serializers.SerializerMethodField()
    high_potential_opportunities = serializers.SerializerMethodField()
    guides = serializers.SerializerMethodField()

    how_to_expand_title = serializers.CharField(max_length=255)
    how_to_expand_image = wagtail_fields.ImageRenditionField('original')
    how_to_expand_intro = core_fields.MarkdownToHTMLField()
    how_to_expand = serializers.SerializerMethodField()

    isd_section_title = serializers.CharField(max_length=255)
    isd_section_text = core_fields.MarkdownToHTMLField()
    isd_section_cta_text = serializers.CharField(max_length=255)
    isd_section_cta_link = serializers.CharField(max_length=255)

    featured_cards = serializers.SerializerMethodField()

    def get_how_we_help(self, instance):
        data = [
            InvestHowWeHelpProxyDataWrapper(
                instance=instance, position_number=position_number
            )
            for position_number in ONE_TO_SIX_WORDS
        ]
        serializer = HowWeHelpSerializer(data, many=True)
        return serializer.data

    def get_sectors(self, instance):
        serialized = []
        items = [
            instance.featured_industry_one,
            instance.featured_industry_two,
            instance.featured_industry_three,
        ]
        for related_page in items:
            if not related_page:
                continue
            serialized.append(
                FeaturedInternationalSectorPageSerializer(related_page.specific).data)
        return serialized

    def get_high_potential_opportunities(self, instance):
        from .models.invest import InvestHighPotentialOpportunityDetailPage
        queryset = InvestHighPotentialOpportunityDetailPage.objects.all(
            ).filter(
            featured=True
        ).live().order_by('heading')
        serializer = InvestHighPotentialOpportunityDetailPageSerializer(
            queryset,
            many=True,
            allow_null=True,
            context=self.context
        )
        return serializer.data

    def get_guides(self, obj):
        article_list = (
               InternationalArticlePage.objects
               .child_of(obj)
               .live()
               .order_by('-first_published_at')
           )[:9]
        serializer = RelatedArticlePageSerializer(article_list, many=True)
        return serializer.data

    def get_featured_cards(self, instance):
        data = [
            FeaturedCardsDataWrapper(
                instance=instance,
                position_number=num
            )
            for num in ['one', 'two', 'three']
        ]
        serializer = FeaturedCardsSerializer(data, many=True)
        return serializer.data

    def get_how_to_expand(self, instance):
        data = [
            ExpandHowToExpandProxyDataWrapper(
                instance=instance, position_number=position_number
            )
            for position_number in ['one', 'two', 'three', 'four']
        ]
        serializer = HowToExpandSerializer(data, many=True)
        return serializer.data


class InvestHighPotentialOpportunityDetailPageBaseSerializer(BasePageSerializer, HeroSerializer):
    breadcrumbs_label = serializers.CharField(max_length=50)
    heading = serializers.CharField(max_length=255)
    description = serializers.CharField(max_length=255)
    featured = serializers.BooleanField()
    contact_proposition = core_fields.MarkdownToHTMLField()
    contact_button = serializers.CharField(max_length=500)
    proposition_one = core_fields.MarkdownToHTMLField()
    proposition_one_image = wagtail_fields.ImageRenditionField('original')
    proposition_one_image_alt = serializers.CharField()
    proposition_one_video = core_fields.VideoField()
    proposition_one_video_transcript = core_fields.MarkdownToHTMLField()
    opportunity_list_title = serializers.CharField()
    opportunity_list_item_one = core_fields.MarkdownToHTMLField()
    opportunity_list_item_two = core_fields.MarkdownToHTMLField()
    opportunity_list_item_three = core_fields.MarkdownToHTMLField()
    opportunity_list_image = wagtail_fields.ImageRenditionField('original')
    opportunity_list_image_alt = serializers.CharField()
    proposition_two = core_fields.MarkdownToHTMLField()
    proposition_two_list_item_one = core_fields.MarkdownToHTMLField()
    proposition_two_list_item_two = core_fields.MarkdownToHTMLField()
    proposition_two_list_item_three = core_fields.MarkdownToHTMLField()
    proposition_two_image = wagtail_fields.ImageRenditionField('original')
    proposition_two_image_alt = serializers.CharField()
    proposition_two_video = core_fields.VideoField()
    proposition_two_video_transcript = core_fields.MarkdownToHTMLField()
    competitive_advantages_title = serializers.CharField()
    competitive_advantages_list_item_one = core_fields.MarkdownToHTMLField()
    competitive_advantages_list_item_one_icon = wagtail_fields.ImageRenditionField('original')
    competitive_advantages_list_item_two = core_fields.MarkdownToHTMLField()
    competitive_advantages_list_item_two_icon = wagtail_fields.ImageRenditionField('original')
    competitive_advantages_list_item_three = core_fields.MarkdownToHTMLField()
    competitive_advantages_list_item_three_icon = wagtail_fields.ImageRenditionField('original')
    testimonial = core_fields.MarkdownToHTMLField()
    testimonial_background = wagtail_fields.ImageRenditionField('original')
    companies_list_text = core_fields.MarkdownToHTMLField()
    companies_list_item_image_one = wagtail_fields.ImageRenditionField('original')
    companies_list_item_image_alt_one = serializers.CharField()
    companies_list_item_image_two = wagtail_fields.ImageRenditionField('original')
    companies_list_item_image_alt_two = serializers.CharField()
    companies_list_item_image_three = wagtail_fields.ImageRenditionField('original')
    companies_list_item_image_alt_three = serializers.CharField()
    companies_list_item_image_four = wagtail_fields.ImageRenditionField('original')
    companies_list_item_image_alt_four = serializers.CharField()
    companies_list_item_image_five = wagtail_fields.ImageRenditionField('original')
    companies_list_item_image_alt_five = serializers.CharField()
    companies_list_item_image_six = wagtail_fields.ImageRenditionField('original')
    companies_list_item_image_alt_six = serializers.CharField()
    companies_list_item_image_seven = wagtail_fields.ImageRenditionField('original')
    companies_list_item_image_alt_seven = serializers.CharField()
    companies_list_item_image_eight = wagtail_fields.ImageRenditionField('original')
    companies_list_item_image_alt_eight = serializers.CharField()
    case_study_list_title = serializers.CharField()
    case_study_one_text = core_fields.MarkdownToHTMLField()
    case_study_one_image = wagtail_fields.ImageRenditionField('original')
    case_study_one_image_alt = serializers.CharField()
    case_study_two_text = core_fields.MarkdownToHTMLField()
    case_study_two_image = wagtail_fields.ImageRenditionField('original')
    case_study_two_image_alt = serializers.CharField()
    case_study_three_text = core_fields.MarkdownToHTMLField()
    case_study_three_image = wagtail_fields.ImageRenditionField('original')
    case_study_three_image_alt = serializers.CharField()
    case_study_four_text = core_fields.MarkdownToHTMLField()
    case_study_four_image = wagtail_fields.ImageRenditionField('original')
    case_study_four_image_alt = serializers.CharField()
    other_opportunities_title = serializers.CharField()
    pdf_document = core_fields.DocumentURLField()
    summary_image = wagtail_fields.ImageRenditionField('original')


class InvestHighPotentialOpportunityDetailPageSerializer(InvestHighPotentialOpportunityDetailPageBaseSerializer):
    other_opportunities = serializers.SerializerMethodField()

    def get_other_opportunities(self, instance):
        queryset = (
            InvestHighPotentialOpportunityDetailPage.objects.all()
            .live()
            .order_by('heading')
            .exclude(slug=instance.slug)
        )
        serializer = InvestHighPotentialOpportunityDetailPageBaseSerializer(
            queryset,
            many=True,
            allow_null=True,
            context=self.context
        )
        return serializer.data


class InvestHighPotentialOpportunityListItemSerializer(BasePageSerializer):
    pdf_document = core_fields.DocumentURLField()
    heading = serializers.CharField(max_length=255)


class InvestHighPotentialOpportunityFormPageSerializer(
    BasePageSerializer,
    metaclass=FormPageSerializerMetaclass
):

    class Meta:
        model_class = InvestHighPotentialOpportunityFormPage

    heading = serializers.CharField(max_length=255)
    sub_heading = serializers.CharField(max_length=255)
    breadcrumbs_label = serializers.CharField(max_length=50)
    opportunity_list = serializers.SerializerMethodField()

    def get_opportunity_list(self, instance):
        queryset = (
            InvestHighPotentialOpportunityDetailPage.objects.all()
            .live()
            .order_by('heading')
            .exclude(slug=instance.slug)
        )
        serializer = InvestHighPotentialOpportunityListItemSerializer(
            queryset,
            many=True,
            allow_null=True,
            context=self.context
        )
        return serializer.data


class InvestHighPotentialOpportunityFormSuccessPageSerializer(
    BasePageSerializer
):
    breadcrumbs_label = serializers.CharField(max_length=50)
    heading = serializers.CharField()
    sub_heading = serializers.CharField()
    next_steps_title = serializers.CharField()
    next_steps_body = serializers.CharField()
    documents_title = serializers.CharField()
    documents_body = serializers.CharField()

    opportunity_list = serializers.SerializerMethodField()

    def get_opportunity_list(self, instance):
        queryset = (
            InvestHighPotentialOpportunityDetailPage.objects.all()
            .live()
            .order_by('heading')
            .exclude(slug=instance.slug)
        )
        serializer = InvestHighPotentialOpportunityDetailPageSerializer(
            queryset,
            many=True,
            allow_null=True,
            context=self.context
        )
        return serializer.data


class PulloutSerializer(serializers.Serializer):
    text = core_fields.MarkdownToHTMLField()
    stat = serializers.CharField(allow_null=True)
    stat_text = serializers.CharField(allow_null=True)


class InvestRegionPageSerializer(BasePageSerializer, ChildPagesSerializerHelper, HeroSerializer):
    featured = serializers.BooleanField()
    description = serializers.CharField()
    heading = serializers.CharField(max_length=255)
    pullout = serializers.SerializerMethodField()
    subsections = serializers.SerializerMethodField()

    def get_pullout(self, instance):
        return PulloutSerializer(
            {
                'text': instance.pullout_text,
                'stat': instance.pullout_stat,
                'stat_text': instance.pullout_stat_text
            }
        ).data

    def get_subsections(self, instance):
        data = [
            SubsectionProxyDataWrapper(instance=instance, suffix=num)
            for num in ONE_TO_SEVEN_WORDS
        ]
        serializer = SubsectionSerializer(data, many=True)
        return serializer.data


class InvestRegionLandingPageSerializer(
    BasePageSerializer, ChildPagesSerializerHelper, HeroSerializer
):
    heading = serializers.CharField(max_length=255)
    regions = serializers.SerializerMethodField()

    def get_regions(self, instance):
        return self.get_child_pages_data_for(
            instance,
            InvestRegionPage,
            InvestRegionPageSerializer
        )


# FAS serializers

class InternationalTradeHomePageSerializer(BasePageSerializer):
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
    how_we_help_cta_text = serializers.CharField(max_length=255)
    how_we_help_cta_link = serializers.CharField(max_length=255)
    industries = serializers.SerializerMethodField()

    def get_industries(self, instance):
        queryset = InternationalSectorPage.objects.filter(
            live=True
        ).order_by('slug')[:3]
        serializer = BaseInternationalSectorPageSerializer(
            queryset,
            many=True,
            allow_null=True,
            context=self.context
        )
        return serializer.data


class InternationalTradeIndustryContactPageSerializer(BasePageSerializer):
    breadcrumbs_label = serializers.CharField()
    breadcrumbs = core_fields.BreadcrumbsField(service_name=cms.FIND_A_SUPPLIER)
    introduction_text = core_fields.MarkdownToHTMLField()
    submit_button_text = serializers.CharField()
    success_message_text = core_fields.MarkdownToHTMLField()
    success_back_link_text = serializers.CharField()


class AboutDitLandingPageSerializer(PageWithRelatedPagesSerializer, BasePageSerializer, HeroSerializer):
    breadcrumbs_label = serializers.CharField()
    hero_title = serializers.CharField()

    intro = serializers.CharField()
    section_one_content = core_fields.MarkdownToHTMLField()
    section_one_image = wagtail_fields.ImageRenditionField('fill-640x360')

    how_dit_help_title = serializers.CharField(max_length=255)

    case_study_image = wagtail_fields.ImageRenditionField('original')
    case_study_title = serializers.CharField(max_length=255)
    case_study_text = serializers.CharField(max_length=255)
    case_study_cta_text = serializers.CharField(max_length=255)
    case_study_cta_link = serializers.CharField(max_length=255)


class AboutDitServiceFieldSerializer(serializers.Serializer):
    icon = wagtail_fields.ImageRenditionField(
        'original'
    )
    title = serializers.CharField()
    summary = serializers.CharField()
    link_text = serializers.CharField()
    link_url = serializers.CharField()


class AboutDitServicesPageSerializer(BasePageSerializer, HeroSerializer):
    breadcrumbs_label = serializers.CharField()
    hero_title = serializers.CharField()
    featured_description = serializers.CharField()
    teaser = core_fields.MarkdownToHTMLField()
    ebook_section_image = wagtail_fields.ImageRenditionField('fill-299x423')
    ebook_section_image_alt_text = serializers.CharField()
    ebook_section_body = core_fields.MarkdownToHTMLField()
    ebook_section_cta_text = serializers.CharField()
    ebook_section_cta_link = serializers.CharField()
    case_study_image = wagtail_fields.ImageRenditionField('original')
    case_study_title = serializers.CharField()
    case_study_text = serializers.CharField()
    case_study_cta_text = serializers.CharField()
    case_study_cta_link = serializers.CharField()
    contact_us_section_title = serializers.CharField()
    contact_us_section_summary = core_fields.MarkdownToHTMLField()
    contact_us_section_cta_text = serializers.CharField()
    contact_us_section_cta_link = serializers.CharField()
    about_dit_services_fields = serializers.SerializerMethodField()

    def get_about_dit_services_fields(self, instance):
        serializer = AboutDitServiceFieldSerializer(
            instance.about_dit_services_fields.all(),
            many=True,
            allow_null=True,
            context=self.context
        )
        return serializer.data


def get_mapped_regions(instance):
    data = [
        AboutUkRegionsProxyDataWrapper(
            instance=instance,
            region_title=region
        )
        for region in REGIONS
    ]
    serializer = AboutUkRegionSerializer(data, many=True)
    return serializer.data


class AboutUkLandingPageSerializer(BasePageSerializer, HeroSerializer):
    breadcrumbs_label = serializers.CharField()
    hero_title = serializers.CharField()

    intro = core_fields.MarkdownToHTMLField()

    why_choose_uk_title = serializers.CharField()
    why_choose_uk_content = core_fields.MarkdownToHTMLField()
    why_choose_uk_image = wagtail_fields.ImageRenditionField('fill-640x360')
    why_choose_uk_cta_text = serializers.CharField()
    why_choose_uk_cta_link = serializers.CharField()

    industries_section_title = serializers.CharField()
    industries_section_intro = core_fields.MarkdownToHTMLField()
    industries_section_cta_text = serializers.CharField()
    industries_section_cta_link = serializers.CharField()

    regions_section_title = serializers.CharField()
    regions_section_intro = core_fields.MarkdownToHTMLField()
    regions_section_cta_text = serializers.CharField()
    regions_section_cta_link = serializers.CharField()

    how_we_help_title = serializers.CharField()
    how_we_help_intro = core_fields.MarkdownToHTMLField()

    how_we_help = serializers.SerializerMethodField()

    def get_how_we_help(self, instance):
        data = [
            HowWeHelpWithTitleProxyDataWrapper(
                instance=instance,
                position_number=num
            )
            for num in ['one', 'two', 'three', 'four', 'five', 'six']
        ]
        serializer = HowWeHelpWithTitleSerializer(data, many=True)
        return serializer.data

    how_we_help_cta_text = serializers.CharField()
    how_we_help_cta_link = serializers.CharField()

    ebook_section_image = wagtail_fields.ImageRenditionField('fill-299x423')
    ebook_section_image_alt_text = serializers.CharField()
    ebook_section_title = serializers.CharField()
    ebook_section_body = core_fields.MarkdownToHTMLField()
    ebook_section_cta_text = serializers.CharField()
    ebook_section_cta_link = core_fields.DocumentURLField()

    contact_title = serializers.CharField()
    contact_text = core_fields.MarkdownToHTMLField()
    contact_cta_text = serializers.CharField()
    contact_cta_link = serializers.CharField()

    all_sectors = serializers.SerializerMethodField()

    def get_all_sectors(self, instance):
        queryset = InternationalSectorPage.objects.live().public().all()
        serialized = InternationalSectorPageSerializer(
            queryset,
            many=True,
            allow_null=True,
            context=self.context
        ).data
        return serialized

    regions = serializers.SerializerMethodField()

    def get_regions(self, instance):
        return get_mapped_regions(instance)


class AboutUkRegionListingPageSerializer(BasePageSerializer, HeroSerializer):
    breadcrumbs_label = serializers.CharField()
    hero_title = serializers.CharField()

    intro = core_fields.MarkdownToHTMLField()

    contact_title = serializers.CharField()
    contact_text = core_fields.MarkdownToHTMLField()
    contact_cta_text = serializers.CharField()
    contact_cta_link = serializers.CharField()

    mapped_regions = serializers.SerializerMethodField()

    def get_mapped_regions(self, instance):
        queryset = AboutUkLandingPage.objects.live().public().first()

        if not queryset:
            return []

        return get_mapped_regions(queryset)


class AboutUkRegionPageSerializer(BasePageSerializer, HeroSerializer):

    hero_title = serializers.CharField(max_length=255)
    breadcrumbs_label = serializers.CharField(max_length=255)

    featured_description = serializers.CharField(max_length=255)

    region_summary_section_image = wagtail_fields.ImageRenditionField(
        'original')
    region_summary_section_intro = serializers.CharField(max_length=255)
    region_summary_section_content = core_fields.MarkdownToHTMLField(
        max_length=255
    )

    investment_opps_title = serializers.CharField(max_length=255)
    investment_opps_intro = serializers.CharField(max_length=255)
    economics_stats = serializers.SerializerMethodField()
    location_stats = serializers.SerializerMethodField()

    subsections_title = serializers.CharField(max_length=255)
    subsections = serializers.SerializerMethodField()

    property_and_infrastructure_section_title = serializers.CharField(
        max_length=255
    )
    property_and_infrastructure_section_image = \
        wagtail_fields.ImageRenditionField('original')
    property_and_infrastructure_section_content = \
        core_fields.MarkdownToHTMLField(max_length=255)

    case_study_image = wagtail_fields.ImageRenditionField('original')
    case_study_title = serializers.CharField(max_length=255)
    case_study_text = serializers.CharField(max_length=255)
    case_study_cta_text = serializers.CharField(max_length=255)

    case_study_cta_link = serializers.CharField(max_length=255)

    contact_title = serializers.CharField(max_length=255)
    contact_text = core_fields.MarkdownToHTMLField()
    contact_cta_link = serializers.CharField(max_length=255)
    contact_cta_text = serializers.CharField(max_length=255)

    mapped_regions = serializers.SerializerMethodField()

    def get_economics_stats(self, instance):
        data = [
            EconomicsStatisticProxyDataWrapper(
                instance=instance,
                position_number=num
            )
            for num in ['1', '2', '3', '4', '5', '6']
        ]
        serializer = EconomicStatSerializer(data, many=True)
        return serializer.data

    def get_location_stats(self, instance):
        data = [
            LocationStatisticProxyDataWrapper(
                instance=instance,
                position_number=num
            )
            for num in ['1', '2', '3', '4', '5', '6']
        ]
        serializer = LocationStatSerializer(data, many=True)
        return serializer.data

    def get_subsections(self, instance):
        data = [
            RegionSubsectionProxyDataWrapper(
                instance=instance,
                position_number=num
            )
            for num in ['one', 'two', 'three']
        ]
        serializer = RegionSubsectionSerializer(data, many=True)
        return serializer.data

    def get_mapped_regions(self, instance):
        queryset = AboutUkLandingPage.objects.live().public().first()

        if not queryset:
            return []

        return get_mapped_regions(queryset)


class AboutUkArticlesFieldSerializer(serializers.Serializer):
    image = wagtail_fields.ImageRenditionField(
        'fill-640x360'
    )
    title = serializers.CharField()
    summary = core_fields.MarkdownToHTMLField()
    link_text = serializers.CharField()
    link_url = serializers.CharField()


class AboutUkWhyChooseTheUkPageSerializer(PageWithRelatedPagesSerializer, BasePageSerializer, HeroSerializer):
    breadcrumbs_label = serializers.CharField()
    hero_title = serializers.CharField()

    teaser = core_fields.MarkdownToHTMLField()

    primary_contact_cta_text = serializers.CharField(max_length=255)
    primary_contact_cta_link = serializers.CharField(max_length=255)

    section_one_body = core_fields.MarkdownToHTMLField()
    section_one_image = wagtail_fields.ImageRenditionField('fill-640x360')
    section_one_video = core_fields.VideoField()

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

    about_uk_articles_fields = serializers.SerializerMethodField()

    def get_about_uk_articles_fields(self, instance):
        serializer = AboutUkArticlesFieldSerializer(
            instance.about_uk_articles_fields.all(),
            many=True,
            allow_null=True,
            context=self.context
        )
        return serializer.data

    ebook_section_image = wagtail_fields.ImageRenditionField('fill-299x423')
    ebook_section_image_alt_text = serializers.CharField()
    ebook_section_title = serializers.CharField()
    ebook_section_body = core_fields.MarkdownToHTMLField()
    ebook_section_cta_text = serializers.CharField()
    ebook_section_cta_link = serializers.CharField()

    how_dit_help_title = serializers.CharField(max_length=255)

    contact_us_section_title = serializers.CharField()
    contact_us_section_summary = core_fields.MarkdownToHTMLField()
    contact_us_section_cta_text = serializers.CharField()
    contact_us_section_cta_link = serializers.CharField()


class CapitalInvestContactFormPageSerializer(BasePageSerializer):
    breadcrumbs_label = serializers.CharField()
    heading = serializers.CharField()
    intro = core_fields.MarkdownToHTMLField()
    comment = serializers.CharField()
    cta_text = serializers.CharField()


class CapitalInvestContactFormSuccessPageSerializer(BasePageSerializer):
    message_box_heading = serializers.CharField()
    message_box_description = core_fields.MarkdownToHTMLField()
    what_happens_next_description = core_fields.MarkdownToHTMLField()
