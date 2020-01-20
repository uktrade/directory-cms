from django.core.cache import cache
from django.db.models import Q
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from rest_framework.generics import RetrieveAPIView, ListAPIView
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response

from conf.signature import SignatureCheckPermission
from export_readiness import models, serializers, snippets


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
    queryset = models.CountryGuidePage.objects.all()
    serializer_class = serializers.CountryGuidePageSerializer
    permission_classes = [SignatureCheckPermission]
    http_method_names = ('get', )
    renderer_classes = (JSONRenderer,)

    @property
    def cache_key(self):
        industry = self.request.GET.get('industry')
        region = self.request.GET.get('region')
        return f'countryguide_{industry}{region}'

    def get_queryset(self):
        queryset = models.CountryGuidePage.objects.all()
        industry = self.request.query_params.get('industry')
        region = self.request.query_params.get('region')
        if not industry and not region:
            return queryset
        q_industries = Q()
        q_regions = Q()
        if industry:
            for value in industry.split(','):
                q_industries |= Q(tags__name=value)
        if region:
            for value in region.split(','):
                q_regions |= Q(country__region__name=value)
        return queryset.filter(q_industries & q_regions).distinct()

    def get(self, *args, **kwargs):

        def foo(response):
            cache.set(key=self.cache_key, value=response.content, timeout=THIRTY_MINUTES_IN_SECONDS)

        cached_content = cache.get(key=self.cache_key)
        if cached_content:
            response = Response(cached_content, content_type='application/json')
        else:
            response = super().get(*args, **kwargs)
            response.add_post_render_callback(foo)
        return response


class RegionsListAPIView(ListAPIView):
    queryset = snippets.Region.objects.all()
    serializer_class = serializers.IDNameSerializer
    permission_classes = [SignatureCheckPermission]

    @method_decorator(cache_page(THIRTY_MINUTES_IN_SECONDS))
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
