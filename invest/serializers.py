from rest_framework import fields

from core.serializers import APIChildrenSerializer


class APIChildrenSectorSerializer(APIChildrenSerializer):
    sorting_key = 'heading'

    @staticmethod
    def get_model():
        from invest.models import SectorPage
        return SectorPage


class APIChildrenSetupGuideSerializer(APIChildrenSerializer):
    sorting_key = 'heading'

    @staticmethod
    def get_model():
        from invest.models import SetupGuidePage
        return SetupGuidePage


class APIHighPotentialOpportunityDetailQuerysetSerializer(fields.ListField):
    def __init__(self, *args, **kwargs):
        self.fields_config = kwargs.pop('fields_config')
        super().__init__(*args, **kwargs)

    def get_attribute(self, instance):
        return instance

    def to_representation(self, instance):
        # avoid circular dependency
        from invest.models import HighPotentialOpportunityDetailPage
        queryset = (
            HighPotentialOpportunityDetailPage.objects.all()
            .live()
            .order_by('heading')
            .exclude(slug=instance.slug)
        )
        serializer_class = self.context['view']._get_serializer_class(
            router=self.context['router'],
            model=HighPotentialOpportunityDetailPage,
            fields_config=self.fields_config,
            nested=True,
        )

        serializer = serializer_class(
            queryset, many=True, context=self.context
        )
        return serializer.data
