from collections import OrderedDict

from rest_framework import serializers
from rest_framework.fields import SkipField
from rest_framework.relations import PKOnlyObject
from wagtail.core.blocks import StructValue
from wagtail.images.api import fields as wagtail_fields


class StreamChildBaseSerializer(serializers.Serializer):

    def to_representation(self, stream_child):
        """
        instance is wagtail.core.blocks.stream_block.StreamValue.StreamChild
        instance.value is either an instance of StructValue, if struct block, or a single value
        """
        ret = OrderedDict()
        fields = self._readable_fields

        for field in fields:
            try:
                if isinstance(stream_child.value, StructValue):
                    # streamfield with struct block
                    attribute = stream_child.value[field.field_name]
                else:
                    # streamfield with single block
                    attribute = field.get_attribute(stream_child.value)
            except SkipField:
                continue

            # We skip `to_representation` for `None` values so that fields do
            # not have to explicitly deal with that case.
            #
            # For related fields with `use_pk_only_optimization` we need to
            # resolve the pk value.
            check_for_none = attribute.pk if isinstance(attribute, PKOnlyObject) else attribute
            if check_for_none is None:
                ret[field.field_name] = None
            else:
                ret[field.field_name] = field.to_representation(attribute)

        return ret


class HeadingContentStreamChildBaseSerializer(StreamChildBaseSerializer):
    heading = serializers.CharField()
    content = serializers.CharField()


class ColumnWithTitleIconTextBlockStreamChildBaseSerializer(HeadingContentStreamChildBaseSerializer):
    icon = wagtail_fields.ImageRenditionField('original', required=False)
    image_alt = serializers.CharField()


class DetailsSummaryBlockStreamChildBaseSerializer(HeadingContentStreamChildBaseSerializer):
    pass


class LinkBlockStreamChildSerializer(StreamChildBaseSerializer):
    source = serializers.CharField(help_text='The source of the link, eg GOV.UK')
    text = serializers.CharField()
    url = serializers.CharField()
