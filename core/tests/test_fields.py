import pytest
from django.utils import translation
from rest_framework.serializers import Serializer

from core import fields
from core import permissions
from find_a_supplier.serializers import IndustryPageSerializer
from find_a_supplier.tests.factories import (
    IndustryLandingPageFactory, IndustryPageFactory,
    LandingPageFactory, IndustryContactPageFactory,
)


@pytest.mark.django_db
def test_meta_field(rf, root_page):
    fas_industry_page = IndustryPageFactory(
        parent=root_page,
        slug='test-slug',
    )

    serializer = IndustryPageSerializer(
        instance=fas_industry_page,
        context={'request': rf.get('/')}
    )
    assert serializer.data['meta'] == {
        'draft_token': None,
        'languages': [('en-gb', 'English')],
        'url': 'http://supplier.trade.great:8005/test-slug/',
        'localised_urls': [
            (
                'en-gb',
                'http://supplier.trade.great:8005/test-slug/'
            )
        ],
        'slug': 'test-slug',
        'pk': fas_industry_page.pk
    }


@pytest.mark.django_db
def test_meta_field_slug_translation(page, rf):
    page.slug = 'test-slug-en'
    page.pk = 4

    with translation.override('de'):
        serializer = IndustryPageSerializer(
            instance=page,
            context={'request': rf.get('/')}
        )
        data = serializer.data['meta']

    assert data == {
        'draft_token': None,
        'languages': [('en-gb', 'English')],
        'url': 'http://supplier.trade.great:8005/test-slug-en/',
        'localised_urls': [
            (
                'en-gb',
                'http://supplier.trade.great:8005/test-slug-en/'
            )
        ],
        'slug': 'test-slug-en',
        'pk': page.pk,
    }


@pytest.mark.django_db
def test_meta_field_contains_draft_token(page_with_reversion, rf):
    page_with_reversion.slug = 'test-slug'
    page_with_reversion.pk = 4

    serializer = IndustryPageSerializer(
        instance=page_with_reversion,
        context={'request': rf.get('/')}
    )

    url = 'http://supplier.trade.great:8005/test-slug/'
    assert serializer.data['meta'] == {
        'draft_token': page_with_reversion.get_draft_token(),
        'languages': [
            ('en-gb', 'English'),
            ('de', 'Deutsch'),
            ('ja', '日本語'),
            ('zh-hans', '简体中文'),
            ('fr', 'Français'),
            ('es', 'español'),
            ('pt', 'Português'),
            ('ar', 'العربيّة'),
        ],
        'url': url,
        'localised_urls': [
            ('en-gb', url),
            ('de', '{}{}'.format(url, '?lang=de')),
            ('ja', '{}{}'.format(url, '?lang=ja')),
            ('ru', '{}{}'.format(url, '?lang=ru')),
            ('zh-hans', '{}{}'.format(url, '?lang=zh-hans')),
            ('fr', '{}{}'.format(url, '?lang=fr')),
            ('es', '{}{}'.format(url, '?lang=es')),
            ('pt', '{}{}'.format(url, '?lang=pt')),
            ('pt-br', '{}{}'.format(url, '?lang=pt-br')),
            ('ar', '{}{}'.format(url, '?lang=ar'))
        ],
        'slug': 'test-slug',
        'pk': page_with_reversion.pk,
    }


@pytest.mark.django_db
def test_meta_field_draft(page, rf):
    request = rf.get('/', {permissions.DraftTokenPermisison.TOKEN_PARAM: '1'})
    serializer = IndustryPageSerializer(
        instance=page,
        context={'request': request}
    )

    assert serializer.data['meta']['url'] == page.get_url(is_draft=True)


@pytest.mark.django_db
def test_markdown_to_html_field(page, rf):
    page.hero_text_en_gb = (
        '[hyperlink](slug:{slug})'.format(slug=page.slug)
    )

    class TestSerializer(Serializer):
        hero_text_en_gb = fields.MarkdownToHTMLField()

    serializer = TestSerializer(
        instance=page,
        context={'request': rf.get('/')}
    )

    assert serializer.data == {
        'hero_text_en_gb': (
            '<p><a href="http://supplier.trade.great:8005/'
            'the-slug/">hyperlink</a></p>'
        )
    }


@pytest.mark.django_db
def test_breadcrumbs_field(page, rf):
    IndustryLandingPageFactory(breadcrumbs_label_en_gb='label-one')
    IndustryPageFactory(breadcrumbs_label_en_gb='label-two')
    LandingPageFactory(breadcrumbs_label_en_gb='label-three')
    IndustryContactPageFactory(breadcrumbs_label_en_gb='label-four')

    serializer = IndustryPageSerializer(
        instance=page,
        context={'request': rf.get('/')}
    )

    assert serializer.data['breadcrumbs'] == {
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
