from unittest.mock import patch

from wagtail.wagtailimages.api.fields import ImageRenditionField
from core import fields


@patch.object(ImageRenditionField, 'to_representation')
def test_absolute_url_image_field(mock_to_representation, rf):
    mock_to_representation.return_value = {'url': 'a.png'}
    field = fields.AbsoluteUrlImageRenditionField(filter_spec=None)
    field.context = {'request': rf.get('/')}

    actual = field.to_representation('a.png')

    assert actual == {'url': 'http://testserver/a.png'}
