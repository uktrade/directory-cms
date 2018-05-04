from core.upstream_serializers import UpstreamModelSerilaizer

import pytest


@pytest.mark.django_db
def test_upstream_model_serializer(page):
    data = UpstreamModelSerilaizer.serialize(page)
    assert data['(image)introduction_column_one_icon'] == (
        page.introduction_column_one_icon.file.name
    )
    assert data['(list)search_filter_sector'] == page.search_filter_sector[0]


@pytest.mark.django_db
def test_upstream_model_deserializer(page):
    serialized_data = {
        '(list)search_filter_sector': page.search_filter_sector[0],
    }
    actual = UpstreamModelSerilaizer.deserialize(serialized_data)

    assert actual['search_filter_sector'] == page.search_filter_sector
