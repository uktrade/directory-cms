from rest_framework.generics import RetrieveAPIView, ListAPIView

from conf.signature import SignatureCheckPermission
from export_readiness import serializers, snippets


class CountryPageLookupByIndustryTagIDListAPIView(RetrieveAPIView):
    queryset = snippets.IndustryTag
    serializer_class = serializers.TagCountryPageSerializer
    permission_classes = [SignatureCheckPermission]


class IndustryTagsListAPIView(ListAPIView):
    queryset = snippets.IndustryTag.objects.all()
    serializer_class = serializers.TagSerializer
    permission_classes = [SignatureCheckPermission]
