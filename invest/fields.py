from wagtail.api import APIField

from .serializers import APIStreamMarkdownAccordionBlockSerializer


class APIStreamMarkdownAccordionBlockField(APIField):
    def __init__(self, name, field_names=None):
        serializer = APIStreamMarkdownAccordionBlockSerializer()
        super().__init__(name=name, serializer=serializer)
