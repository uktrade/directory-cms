import pytest

from core.blocks import InternalOrExternalLinkBlock

pytestmark = pytest.mark.django_db


def test_internal_link_structure_value(international_root_page):
    block = InternalOrExternalLinkBlock()
    value = block.to_python({'internal_link': international_root_page.id})
    assert international_root_page.url_path == value.url


def test_external_link_structure_value():
    block = InternalOrExternalLinkBlock()
    value = block.to_python({'external_link': 'https://great.gov.uk/'})
    assert value.url == 'https://great.gov.uk/'
