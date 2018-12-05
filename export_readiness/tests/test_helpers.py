import pytest
import wagtail_factories
from core.helpers import image_rendition_as_json


@pytest.mark.django_db
@pytest.mark.parametrize('image_format,filename', [
    (
        'fill-640x360|jpegquality-60|format-jpeg',
        'fill-640x360.jpegquality-60.format-jpeg'
    ),
    (
        'fill-640x360|jpegquality-60',
        'fill-640x360.jpegquality-60'
    ),
    (
        'fill-1600x900',
        'fill-1600x900'
    ),
    (
        'original',
        'original'
    ),
]
)
def test_image_rendition_helper(image_format, filename):
    image = wagtail_factories.ImageFactory.create()

    rendition = image_rendition_as_json(
        image, image_format)

    assert filename in rendition['url']
    assert rendition.get('url')
    assert rendition.get('width')
    assert rendition.get('height')
