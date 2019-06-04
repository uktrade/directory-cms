import django_filters
from django.contrib.contenttypes.models import ContentType
from wagtail.core.models import PAGE_MODEL_CLASSES, Page


class ServiceNameFilter(django_filters.FilterSet):
    service_name = django_filters.CharFilter(method='filter_service_name')

    class Meta:
        model = Page
        fields = ['service_name']

    def filter_service_name(self, queryset, name, value):
        relevant_models = [
            model for model in PAGE_MODEL_CLASSES if (
                not model._meta.abstract and
                getattr(model, 'service_name_value', '') == value
            )
        ]
        ctype_ids = [
            ctype.id for ctype in
            ContentType.objects.get_for_models(*relevant_models).values()
        ]
        return queryset.filter(content_type_id__in=ctype_ids)


class ServiceNameDRFFilter(django_filters.rest_framework.FilterSet,
                           ServiceNameFilter):
    pass
