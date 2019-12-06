from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import RetrieveAPIView, ListAPIView

from conf.signature import SignatureCheckPermission
from export_readiness import filters, models, serializers, snippets


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
    filter_backends = [DjangoFilterBackend]
    serializer_class = serializers.CountryGuidePageSerializer
    filterset_class = filters.CountryGuideFilter
    permission_classes = [SignatureCheckPermission]


class RegionsListAPIView(ListAPIView):
    queryset = snippets.Region.objects.all()
    serializer_class = serializers.IDNameSerializer
    permission_classes = [SignatureCheckPermission]
