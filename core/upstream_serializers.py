import abc
from datetime import date, datetime

from wagtail.images.models import Image

from django.forms.models import model_to_dict

from core import helpers, models


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


class NoOpFieldSerializer(AbstractFieldSerializer):
    FIELD_NAME_PREFIX = ''

    @classmethod
    def serialize_value(cls, value):
        return value

    @classmethod
    def deserialize_value(cls, value):
        return value


class UpstreamModelSerilaizer:

    EMPTY_VALUES = ['', 'None', None]

    field_serializers = {
        Image: ImageFieldSerializer,
        list: ListFieldSerializer,
        date: DateFieldSerializer,
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
        data = model_to_dict(model_instance, exclude=['pk', 'id'])
        serialized = {}
        for name in cls.remove_empty(data):
            value = getattr(model_instance, name)
            serializer = cls.get_field_serializer_by_field_value(value)
            name, value = serializer.serialize(name=name, value=value)
            serialized[name] = value
        return serialized

    @classmethod
    def deserialize(cls, serialized_data):
        deserialized = {}
        for name, value in cls.remove_empty(serialized_data).items():
            value = serialized_data[name]
            serializer = cls.get_field_serializer_by_field_name(name)
            name, value = serializer.deserialize(name=name, value=value)
            deserialized[name] = value
        return deserialized
