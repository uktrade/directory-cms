from rest_framework import fields


class APIStreamMarkdownAccordionBlockSerializer(fields.ListField):

    def to_representation(self, value):
        import ipdb; ipdb.set_trace()
        pass