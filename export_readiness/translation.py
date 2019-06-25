from modeltranslation.decorators import register

from core.translation import BaseTranslationOptions
from export_readiness import models


@register(models.TermsAndConditionsPage)
class TermsAndConditionsPageTranslationOptions(BaseTranslationOptions):
    fields = []


@register(models.SitePolicyPages)
class SitePolicyPagesTranslationOptions(BaseTranslationOptions):
    fields = []


@register(models.CountryGuidePage)
class CountryGuidePage(BaseTranslationOptions):
    fields = []


@register(models.MarketingPages)
class MarketingPages(BaseTranslationOptions):
    fields = []


@register(models.CampaignPage)
class CampaignPage(BaseTranslationOptions):
    fields = []


@register(models.PrivacyAndCookiesPage)
class PrivacyAndCookiesPageTranslationOptions(BaseTranslationOptions):
    fields = []


@register(models.GetFinancePage)
class GetFinancePageTranslationOptions(BaseTranslationOptions):
    fields = []


@register(models.PerformanceDashboardPage)
class PerformanceDashboardPageTranslationOptions(BaseTranslationOptions):
    fields = []


@register(models.PerformanceDashboardNotesPage)
class PerformanceDashboardNotesPageTranslationOptions(BaseTranslationOptions):
    fields = []


@register(models.TopicLandingPage)
class TopicLandingPageTranslationOptions(BaseTranslationOptions):
    fields = []


@register(models.SuperregionPage)
class SuperregionPage(BaseTranslationOptions):
    fields = []


@register(models.ArticleListingPage)
class ArticleListingPageTranslationOptions(BaseTranslationOptions):
    fields = []


@register(models.ArticlePage)
@register(models.MarketArticlePage)
class ArticlePageTranslationOptions(BaseTranslationOptions):
    fields = []


@register(models.HomePage)
@register(models.HomePageOld)
class HomePageTranslationOptions(BaseTranslationOptions):
    fields = []


@register(models.EUExitInternationalFormPage)
class EUExitInternationalFormPageTranslationOptions(BaseTranslationOptions):
    fields = []


@register(models.EUExitDomesticFormPage)
class EUExitDomesticFormPageTranslationOptions(BaseTranslationOptions):
    fields = []


@register(models.EUExitFormSuccessPage)
class EUExitFormSuccessPageTranslationOptions(BaseTranslationOptions):
    fields = []


@register(models.EUExitFormPages)
class EUExitFormPagesTranslationOptions(BaseTranslationOptions):
    fields = []


@register(models.InternationalLandingPage)
class InternationalLandingPageTranslationOptions(BaseTranslationOptions):
    fields = []


@register(models.ContactUsGuidancePage)
class ContactUsGuidancePageTranslationOptions(BaseTranslationOptions):
    fields = []


@register(models.ContactSuccessPage)
class ContactSuccessPageTranslationOptions(BaseTranslationOptions):
    fields = []


@register(models.ContactUsGuidancePages)
class ContactUsGuidancePagesTranslationOptions(BaseTranslationOptions):
    fields = []


@register(models.ContactSuccessPages)
class ContactSuccessPagesTranslationOptions(BaseTranslationOptions):
    fields = []


@register(models.AllContactPagesPage)
class AllContactPagesPageTranslationOptions(BaseTranslationOptions):
    fields = []
