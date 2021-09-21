import random

from django.conf import settings
from directory_constants import cms
from rest_framework import serializers
from wagtail.api.v2.serializers import StreamField as StreamFieldSerializer
from wagtail.images.api import fields as wagtail_fields

from core import fields as core_fields
from core.helpers import num2words_list
from core.serializers import BasePageSerializer, ChildPagesSerializerHelper, FormPageSerializerMetaclass, HeroSerializer

from .models.capital_invest import CapitalInvestOpportunityPage
from .models.great_international import (
    AboutDitServicesPage,
    AboutUkLandingPage,
    InternationalArticleListingPage,
    InternationalArticlePage,
    InternationalCampaignPage,
    InternationalEUExitFormPage,
    InternationalGuideLandingPage,
    InternationalInvestmentSectorPage,
    InternationalInvestmentSubSectorPage,
    InternationalSectorPage,
    InternationalSubSectorPage,
    WhyInvestInTheUKPage,
    InternationalTopicLandingPage,
    AboutUkRegionPage,
    AboutUkRegionListingPage,
)
from .models.invest import (
    InvestHighPotentialOpportunityDetailPage,
    InvestRegionPage,
)
from .models.investment_atlas import (
    ForeignDirectInvestmentFormPage,
    InvestmentOpportunityPage,
    InvestmentGeneralContentPage,
    InvestmentOpportunityListingPage,
)


REGIONS = [
    "scotland",
    "northern_ireland",
    "north_england",
    "wales",
    "midlands",
    "south_england",
]


class EntitySummarySerializerBase(serializers.Serializer):
    """Base class for nested entities that don't need full page representations"""

    id = serializers.IntegerField()

    full_url = serializers.CharField(max_length=255)
    full_path = serializers.CharField(max_length=255, source="specific.full_path")
    last_published_at = serializers.DateTimeField()

    title = serializers.CharField()
    page_type = serializers.SerializerMethodField()

    def get_page_type(self, instance):
        return instance.__class__.__name__


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
    url = serializers.CharField(max_length=255)


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
            serializer = MinimalPageWithHeroTitleAndHeroImageSerializer(region.specific)

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


class RelatedWhyInvestInTheUKPageSerializer(BasePageSerializer):
    title = serializers.CharField()
    hero_image = wagtail_fields.ImageRenditionField('fill-640x360')
    featured_description = serializers.CharField(source='strapline')


class RelatedInternationalTopicLandingPageSerializer(BasePageSerializer):
    title = serializers.CharField(source='landing_page_title')
    hero_image = wagtail_fields.ImageRenditionField('fill-640x360')
    featured_description = serializers.CharField(source='hero_teaser')


class RelatedAboutUkRegionPageSerializer(BasePageSerializer):
    title = serializers.CharField(source='hero_title')
    hero_image = wagtail_fields.ImageRenditionField('fill-640x360')
    featured_description = serializers.CharField()


class RelatedInvestmentOpportunityPageSerializer(BasePageSerializer):
    title = serializers.CharField()
    hero_image = wagtail_fields.ImageRenditionField('fill-640x360')
    featured_description = serializers.CharField(source='strapline')


class RelatedInvestmentGeneralContentPageSerializer(BasePageSerializer):
    title = serializers.CharField()
    hero_image = wagtail_fields.ImageRenditionField('fill-640x360')
    featured_description = serializers.CharField(source='strapline')


class RelatedAboutUkRegionListingPageSerializer(BasePageSerializer):
    title = serializers.CharField()
    hero_image = wagtail_fields.ImageRenditionField('fill-640x360')
    featured_description = serializers.CharField(source='hero_title')


class RelatedInvestmentOpportunityListingPageSerializer(BasePageSerializer):
    title = serializers.CharField()
    featured_description = serializers.CharField(source='hero_text')


MODEL_TO_SERIALIZER_MAPPING = {
    InternationalArticlePage: RelatedArticlePageSerializer,
    InternationalCampaignPage: RelatedCampaignPageSerializer,
    CapitalInvestOpportunityPage: RelatedCapitalInvestOpportunityPageSerializer,
    AboutDitServicesPage: RelatedDitServicesPageSerializer,
    WhyInvestInTheUKPage: RelatedWhyInvestInTheUKPageSerializer,
    InternationalTopicLandingPage: RelatedInternationalTopicLandingPageSerializer,
    AboutUkRegionPage: RelatedAboutUkRegionPageSerializer,
    InvestmentOpportunityPage: RelatedInvestmentOpportunityPageSerializer,
    InvestmentGeneralContentPage: RelatedInvestmentGeneralContentPageSerializer,
    AboutUkRegionListingPage: RelatedAboutUkRegionListingPageSerializer,
    InvestmentOpportunityListingPage: RelatedInvestmentOpportunityListingPageSerializer,
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
    # DEPRECATED

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
            for num in num2words_list(3)
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
            for num in num2words_list(2)
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
    # DEPRECATED - see InternationalInvestmentSectorPageSerializer instead

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


class InternationalHomePageSerializer(BasePageSerializer):
    # Note that this is massively cut down from the original version,
    # but that the older fields still exist on the model (see the comment there)

    hero_title = serializers.CharField(max_length=255)
    homepage_link_panels = StreamFieldSerializer()

    # For now the hero_image and CSS colour for the page background will
    # be hard-coded, but we can make it editable via the CMS and expose them here
    # as API data when we need to.


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


class InternationalTopicLandingPageSerializer(
    PageWithRelatedPagesSerializer,
    ChildPagesSerializerHelper,
    HeroSerializer
):
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
            InternationalInvestmentSectorPage,  # NB this is the new Sector page, not the old one
            InternationalInvestmentSectorPageSerializer
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
    hero_cta_link = serializers.CharField(max_length=255)

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
            for num in num2words_list(4)
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
            for num in num2words_list(3)
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
    # Deprecated
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
    RelatedRegionSerializer, BasePageSerializer, HeroSerializer
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

    related_opportunities = serializers.SerializerMethodField()

    def get_related_opportunities(self, instance):
        related_sectors_ids = instance.related_sectors.values_list('related_sector_id', flat=True)

        if not related_sectors_ids:
            return []

        random_sector_id = random.choice(related_sectors_ids)

        related_opps_ids = CapitalInvestOpportunityPage.objects.filter(
            related_sectors__related_sector_id=random_sector_id
        ).exclude(id=instance.id).values_list('pk', flat=True)

        if not related_opps_ids:
            return []

        elif len(related_opps_ids) > 3:
            random_ids = random.sample(list(related_opps_ids), 3)

        else:
            random_ids = related_opps_ids

        related_opps = []

        for id in random_ids:
            related_opps.append(CapitalInvestOpportunityPage.objects.get(pk=id))

        serializer = RelatedCapitalInvestOpportunityPageSerializer(
            related_opps,
            many=True,
            allow_null=True,
            context=self.context
        )
        return serializer.data


class MinimalPageSerializer(BasePageSerializer):
    heading = serializers.CharField(max_length=255)


class MinimalPageWithHeroTitleAndHeroImageSerializer(BasePageSerializer):
    hero_title = serializers.CharField(max_length=255)
    hero_image_thumbnail = wagtail_fields.ImageRenditionField(
        'fill-640x360',
        allow_null=True,
        source='hero_image'
    )


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
            for position_number in num2words_list(6)
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
            for num in num2words_list(3)
        ]
        serializer = FeaturedCardsSerializer(data, many=True)
        return serializer.data

    def get_how_to_expand(self, instance):
        data = [
            ExpandHowToExpandProxyDataWrapper(
                instance=instance, position_number=position_number
            )
            for position_number in num2words_list(4)
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


class InvestmentOpportunityForFormPageSerializer(BasePageSerializer):

    heading = serializers.CharField(
        max_length=255,
        source='title',  # Remapping to keep with what GIUI is currently expecting
    )

    # In the future, if we revert to sending PDF attachments, we will need to
    # re-include a `pdf_document` field in this serializer, with a value of
    # the url to the relevant PDF doc from the Documents library.
    # Great-international-ui then has a view and a template which
    # specifically use this document value to send links to
    # the files, as well as show them on the success page.

    # Also, we may need to add in extra details such as the `opportunity_summary`
    # field to be displayed alongside any PDF links


class ForeignDirectInvestmentFormPageSerializer(
    BasePageSerializer,
    metaclass=FormPageSerializerMetaclass
):

    class Meta:
        model_class = ForeignDirectInvestmentFormPage

    heading = serializers.CharField(max_length=255)
    sub_heading = serializers.CharField(max_length=255)
    breadcrumbs_label = serializers.CharField(max_length=50)
    opportunity_list = serializers.SerializerMethodField()

    def get_opportunity_list(self, instance):

        queryset = (
            InvestmentOpportunityPage.objects.filter(
                investment_type__name=settings.FOREIGN_DIRECT_INVESTMENT_SNIPPET_LABEL
            )
            .live()
            .order_by('title')
        )
        # In the future, we might need to use a more fully-specced serializer, if
        # we also need to show more info about the Opporutnity as well as a download
        # link - see serializer comments
        serializer = InvestmentOpportunityForFormPageSerializer(
            queryset,
            many=True,
            allow_null=True,
            context=self.context
        )
        return serializer.data


class ForeignDirectInvestmentFormSuccessPageSerializer(
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
            InvestmentOpportunityPage.objects.filter(
                investment_type__name=settings.FOREIGN_DIRECT_INVESTMENT_SNIPPET_LABEL
            )
            .live()
            .order_by('title')
        )
        # In the future, we might need to use a more fully-specced serializer, if
        # we also need to show more info about the Opporutnity as well as a download
        # link - see serializer comments
        serializer = InvestmentOpportunityForFormPageSerializer(
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
            for num in num2words_list(7)
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
        queryset = InternationalInvestmentSectorPage.objects.filter(
            live=True
        ).order_by('slug')[:3]
        serializer = InternationalInvestmentSectorPageSerializer(
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
            for num in num2words_list(6)
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
        queryset = InternationalInvestmentSectorPage.objects.live().public().all()
        serialized = InternationalInvestmentSectorPageSerializer(
            queryset,
            many=True,
            allow_null=True,
            context=self.context
        ).data
        return serialized

    regions = serializers.SerializerMethodField()

    def get_regions(self, instance):
        return get_mapped_regions(instance)


class AboutUkRegionListingPageSerializer(PageWithRelatedPagesSerializer, HeroSerializer):
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
    region_summary_section_strapline = serializers.CharField(max_length=255)
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
    property_and_infrastructure_section_image = wagtail_fields.ImageRenditionField('original')
    property_and_infrastructure_section_content = core_fields.MarkdownToHTMLField(max_length=255)

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

    related_opportunities = serializers.SerializerMethodField()

    def get_related_opportunities(self, instance):
        # Return up to three investment_atlas.InvestmentOpportunties,
        # related by Region, ordered by their weighting and then pk
        # as a tie-breaker, so newer ones come first if weighting is
        # the same

        relevant_regions = instance.investmentopportunitypage_set.order_by(
            '-priority_weighting', '-pk'
        )
        data = relevant_regions[:3]
        serializer = RelatedInvestmentOpportunityPageSerializer(
            data,
            many=True,
        )
        return serializer.data

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
            for num in num2words_list(3)
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


class RegionPageSummarySerializer(EntitySummarySerializerBase, HeroSerializer):
    """Shorter version of AboutUkRegionPageSerializer for nesting content
    in InvestmentOpportunityPageSerializer results

    Note that HeroSerializer gives us a number hero image options
    """

    IMAGE_RENDITION_SPEC = "fill-640x360"

    hero_title = serializers.CharField(max_length=255)
    featured_description = serializers.CharField(max_length=255)

    region_summary_section_image = wagtail_fields.ImageRenditionField(
        IMAGE_RENDITION_SPEC
    )
    region_summary_section_intro = serializers.CharField(max_length=255)
    region_summary_section_content = core_fields.MarkdownToHTMLField(max_length=255)


class SectorSummarySerializer(EntitySummarySerializerBase):

    IMAGE_RENDITION_SPEC = "fill-960x540"

    title = serializers.CharField(max_length=255, source="heading")
    image = wagtail_fields.ImageRenditionField(
        IMAGE_RENDITION_SPEC, source="hero_image"
    )
    featured_description = serializers.CharField(max_length=255)


class InvestmentAtlasLandingPageSerializer(BasePageSerializer):
    IMAGE_RENDITION_SPEC = "original"
    MOBILE_IMAGE_RENDITION_SPEC = "original"

    breadcrumbs_label = serializers.CharField()
    hero_image = wagtail_fields.ImageRenditionField(
        IMAGE_RENDITION_SPEC
    )
    mobile_hero_image = wagtail_fields.ImageRenditionField(
        MOBILE_IMAGE_RENDITION_SPEC,
    )
    hero_strapline = serializers.CharField()
    downpage_sections = StreamFieldSerializer()


class InvestmentOpportunitySummarySerializer(EntitySummarySerializerBase):

    IMAGE_RENDITION_SPEC = "fill-960x540"

    title = serializers.CharField(max_length=255, source="heading")
    image = wagtail_fields.ImageRenditionField(
        IMAGE_RENDITION_SPEC, source="featured_image_1"
    )
    featured_description = serializers.CharField(
        max_length=255, source="executive_summary"
    )


class InvestmentOpportunityPageSerializer(BasePageSerializer):

    IMAGE_RENDITION_SPEC = "fill-960x540"
    AVATAR_RENDITION_SPEC = "fill-500x500"
    HERO_IMAGE_RENDITION_SPEC = "original"

    # Intro/summary
    # title is automatic, from BasePageSerializer
    breadcrumbs_label = serializers.CharField()
    strapline = serializers.CharField()
    introduction = core_fields.MarkdownToHTMLField()
    hero_image = wagtail_fields.ImageRenditionField(
        HERO_IMAGE_RENDITION_SPEC,
    )
    intro_image = wagtail_fields.ImageRenditionField(
        IMAGE_RENDITION_SPEC,
    )

    # Key facts
    location = serializers.CharField()
    location_coords = serializers.CharField()

    promoter = serializers.CharField()
    scale = serializers.CharField()
    scale_value = serializers.CharField()
    planning_status = serializers.SerializerMethodField()
    investment_type = serializers.CharField()
    time_to_investment_decision = serializers.SerializerMethodField()

    # Main opportunity content
    main_content = StreamFieldSerializer()

    important_links = core_fields.MarkdownToHTMLField()

    contact_name = serializers.CharField()
    contact_job_title = serializers.CharField()
    contact_link = serializers.CharField()
    contact_avatar = wagtail_fields.ImageRenditionField(
        AVATAR_RENDITION_SPEC,
    )

    # Relations
    related_regions = RegionPageSummarySerializer(
        many=True,
        read_only=True,
    )
    related_sectors = serializers.SerializerMethodField()
    sub_sectors = serializers.SerializerMethodField()
    related_opportunities = serializers.SerializerMethodField()

    def get_time_to_investment_decision(self, instance):
        return instance.get_time_to_investment_decision_display()

    def get_planning_status(self, instance):
        # TODO: add modeltranslation support as required, at the snippet model level
        if instance.planning_status:
            return {
                'name': instance.planning_status.name,
                'verbose_description': instance.planning_status.verbose_description,
            }
        else:
            return {}

    def get_related_sectors(self, instance):
        serializer = RelatedSectorSerializer(
            instance.related_sectors.all(),
            many=True,
            allow_null=True,
            context=self.context
        )
        return serializer.data

    def get_sub_sectors(self, instance):
        serializer = RelatedSubSectorSerializer(
            instance.related_sub_sectors.all(),
            many=True,
            allow_null=True,
            context=self.context
        )
        sub_sectors_list = [sub_sector['related_sub_sector'] for sub_sector in serializer.data]
        return sub_sectors_list

    def get_related_opportunities(self, instance):
        # Related opportunities are defined as ones in the same REGION, whereas previously (with the
        # CapitalInvestOpportunityPageSerializer) we were showing based on SECTOR.

        related_regions_ids = instance.related_regions.values_list('id', flat=True)

        if not related_regions_ids:
            return []

        related_opps = InvestmentOpportunityPage.objects.live().public().filter(
            related_regions__in=related_regions_ids
        ).exclude(
            id=instance.id
        ).order_by(
            '-priority_weighting'
        ).distinct()

        if not related_opps:
            return []

        serializer = RelatedInvestmentOpportunityPageSerializer(
            related_opps,
            many=True,
            allow_null=True,
            context=self.context
        )
        return serializer.data


class MinimalRegionPageSummarySerializer(BasePageSerializer):
    title = serializers.CharField(source="hero_title")


class RelatedInvestmentOpportunityPageSerializer(BasePageSerializer):
    """Less detailed version of an InvestmentOpportunity - for instance used
    by InvestmentOpportunityPageSerializer.get_related_opportunities
    and AboutUkRegionPageSerializer.get_related_opportunities"""

    # title comes from BasePageSerializer
    thumbnail_image = wagtail_fields.ImageRenditionField(
        'fill-640x360',
        source='hero_image'
    )

    opportunity_summary = serializers.CharField()
    regions = serializers.SerializerMethodField()
    sectors = serializers.SerializerMethodField()
    sub_sectors = serializers.SerializerMethodField()

    def get_regions(self, instance):
        related_regions = instance.related_regions.live().all()
        serializer = MinimalRegionPageSummarySerializer(
            related_regions,
            many=True,
            read_only=True,
        )
        return serializer.data

    def get_sectors(self, instance):
        # Note: This serializer is more verbose than we _need_ here
        serializer = RelatedSectorSerializer(
            instance.related_sectors.all(),
            many=True,
            allow_null=True,
            context=self.context
        )
        return serializer.data

    def get_sub_sectors(self, instance):
        # Note: This serializer is more verbose than we _need_ here
        serializer = RelatedSubSectorSerializer(
            instance.related_sub_sectors.all(),
            many=True,
            allow_null=True,
            context=self.context
        )
        sub_sectors_list = [sub_sector['related_sub_sector'] for sub_sector in serializer.data]
        return sub_sectors_list


class InvestmentOpportunityForListPageSerializer(BasePageSerializer):

    title = serializers.CharField(max_length=255)
    hero_image = wagtail_fields.ImageRenditionField(
        'fill-640x360',
    )
    # key facts we want to filter by
    # sector = serializers.CharField(max_length=255)  # doesn't exist on new opp model [yet?]
    opportunity_summary = serializers.CharField()

    scale = serializers.CharField(max_length=255)
    scale_value = serializers.DecimalField(max_digits=10, decimal_places=2)
    planning_status = serializers.SerializerMethodField()
    investment_type = serializers.CharField(max_length=255)
    time_to_investment_decision = serializers.SerializerMethodField()

    related_regions = serializers.SerializerMethodField()
    related_sectors = serializers.SerializerMethodField()
    sub_sectors = serializers.SerializerMethodField()

    def get_planning_status(self, instance):
        # Ensure we always return the name, not the entire object. This protects against
        # the __str__ method being changed and breaking things
        return instance.planning_status.name if instance.planning_status else None

    def get_time_to_investment_decision(self, instance):
        return instance.get_time_to_investment_decision_display()

    def get_related_regions(self, instance):
        related_regions = instance.related_regions.live().all()
        serializer = MinimalRegionPageSummarySerializer(
            related_regions,
            many=True,
            read_only=True,
        )
        return serializer.data

    def get_related_sectors(self, instance):
        serializer = RelatedSectorSerializer(
            instance.related_sectors.all(),
            many=True,
            allow_null=True,
            context=self.context
        )
        return serializer.data

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


class InvestmentOpportunityListingPageSerializer(BasePageSerializer):
    # Heavily based on the CapitalInvestOpportunityListingSerializer it basically replaces

    breadcrumbs_label = serializers.CharField()
    search_results_title = serializers.CharField()
    hero_text = serializers.CharField()
    contact_cta_title = serializers.CharField()
    contact_cta_text = serializers.CharField()
    contact_cta_link = serializers.CharField()

    opportunity_list = serializers.SerializerMethodField()
    sector_with_sub_sectors = serializers.SerializerMethodField()

    def get_opportunity_list(self, instance):

        queryset = InvestmentOpportunityPage.objects.live().public()

        if not queryset:
            return []

        serializer = InvestmentOpportunityForListPageSerializer(
            queryset,
            many=True,
            allow_null=True,
            context=self.context
        )
        return serializer.data

    def get_sub_sector_headings(self, sector):

        return [sub_sector['heading'] for sub_sector in sector['child_sub_sectors']]

    def get_sector_with_sub_sectors(self, instance):

        all_sectors = InternationalInvestmentSectorPage.objects.live().public()

        sectors = InternationalInvestmentSectorPageSerializer(
            all_sectors,
            many=True,
            allow_null=True,
            context=self.context
        ).data

        return {sector['heading']: self.get_sub_sector_headings(sector) for sector in sectors}


class InternationalInvestmentSectorPageSerializer(
    BasePageSerializer,
    HeroSerializer,
    ChildPagesSerializerHelper,
):

    IMAGE_RENDITION_SPEC = "fill-960x540"
    AVATAR_RENDITION_SPEC = "fill-500x500"

    # hero_image is serialized by HeroSerializer
    heading = serializers.CharField()
    sub_heading = serializers.CharField(source='standfirst')
    featured_description = serializers.CharField()
    intro_text = core_fields.MarkdownToHTMLField()
    intro_image = wagtail_fields.ImageRenditionField(IMAGE_RENDITION_SPEC)

    # contact details
    contact_name = serializers.CharField()
    contact_avatar = wagtail_fields.ImageRenditionField(AVATAR_RENDITION_SPEC)
    contact_job_title = serializers.CharField()
    contact_link = serializers.CharField()
    contact_link_button_preamble = serializers.CharField()
    contact_link_button_label = serializers.CharField()

    # Related opportunities
    related_opportunities_header = serializers.CharField()
    related_opportunities = serializers.SerializerMethodField()

    # Main downpage content
    downpage_content = StreamFieldSerializer()

    # Early Opportunities content
    early_opportunities_header = serializers.CharField()
    early_opportunities = StreamFieldSerializer()

    # Sub-sector and child page serialization
    child_sub_sectors = serializers.SerializerMethodField()
    child_articles = serializers.SerializerMethodField()

    def get_child_sub_sectors(self, obj):
        return self.get_child_pages_data_for(
            obj,
            InternationalInvestmentSubSectorPage,
            MinimalPageSerializer
        )

    def get_child_articles(self, obj):
        return self.get_child_pages_data_for(
            obj,
            InternationalArticlePage,
            RelatedArticlePageSerializer
        )

    def get_related_opportunities(self, instance):
        # If instance.manually_selected_related_opportunities has content,
        # (it's a StreamField, remember), return them (up to three),
        # else grab up to three related opportunities based on matching sector.
        #
        # Note that for now, ordering of the auto-selected ones is based
        # on the priority_weighting and creation order on the relevant
        # opportunities.

        opportunities = []

        if len(instance.manually_selected_related_opportunities):
            opportunities = [
                x.value for x in instance.manually_selected_related_opportunities
                if x.value and x.value.live
            ]
        else:
            for page in InvestmentOpportunityPage.objects.live().public().order_by(
                '-priority_weighting', '-pk'
            ):
                for related_sectors in page.related_sectors.all():
                    if not related_sectors.related_sector:
                        continue
                    elif related_sectors.related_sector.title == instance.title:
                        opportunities.append(page)

            opportunities = opportunities[:3]  # limit to three Opps, max

        if not opportunities:
            return []

        serializer = RelatedInvestmentOpportunityPageSerializer(
            opportunities,
            allow_null=True,
            many=True,
            context=self.context
        )
        return serializer.data


class InternationalInvestmentSubSectorPageSerializer(
    BasePageSerializer,
):
    heading = serializers.CharField()


class WhyInvestInTheUKPageSerializer(
    BasePageSerializer,
    HeroSerializer,
):
    IMAGE_RENDITION_SPEC = "fill-960x540"

    strapline = serializers.CharField()
    introduction = core_fields.MarkdownToHTMLField()
    intro_image = wagtail_fields.ImageRenditionField(
        IMAGE_RENDITION_SPEC
    )
    uk_strength_title = serializers.CharField()
    uk_strength_intro = serializers.CharField()
    uk_strength_panels = StreamFieldSerializer()


class InvestmentGeneralContentPageSerializer(
    BasePageSerializer,
    HeroSerializer,
):
    IMAGE_RENDITION_SPEC = "fill-960x540"

    # title comes from BasePageSerializer
    # hero_image comes from HeroSerializer
    strapline = serializers.CharField()
    introduction = core_fields.MarkdownToHTMLField()
    intro_image = wagtail_fields.ImageRenditionField(
        IMAGE_RENDITION_SPEC
    )
    main_content = StreamFieldSerializer()
