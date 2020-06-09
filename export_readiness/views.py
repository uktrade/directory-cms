from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from rest_framework.generics import RetrieveAPIView, ListAPIView
from rest_framework.response import Response

from conf.signature import SignatureCheckPermission
from export_readiness import serializers, snippets
from core.cache import CountryPagesCache

THIRTY_MINUTES_IN_SECONDS = 30 * 60


class CountryPageLookupByIndustryTagIDListAPIView(RetrieveAPIView):
    queryset = snippets.IndustryTag.objects.all()
    serializer_class = serializers.TagCountryPageSerializer
    permission_classes = [SignatureCheckPermission]


class IndustryTagsListAPIView(ListAPIView):
    queryset = snippets.IndustryTag.objects.all()
    serializer_class = serializers.IndustryTagSerializer
    permission_classes = [SignatureCheckPermission]

    @method_decorator(cache_page(THIRTY_MINUTES_IN_SECONDS))
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class CountryPageListAPIView(ListAPIView):
    permission_classes = [SignatureCheckPermission]
    http_method_names = ('get', )

    def get(self, *args, **kwargs):
        filters = {}
        industries = self.request.GET.get('industry')
        countries = self.request.GET.get('region')
        if industries:
            filters['industries'] = industries.split(',')
        if countries:
            filters['countries'] = countries.split(',')
        cached_content = CountryPagesCache.get_many(**filters)
        return Response(cached_content or [], content_type='application/json')


class RegionsListAPIView(ListAPIView):
    queryset = snippets.Region.objects.all()
    serializer_class = serializers.IDNameSerializer
    permission_classes = [SignatureCheckPermission]

    @method_decorator(cache_page(THIRTY_MINUTES_IN_SECONDS))
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
