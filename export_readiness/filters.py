import django_filters

from export_readiness import models


class ConjoinedCharField(django_filters.CharFilter):
    def filter(self, qs, value):
        if not value:
            return qs
        values = value.split(',')
        for value in values:
            qs &= qs.filter(**{f'{self.field_name}__{self.lookup_expr}': value})
        return qs


class CountryGuideFilter(django_filters.FilterSet):
    region = ConjoinedCharField(field_name='country__region__name', lookup_expr='contains',)
    industry = ConjoinedCharField(field_name='tags__name', lookup_expr='contains')

    class Meta:
        model = models.CountryGuidePage
        fields = ('heading', )
