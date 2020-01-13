from rest_framework import serializers
from wagtail.images.api import fields as wagtail_fields

from core import fields
from great_international.models.capital_invest import \
    CapitalInvestOpportunityPage


class PageTitleAndUrlSerializer(serializers.Serializer):
    title = serializers.CharField()
    url = serializers.CharField()


class PageBreadcrumbsAndUrlSerializer(serializers.Serializer):
    title = serializers.CharField(source='breadcrumbs_label')
    url = serializers.CharField()


class HeroSerializer(serializers.Serializer):
    hero_image = wagtail_fields.ImageRenditionField('original')
    hero_image_thumbnail = wagtail_fields.ImageRenditionField('fill-640x360', source='hero_image')
    hero_xlarge = wagtail_fields.ImageRenditionField('fill-1500x375', source='hero_image')
    hero_xlarge_tall = wagtail_fields.ImageRenditionField('fill-1500x500', source='hero_image')
    hero_large = wagtail_fields.ImageRenditionField('fill-1280x375', source='hero_image')
    hero_medium = wagtail_fields.ImageRenditionField('fill-768x300', source='hero_image')
    hero_medium_tall = wagtail_fields.ImageRenditionField('fill-768x376', source='hero_image')
    hero_small = wagtail_fields.ImageRenditionField('fill-640x300', source='hero_image')


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
    tree_based_breadcrumbs = serializers.SerializerMethodField()

    def get_tree_based_breadcrumbs(self, instance):
        breadcrumbs = [
            page.specific for page in instance.specific.ancestors_in_app]
        breadcrumbs.append(instance)
        serialized = []

        for crumb in breadcrumbs:
            if hasattr(crumb, 'breadcrumbs_label'):
                serialized.append(PageBreadcrumbsAndUrlSerializer(crumb).data)
            else:
                serialized.append(PageTitleAndUrlSerializer(crumb).data)

        return serialized

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
        queryset = page_type.objects.child_of(parent).live()
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
