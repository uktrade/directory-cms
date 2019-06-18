import abc
from datetime import date, datetime

from wagtail.core.models import Page
from wagtail.documents.models import Document
from wagtail.images.models import Image

from django.forms import ValidationError
from django.forms.models import model_to_dict
from django.contrib import messages

from core import helpers
from core.cache import SERVICE_NAMES_TO_ROOT_PATHS


class AbstractFieldSerializer(abc.ABC):

    @property
    @abc.abstractmethod
    def FIELD_NAME_PREFIX(self):
        pass

    @classmethod
    def serialize_name(cls, name):
        return cls.FIELD_NAME_PREFIX + name

    @classmethod
    def deserialize_name(cls, name):
        return name.replace(cls.FIELD_NAME_PREFIX, '')

    @classmethod
    def serialize(cls, name, value):
        return cls.serialize_name(name), cls.serialize_value(value)

    @classmethod
    def deserialize(cls, name, value):
        return cls.deserialize_name(name), cls.deserialize_value(value)


class ImageFieldSerializer(AbstractFieldSerializer):
    FIELD_NAME_PREFIX = '(image)'

    @classmethod
    def serialize_value(cls, value):
        return value.file.name

    @classmethod
    def deserialize_value(cls, value):
        return helpers.get_or_create_image(value).pk


class DocumentFieldSerializer(AbstractFieldSerializer):
    FIELD_NAME_PREFIX = '(document)'

    @classmethod
    def serialize_value(cls, value):
        return value.file.name

    @classmethod
    def deserialize_value(cls, value):
        return helpers.get_or_create_document(value).pk


class ListFieldSerializer(AbstractFieldSerializer):
    FIELD_NAME_PREFIX = '(list)'

    @classmethod
    def serialize_value(cls, value):
        return ','.join(value)

    @classmethod
    def deserialize_value(cls, value):
        return value.split(',')


class DateFieldSerializer(AbstractFieldSerializer):
    FIELD_NAME_PREFIX = '(date)'
    DATE_FORMAT = '%Y-%m-%d'

    @classmethod
    def serialize_value(cls, value):
        return value.strftime(cls.DATE_FORMAT)

    @classmethod
    def deserialize_value(cls, value):
        return datetime.strptime(value, cls.DATE_FORMAT)


class RelatedPageSerializer(AbstractFieldSerializer):
    FIELD_NAME_PREFIX = '(page)'

    @classmethod
    def serialize_value(cls, value):
        return {
            'slug': value.slug,
            'service_name_value': value.specific.service_name_value
        }

    @classmethod
    def deserialize_value(cls, value):
        parent_app_slug = SERVICE_NAMES_TO_ROOT_PATHS[
            value['service_name_value']]
        app_pages = Page.objects.get(slug=parent_app_slug).get_descendants()

        try:
            return app_pages.get(slug=value['slug'])

        except Page.DoesNotExist:
            raise ValidationError(
                f"Related page with the slug {value['slug']} could not be "
                "found in this environment. Please create it then "
                "add it as one of this page's related pages."
            )


class NoOpFieldSerializer(AbstractFieldSerializer):
    FIELD_NAME_PREFIX = ''

    @classmethod
    def serialize_value(cls, value):
        return value

    @classmethod
    def deserialize_value(cls, value):
        return value


class UpstreamModelSerializer:

    EMPTY_VALUES = ['', 'None', None]

    field_serializers = {
        Image: ImageFieldSerializer,
        Document: DocumentFieldSerializer,
        list: ListFieldSerializer,
        date: DateFieldSerializer,
        Page: RelatedPageSerializer,
    }
    default_field_serializer = NoOpFieldSerializer

    @classmethod
    def get_field_serializer_by_field_value(cls, value):
        for field_class, serializer in cls.field_serializers.items():
            if isinstance(value, field_class):
                return serializer
        else:
            return cls.default_field_serializer

    @classmethod
    def get_field_serializer_by_field_name(cls, name):
        for serializer in cls.field_serializers.values():
            if serializer.FIELD_NAME_PREFIX in name:
                return serializer
        else:
            return cls.default_field_serializer

    @classmethod
    def remove_empty(cls, data):
        return {
            name: value for name, value in data.items()
            if value not in cls.EMPTY_VALUES
        }

    @classmethod
    def serialize(cls, model_instance):
        data = model_to_dict(model_instance, exclude=['pk', 'id', 'page_ptr'])
        serialized = {}
        for name in cls.remove_empty(data):
            value = getattr(model_instance, name)
            serializer = cls.get_field_serializer_by_field_value(value)
            name, value = serializer.serialize(name=name, value=value)
            serialized[name] = value
        return serialized

    @classmethod
    def deserialize(cls, serialized_data, request):
        deserialized = {}
        for name, value in cls.remove_empty(serialized_data).items():
            value = serialized_data[name]
            serializer = cls.get_field_serializer_by_field_name(name)
            try:
                name, value = serializer.deserialize(name=name, value=value)
            except ValidationError as e:
                messages.error(request, e.message)
            else:
                deserialized[name] = value
        return deserialized
