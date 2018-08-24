from modeltranslation.decorators import register

from core.translation import BaseTranslationOptions
from export_readiness import models


@register(models.TermsAndConditionsPage)
class TermsAndConditionsPageTranslationOptions(BaseTranslationOptions):
    fields = []


@register(models.PrivacyAndCookiesPage)
class PrivacyAndCookiesPageTranslationOptions(BaseTranslationOptions):
    fields = []


@register(models.GetFinancePage)
class GetFinancePageTranslationOptions(BaseTranslationOptions):
    fields = []


@register(models.ExportReadinessApp)
class ExportReadinessAppTranslationOptions(BaseTranslationOptions):
    fields = []


@register(models.PerformanceDashboardPage)
class PerformanceDashboardPageTranslationOptions(BaseTranslationOptions):
    fields = []


@register(models.PerformanceDashboardNotesPage)
class PerformanceDashboardNotesPageTranslationOptions(BaseTranslationOptions):
    fields = []


@register(models.HighPotentialOfferFormPage)
class HighPotentialOfferFormPageTranslationOptions(BaseTranslationOptions):
    fields = []
