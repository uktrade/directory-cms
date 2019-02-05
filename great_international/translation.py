from modeltranslation.decorators import register

from core.translation import BaseTranslationOptions
from great_international import models


@register(models.GreatInternationalApp)
class GreatInternationalAppTranslationOptions(BaseTranslationOptions):
    fields = []


@register(models.InternationalMarketingPages)
class MarketingPages(BaseTranslationOptions):
    fields = []


@register(models.InternationalArticlePage)
class ArticlePageTranslationOptions(BaseTranslationOptions):
    fields = []


@register(models.InternationalHomePage)
class HomePageTranslationOptions(BaseTranslationOptions):
    fields = []
