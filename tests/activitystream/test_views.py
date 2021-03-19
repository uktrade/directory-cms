import datetime
from os import environ

import mohawk
import pytest
from freezegun import freeze_time
from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APIClient
from django.conf import settings
from django.utils import timezone

from tests.export_readiness.factories import (
    ArticlePageFactory,
    CountryGuidePageFactory,
    IndustryTagFactory,
    MarketingArticlePageFactory,
)

URL = 'http://testserver' + reverse('activity-stream')
URL_INCORRECT_DOMAIN = 'http://incorrect' + reverse('activity-stream')
URL_INCORRECT_PATH = 'http://testserver' + \
    reverse('activity-stream') + 'incorrect/'
EMPTY_COLLECTION = {
    '@context': 'https://www.w3.org/ns/activitystreams',
    'type': 'Collection',
    'orderedItems': [],
}

# --- Helper Functions ---


@pytest.fixture
def api_client():
    return APIClient()


def article_attribute(activity, attribute):
    return activity['object'][attribute]


def auth_sender(key_id=settings.ACTIVITY_STREAM_ACCESS_KEY_ID,
                secret_key=settings.ACTIVITY_STREAM_SECRET_ACCESS_KEY,
                url=URL, method='GET', content='', content_type=''):
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


# --- Authentication tests ---


@pytest.mark.django_db
def test_empty_object_returned_with_authentication(api_client, en_locale):
    """If the Authorization and X-Forwarded-For headers are correct, then
    the correct, and authentic, data is returned
    """
    sender = auth_sender()
    response = api_client.get(
        URL,
        content_type='',
        HTTP_AUTHORIZATION=sender.request_header,
        HTTP_X_FORWARDED_FOR='1.2.3.4, 123.123.123.123',
    )

    assert response.status_code == status.HTTP_200_OK
    assert response.json() == EMPTY_COLLECTION

    # sender.accept_response will raise an error if the
    # inputs are not valid
    sender.accept_response(
        response_header=response['Server-Authorization'],
        content=response.content,
        content_type=response['Content-Type'],
    )
    with pytest.raises(mohawk.exc.MacMismatch):
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
        reverse('activity-stream'),
        content_type='',
        HTTP_AUTHORIZATION=auth,
        HTTP_X_FORWARDED_FOR='1.2.3.4, 123.123.123.123',
    )

    assert response.status_code == status.HTTP_401_UNAUTHORIZED
    error = {'detail': 'Incorrect authentication credentials.'}
    assert response.json() == error


# --- Content tests ---


@pytest.mark.django_db
def test_lists_live_articles_in_stream(api_client, en_locale):

    # Create the articles
    with freeze_time('2019-01-14 12:00:01'):
        article_a = ArticlePageFactory(
            article_title='Article A',
            article_teaser='Descriptive text',
            article_body_text='Body text',
            last_published_at=timezone.now(),
            slug='article-a')

        article_b = ArticlePageFactory(
            article_title='Article B',
            article_teaser='Descriptive text',
            article_body_text='Body text',
            last_published_at=timezone.now(),
            slug='article-b')

        marketing_article_1 = MarketingArticlePageFactory(
            article_title='Marketing Article One',
            article_teaser='Descriptive text for marketing article',
            article_body_text='Body text for marketing article',
            last_published_at=timezone.now(),
            slug='marketing-article-one',
        )

    with freeze_time('2019-01-14 12:00:02'):
        article_c = ArticlePageFactory(
            article_title='Article C',
            article_teaser='Descriptive text',
            article_body_text='Body text',
            last_published_at=timezone.now(),
            slug='article-c')

        ArticlePageFactory(
            article_title='Article D',
            article_teaser='Non-live Article',
            article_body_text='Body text',
            last_published_at=timezone.now(),
            slug='article-d',
            live=False)

        marketing_article_2 = MarketingArticlePageFactory(
            article_title='Marketing Article Two',
            article_teaser='Descriptive text for second marketing article',
            article_body_text='Body text for second marketing article',
            last_published_at=timezone.now(),
            slug='marketing-article-two',
        )

        # Note CountryGuidePageFactory creates an additional
        # ArticlePage as a related page.
        country_guide_page_e = CountryGuidePageFactory(
            heading='Market Page E',
            sub_heading='Descriptive text',
            section_one_body='Body text',
            last_published_at=timezone.now(),
            slug='article-e')

        tag1 = IndustryTagFactory(name='tag1')
        tag2 = IndustryTagFactory(name='tag2')
        country_guide_page_e.tags = [tag1, tag2]
        country_guide_page_e.save()

    sender = auth_sender()
    response = api_client.get(
        URL,
        content_type='',
        HTTP_AUTHORIZATION=sender.request_header,
        HTTP_X_FORWARDED_FOR='1.2.3.4, 123.123.123.123',
    )
    items = response.json()['orderedItems']

    id_prefix = 'dit:cms:Article:'

    # Three ArticlePages defined above, plus two MarketingArticlePages,
    # plus one CountryGuidePage,
    # Plus the extra ArticlePage created by CountryGuidePageFactory
    assert len(items) == 7

    assert article_attribute(items[0], 'name') == 'Article A'
    assert article_attribute(items[0], 'id') == id_prefix + str(article_a.id)
    assert article_attribute(items[0], 'summary') == 'Descriptive text'
    assert article_attribute(items[0], 'content') == 'Body text'
    assert article_attribute(items[0], 'url') == \
        environ["APP_URL_EXPORT_READINESS"] + '/article-a/'
    assert items[0]['published'] == '2019-01-14T12:00:01+00:00'

    assert article_attribute(items[1], 'name') == 'Article B'
    assert article_attribute(items[1], 'id') == id_prefix + str(article_b.id)
    assert items[1]['published'] == '2019-01-14T12:00:01+00:00'

    assert article_attribute(items[2], 'name') == 'Marketing Article One'
    assert article_attribute(items[2], 'id') == id_prefix + str(marketing_article_1.id)
    assert items[2]['published'] == '2019-01-14T12:00:01+00:00'

    assert article_attribute(items[3], 'name') == 'Article C'
    assert article_attribute(items[3], 'id') == id_prefix + str(article_c.id)
    assert items[3]['published'] == '2019-01-14T12:00:02+00:00'

    assert article_attribute(items[4], 'name') == 'Marketing Article Two'
    assert article_attribute(items[4], 'id') == id_prefix + str(marketing_article_2.id)
    assert items[4]['published'] == '2019-01-14T12:00:02+00:00'

    assert article_attribute(items[5], 'name') == 'Market Page E'
    assert article_attribute(items[5], 'id') == id_prefix + str(country_guide_page_e.id)
    assert items[5]['published'] == '2019-01-14T12:00:02+00:00'
    assert article_attribute(items[5], 'keywords') == 'tag1 tag2'

    # items[6] will be the Article created when the Country Guide page was also made


@pytest.mark.django_db
def test_pagination(api_client, django_assert_num_queries, en_locale):
    """The requests are paginated, ending on a article without a next key
    """

    """ create 50 articles. Second set should appear in feed first. """
    with freeze_time('2012-01-14 12:00:02'):
        for i in range(0, 25):
            ArticlePageFactory(
                article_title='article_' + str(i),
                article_teaser='Descriptive text',
                article_body_text='Body text',
                last_published_at=timezone.now(),
                slug='article-' + str(i)
            )

    with freeze_time('2012-01-14 12:00:01'):
        for i in range(25, 50):
            ArticlePageFactory(
                article_title='article_' + str(i),
                article_teaser='Descriptive text',
                article_body_text='Body text',
                last_published_at=timezone.now(),
                slug='article-' + str(i)
            )

    items = []
    next_url = URL
    num_pages = 0

    """ One query to pull items 0 -> 24,
        Two queries to pull items 25 -> 49 due to filter being used,
        No queries on final blank page
    """
    # TODO: Improve performance of page.url, full_url, full_path
    # Since page.url needs to get the slugs of the article's parent
    # pages it is doing a TON of queries each time this endpoint is hit
    with django_assert_num_queries(55):
        while next_url:
            num_pages += 1
            sender = auth_sender(url=next_url)
            response = api_client.get(
                next_url,
                content_type='',
                HTTP_AUTHORIZATION=sender.request_header,
                HTTP_X_FORWARDED_FOR='1.2.3.4, 123.123.123.123',
            )
            response_json = response.json()
            items += response_json['orderedItems']
            next_url = \
                response_json['next'] if 'next' in response_json else \
                None

    assert num_pages == 3
    assert len(items) == 50
    assert len(set([item['id'] for item in items])) == 50  # All unique
    assert article_attribute(items[49], 'name') == 'article_24'
