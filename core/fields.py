from rest_framework import fields

from conf import settings
from core import helpers, models


class MarkdownToHTMLField(fields.CharField):
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        return helpers.render_markdown(representation)


class MetaDictField(fields.DictField):

    def get_attribute(self, instance):
        if 'request' in self.context:
            is_draft = helpers.is_draft_requested(self.context['request'])
        else:
            is_draft = False
        return {
            'languages': [
                (code, label) for (code, label) in settings.LANGUAGES_LOCALIZED
                if code in instance.specific.translated_languages
            ],
            'url': instance.specific.get_url(
                is_draft=is_draft,
                language_code=settings.LANGUAGE_CODE,
            ),
            'slug': instance.slug,
            'localised_urls': instance.specific.get_localized_urls(),
            'pk': instance.pk,
            'draft_token': (instance.get_draft_token()
                            if instance.has_unpublished_changes else None)
        }


class TagsListField(fields.ListField):
    """This assumes the ParentalM2M field on the model is called tags."""

    def get_attribute(self, instance):
        return [
            {'name': item.name, 'slug': item.slug}
            for item in instance.tags.all()
        ]


class VideoField(fields.DictField):
    def to_representation(self, instance):
        return {
            'url': instance.url,
            'thumbnail': instance.thumbnail.url if
            instance.thumbnail else None,
            'width': instance.width,
            'height': instance.height,
            'duration': instance.duration,
            'file_extension': instance.file_extension,
        }


class DocumentURLField(fields.CharField):

    def to_representation(self, instance):
        return instance.file.url


class BreadcrumbsField(fields.DictField):
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


class FieldAttributesField(fields.DictField):
    def get_attribute(self, instance):
        return {
            'label': getattr(instance, self.source + '_label'),
            'help_text':  getattr(instance, self.source + '_help_text'),
        }


class OpportunitiesListField(fields.ListField):
    def get_attribute(self, instance):
        for item in instance.opportunities.all():
            print('\n\n\n\n\n it got to here return a load of stuff', item.breadcrumbs_label)
        return [
            {'breadcrumbs_label': item.breadcrumbs_label,
             'hero_image': item.hero_image,
             'hero_title': item.hero_title,
             'opportunity_summary_intro': item.opportunity_summary_intro,
             'opportunity_summary_content': item.opportunity_summary_content,
             'opportunity_summary_image': item.opportunity_summary_image,
             'location': item.location,
             'project_promoter': item.project_promoter,
             'scale': item.scale,
             'programme': item.programme,
             'investment_type': item.investment_type,
             'planning_status': item.planning_status,
             'project_background_title': item.project_background_title,
             'project_background_intro': item.project_background_intro,
             'project_description_title': item.project_description_title,
             'project_description_content': item.project_description_content,
             'project_promoter_title': item.project_promoter_title,
             'project_promoter_content': item.project_promoter_content,
             'project_image': item.project_image,
             'case_study_image': item.case_study_image,
             'case_study_title': item.case_study_title,
             'case_study_text': item.case_study_text,
             'case_study_cta_text': item.case_study_cta_text,
             'case_study_cta_link': item.case_study_cta_link,
             'next_steps_title': item.next_steps_title,
             'next_steps_intro': item.next_steps_intro,
             'invest_cta_text': item.invest_cta_text,
             'buy_cta_text': item.buy_cta_text
             }
            for item in instance.opportunities.all()
        ]
