from django.db.models import Q
from rest_framework.generics import RetrieveAPIView, ListAPIView

from conf.signature import SignatureCheckPermission
from export_readiness import models, serializers, snippets


class CountryPageLookupByIndustryTagIDListAPIView(RetrieveAPIView):
    queryset = snippets.IndustryTag.objects.all()
    serializer_class = serializers.TagCountryPageSerializer
    permission_classes = [SignatureCheckPermission]


class IndustryTagsListAPIView(ListAPIView):
    queryset = snippets.IndustryTag.objects.all()
    serializer_class = serializers.IndustryTagSerializer
    permission_classes = [SignatureCheckPermission]


class CountryPageListAPIView(ListAPIView):
    queryset = models.CountryGuidePage.objects.all()
    serializer_class = serializers.CountryGuidePageSerializer
    permission_classes = [SignatureCheckPermission]

    def get_queryset(self):
        queryset = models.CountryGuidePage.objects.all()
        industry = self.request.query_params.get('industry')
        region = self.request.query_params.get('region')
        q_industries = Q()
        q_regions = Q()
        if industry:
            for value in industry.split(','):
                q_industries |= Q(**{'country__region__name': value})
                queryset.filter(q_industries)
        if region:
            for value in region.split(','):
                q_regions |= Q(**{'tags__name': value})
                queryset.filter(q_regions)

        return queryset.distinct()


class RegionsListAPIView(ListAPIView):
    queryset = snippets.Region.objects.all()
    serializer_class = serializers.IDNameSerializer
    permission_classes = [SignatureCheckPermission]
