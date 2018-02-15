from wagtail.wagtailimages.api.fields import ImageRenditionField


class AbsoluteUrlImageRenditionField(ImageRenditionField):
    def to_representation(self, image):
        representation = super().to_representation(image)
        representation['url'] = self.context['request'].build_absolute_uri(
            representation['url']
        )
        return representation
