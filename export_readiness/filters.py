import django_filters

from export_readiness import models


class CharFilter(django_filters.CharFilter):
    def filter(self, qs, value):
        if not value:
            return qs
        values = value.split(',')
        for value in values:
            qs |= qs.filter(**{f'{self.field_name}__{self.lookup_expr}': value})
        return qs.distinct()


class CountryGuideFilter(django_filters.FilterSet):
    region = CharFilter(field_name='country__region__name', lookup_expr='icontains',)
    industry = CharFilter(field_name='tags__name', lookup_expr='icontains')

    class Meta:
        model = models.CountryGuidePage
        fields = ('region', 'industry')
