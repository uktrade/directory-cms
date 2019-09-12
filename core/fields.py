from rest_framework import fields
from wagtail.core import blocks
from wagtail.core.fields import StreamField

from conf import settings
from core import helpers, models


class MarkdownToHTMLField(fields.CharField):
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        return helpers.render_markdown(representation)


class MetaDictField(fields.DictField):

    def get_attribute(self, instance):
        if 'request' in self.context:
            is_draft = helpers.is_draft_requested(self.context['request'])
        else:
            is_draft = False
        return {
            'languages': [
                (code, label) for (code, label) in settings.LANGUAGES_LOCALIZED
                if code in instance.specific.translated_languages
            ],
            'url': instance.specific.get_url(
                is_draft=is_draft,
                language_code=settings.LANGUAGE_CODE,
            ),
            'slug': instance.slug,
            'localised_urls': instance.specific.get_localized_urls(),
            'pk': instance.pk,
            'draft_token': (instance.get_draft_token()
                            if instance.has_unpublished_changes else None)
        }


class TagsListField(fields.ListField):
    """This assumes the ParentalM2M field on the model is called tags."""

    def get_attribute(self, instance):
        return [
            {'name': item.name}
            for item in instance.tags.all()
        ]


class VideoField(fields.DictField):
    def to_representation(self, instance):
        return {
            'url': instance.url,
            'thumbnail': instance.thumbnail.url if
            instance.thumbnail else None,
            'width': instance.width,
            'height': instance.height,
            'duration': instance.duration,
            'file_extension': instance.file_extension,
        }


class DocumentURLField(fields.CharField):

    def to_representation(self, instance):
        return instance.file.url


class BreadcrumbsField(fields.DictField):
    def __init__(self, service_name, *args, **kwargs):
        self.service_name = service_name
        super().__init__(*args, **kwargs)

    def get_attribute(self, instance):
        service_name = self.service_name
        queryset = (
            models.Breadcrumb.objects
            .select_related('content_type')
            .filter(service_name=service_name)
        )
        return {
            item.content_type.model: {
                'label': item.label, 'slug': item.slug,
            }
            for item in queryset
        }


class FieldAttributesField(fields.DictField):
    def get_attribute(self, instance):
        return {
            'label': getattr(instance, self.source + '_label'),
            'help_text': getattr(instance, self.source + '_help_text'),
        }


def single_struct_block_stream_field_factory(
        field_name, block_class_instance, max_num=None, min_num=None, required=False, **kwargs
):
    field = StreamField(
        blocks.StreamBlock(
            [(field_name, block_class_instance)],
            max_num=max_num,
            min_num=min_num,
            required=required
        ),
        **kwargs)
    return field
