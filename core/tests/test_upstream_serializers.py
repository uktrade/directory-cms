import pytest
from unittest import mock

from django.contrib.messages.storage.fallback import FallbackStorage

from core.upstream_serializers import UpstreamModelSerilaizer
from export_readiness.tests.factories import (
    ArticlePageFactory, CountryGuidePageFactory
)
from django.http import HttpRequest


class RequestWithMessages(HttpRequest):
    session = 'session'

    def __init__(self):
        super(RequestWithMessages, self).__init__()
        self._messages = FallbackStorage(self)

    def get_messages(self):
        return getattr(self._messages, '_queued_messages')

    def get_message_strings(self):
        return [str(m) for m in self.get_messages()]


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
@mock.patch('core.views.PreloadPageView.get_form_kwargs')
def test_upstream_model_deserializer(mock_get_form_kwargs, rf, page):
    serialized_data = {
        '(list)search_filter_sector': page.search_filter_sector[0],
    }

    actual = UpstreamModelSerilaizer.deserialize(serialized_data, rf)

    assert actual['search_filter_sector'] == page.search_filter_sector


@pytest.mark.django_db
def test_document_field_serialize(high_potential_opportunity_page):

    data = UpstreamModelSerilaizer.serialize(high_potential_opportunity_page)

    assert data['(document)pdf_document'] == (
        high_potential_opportunity_page.pdf_document.file.name
    )


@pytest.mark.django_db
def test_document_field_deserializer(rf, high_potential_opportunity_page):
    serialized_data = {
        '(document)pdf_document': (
            high_potential_opportunity_page.pdf_document.file.name
        )
    }
    actual = UpstreamModelSerilaizer.deserialize(serialized_data, rf)

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
def test_related_page_field_deserializer(rf, article_page):
    serialized_data = {
        '(page)related_page_one': article_page.slug
    }
    actual = UpstreamModelSerilaizer.deserialize(serialized_data, rf)

    assert actual['related_page_one'] == article_page


@pytest.mark.django_db
def test_related_page_field_deserializer_invalid_slug(rf):
    missing_slug = 'some-missing-slug'

    serialized_data = {
        '(page)related_page_one': missing_slug
    }

    request = RequestWithMessages()

    UpstreamModelSerilaizer.deserialize(serialized_data, request)

    message_string = (
        f"Related page with the slug {missing_slug} could not be "
        "found in this environment. Please create it then "
        "add it as one of this page's related pages.")

    assert request.get_message_strings()[0] == message_string
