from modeltranslation.translator import TranslationOptions
from modeltranslation.decorators import register

from export_readiness import models


@register(models.TermsAndConditionsPage)
class TermsAndConditionsPageTranslationOptions(TranslationOptions):
    fields = (
        'terms_title',
        'body',
    )
    required_languages = []


@register(models.ExportReadinessApp)
class ExportReadinessAppTranslationOptions(TranslationOptions):
    fields = []
    required_languages = []
