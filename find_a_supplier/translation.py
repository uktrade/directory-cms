from modeltranslation.decorators import register

from core.translation import BaseTranslationOptions
from find_a_supplier import models


@register(models.IndustryPage)
class IndustryPageTranslationOptions(BaseTranslationOptions):
    fields = (
        'hero_text',
        'hero_image_caption',
        'introduction_text',
        'introduction_call_to_action_button_text',
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


@register(models.IndustryPageArticleSummary)
class IndustryPageArticleSummaryTranslationOptions(BaseTranslationOptions):
    fields = (
        'page',
    )


@register(models.IndustryArticlePage)
class IndustryArticlePageTranslationOptions(BaseTranslationOptions):
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


@register(models.IndustryLandingPage)
class IndustryLandingPageTranslationOptions(BaseTranslationOptions):
    fields = (
        'hero_title',
        'hero_image_caption',
        'proposition_text',
        'call_to_action_text',
        'breadcrumbs_label',
        'more_industries_title',
    )


@register(models.LandingPage)
class LandingPageTranslationOptions(BaseTranslationOptions):
    fields = (
        'breadcrumbs_label',
        'hero_text',
        'hero_image_caption',
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


@register(models.LandingPageArticleSummary)
class LandingPageArticleSummaryTranslationOptions(BaseTranslationOptions):
    fields = (
        'page',
    )


@register(models.IndustryContactPage)
class IndustryContactPageTranslationOptions(BaseTranslationOptions):
    fields = (
        'breadcrumbs_label',
        'introduction_text',
        'submit_button_text',
        'success_message_text',
        'success_back_link_text',
    )
