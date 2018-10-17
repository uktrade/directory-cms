from rest_framework import fields

from django.conf import settings

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
                language_code=settings.LANGUAGE_CODE,
            ),
            'slug': instance.slug,
            'localised_urls': instance.get_localized_urls(),
            'pk': instance.pk,
            'draft_token': (instance.get_draft_token()
                            if instance.has_unpublished_changes else None)
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
            nested=True,
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
            key=lambda x: x[self.sorting_key]
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


class APIFormFieldSerializer(fields.DictField):
    def get_attribute(self, instance):
        return {
            'label': getattr(instance, self.source + '_label'),
            'help_text':  getattr(instance, self.source + '_help_text'),
        }


class APIDocumentUrlSerializer(fields.CharField):

    def to_representation(self, document):
        return document.file.url


class APITagsSerializer(fields.CharField):

    def to_representation(self, value):
        tags = []
        for tag in value.all():
            tags.append({'name': tag.name, 'slug': tag.slug})
        return tags
