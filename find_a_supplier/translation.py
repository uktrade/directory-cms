from modeltranslation.translator import TranslationOptions
from modeltranslation.decorators import register

from django.conf import settings

from find_a_supplier import models


@register(models.IndustryPage)
class IndustryPageTranslationOptions(TranslationOptions):
    fields = (
        'hero_text',
        'introduction_text',
        'introduction_column_one_text',
        'introduction_column_two_text',
        'introduction_column_three_text',
        'breadcrumbs_label',
        'introduction_column_one_icon',
        'introduction_column_two_icon',
        'introduction_column_three_icon',
        'company_list_text',
        'company_list_search_input_placeholder_text',
        'company_list_call_to_action_text',
    )
    required_languages = (settings.LANGUAGE_CODE,)


@register(models.IndustryArticlePage)
class IndustryArticlePageTranslationOptions(TranslationOptions):
    fields = (
        'author_name',
        'job_title',
        'date',
        'body',
        'introduction_title',
        'breadcrumbs_label',
        'proposition_text',
        'call_to_action_text',
    )
    required_languages = (settings.LANGUAGE_CODE,)


@register(models.IndustryLandingPage)
class IndustryLandingPageTranslationOptions(TranslationOptions):
    fields = (
        'hero_title',
        'proposition_text',
        'call_to_action_text',
        'breadcrumbs_label',
    )
    required_languages = (settings.LANGUAGE_CODE,)


@register(models.LandingPage)
class LandingPageTranslationOptions(TranslationOptions):
    fields = (
        'breadcrumbs_label',
        'hero_text',
        'search_field_placeholder',
        'search_button_text',
        'proposition_text',
        'call_to_action_text',
        'industries_list_text',
        'industries_list_call_to_action_text',
        'services_list_text',
        'services_column_one',
        'services_column_two',
        'services_column_three',
        'services_column_four',
        'services_column_one_icon',
        'services_column_two_icon',
        'services_column_three_icon',
        'services_column_four_icon',
    )
    required_languages = (settings.LANGUAGE_CODE,)


@register(models.IndustryContactPage)
class IndustryContactPageTranslationOptions(TranslationOptions):
    fields = (
        'breadcrumbs_label',
        'introduction_text',
        'submit_button_text',
        'success_message_text',
        'success_back_link_text',
    )
    required_languages = (settings.LANGUAGE_CODE,)
