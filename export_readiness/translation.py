from modeltranslation.decorators import register

from core.translation import BaseTranslationOptions
from export_readiness import models


@register(models.TermsAndConditionsPage)
class TermsAndConditionsPageTranslationOptions(BaseTranslationOptions):
    fields = (
        'terms_title',
        'body',
    )


@register(models.ExportReadinessApp)
class ExportReadinessAppTranslationOptions(BaseTranslationOptions):
    fields = []
