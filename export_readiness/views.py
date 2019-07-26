from rest_framework.generics import RetrieveAPIView

from conf.signature import SignatureCheckPermission
from export_readiness import serializers, snippets


class PageLookupByTagListAPIEndpoint(RetrieveAPIView):
    queryset = snippets.Tag
    serializer_class = serializers.TagSerializer
    lookup_field = 'slug'
    permission_classes = [SignatureCheckPermission]
