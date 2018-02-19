from urllib.parse import urlparse

from wagtail.wagtailimages.api.fields import ImageRenditionField


class AbsoluteUrlImageRenditionField(ImageRenditionField):

    @staticmethod
    def is_url_absolute(url):
        return bool(urlparse(url).netloc)

    def to_representation(self, image):
        result = super().to_representation(image)
        url = result['url']
        if not self.is_url_absolute(url):
            result['url'] = self.context['request'].build_absolute_uri(url)
        return result
