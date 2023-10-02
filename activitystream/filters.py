from django_filters import NumberFilter, FilterSet
from wagtail.models import Page


class ActivityStreamCMSContentFilter(FilterSet):
    after = NumberFilter(method='filter_after')

    def filter_after(self, queryset, name, value):
        value = value or 0
        return queryset.filter(id__gt=value)

    class Meta:
        model = Page
        fields = ['id']
