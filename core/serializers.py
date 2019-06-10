from rest_framework import serializers

from core import fields
from great_international.models import CapitalInvestOpportunityPage


class BasePageSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    seo_title = serializers.CharField()
    search_description = serializers.CharField()
    meta = fields.MetaDictField()
    full_url = serializers.CharField(max_length=255)
    full_path = serializers.CharField(
        max_length=255, source='specific.full_path')
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
            attrs[field_name] = fields.FieldAttributesField()
        return super().__new__(mcls, name, bases, attrs)


class PagesTypesSerializer(serializers.Serializer):

    types = serializers.ListField(
        child=serializers.CharField()
    )


class WagtailPageSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField()
    slug = serializers.CharField()


class ChildPagesSerializerHelper(serializers.Serializer):
    def get_child_pages_data_for(self, parent, page_type, serializer):
        queryset = page_type.objects.descendant_of(parent).live()
        serializer = serializer(
            queryset,
            many=True,
            allow_null=True,
            context=self.context
        )
        return serializer.data


class ParentPageSerializerHelper(serializers.Serializer):
    def get_parent_page_data_for(self, instance, serializer):
        queryset = instance.get_parent().specific
        serializer = serializer(
            queryset,
            allow_null=True,
            context=self.context
        )
        return serializer.data


class OpportunityPageWithRelatedSectorPageSerializerHelper(
    serializers.Serializer
):
    def get_opportunity_page_with_self_as_related_sector_data_for(
            self,
            instance,
            serializer
    ):
        page_type = CapitalInvestOpportunityPage
        queryset = []

        all_opportunity_pages = page_type.objects.live().public()

        for page in all_opportunity_pages:
            for related_sectors in page.related_sectors.all():
                if not related_sectors.related_sector:
                    continue
                elif related_sectors.related_sector.title == instance.title:
                    queryset.append(page)

        if not queryset:
            return []

        serializer = serializer(
            queryset,
            allow_null=True,
            context=self.context
        )
        return serializer.data
