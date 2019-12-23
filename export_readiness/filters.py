from django.db.models import Q
import django_filters

from export_readiness import models


class CharFilter(django_filters.CharFilter):
    def filter(self, qs, value):
        if not value:
            return qs
        values = value.split(',')
        if len(values) == 1:
            qs = qs.filter(**{f'{self.field_name}__{self.lookup_expr}': value})
        else:
            q_objects = Q()
            for value in values:
                q_objects |= Q(**{f'{self.field_name}__{self.lookup_expr}': value})
                qs = qs.filter(q_objects)
        return qs.distinct()


class CountryGuideFilter(django_filters.FilterSet):
    region = CharFilter(field_name='country__region__name', lookup_expr='icontains',)
    industry = CharFilter(field_name='tags__name', lookup_expr='icontains')

    class Meta:
        model = models.CountryGuidePage
        fields = ('region', 'industry')
