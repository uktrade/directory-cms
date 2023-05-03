from unittest import mock

import pytest
from django.test import override_settings
from wagtail.blocks import StreamBlock

from core.blocks import DEFAULT_IMAGE_RENDITION_SPEC, GreatMediaBlock
from great_international.blocks.great_international import FeaturedImageBlock, MarkdownBlock
from great_international.blocks.investment_atlas import (
    InlineOpportunityImageBlock,
    ReusableSnippetChooserBlock,
    _get_block_for_block_name,
)
from great_international.models.investment_atlas import ReusableContentSection
from tests.core.helpers import make_test_video

from .factories import ReusableContentSectionFactory

pytestmark = pytest.mark.django_db


@pytest.mark.parametrize('rendition_spec', ('None', 'fill-1200x200', 'SKIP'))
def test_featured_image_block__get_api_representation(rendition_spec):

    block = FeaturedImageBlock()
    mock_image = mock.Mock()
    mock_image.get_rendition = mock.Mock()
    mock_rendition = mock.Mock()
    mock_rendition.url = 'https://example.com/path/to/image-max123x456.jpg'
    mock_image.get_rendition.return_value = mock_rendition

    faked_block_value = dict(
        image=mock_image,
        image_alt='image alt text',
        caption='caption text',
    )

    expected = {
        'image': 'https://example.com/path/to/image-max123x456.jpg',
        'image_alt': 'image alt text',
        'caption': 'caption text',
    }

    context = {}
    if rendition_spec != 'SKIP':
        context.update({'rendition_spec': rendition_spec})

    assert block.get_api_representation(value=faked_block_value, context=context) == expected

    if rendition_spec != 'SKIP':
        mock_image.get_rendition.assert_called_once_with(rendition_spec)
    else:
        mock_image.get_rendition.assert_called_once_with(DEFAULT_IMAGE_RENDITION_SPEC)


@pytest.mark.parametrize('rendition_spec', ('None', 'fill-1200x200', 'SKIP'))
def test_featured_image_block__get_api_representation__no_data(rendition_spec):
    block = FeaturedImageBlock()

    faked_block_value = dict()
    expected = dict()

    context = {}
    if rendition_spec != 'SKIP':
        context.update({'rendition_spec': rendition_spec})

    assert block.get_api_representation(value=faked_block_value, context=context) == expected


@pytest.mark.parametrize('rendition_spec', ('None', 'fill-1200x200', 'SKIP'))
def test_inline_image_block__get_api_representation(rendition_spec):
    block = InlineOpportunityImageBlock()
    mock_image = mock.Mock()
    mock_image.get_rendition = mock.Mock()
    mock_rendition = mock.Mock()
    mock_rendition.url = 'https://example.com/path/to/image-max123x456.jpg'
    mock_image.get_rendition.return_value = mock_rendition

    faked_block_value = dict(
        image=mock_image,
        image_alt='image alt text',
        caption='caption text',
        custom_css_class='custom_css_class-one'
    )

    expected = {
        'image': 'https://example.com/path/to/image-max123x456.jpg',
        'image_alt': 'image alt text',
        'caption': 'caption text',
        'custom_css_class': 'custom_css_class-one',
    }

    context = {}
    if rendition_spec != 'SKIP':
        context.update({'rendition_spec': rendition_spec})

    assert block.get_api_representation(value=faked_block_value, context=context) == expected

    if rendition_spec != 'SKIP':
        mock_image.get_rendition.assert_called_once_with(rendition_spec)
    else:
        mock_image.get_rendition.assert_called_once_with(DEFAULT_IMAGE_RENDITION_SPEC)


@pytest.mark.parametrize('rendition_spec', ('None', 'fill-1200x200', 'SKIP'))
def test_inline_image_block__get_api_representation__no_data(rendition_spec):

    block = InlineOpportunityImageBlock()

    faked_block_value = dict()
    expected = dict()

    context = {}
    if rendition_spec != 'SKIP':
        context.update({'rendition_spec': rendition_spec})

    assert block.get_api_representation(value=faked_block_value, context=context) == expected


def test_markdown_block__get_api_representation():
    block = MarkdownBlock()
    # show that the markdown is turned to HTML, that's all we need here
    assert block.get_api_representation(value='**hello world**') == '<p><strong>hello world</strong></p>'


def test_markdown__get_api_representation__no_data():
    block = MarkdownBlock()
    assert block.get_api_representation(value='') == ''
    assert block.get_api_representation(value=None) == ''


@override_settings(WAGTAILMEDIA_MEDIA_MODEL="core.GreatMedia")
@pytest.mark.django_db
def test_video_block_get_api_representation():
    video = make_test_video(transcript='Test transcript', subtitles='test subtitle')
    video.save()
    block = GreatMediaBlock()

    block_response = block.get_api_representation(value=video)
    assert block_response == {
        'title': 'Test file',
        'transcript': 'Test transcript',
        'sources': [
            {
                'src': video.url,
                'type': 'video/mp4',
                'transcript': 'Test transcript'
            }
        ],
        'url': video.url,
        'thumbnail': None,
        'subtitles': [{
            'default': False,
            'label': 'English',
            'srclang': 'en',
            'url': '/subtitles/1/en/content.vtt'}]
    }
    # for empty video
    block_response = block.get_api_representation(value=None)
    assert block_response == {}


@pytest.mark.parametrize(
    'block_name,expected_class',
    (
        ('text', MarkdownBlock),
        ('image', InlineOpportunityImageBlock),
        ('columns', StreamBlock),
        ('absent_from_spec', None),
    )
)
def test_get_block_for_block_name(block_name, expected_class):

    block = _get_block_for_block_name(block_name)

    if block_name == 'absent_from_spec':
        assert block is None
    else:
        assert block.__class__ == expected_class


def test_reusable_snippet_chooser_block__get_api_representation():

    snippet = ReusableContentSectionFactory()
    assert all([snippet.title, snippet.block_slug])
    # The factory bootstraps some values, but let's add some streamfield spec to the snippet too

    snippet.content = [
        ('text', '##Hello world.\n*bold* text'),
        ('text', 'Line of text here.')
    ]

    block = ReusableSnippetChooserBlock(ReusableContentSection)

    assert block.get_api_representation(value=snippet) == {
        'block_slug': snippet.block_slug,
        'content': [
            {
                "type": "text",
                "value": "<h2>Hello world.</h2>\n<p><em>bold</em> text</p>",  # light check the MarkdownBlock was used
                "id": None  # IDs are set when a streamfield is saved
            },
            {
                "type": "text",
                "value": "<p>Line of text here.</p>",
                "id": None  # IDs are set when a streamfield is saved
            },
        ]
    }


def test_reusable_snippet_chooser_block__get_api_representation__null_value():
    block = ReusableSnippetChooserBlock(ReusableContentSection)
    assert block.get_api_representation(value=None) == {}
