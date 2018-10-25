from modeltranslation.decorators import register

from core.translation import BaseTranslationOptions
from components import models


@register(models.ComponentsApp)
class ComponentsAppTranslationOptions(BaseTranslationOptions):
    fields = []


@register(models.BannerComponent)
class BannerComponentTranslationOptions(BaseTranslationOptions):
    fields = (
        'banner_content',
        'banner_label',
    )
