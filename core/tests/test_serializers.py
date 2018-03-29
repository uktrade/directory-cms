import pytest
from rest_framework.serializers import Serializer

from core import permissions, serializers


@pytest.mark.django_db
def test_url_hyperlink_serializer_draft(page, rf):

    class TestSerializer(Serializer):
        url = serializers.URLHyperlinkSerializer()

    request = rf.get('/', {permissions.DraftTokenPermisison.TOKEN_PARAM: '1'})
    serializer = TestSerializer(instance=page, context={'request': request})

    assert serializer.data['url'] == page.get_url(
        is_draft=True
    )


@pytest.mark.django_db
def test_url_hyperlink_serializer_published(page, rf):

    class TestSerializer(Serializer):
        url = serializers.URLHyperlinkSerializer()

    serializer = TestSerializer(
        instance=page, context={'request': rf.get('/')}
    )

    assert serializer.data['url'] == page.get_url()


@pytest.mark.django_db
def test_rich_text_serializer(page, rf):
    serializer = serializers.APIRichTextSerializer()

    actual = serializer.to_representation(page)

    assert actual


@pytest.mark.django_db
def test_meta_serializer(page, rf):
    page.slug = 'test-slug'
    page.pk = 4

    class TestSerializer(Serializer):
        meta = serializers.APIMetaSerializer()

    serializer = TestSerializer(
        instance=page,
        context={'request': rf.get('/')}
    )

    assert serializer.data == {
        'meta': {
            'languages': [('en-gb', 'English')],
            'url': 'http://supplier.trade.great:8005/industries/4/test-slug/',
            'localised_urls': [
                (
                    'en-gb',
                    'http://supplier.trade.great:8005/industries/4/test-slug/'
                )
            ],
            'slug': 'test-slug'
        }
    }
