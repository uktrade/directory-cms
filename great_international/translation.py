from modeltranslation.decorators import register

from core.translation import BaseTranslationOptions
from great_international import models


@register(models.GreatInternationalApp)
class GreatInternationalAppTranslationOptions(BaseTranslationOptions):
    fields = []


@register(models.InternationalSectorPage)
class InternationalSectorPageTranslationOptions(BaseTranslationOptions):
    fields = []


@register(models.InternationalArticlePage)
class InternationalArticlePageTranslationOptions(BaseTranslationOptions):
    fields = []


@register(models.InternationalCampaignPage)
class InternationalCampaignPageTranslationOptions(BaseTranslationOptions):
    fields = []


@register(models.InternationalHomePage)
class InternationalHomePageTranslationOptions(BaseTranslationOptions):
    fields = []


@register(models.InternationalArticleListingPage)
class InternationalArticleListingPage(BaseTranslationOptions):
    fields = []


@register(models.InternationalRegionPage)
class InternationalRegionPageTranslationOptions(BaseTranslationOptions):
    fields = []


@register(models.InternationalTopicLandingPage)
class InternationalTopicLandingPageTranslationOptions(BaseTranslationOptions):
    fields = []


@register(models.InternationalCuratedTopicLandingPage)
class InternationalCuratedTopicLandingPageTranslationOptions(
    BaseTranslationOptions
):
    fields = []


@register(models.InternationalGuideLandingPage)
class InternationalGuideLandingPageTranslationOptions(
    BaseTranslationOptions
):
    fields = []


@register(models.InternationalLocalisedFolderPage)
class InternationalRegionalFolderPageTranslationOptions(
    BaseTranslationOptions
):
    fields = []
