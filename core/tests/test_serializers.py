from core import permissions, serializers

import pytest


@pytest.mark.django_db
def test_url_hyperlink_serializer_draft(page, rf):
    request = rf.get('/', {permissions.DraftTokenPermisison.TOKEN_PARAM: '1'})
    serializer = serializers.URLHyperlinkSerializer(
        draft_url_attribute='draft_url',
        published_url_attribute='published_url',
    )
    serializer.context = {'request': request}

    actual = serializer.get_attribute(page)

    assert actual == page.draft_url


@pytest.mark.django_db
def test_url_hyperlink_serializer_published(page, rf):
    request = rf.get('/')
    serializer = serializers.URLHyperlinkSerializer(
        draft_url_attribute='draft_url',
        published_url_attribute='published_url',
    )
    serializer.context = {'request': request}

    actual = serializer.get_attribute(page)

    assert actual == page.published_url
