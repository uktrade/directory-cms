from unittest import mock
import pytest

from great_international.blocks.investment_atlas import (
    DEFAULT_IMAGE_RENDITION_SPEC,
    FeaturedImageBlock,
    InlineOpportunityImageBlock,
    MarkdownBlock,
)

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
