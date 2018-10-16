from rest_framework import fields

from conf import settings
from core import helpers


class MarkdownToHTMLField(fields.CharField):
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        return helpers.render_markdown(representation)


class MetaDictField(fields.DictField):

    def get_attribute(self, instance):
        return {
            'languages': [
                (code, label) for (code, label) in settings.LANGUAGES_LOCALIZED
                if code in instance.translated_languages
            ],
            'url': instance.get_url(
                is_draft=helpers.is_draft_requested(self.context['request']),
                language_code=settings.LANGUAGE_CODE,
            ),
            'slug': instance.slug,
            'localised_urls': instance.get_localized_urls(),
            'pk': instance.pk,
            'draft_token': (instance.get_draft_token()
                            if instance.has_unpublished_changes else None)
        }


class TagsListField(fields.ListField):
    """This assumes the ParentalM2M field on the model is called tags."""

    def get_attribute(self, instance):
        tags = []
        for tag in instance.tags.all():
            tags.append({'name': tag.name, 'slug': tag.slug})
        return tags
