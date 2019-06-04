from functools import reduce
import operator

import django_filters
from wagtail.core.models import PAGE_MODEL_CLASSES, Page

from django.db.models import Q


class ServiceNameFilter(django_filters.FilterSet):
    service_name = django_filters.CharFilter(method='filter_service_name')

    class Meta:
        model = Page
        fields = ['service_name']

    def filter_service_name(self, queryset, name, value):

        concrete_page_model_names = [
            model._meta.model_name
            for model in PAGE_MODEL_CLASSES if(
                not model._meta.abstract and
                hasattr(model, 'service_name_value')
            )
        ]
        queries = (
            Q(**{model_name + '__service_name': value})
            for model_name in concrete_page_model_names
        )
        return queryset.filter(reduce(operator.or_, queries))


class ServiceNameDRFFilter(django_filters.rest_framework.FilterSet,
                           ServiceNameFilter):
    pass
