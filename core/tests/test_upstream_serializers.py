from django.forms import ValidationError

from core.upstream_serializers import UpstreamModelSerilaizer

import pytest

from export_readiness.tests.factories import (
    ArticlePageFactory, CountryGuidePageFactory
)


@pytest.fixture
def article_page():
    return ArticlePageFactory()


@pytest.fixture
def country_guide_page(article_page):
    return CountryGuidePageFactory(
        related_page_one=article_page
    )


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


@pytest.mark.django_db
def test_related_page_field_serialize(country_guide_page):

    data = UpstreamModelSerilaizer.serialize(country_guide_page)

    assert data['(page)related_page_one'] == (
        country_guide_page.related_page_one.slug
    )


@pytest.mark.django_db
def test_related_page_field_deserializer(article_page):
    serialized_data = {
        '(page)related_page_one': article_page.slug
    }
    actual = UpstreamModelSerilaizer.deserialize(serialized_data)

    assert actual['related_page_one'] == article_page


@pytest.mark.django_db
def test_related_page_field_deserializer(article_page):
    serialized_data = {
        '(page)related_page_one': 'some-missing-slug'
    }

    with pytest.raises(ValidationError):
        UpstreamModelSerilaizer.deserialize(serialized_data)
