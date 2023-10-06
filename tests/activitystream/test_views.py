import datetime
import mohawk
import pytest
from django.conf import settings
from django.utils import timezone
from freezegun import freeze_time
from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APIClient
from activitystream.authentication import NO_CREDENTIALS_MESSAGE
from core.models import RoutingSettings
from wagtail.models import Site, Page

URL = 'http://testserver' + reverse('activitystream:cms-content')
URL_INCORRECT_DOMAIN = 'http://incorrect' + reverse('activitystream:cms-content')
URL_INCORRECT_PATH = 'http://testserver' + reverse('activitystream:cms-content') + 'incorrect/'
EMPTY_COLLECTION = {
    '@context': 'https://www.w3.org/ns/activitystreams',
    'type': 'Collection',
    'orderedItems': [],
}


@pytest.fixture
def api_client():
    return APIClient()


def article_attribute(activity, attribute):
    return activity['object'][attribute]


def auth_sender(
    key_id=settings.ACTIVITY_STREAM_ACCESS_KEY_ID,
    secret_key=settings.ACTIVITY_STREAM_SECRET_ACCESS_KEY,
    url=URL,
    method='GET',
    content='',
    content_type='',
):
    credentials = {
        'id': key_id,
        'key': secret_key,
        'algorithm': 'sha256',
    }

    return mohawk.Sender(
        credentials,
        url,
        method,
        content=content,
        content_type=content_type,
    )


@pytest.mark.django_db
def test_site_pages_returned_with_authentication(api_client, en_locale):
    """If the Authorization and X-Forwarded-For headers are correct, then
    the correct, and authentic, data is returned
    """
    Page.objects.all().update(url_path = '/great-international-home/')

    sender = auth_sender()
    response = api_client.get(
        URL,
        content_type='',
        HTTP_AUTHORIZATION=sender.request_header,
        HTTP_X_FORWARDED_FOR='1.2.3.4, 123.123.123.123',
    )

    assert response.status_code == status.HTTP_200_OK
    body = response.json()
    assert body['@context'] == 'https://www.w3.org/ns/activitystreams'
    assert body['type'] == 'Collection'
    assert len(body['orderedItems']) == 3

    # sender.accept_response will raise an error if the
    # inputs are not valid
    sender.accept_response(
        response_header=response['Server-Authorization'],
        content=response.content,
        content_type=response['Content-Type'],
    )
    with pytest.raises(mohawk.exc.MacMismatch):
        sender.accept_response(
            response_header=(
                response['Server-Authorization'][:-12] + 'incorrect' + response['Server-Authorization'][-3:]
            ),
            content=response.content,
            content_type=response['Content-Type'],
        )
    with pytest.raises(mohawk.exc.BadHeaderValue):
        sender.accept_response(
            response_header=response['Server-Authorization'] + 'incorrect',
            content=response.content,
            content_type=response['Content-Type'],
        )
    with pytest.raises(mohawk.exc.MisComputedContentHash):
        sender.accept_response(
            response_header=response['Server-Authorization'],
            content='incorrect',
            content_type=response['Content-Type'],
        )
    with pytest.raises(mohawk.exc.MisComputedContentHash):
        sender.accept_response(
            response_header=response['Server-Authorization'],
            content=response.content,
            content_type='incorrect',
        )


@pytest.mark.django_db
def test_authentication_fails_if_url_mismatched(api_client, en_locale):
    """Creates a Hawk header with incorrect domain"""
    sender = auth_sender(url=URL_INCORRECT_DOMAIN)
    response = api_client.get(
        URL,
        content_type='',
        HTTP_AUTHORIZATION=sender.request_header,
        HTTP_X_FORWARDED_FOR='1.2.3.4, 123.123.123.123',
    )

    assert response.status_code == status.HTTP_401_UNAUTHORIZED

    """Creates a Hawk header with incorrect path"""
    sender = auth_sender(url=URL_INCORRECT_PATH)
    response = api_client.get(
        URL,
        content_type='',
        HTTP_AUTHORIZATION=sender.request_header,
        HTTP_X_FORWARDED_FOR='1.2.3.4, 123.123.123.123',
    )

    assert response.status_code == status.HTTP_401_UNAUTHORIZED


@pytest.mark.django_db
def test_if_61_seconds_in_past_401_returned(api_client, en_locale):
    """If the Authorization header is generated 61 seconds in the past, then a
    401 is returned
    """
    past = timezone.now() - datetime.timedelta(seconds=61)
    with freeze_time(past):
        auth = auth_sender().request_header

    response = api_client.get(
        reverse('activitystream:cms-content'),
        content_type='',
        HTTP_AUTHORIZATION=auth,
        HTTP_X_FORWARDED_FOR='1.2.3.4, 123.123.123.123',
    )

    assert response.status_code == status.HTTP_401_UNAUTHORIZED
    error = {'detail': 'Incorrect authentication credentials.'}
    assert response.json() == error


@pytest.mark.django_db
def test_error_for_no_authorization_field_in_header(api_client):
    response = api_client.get(
        URL,
        content_type='',
        HTTP_X_FORWARDED_FOR='1.2.3.4, 123.123.123.123',
    )
    assert response.status_code == 401
    assert response.json()['detail'] == NO_CREDENTIALS_MESSAGE
