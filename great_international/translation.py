from modeltranslation.decorators import register

from core.translation import BaseTranslationOptions
from great_international import models


@register(models.GreatInternationalApp)
class GreatInternationalAppTranslationOptions(BaseTranslationOptions):
    fields = []


@register(models.InternationalMarketingPages)
class InternationalMarketingPages(BaseTranslationOptions):
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
