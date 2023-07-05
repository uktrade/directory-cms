from django.conf import settings
from directory_constants import cms
from rest_framework import serializers
from wagtail.api.v2.serializers import StreamField as StreamFieldSerializer
from wagtail.images.api import fields as wagtail_fields

from core import fields as core_fields
from core.helpers import num2words_list
from core.serializers import BasePageSerializer, ChildPagesSerializerHelper, FormPageSerializerMetaclass, HeroSerializer

from .models.great_international import (
    AboutDitServicesPage,
    InternationalArticleListingPage,
    InternationalArticlePage,
    InternationalCampaignPage,
    InternationalInvestmentSectorPage,
    InternationalInvestmentSubSectorPage,
    WhyInvestInTheUKPage,
    InternationalTopicLandingPage,
    AboutUkRegionPage,
    AboutUkRegionListingPage,
)
from .models.investment_atlas import (
    ForeignDirectInvestmentFormPage,
    InvestmentOpportunityPage,
    InvestmentGeneralContentPage,
    InvestmentOpportunityListingPage,
    INVESTMENT_TYPE
)


class GreatMediaSerializer(serializers.Serializer):
    title = serializers.CharField()
    transcript = serializers.SerializerMethodField()
    sources = serializers.SerializerMethodField()
    url = serializers.CharField()
    thumbnail = serializers.SerializerMethodField()
    subtitles = serializers.SerializerMethodField()

    def get_transcript(self, obj):
        return obj.greatmedia.transcript

    def get_sources(self, obj):
        return obj.greatmedia.sources

    def get_subtitles(self, obj):
        return obj.greatmedia.subtitles

    def get_thumbnail(self, obj):
        if obj.thumbnail:
            return obj.thumbnail.url


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


class AboutUkRegionsProxyDataWrapper:

    def __init__(self, instance):
        self.instance = instance

    @property
    def text(self):
        return self.instance.featured_description


class EconomicStatSerializer(serializers.Serializer):
    number = serializers.CharField(max_length=255)
    heading = serializers.CharField(max_length=255)
    smallprint = serializers.CharField(max_length=255)


class LocationStatSerializer(serializers.Serializer):
    number = serializers.CharField(max_length=255)
    heading = serializers.CharField(max_length=255)
    smallprint = serializers.CharField(max_length=255)


class AboutUkRegionSerializer(serializers.Serializer):
    region = serializers.SerializerMethodField()
    text = serializers.CharField(max_length=255)

    def get_region(self, obj):
        region = obj.instance

        if not region:
            return []

        serializer = MinimalPageWithHeroTitleAndHeroImageSerializer(region)

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


class RelatedInvestmentOpportunityPageMinimalSerializer(BasePageSerializer):
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
    AboutDitServicesPage: RelatedDitServicesPageSerializer,
    WhyInvestInTheUKPage: RelatedWhyInvestInTheUKPageSerializer,
    InternationalTopicLandingPage: RelatedInternationalTopicLandingPageSerializer,
    AboutUkRegionPage: RelatedAboutUkRegionPageSerializer,
    InvestmentOpportunityPage: RelatedInvestmentOpportunityPageMinimalSerializer,
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


class InternationalArticlePageSerializer(BasePageSerializer):
    type_of_article = serializers.CharField()

    display_title = serializers.CharField(source='article_title')
    article_title = serializers.CharField()
    article_teaser = serializers.CharField()
    hero_image = wagtail_fields.ImageRenditionField('original')
    hero_video = core_fields.VideoField()
    article_subheading = serializers.CharField()

    article_image = wagtail_fields.ImageRenditionField('original')
    article_image_thumbnail = wagtail_fields.ImageRenditionField('fill-640x360', source='article_image')
    article_video = GreatMediaSerializer()

    article_body_text = core_fields.MarkdownToHTMLField()

    cta_title = serializers.CharField()
    cta_teaser = serializers.CharField()
    cta_link_label = serializers.CharField()
    cta_link = serializers.CharField()

    tags = core_fields.TagsListField()

    freeport_data = serializers.SerializerMethodField()

    def get_freeport_data(self, instance):
        if instance.type_of_article == 'Freeport landing':
            queryset = InvestmentOpportunityPage.objects.live().public().filter(investment_type__name='Freeport')
            if not queryset:
                return []

            serializer = InvestmentOpportunityForListPageSerializer(
                queryset,
                many=True,
                allow_null=True,
                context=self.context
            )
            return serializer.data


class InternationalHomePageSerializer(BasePageSerializer):
    # Note that this is massively cut down from the original version,
    # but that the older fields still exist on the model (see the comment there)

    hero_title = serializers.CharField(max_length=255)
    hero_video = GreatMediaSerializer()
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
    hero_video = GreatMediaSerializer()

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
        sectors = self.get_child_pages_data_for(
            obj,
            InternationalInvestmentSectorPage,  # NB this is the new Sector page, not the old one
            InternationalInvestmentSectorPageSerializer
        )
        sectors = sorted(sectors, key=lambda x: x['heading'])
        return articles + campaigns + sectors


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

class RegionSubsectionSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=255)
    content = core_fields.MarkdownToHTMLField()
    icon = wagtail_fields.ImageRenditionField(
        'original',
        allow_null=True
    )


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


def get_mapped_regions(queryset):
    data = [
        AboutUkRegionsProxyDataWrapper(
            instance=region,
        )
        for region in queryset
    ]
    serializer = AboutUkRegionSerializer(data, many=True)
    return serializer.data


class AboutUkRegionListingPageSerializer(PageWithRelatedPagesSerializer, HeroSerializer):
    breadcrumbs_label = serializers.CharField()
    hero_title = serializers.CharField()
    hero_video = GreatMediaSerializer()

    intro = core_fields.MarkdownToHTMLField()

    contact_title = serializers.CharField()
    contact_text = core_fields.MarkdownToHTMLField()
    contact_cta_text = serializers.CharField()
    contact_cta_link = serializers.CharField()

    mapped_regions = serializers.SerializerMethodField()

    def get_mapped_regions(self, instance):
        queryset = AboutUkRegionPage.objects.live().public()

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
    region_summary_section_content = core_fields.MarkdownToHTMLField()

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
    property_and_infrastructure_section_content = core_fields.MarkdownToHTMLField()

    case_study_image = wagtail_fields.ImageRenditionField('original')
    case_study_title = serializers.CharField(max_length=255)
    case_study_text = core_fields.MarkdownToHTMLField()
    case_study_cta_text = serializers.CharField(max_length=255)

    case_study_cta_link = serializers.CharField(max_length=255)

    contact_title = serializers.CharField(max_length=255)
    contact_text = core_fields.MarkdownToHTMLField()
    contact_cta_link = serializers.CharField(max_length=255)
    contact_cta_text = serializers.CharField(max_length=255)

    mapped_regions = serializers.SerializerMethodField()

    related_opportunities = serializers.SerializerMethodField()

    def _get_regions(self, instance):
        return set([item.value['region'] for item in instance.regions_with_locations])

    def get_related_opportunities(self, instance):
        # Return up to three investment_atlas.InvestmentOpportunties,
        # related by Region, ordered by their weighting and then pk
        # as a tie-breaker, so newer ones come first if weighting is
        # the same
        related_opps = []

        for opp in InvestmentOpportunityPage.objects.live().public().order_by(
                '-priority_weighting', '-pk'

        ).distinct():
            if instance in self._get_regions(opp):
                # only interested in first three opportunities
                if len(related_opps) >= 3:
                    break
                related_opps.append(opp)

        serializer = RelatedInvestmentOpportunityPageSerializer(
            related_opps,
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
        queryset = AboutUkRegionPage.objects.live().public()

        if not queryset:
            return []

        return get_mapped_regions(queryset)


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
    hero_video = GreatMediaSerializer()
    hero_strapline = serializers.CharField()
    hero_cta_text = serializers.CharField()
    hero_cta_link = serializers.CharField()
    downpage_sections = StreamFieldSerializer()


class InvestmentOpportunityPageSerializer(BasePageSerializer, HeroSerializer):

    IMAGE_RENDITION_SPEC = "fill-960x540"
    AVATAR_RENDITION_SPEC = "fill-500x500"
    HERO_IMAGE_RENDITION_SPEC = "original"

    # Intro/summary
    # title is automatic, from BasePageSerializer
    breadcrumbs_label = serializers.CharField()
    strapline = serializers.CharField()
    introduction = core_fields.MarkdownToHTMLField()
    intro_image = wagtail_fields.ImageRenditionField(
        IMAGE_RENDITION_SPEC,
    )
    intro_video = GreatMediaSerializer()
    hero_video = GreatMediaSerializer()

    # Key facts
    location = serializers.CharField()
    locations_for_regions = StreamFieldSerializer(source='regions_with_locations')

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

    related_sectors = serializers.SerializerMethodField()
    sub_sectors = serializers.SerializerMethodField()
    related_opportunities = serializers.SerializerMethodField()
    related_regions = serializers.SerializerMethodField()

    def _get_regions(self, instance):
        return set([item.value['region'] for item in instance.regions_with_locations
                    if item.value['region'] and item.value['region'].live])

    def get_related_regions(self, instance):
        related_regions = self._get_regions(instance)

        serializer = RegionPageSummarySerializer(
            related_regions,
            many=True,
            read_only=True,
        )
        return serializer.data

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

    def get_related_opportunities_by_sector(self, instance):
        related_sectors_set = set(sector.related_sector_id for sector in instance.related_sectors.all())

        if not related_sectors_set:
            return []

        related_opps = []
        for opp in InvestmentOpportunityPage.objects.live().public().exclude(
                id=instance.id
        ).order_by(
            '-priority_weighting'
        ).distinct():
            opp_sectors_set = set(sector.related_sector_id for sector in opp.related_sectors.all())
            if opp_sectors_set.intersection(related_sectors_set):
                related_opps.append(opp)

        return related_opps

    def get_related_opportunities_by_investment_type(self, instance):
        if not instance.investment_type:
            return []

        possible_opps = InvestmentOpportunityPage.objects.live().public().exclude(
            id=instance.id
        ).order_by('-priority_weighting').distinct()

        return [opp for opp in possible_opps if opp.investment_type == instance.investment_type]

    def get_related_opportunities(self, instance):
        # Related opportunities are by default based on SECTOR,
        # but can also be based on investment type

        if instance.get_related_opportunities_by == INVESTMENT_TYPE:
            related_opps = self.get_related_opportunities_by_investment_type(instance)
        else:
            related_opps = self.get_related_opportunities_by_sector(instance)

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

    def _get_regions(self, instance):
        return set([item.value['region'] for item in instance.regions_with_locations if item.value['region'].live])

    def get_regions(self, instance):
        related_regions = self._get_regions(instance)
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
    locations_with_regions = StreamFieldSerializer(source="regions_with_locations")

    related_regions = serializers.SerializerMethodField()
    related_sectors = serializers.SerializerMethodField()
    sub_sectors = serializers.SerializerMethodField()

    def _get_regions(self, instance):
        return set([item.value['region'] for item in instance.regions_with_locations
                    if item.value['region'] and item.value['region'].live])

    def get_planning_status(self, instance):
        # Ensure we always return the name, not the entire object. This protects against
        # the __str__ method being changed and breaking things
        return instance.planning_status.name if instance.planning_status else None

    def get_time_to_investment_decision(self, instance):
        return instance.get_time_to_investment_decision_display()

    def get_related_regions(self, instance):

        related_regions = self._get_regions(instance)

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
    hero_video = GreatMediaSerializer()
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
    hero_video = GreatMediaSerializer()

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

    hero_video = GreatMediaSerializer()
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
    hero_video = GreatMediaSerializer()
    main_content = StreamFieldSerializer()
