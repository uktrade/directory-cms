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


@pytest.mark.django_db
def test_document_field_serialize(high_potential_opportunity_page):

    data = UpstreamModelSerilaizer.serialize(high_potential_opportunity_page)

    assert data['(document)pdf_document'] == (
        high_potential_opportunity_page.pdf_document.file.name
    )


@pytest.mark.django_db
def test_document_field_deserializer(high_potential_opportunity_page):
    serialized_data = {
        '(document)pdf_document': (
            high_potential_opportunity_page.pdf_document.file.name
        )
    }
    actual = UpstreamModelSerilaizer.deserialize(serialized_data)

    assert actual['pdf_document'] == (
        high_potential_opportunity_page.pdf_document.pk
    )
