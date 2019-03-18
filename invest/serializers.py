from rest_framework import serializers
from wagtail.images.api import fields as wagtail_fields

from core import fields as core_fields
from core.serializers import (
    BasePageSerializer, FormPageSerializerMetaclass, ChildPagesSerializerHelper
)
from .models import (
    HighPotentialOpportunityFormPage, HighPotentialOpportunityDetailPage,
    SectorPage, SetupGuidePage
)

ONE_TO_SIX_WORDS = ['one', 'two', 'three', 'four', 'five', 'six']
ONE_TO_SEVEN_WORDS = ONE_TO_SIX_WORDS + ['seven']


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


class HowWeHelpProxyDataWrapper:

    def __init__(self, instance, suffix):
        self.suffix = suffix
        self.instance = instance

    @property
    def text(self):
        return getattr(self.instance, f'how_we_help_text_{self.suffix}')

    @property
    def icon(self):
        return getattr(
            self.instance,
            f'how_we_help_icon_{self.suffix}',
            None
        )


class PulloutSerializer(serializers.Serializer):
    text = core_fields.MarkdownToHTMLField()
    stat = serializers.CharField(allow_null=True)
    stat_text = serializers.CharField(allow_null=True)


class SubsectionSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=255)
    content = core_fields.MarkdownToHTMLField()
    map = wagtail_fields.ImageRenditionField(
        'original',
        allow_null=True
    )


class SectorPageSerializer(BasePageSerializer, ChildPagesSerializerHelper):
    featured = serializers.BooleanField()
    description = serializers.CharField()
    heading = serializers.CharField(max_length=255)
    hero_image = wagtail_fields.ImageRenditionField('original')
    pullout = serializers.SerializerMethodField()
    subsections = serializers.SerializerMethodField()
    children_sectors = serializers.SerializerMethodField()

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

    def get_children_sectors(self, instance):
        return self.get_child_pages_data_for(
            instance,
            SectorPage,
            SectorPageSerializer
        )


class SectorLandingPageGenericSerializer(
    BasePageSerializer, ChildPagesSerializerHelper
):
    """This can be used for SectorLandingPage and RegionalLandingPage"""
    heading = serializers.CharField(max_length=255)
    hero_image = wagtail_fields.ImageRenditionField('original')
    children_sectors = serializers.SerializerMethodField()

    def get_children_sectors(self, instance):
        return self.get_child_pages_data_for(
            instance,
            SectorPage,
            SectorPageSerializer
        )


class SetupGuidePageSerializer(BasePageSerializer):
    description = serializers.CharField()
    heading = serializers.CharField(max_length=255)
    sub_heading = serializers.CharField(max_length=255)
    subsections = serializers.SerializerMethodField()
    children_setup_guides = serializers.SerializerMethodField()

    def get_children_setup_guides(self, instance):
        queryset = instance.get_descendants().type(
            SetupGuidePage
        ).live().specific()
        serializer = SetupGuidePageSerializer(
            queryset,
            many=True,
            allow_null=True,
            context=self.context
        )
        return serializer.data

    def get_subsections(self, instance):
        data = [
            SubsectionProxyDataWrapper(instance=instance, suffix=num)
            for num in ONE_TO_SEVEN_WORDS
        ]
        serializer = SubsectionSerializer(data, many=True)
        return serializer.data


class SetupGuideLandingPageSerializer(
    BasePageSerializer, ChildPagesSerializerHelper
):
    heading = serializers.CharField(max_length=255)
    sub_heading = serializers.CharField(max_length=255)
    lead_in = serializers.CharField(allow_null=True, allow_blank=True)
    children_setup_guides = serializers.SerializerMethodField()

    def get_children_setup_guides(self, instance):
        from .models import SetupGuidePage
        queryset = instance.get_descendants().type(
            SetupGuidePage
        ).live().specific()
        serializer = SetupGuidePageSerializer(
            queryset,
            many=True,
            allow_null=True,
            context=self.context
        )
        return serializer.data


class HowWeHelpSerializer(serializers.Serializer):
    text = serializers.CharField(max_length=255)
    icon = wagtail_fields.ImageRenditionField(
        'original',
        allow_null=True
    )


class InvestHomePageSerializer(BasePageSerializer):
    heading = serializers.CharField(max_length=255)
    sub_heading = serializers.CharField(max_length=255)
    hero_call_to_action_text = serializers.CharField(max_length=255)
    hero_image = wagtail_fields.ImageRenditionField('original')
    benefits_section_title = serializers.CharField(max_length=255)
    benefits_section_intro = serializers.CharField(max_length=255)
    benefits_section_content = core_fields.MarkdownToHTMLField()
    benefits_section_img = wagtail_fields.ImageRenditionField('original')
    benefits_section_img_caption = serializers.CharField(max_length=255)
    eu_exit_section_title = serializers.CharField(max_length=255)
    eu_exit_section_content = core_fields.MarkdownToHTMLField()
    eu_exit_section_call_to_action_text = serializers.CharField(max_length=255)
    eu_exit_section_img = wagtail_fields.ImageRenditionField('original')
    eu_exit_section_img_caption = serializers.CharField(max_length=255)
    subsections = serializers.SerializerMethodField()
    sector_title = serializers.CharField(max_length=255)
    sector_button_text = serializers.CharField(max_length=255)
    setup_guide_title = serializers.CharField(max_length=255)
    setup_guide_content = core_fields.MarkdownToHTMLField()
    setup_guide_img = wagtail_fields.ImageRenditionField('original')
    setup_guide_img_caption = serializers.CharField(max_length=255)
    setup_guide_call_to_action_text = serializers.CharField(max_length=255)
    setup_guide_lead_in = serializers.CharField(
        max_length=255,
        allow_null=True
    )
    how_we_help_title = serializers.CharField(max_length=255)
    how_we_help_lead_in = serializers.CharField(max_length=255)
    how_we_help = serializers.SerializerMethodField()
    contact_section_title = serializers.CharField(max_length=255)
    contact_section_content = serializers.CharField(max_length=255)
    contact_section_call_to_action_text = serializers.CharField(max_length=255)
    sectors = serializers.SerializerMethodField()
    high_potential_opportunities = serializers.SerializerMethodField()
    guides = serializers.SerializerMethodField()

    def get_how_we_help(self, instance):
        data = [
            HowWeHelpProxyDataWrapper(instance=instance, suffix=num)
            for num in ONE_TO_SIX_WORDS
        ]
        serializer = HowWeHelpSerializer(data, many=True)
        return serializer.data

    def get_subsections(self, instance):
        data = [
            SubsectionProxyDataWrapper(instance=instance, suffix=num)
            for num in ONE_TO_SEVEN_WORDS
        ]
        serializer = SubsectionSerializer(data, many=True)
        return serializer.data

    def get_sectors(self, instance):
        queryset = SectorPage.objects.all().filter(
            featured=True
        ).live().order_by('heading')
        serializer = SectorPageSerializer(
            queryset,
            many=True,
            allow_null=True,
            context=self.context
        )
        print("sectors: ", SectorPage.objects.all())
        return serializer.data

    def get_high_potential_opportunities(self, instance):
        from .models import HighPotentialOpportunityDetailPage
        queryset = HighPotentialOpportunityDetailPage.objects.all().filter(
            featured=True
        ).live().order_by('heading')
        serializer = HighPotentialOpportunityDetailPageSerializer(
            queryset,
            many=True,
            allow_null=True,
            context=self.context
        )
        print("HPOs: ", HighPotentialOpportunityDetailPage.objects.all())
        return serializer.data

    def get_guides(self, instance):
        queryset = SetupGuidePage.objects.all().live().order_by('heading')
        serializer = SetupGuidePageSerializer(
            queryset,
            many=True,
            allow_null=True,
            context=self.context
        )
        return serializer.data


class InfoPageSerializer(BasePageSerializer):
    content = core_fields.MarkdownToHTMLField()


class HighPotentialOpportunityDetailPageBaseSerializer(BasePageSerializer):
    breadcrumbs_label = serializers.CharField(max_length=50)
    heading = serializers.CharField(max_length=255)
    hero_image = wagtail_fields.ImageRenditionField('original')
    description = serializers.CharField(max_length=255)
    featured = serializers.BooleanField()
    contact_proposition = core_fields.MarkdownToHTMLField()
    contact_button = serializers.CharField(max_length=500)
    proposition_one = core_fields.MarkdownToHTMLField()
    proposition_one_image = wagtail_fields.ImageRenditionField('original')
    proposition_one_video = core_fields.VideoField()
    opportunity_list_title = serializers.CharField()
    opportunity_list_item_one = core_fields.MarkdownToHTMLField()
    opportunity_list_item_two = core_fields.MarkdownToHTMLField()
    opportunity_list_item_three = core_fields.MarkdownToHTMLField()
    opportunity_list_image = wagtail_fields.ImageRenditionField('original')
    proposition_two = core_fields.MarkdownToHTMLField()
    proposition_two_list_item_one = core_fields.MarkdownToHTMLField()
    proposition_two_list_item_two = core_fields.MarkdownToHTMLField()
    proposition_two_list_item_three = core_fields.MarkdownToHTMLField()
    proposition_two_image = wagtail_fields.ImageRenditionField('original')
    proposition_two_video = core_fields.VideoField()
    competitive_advantages_title = serializers.CharField()
    competitive_advantages_list_item_one = core_fields.MarkdownToHTMLField()
    competitive_advantages_list_item_one_icon = \
        wagtail_fields.ImageRenditionField('original')
    competitive_advantages_list_item_two = core_fields.MarkdownToHTMLField()
    competitive_advantages_list_item_two_icon = \
        wagtail_fields.ImageRenditionField('original')
    competitive_advantages_list_item_three = core_fields.MarkdownToHTMLField()
    competitive_advantages_list_item_three_icon = \
        wagtail_fields.ImageRenditionField('original')
    testimonial = core_fields.MarkdownToHTMLField()
    testimonial_background = wagtail_fields.ImageRenditionField('original')
    companies_list_text = core_fields.MarkdownToHTMLField()
    companies_list_item_image_one = wagtail_fields.ImageRenditionField(
        'original'
    )
    companies_list_item_image_two = wagtail_fields.ImageRenditionField(
        'original'
    )
    companies_list_item_image_three = wagtail_fields.ImageRenditionField(
        'original'
    )
    companies_list_item_image_four = wagtail_fields.ImageRenditionField(
        'original'
    )
    companies_list_item_image_five = wagtail_fields.ImageRenditionField(
        'original'
    )
    companies_list_item_image_six = wagtail_fields.ImageRenditionField(
        'original'
    )
    companies_list_item_image_seven = wagtail_fields.ImageRenditionField(
        'original'
    )
    companies_list_item_image_eight = wagtail_fields.ImageRenditionField(
        'original'
    )
    case_study_list_title = serializers.CharField()
    case_study_one_text = core_fields.MarkdownToHTMLField()
    case_study_one_image = wagtail_fields.ImageRenditionField('original')
    case_study_two_text = core_fields.MarkdownToHTMLField()
    case_study_two_image = wagtail_fields.ImageRenditionField('original')
    case_study_three_text = core_fields.MarkdownToHTMLField()
    case_study_three_image = wagtail_fields.ImageRenditionField('original')
    case_study_four_text = core_fields.MarkdownToHTMLField()
    case_study_four_image = wagtail_fields.ImageRenditionField('original')
    other_opportunities_title = serializers.CharField()
    pdf_document = core_fields.DocumentURLField()
    summary_image = wagtail_fields.ImageRenditionField('original')


class HighPotentialOpportunityDetailPageSerializer(
    HighPotentialOpportunityDetailPageBaseSerializer
):
    other_opportunities = serializers.SerializerMethodField()

    def get_other_opportunities(self, instance):
        queryset = (
            HighPotentialOpportunityDetailPage.objects.all()
            .live()
            .order_by('heading')
            .exclude(slug=instance.slug)
        )
        serializer = HighPotentialOpportunityDetailPageBaseSerializer(
            queryset,
            many=True,
            allow_null=True,
            context=self.context
        )
        return serializer.data


class HighPotentialOpportunityFormPageSerializer(
    BasePageSerializer,
    metaclass=FormPageSerializerMetaclass
):
    class Meta:
        model_class = HighPotentialOpportunityFormPage

    heading = serializers.CharField(max_length=255)
    sub_heading = serializers.CharField(max_length=255)
    breadcrumbs_label = serializers.CharField(max_length=50)
    opportunity_list = serializers.SerializerMethodField()

    def get_opportunity_list(self, instance):
        queryset = (
            HighPotentialOpportunityDetailPage.objects.all()
            .live()
            .order_by('heading')
            .exclude(slug=instance.slug)
        )
        serializer = HighPotentialOpportunityDetailPageSerializer(
            queryset,
            many=True,
            allow_null=True,
            context=self.context
        )
        return serializer.data


class HighPotentialOpportunityFormSuccessPageSerializer(BasePageSerializer):
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
            HighPotentialOpportunityDetailPage.objects.all()
            .live()
            .order_by('heading')
            .exclude(slug=instance.slug)
        )
        serializer = HighPotentialOpportunityDetailPageSerializer(
            queryset,
            many=True,
            allow_null=True,
            context=self.context
        )
        return serializer.data
