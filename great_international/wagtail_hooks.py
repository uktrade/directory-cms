from django.conf import settings

from django.db import models as django_models

from wagtail.core import hooks

from wagtail.images.models import Image
from wagtailmedia.models import Media

from wagtail_transfer.serializers import ModelSerializer, PageSerializer
from wagtail_transfer.field_adapters import ForeignKeyAdapter

from great_international.models.great_international import InternationalSectorPage


lang_code = settings.LANGUAGE_CODE
lang_suffixes_to_ignore = [
    f"_{x[0].replace('-', '_')}" for x in settings.LANGUAGES
]  # ie, ALL language suffixes, with hyphens flattened to underscores


def _ignorable(fieldname):
    for suffix in lang_suffixes_to_ignore:
        if fieldname.endswith(suffix):
            return True

    return False


def _get_translation_fields_to_ignore(klass):
    return [
        x.name for x in klass._meta.get_fields() if _ignorable(x.name)
    ]


class InternationalSectorPageSerializer(PageSerializer):
    """
    Proof-of-concept custom serializer that
    * only exports the default fields (no translated fields at all)
    * amends the destination app of the model from 'great_international' to just 'international'

    """
    ignored_fields = (
        PageSerializer.ignored_fields +
        _get_translation_fields_to_ignore(
            InternationalSectorPage
        )
    )


    def serialize(self, instance):
        """Adapted from from wagtail_transfer.serializers.ModelSerializer to
        target a different app_label for a model with the same name, so that
        Magna doesn't have to live with the same app structure as Great V1
        """

        # We need the base data structure that the PageSerializer gets from
        # TreeModelSerializer
        initial_result = super().serialize(instance)

        _source_model_spec = self.model._meta.label_lower
        _target_model_spec = _source_model_spec.replace('great_international', 'international')
        initial_result.update({
            'model': _target_model_spec,
            'pk': instance.pk,
            'fields': self.serialize_fields(instance)
        })
        return initial_result


# class CustomImageSerializer(ModelSerializer):
#     """Patch wagtailimages.Image to its new name in Magna: core.AltTextImage"""

#     def serialize(self, instance):
#         initial_result = super().serialize(instance)

#         return initial_result


# class CustomMediaSerializer(ModelSerializer):
#     """Patch wagtailmedia.Media to its new name in Magna: core.AltTextImage"""

#     def serialize(self, instance):
#         initial_result = super().serialize(instance)

#         return initial_result


@hooks.register('register_custom_serializers')
def register_custom_serializers():
    return {
        InternationalSectorPage: InternationalSectorPageSerializer,
        # Image: CustomImageSerializer,
        # Media: CustomMediaSerializer,
    }


# class SelectiveRemapForeignKeyAdapter(ForeignKeyAdapter):
#     """For all ForeignKey fields that reference either of:
#     * wagtailimages' Image model
#     * wagtailmedia's Video model
#     we want to rewrite the JSON-serialized name of the target model to be
#     the Magna/V2 version of that model

#     We do this by patching the output of serialize at the last opportunity
#     so that we don't mess with any other lookups
#     """


#     def get_dependencies(self, value):
#         if value is None:
#             return set()
#         elif self.field.blank and self.field.null:
#             # field is nullable, so it's a soft dependency; we can leave the field empty in the
#             # case that the target object cannot be created
#             import ipdb; ipdb.set_trace()
#             return {(self.related_base_model, value, False)}
#         else:
#             # this is a hard dependency
#             import ipdb; ipdb.set_trace()
#             return {(self.related_base_model, value, True)}


#     def update_object_references(self, value, destination_ids_by_source):
#         """
#         Return a modified version of value with object references replaced by their corresponding
#         entries in destination_ids_by_source - a mapping of (model_class, source_id) to
#         destination_id
#         """
#         import ipdb; ipdb.set_trace()

#         return value

#     # DOESN'T LET US REACH WHAT WE WANT TO
#     # def serialize(self, instance):
#     #     value = super().serialize(instance)
#     #     print("serialize", value, type(instance), self.related_base_model)
#     #     import ipdb; ipdb.set_trace()
#     #     return value


# @hooks.register('register_field_adapters')
# def register_media_model_remap_field_adapter():

#     extra_adapters = {
#         django_models.ForeignKey: SelectiveRemapForeignKeyAdapter,
#     }
#     return extra_adapters
