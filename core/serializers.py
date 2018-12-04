from rest_framework import serializers

from core import fields


class BasePageSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    seo_title = serializers.CharField()
    search_description = serializers.CharField()
    meta = fields.MetaDictField()
    full_url = serializers.CharField(max_length=255)
    full_path = serializers.CharField(max_length=255)
    last_published_at = serializers.DateTimeField()
    title = serializers.CharField()
    page_type = serializers.SerializerMethodField()

    def get_page_type(self, instance):
        return instance.__class__.__name__


class FormPageSerializerMetaclass(serializers.SerializerMetaclass):
    """Metaclass that adds <field_name>_label and <field_name>_help_text to a
    serializer when given a list of form_field_names.
    """

    def __new__(mcls, name, bases, attrs):
        form_field_names = attrs['Meta'].model_class.form_field_names
        for field_name in form_field_names:
            attrs[field_name + '_help_text'] = serializers.CharField()
            attrs[field_name + '_label'] = serializers.CharField()

        return super().__new__(mcls, name, bases, attrs)
