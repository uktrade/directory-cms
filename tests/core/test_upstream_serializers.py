from unittest import mock

import pytest

from django.contrib.messages.storage.fallback import FallbackStorage
from django.http import HttpRequest

from core.upstream_serializers import UpstreamModelSerializer
from tests.export_readiness.factories import (
    TagFactory
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
