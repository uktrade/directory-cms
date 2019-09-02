import json
from unittest import mock

from directory_constants import cms
import pytest

from django.contrib.messages.storage.fallback import FallbackStorage
from django.http import HttpRequest

from core.upstream_serializers import UpstreamModelSerializer
from tests.export_readiness.factories import (
    ArticlePageFactory, CountryGuidePageFactory,
    TopicLandingPageFactory, ArticleListingPageFactory,
    HomePageFactory, TagFactory
)


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
def test_list_serializer(international_root_page):
    data = UpstreamModelSerializer.serialize(international_root_page)
    assert data['(image)hero_image'] == (
        international_root_page.hero_image.file.name
    )


@pytest.mark.django_db
@mock.patch('core.views.PreloadPageView.get_form_kwargs', mock.Mock())
def test_list_deserializer(rf, international_root_page):
    serialized_data = {
        '(list)search_filter_sector': international_root_page.search_filter_sector[0],
    }

    actual = UpstreamModelSerializer.deserialize(serialized_data, rf)

    assert actual['search_filter_sector'] == international_root_page.search_filter_sector


@pytest.mark.django_db
def test_tag_serializer(root_page):
    legal = TagFactory.create(name='Legal')
    eagle = TagFactory.create(name='Eagle')

    page = ArticlePageFactory(
        parent=root_page,
        slug='related-slug',
        tags=[legal, eagle]
    )

    data = UpstreamModelSerializer.serialize(page)
    assert data['(tag)tags'] == 'Legal,Eagle'


@pytest.mark.django_db
@mock.patch('core.views.PreloadPageView.get_form_kwargs', mock.Mock())
def test_tag_deserializer(rf):
    legal = TagFactory.create(name='Legal')
    eagle = TagFactory.create(name='Eagle')
    serialized_data = {
        '(tag)tags': 'Legal,Eagle'
    }

    actual = UpstreamModelSerializer.deserialize(serialized_data, rf)

    assert len(actual['tags']) == 2
    assert legal in actual['tags']
    assert eagle in actual['tags']


@pytest.mark.django_db
def test_document_field_serialize(high_potential_opportunity_page):

    data = UpstreamModelSerializer.serialize(high_potential_opportunity_page)

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
    actual = UpstreamModelSerializer.deserialize(serialized_data, rf)

    assert actual['pdf_document'] == (
        high_potential_opportunity_page.pdf_document.pk
    )


@pytest.mark.django_db
def test_related_page_field_serialize(country_guide_page):

    data = UpstreamModelSerializer.serialize(country_guide_page)

    assert data['(page)related_page_one'] == json.dumps(
        {
            'slug': country_guide_page.related_page_one.slug,
            'service_name_value': (
                country_guide_page.related_page_one.service_name_value),
        }
    )


@pytest.mark.django_db
def test_related_page_field_deserializer(rf, root_page):
    domestic_homepage = HomePageFactory(parent=root_page)
    topic_page = TopicLandingPageFactory(parent=domestic_homepage)
    article_list_page = ArticleListingPageFactory(parent=topic_page)

    article_page = ArticlePageFactory(
        parent=article_list_page,
        slug='related-slug')

    serialized_data = {
        '(page)related_page_one': json.dumps({
            'slug': 'related-slug',
            'service_name_value': article_page.specific.service_name_value,
        })
    }

    actual = UpstreamModelSerializer.deserialize(serialized_data, rf)

    assert actual['related_page_one'].specific == article_page


@pytest.mark.django_db
def test_related_page_field_deserializer_invalid_slug(root_page):
    HomePageFactory(parent=root_page)
    missing_slug = 'some-missing-slug'

    serialized_data = {
        '(page)related_page_one': json.dumps({
            'slug': missing_slug,
            'service_name_value': cms.EXPORT_READINESS,
        })
    }

    request = RequestWithMessages()

    UpstreamModelSerializer.deserialize(serialized_data, request)

    message_string = (
        f"Related page with the slug {missing_slug} could not be "
        "found in this environment. Please create it then "
        "add it as one of this page's related pages.")

    assert request.get_message_strings()[0] == message_string
