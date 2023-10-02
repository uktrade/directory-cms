import pytest
from activitystream.filters import ActivityStreamCMSContentFilter
from wagtail.models import Page


@pytest.mark.django_db
def test_cms_content_filter(international_site):
    queryset = Page.objects.all()
    assert queryset.count() == 3
    filtered = ActivityStreamCMSContentFilter().filter_after(queryset, '', 1)
    assert filtered.count() == 2
    assert filtered[0].id == 2
    assert filtered[1].id == 3
