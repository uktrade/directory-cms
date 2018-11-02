from rest_framework import serializers
from wagtail.images.api import fields as wagtail_fields

from core import fields as core_fields
from core.serializers import BasePageSerializer, FormPageSerializerMetaclass
from .models import HighPotentialOpportunityFormPage, \
    HighPotentialOpportunityDetailPage

ONE_TO_SEVEN_WORDS = ('one', 'two', 'three', 'four', 'five', 'six', 'seven')


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


class SectorPageSerializer(BasePageSerializer):
    features = serializers.BooleanField()
    description = serializers.CharField()
    heading = serializers.CharField(max_length=255)
    hero_image = wagtail_fields.ImageRenditionField('original')
    pullout = serializers.SerializerMethodField()
    subsections = serializers.SerializerMethodField()
    sectors = serializers.SerializerMethodField()

    def get_pullout(self, instance):
        return PulloutSerializer(
            text=instance.pullout_text,
            stat=instance.pullout_stat,
            stat_text=instance.stat_text
        ).data

    def get_subsections(self, instance):
        data = [
            SubsectionProxyDataWrapper(instance=instance, suffix=num)
            for num in ONE_TO_SEVEN_WORDS
        ]
        serializer = SubsectionSerializer(data, many=True)
        return serializer.data

    def get_sectors(self, instance):
        from .models import SectorPage
        queryset = instance.get_descendants.type(SectorPage).live().specific()
        serializer = SectorPageSerializer(
            queryset,
            many=True,
            allow_null=True,
            context=self.context
        )
        return serializer.data


class SectorLandingPageGenericSerializer(BasePageSerializer):
    """This can be used for SectorLandingPage and RegionalLandingPage"""
    heading = serializers.CharField(max_length=255)
    hero_image = wagtail_fields.ImageRenditionField('original')
    children_sectors = serializers.SerializerMethodField()

    def get_children_sectors(self, instance):
        from .models import SectorPage
        queryset = instance.get_descendants.type(SectorPage).live().specific()
        serializer = SectorPageSerializer(
            queryset,
            many=True,
            allow_null=True,
            context=self.context
        )
        return serializer.data


class SetupGuidePageSerializer(BasePageSerializer):
    description = serializers.CharField()
    heading = serializers.CharField(max_length=255)
    sub_heading = serializers.CharField(max_length=255)
    subsections = serializers.SerializerMethodField()

    def get_subsections(self, instance):
        data = [
            SubsectionProxyDataWrapper(instance=instance, suffix=num)
            for num in ONE_TO_SEVEN_WORDS
        ]
        serializer = SubsectionSerializer(data, many=True)
        return serializer.data


class SetupGuideLandingPageSerializer(BasePageSerializer):
    heading = serializers.CharField(max_length=255)
    sub_heading = serializers.CharField(max_length=255)
    lead_in = serializers.CharField(allow_null=True, allow_blank=True)
    children_setup_guides = serializers.SerializerMethodField()

    def get_children_setup_guides(self, instance):
        from .models import SetupGuidePage
        queryset = instance.get_descendants.type(
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
    hero_image = wagtail_fields.ImageRenditionField('original')
    subsections = serializers.SerializerMethodField()
    sector_title = serializers.CharField(max_length=255)
    sector_button_text = serializers.CharField(max_length=255)
    setup_guide_title = serializers.CharField(max_length=255)
    setup_guide_lead_in = serializers.CharField(
        max_length=255,
        allow_null=True
    )
    how_we_help_title = serializers.CharField(max_length=255)
    how_we_help_lead_in = serializers.CharField(max_length=255)
    how_we_help = serializers.SerializerMethodField()
    sectors = serializers.SerializerMethodField()
    guides = serializers.SerializerMethodField()

    def get_how_we_help(self, instance):
        data = [
            HowWeHelpProxyDataWrapper(instance=instance, suffix=num)
            for num in ONE_TO_SEVEN_WORDS
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
        from .models import SectorPage
        queryset = SectorPage.objects.all().filter(
            featured=True
        ).live().order_by('heading')
        serializer = SectorPageSerializer(
            queryset,
            many=True,
            allow_null=True,
            context=self.context
        )
        return serializer.data

    def get_guides(self, instance):
        from .models import SetupGuidePage
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


class HighPotentialOpportunityDetailPageSerializer(BasePageSerializer):
    breadcrumbs_label = serializers.CharField(max_length=50)
    heading = serializers.CharField(max_length=255)
    hero_image = wagtail_fields.ImageRenditionField('original')
    contact_proposition = core_fields.MarkdownToHTMLField()
    contact_button = serializers.CharField(max_length=500)
    proposition_one = core_fields.MarkdownToHTMLField()
    proposition_one_image = wagtail_fields.ImageRenditionField('original')



class HighPotentialOpportunityFormPageSerializer(BasePageSerializer,
    metaclass=FormPageSerializerMetaclass):

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
