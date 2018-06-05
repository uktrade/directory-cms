from django.conf import settings
from django.utils import translation
from rest_framework import fields
from rest_framework.serializers import ValidationError
from wagtail.core.blocks import CharBlock, PageChooserBlock
from wagtail.core.models import Page
from wagtail.embeds import embeds
from wagtail.embeds.exceptions import EmbedUnsupportedProviderException
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


class APIModelChildrenSerializer(fields.ListField):
    def __init__(self, *args, **kwargs):
        self.fields_config = kwargs.pop('fields_config')
        super().__init__(*args, **kwargs)

    def get_attribute(self, instance):
        return instance

    def to_representation(self, instance):
        model_class = instance.__class__
        queryset = instance.get_descendants() \
            .type(model_class) \
            .live() \
            .order_by('sectorpage__heading') \
            .specific()
        serializer_class = self.context['view']._get_serializer_class(
            router=self.context['router'],
            model=model_class,
            fields_config=self.fields_config,
        )
        serializer = serializer_class(
            queryset, many=True, context=self.context
        )
        return serializer.data


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


class APIVideoSerializer(fields.CharField):
    def to_representation(self, value):
        try:
            return embeds.get_embed(value).html
        except EmbedUnsupportedProviderException:
            return ''


class APIStreamFieldStructBlockSerializer(fields.ListField):

    SUPPORTED_BLOCKS_CLASSES = frozenset((
        ImageChooserBlock,
        CharBlock,
        MarkdownBlock,
        PageChooserBlock
    ))

    def to_representation(self, blocks):
        elements = []
        for block in blocks:
            element = {}
            for key, value in block.value.items():
                block_class_instance = block.block.child_blocks[key]
                block_class = block_class_instance.__class__
                if block_class not in self.SUPPORTED_BLOCKS_CLASSES:
                    raise ValidationError()
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

            elements.append(element)
        return elements
