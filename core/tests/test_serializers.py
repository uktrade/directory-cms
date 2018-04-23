import pytest
from rest_framework.serializers import Serializer

from core import permissions, serializers
from find_a_supplier.tests import factories


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
            'url': 'http://supplier.trade.great:8005/industries/test-slug/',
            'localised_urls': [
                (
                    'en-gb',
                    'http://supplier.trade.great:8005/industries/test-slug/'
                )
            ],
            'slug': 'test-slug',
            'pk': page.pk,
        }
    }


@pytest.mark.django_db
def test_breadcrums_serializer(page, rf):
    factories.IndustryLandingPageFactory(
        slug_en_gb='slug-one', breadcrumbs_label_en_gb='label-one'
    )
    factories.IndustryPageFactory(
        slug_en_gb='slug-two', breadcrumbs_label_en_gb='label-two'
    )
    factories.LandingPageFactory(
        slug_en_gb='slug-three', breadcrumbs_label_en_gb='label-three'
    )
    factories.IndustryContactPageFactory(
        slug_en_gb='slug-four', breadcrumbs_label_en_gb='label-four'
    )

    class TestSerializer(Serializer):
        breadcrumbs = serializers.APIBreadcrumsSerializer(
            app_label='find_a_supplier'
        )

    serializer = TestSerializer(
        instance=page,
        context={'request': rf.get('/')}
    )

    assert serializer.data == {
        'breadcrumbs': {
            'industrylandingpage': {
                'slug': 'slug-one',
                'label': 'label-one'
            },
            'industrycontactpage': {
                'slug': 'slug-four',
                'label': 'label-four'
            },
            'landingpage': {
                'slug': 'slug-three',
                'label': 'label-three'
            }
        }
    }
