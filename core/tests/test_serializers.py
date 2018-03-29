import pytest
from rest_framework.serializers import Serializer

from core import permissions, serializers



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
    serializer = serializers.URLHyperlinkSerializer(
        draft_url_attribute='draft_url',
        published_url_attribute='published_url',
    )
    serializer.context = {'request': rf.get('/')}

    actual = serializer.get_attribute(page)

    assert actual == page.published_url


@pytest.mark.django_db
def test_rich_text_serializer(page, rf):
    serializer = serializers.APIRichTextSerializer()

    actual = serializer.to_representation(page)

    assert actual


@pytest.mark.django_db
def test_meta_serializer(page, rf):
    page.slug = 'test-slug'
    class TestSerializer(Serializer):
        meta = serializers.APIMetaSerializer()

    serializer = TestSerializer(
        instance=page,
        context={'request': rf.get('/')}
    )

    assert serializer.data == {
        'meta': {
            'url': 'http://supplier.trade.great:8005/industries/3/test-slug/',
            'slug': 'test-slug',
            'languages': [('en-gb', 'English')]
        }
    }
