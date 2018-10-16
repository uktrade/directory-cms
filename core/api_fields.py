from django.db import models
from wagtail.api import APIField
from wagtail.images.api.fields import ImageRenditionField
from wagtailmarkdown.fields import MarkdownField as OriginalMarkdownField

from core import api_serializers
from core import validators as core_validators, widgets


class APIMarkdownToHTMLField(APIField):
    def __init__(self, name):
        serializer = api_serializers.APIMarkdownToHTMLSerializer()
        super().__init__(name=name, serializer=serializer)


class APIImageField(APIField):
    def __init__(self, name):
        serializer = ImageRenditionField('original')
        super().__init__(name=name, serializer=serializer)


class APIMetaField(APIField):
    def __init__(self, name):
        serializer = api_serializers.APIMetaSerializer(name)
        super().__init__(name=name, serializer=serializer)


class APIBreadcrumbsField(APIField):
    def __init__(self, name, service_name):
        serializer = api_serializers.APIBreadcrumbsSerializer(
            service_name
        )
        super().__init__(name=name, serializer=serializer)


class APIVideoField(APIField):
    def __init__(self, name):
        serializer = api_serializers.APIVideoSerializer()
        super().__init__(name=name, serializer=serializer)


class MarkdownField(OriginalMarkdownField):
    def __init__(self, validators=None, *args, **kwargs):
        validators = validators or []
        if core_validators.slug_hyperlinks not in validators:
            validators.append(core_validators.slug_hyperlinks)
        super().__init__(validators=validators, *args, **kwargs)

    def formfield(self, **kwargs):
        kwargs['widget'] = widgets.MarkdownTextarea
        return super().formfield(**kwargs)


class APIFormFieldField(APIField):
    def __init__(self, name):
        serializer = api_serializers.APIFormFieldSerializer(name)
        super().__init__(name=name, serializer=serializer)


class APIDocumentUrlField(APIField):
    def __init__(self, name):
        serializer = api_serializers.APIDocumentUrlSerializer()
        super().__init__(name=name, serializer=serializer)


class APITagsField(APIField):
    def __init__(self, name):
        serializer = api_serializers.APITagsSerializer()
        super().__init__(name=name, serializer=serializer)


class FormHelpTextField(models.CharField):

    def __init__(self, *args, **kwargs):
        kwargs = {
            'max_length': 200,
            'verbose_name': 'Help text',
            'null': True,
            'blank': True,
            **kwargs,
        }
        super().__init__(*args, **kwargs)


class FormLabelField(models.CharField):
    def __init__(self, *args, **kwargs):
        kwargs = {
            'max_length': 200,
            'verbose_name': 'label',
            **kwargs,
        }
        super().__init__(*args, **kwargs)