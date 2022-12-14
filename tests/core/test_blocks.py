import pytest

from core.blocks import InternalOrExternalLinkBlock
from core.blocks_serializers import ColumnWithTitleIconTextBlockStreamChildBaseSerializer

pytestmark = pytest.mark.django_db


def test_internal_or_external_link_block__custom_get_api_representation(
    international_root_page,
):

    assert international_root_page.get_url() is not None

    block = InternalOrExternalLinkBlock()

    # single internal URL configured
    assert block.get_api_representation(
        {'internal_link': international_root_page}
    ) == international_root_page.get_url()

    # single external URL configured
    assert block.get_api_representation(
        {'external_link': 'https://www.example.com/external/'}
    ) == 'https://www.example.com/external/'

    # single internal URL configured, external null
    assert block.get_api_representation(
        {
            'internal_link': international_root_page,
            'external_link': ''
        }
    ) == international_root_page.get_url()

    # single external URL configured, internal null
    assert block.get_api_representation(
        {
            'internal_link': None,
            'external_link': 'https://www.example.com/external/'
        }
    ) == 'https://www.example.com/external/'

    # Both URLs configured, internal is the one that is used
    assert block.get_api_representation(
        {
            'internal_link': international_root_page,
            'external_link': 'https://www.example.com/external/'
        }
    ) == international_root_page.get_url()


def test_block_serializer(
    international_root_page,
):

    block = ColumnWithTitleIconTextBlockStreamChildBaseSerializer()
    assert block is not None
