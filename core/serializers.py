from django.conf import settings
from django.utils import translation
from rest_framework import fields
from rest_framework.serializers import ValidationError
from wagtail.core.blocks import CharBlock, PageChooserBlock
from wagtail.core.models import Page
from wagtail.images.blocks import ImageChooserBlock
from wagtailmarkdown.blocks import MarkdownBlock

from core import helpers, models


class APIMarkdownToHTMLSerializer(fields.CharField):
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        return helpers.render_markdown(representation)


class APIMetaSerializer(fields.DictField):

    def get_attribute(self, instance):
        return {
            'languages': [
                (code, label) for (code, label) in settings.LANGUAGES_LOCALIZED
                if code in instance.translated_languages
            ],
            'url': instance.get_url(
                is_draft=helpers.is_draft_requested(self.context['request']),
                language_code=translation.get_language(),
            ),
            'slug': instance.slug,
            'localised_urls': instance.get_localized_urls(),
            'pk': instance.pk,
        }


class APIChildrenSerializer(fields.ListField):
    sorting_key = ''

    def __init__(self, *args, **kwargs):
        self.fields_config = kwargs.pop('fields_config')
        super().__init__(*args, **kwargs)

    @staticmethod
    def get_model():
        raise NotImplemented

    def get_attribute(self, instance):
        return instance

    def to_representation(self, instance):
        queryset = instance.get_descendants() \
            .type(self.get_model()) \
            .live() \
            .specific()
        serializer_class = self.context['view']._get_serializer_class(
            router=self.context['router'],
            model=self.get_model(),
            fields_config=self.fields_config,
        )
        serializer = serializer_class(
            queryset, many=True, context=self.context
        )
        data = serializer.data
        # When ordering at the database level, the lookup seems to happens on
        # the superclass `Page` table level, so it is not aware of the fields
        # the subclass has. We are ordering on the application level
        sorted_data = sorted(
            data,
            key=lambda x: x[self.sorting_key], reverse=True
        )
        return sorted_data


class APIQuerysetSerializer(fields.ListField):
    def __init__(self, *args, **kwargs):
        self.fields_config = kwargs.pop('fields_config')
        self.queryset = kwargs.pop('queryset')
        super().__init__(*args, **kwargs)

    def get_attribute(self, instance):
        return instance

    def to_representation(self, instance):
        serializer_class = self.context['view']._get_serializer_class(
            router=self.context['router'],
            model=self.queryset.model,
            fields_config=self.fields_config,
        )
        serializer = serializer_class(
            self.queryset, many=True, context=self.context
        )
        return serializer.data


class APIBreadcrumbsSerializer(fields.DictField):
    def __init__(self, app_label, *args, **kwargs):
        self.app_label = app_label
        super().__init__(*args, **kwargs)

    def get_attribute(self, instance):
        queryset = (
            Page.objects.all()
                .filter(content_type__app_label=self.app_label)
                .only('breadcrumbs_label', 'slug')
                .select_related('content_tyle__model')
                .specific()
        )
        return {
            item.content_type.model: {
                'label': item.breadcrumbs_label, 'slug': item.slug,
            }
            for item in queryset
            if isinstance(item, models.ExclusivePageMixin)
            and isinstance(item, models.BasePage)
        }


class APIStreamFieldStructBlockSerializer(fields.ListField):

    def to_representation(self, blocks):
        elements = []
        for block in blocks:
            element = {}
            for key, value in block.value.items():
                block_class_instance = block.block.child_blocks[key]
                if isinstance(block_class_instance, PageChooserBlock):
                    page_url = value.specific.get_full_url()
                    element[key] = page_url
                elif isinstance(block_class_instance, ImageChooserBlock):
                    image = value.get_rendition('original')
                    image_url = image.url
                    element[key] = image_url
                elif isinstance(block_class_instance, CharBlock):
                    element[key] = value
                elif isinstance(block_class_instance, MarkdownBlock):
                    element[key] = helpers.render_markdown(value)
                else:
                    raise ValidationError(
                        'Block not supported for serialization'
                    )

            elements.append(element)
        return elements


class APIVideoSerializer(fields.DictField):
    def to_representation(self, value):
        return {
            'url': value.url,
            'thumbnail': value.thumbnail.url if value.thumbnail else None,
            'width': value.width,
            'height': value.height,
            'duration': value.duration,
            'file_extension': value.file_extension,
        }
