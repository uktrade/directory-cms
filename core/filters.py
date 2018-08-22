from functools import reduce
import operator

import django_filters
from wagtail.core.models import Page

from django.db.models import Q

from core.models import BasePage


class ServiceNameFilter(django_filters.FilterSet):
    service_name = django_filters.CharFilter(
        name='service_name', method='filter_service_name',
    )

    def filter_service_name(self, queryset, name, value):
        concrete_model_names = [
            concrete_model_class._meta.model_name
            for concrete_model_class in BasePage.__subclasses__()
        ]
        queries = (
            Q(**{concrete_model_name + '__service_name': value})
            for concrete_model_name in concrete_model_names
        )
        return queryset.filter(reduce(operator.or_, queries))

    class Meta:
        model = Page
        fields = ['service_name']


class ServiceNameDRFFilter(django_filters.rest_framework.FilterSet,
                           ServiceNameFilter):
    pass
