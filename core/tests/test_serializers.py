import pytest
from rest_framework.serializers import Serializer

from core import permissions, serializers
from find_a_supplier.tests import factories


@pytest.mark.django_db
def test_markdown_to_html_serializer(page, rf):
    page.slug_en_gb = 'the-slug'
    page.hero_text_en_gb = (
        '[hyperlink](slug:{slug})'.format(slug=page.slug)
    )
    page.save()

    class TestSerializer(Serializer):
        hero_text_en_gb = serializers.APIMarkdownToHTMLSerializer()

    serializer = TestSerializer(
        instance=page,
        context={'request': rf.get('/')}
    )

    assert serializer.data == {
        'hero_text_en_gb': (
            '<p><a href="http://supplier.trade.great:8005/'
            'industries/the-slug/">hyperlink</a></p>'
        )
    }


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
def test_meta_serializer_draft(page, rf):

    class TestSerializer(Serializer):
        meta = serializers.APIMetaSerializer()

    serializer = TestSerializer(
        instance=page,
        context={'request': rf.get('/')}
    )

    request = rf.get('/', {permissions.DraftTokenPermisison.TOKEN_PARAM: '1'})
    serializer = TestSerializer(instance=page, context={'request': request})

    assert serializer.data['meta']['url'] == page.get_url(is_draft=True)


@pytest.mark.django_db
def test_breadcrums_serializer(page, rf):
    factories.IndustryLandingPageFactory(
        breadcrumbs_label_en_gb='label-one'
    )
    factories.IndustryPageFactory(
        breadcrumbs_label_en_gb='label-two'
    )
    factories.LandingPageFactory(
        breadcrumbs_label_en_gb='label-three'
    )
    factories.IndustryContactPageFactory(
        breadcrumbs_label_en_gb='label-four'
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
                'slug': 'industries-landing-page',
                'label': 'label-one'
            },
            'industrycontactpage': {
                'slug': 'industry-contact',
                'label': 'label-four'
            },
            'landingpage': {
                'slug': 'landing-page',
                'label': 'label-three'
            }
        }
    }
