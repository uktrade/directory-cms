import pytest
from activitystream.pagination import ActivityStreamCMSContentPagination
from wagtail.models import Page
from unittest.mock import MagicMock


@pytest.mark.django_db
def test_get_next_link(international_site, monkeypatch):
    monkeypatch.setattr(ActivityStreamCMSContentPagination, 'page_size', 2)
    request = MagicMock()

    queryset = Page.objects.all()
    pagination_instance = ActivityStreamCMSContentPagination()
    pagination_instance.paginate_queryset(queryset, request)
    next_link = pagination_instance.get_next_link()

    assert '?after=2' in next_link['next']
