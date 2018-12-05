from rest_framework.generics import RetrieveAPIView

from export_readiness import models, serializers


class PageLookupByTagListAPIEndpoint(RetrieveAPIView):
    queryset = models.Tag
    serializer_class = serializers.TagSerializer
    lookup_field = 'slug'
