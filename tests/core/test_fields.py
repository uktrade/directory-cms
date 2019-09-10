import pytest
from django.utils import translation
from rest_framework.serializers import Serializer
from wagtail.core import blocks
from wagtail.core.fields import StreamField

from core import fields
from core import permissions
from find_a_supplier.serializers import IndustryPageSerializer
from tests.find_a_supplier.factories import (IndustryLandingPageFactory, IndustryPageFactory, LandingPageFactory,
                                             IndustryContactPageFactory)


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
    token = page_with_reversion.get_draft_token()
    assert serializer.data['meta']['draft_token'] == token
    assert serializer.data['meta']['languages'] == [
            ('en-gb', 'English'),
            ('de', 'Deutsch'),
            ('ja', '日本語'),
            ('zh-hans', '简体中文'),
            ('fr', 'Français'),
            ('es', 'español'),
            ('pt', 'Português'),
            ('ar', 'العربيّة'),
    ]
    assert sorted(serializer.data['meta']['localised_urls']) == [
        ('ar', '{}{}'.format(url, '?lang=ar')),
        ('de', '{}{}'.format(url, '?lang=de')),
        ('en-gb', url),
        ('es', '{}{}'.format(url, '?lang=es')),
        ('fr', '{}{}'.format(url, '?lang=fr')),
        ('ja', '{}{}'.format(url, '?lang=ja')),
        ('pt', '{}{}'.format(url, '?lang=pt')),
        ('zh-hans', '{}{}'.format(url, '?lang=zh-hans')),
    ]


@pytest.mark.django_db
def test_meta_field_draft(page, rf):
    request = rf.get('/', {permissions.DraftTokenPermisison.TOKEN_PARAM: '1'})
    serializer = IndustryPageSerializer(
        instance=page,
        context={'request': request}
    )

    assert serializer.data['meta']['url'] == page.get_url(is_draft=True)


@pytest.mark.django_db
def test_markdown_to_html_field_without_slug_hyperlinks(page, rf):
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
            '<p><a>hyperlink</a></p>'
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


@pytest.mark.django_db
def test_single_struct_block_stream_field_factory():
    field = fields.single_struct_block_stream_field_factory(
        'test',
        block_class=blocks.TextBlock,
        max_num=6,
        min_num=1,
        null=True,
        blank=True
    )
    assert isinstance(field, StreamField)
    assert field.null is True
    assert field.blank is True
    assert field.stream_block._constructor_kwargs == {'max_num': 6, 'min_num': 1}
    assert isinstance(field.stream_block.child_blocks['test'], blocks.TextBlock)
