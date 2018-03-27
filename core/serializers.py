from rest_framework import fields
from wagtail.wagtailcore.rich_text import expand_db_html

from django.conf import settings

from core import helpers


class URLHyperlinkSerializer(fields.CharField):

    draft_url_attribute = None
    published_url_attribute = None

    def __init__(self, *args, **kwargs):
        self.draft_url_attribute = kwargs.pop('draft_url_attribute')
        self.published_url_attribute = kwargs.pop('published_url_attribute')
        super().__init__(*args, **kwargs)

    def get_attribute(self, instance):
        if helpers.is_draft_requested(self.context['request']):
            attribute = self.draft_url_attribute
        else:
            attribute = self.published_url_attribute
        return getattr(instance, attribute)


class APIRichTextSerializer(fields.CharField):
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        return expand_db_html(representation)


class APITranslationsSerializer(fields.ListField):
    def get_attribute(self, instance):
        return [
            (code, label) for (code, label) in settings.LANGUAGES_LOCALIZED
            if code in instance.translated_languages
        ]


class APIMetaSerializer(fields.DictField):

    languages = APITranslationsSerializer()
    url = URLHyperlinkSerializer(
        draft_url_attribute='draft_url',
        published_url_attribute='published_url',
    )

    def get_attribute(self, instance):
        self.url.context = self.context
        return {
            'languages': self.languages.get_attribute(instance),
            'url': self.url.get_attribute(instance)
        }
