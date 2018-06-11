from modeltranslation.decorators import register

from core.translation import BaseTranslationOptions
from . import models


@register(models.InvestHomePage)
class InvestHomePageTranslation(BaseTranslationOptions):
    fields = (
        'heading',
        'sub_heading',
        'subsections',
        'sector_title',
        'setup_guide_title',
        'setup_guide_lead_in',
        'how_we_help_title',
        'how_we_help_lead_in',
        'how_we_help',
        'sector_button_text'
    )


@register(models.SectorPage)
class SectorPageTranslation(BaseTranslationOptions):
    fields = (
        'description',
        'heading',
        'pullout',
        'subsections',
    )


@register(models.SectorLandingPage)
class SectorLandingPageTranslation(BaseTranslationOptions):
    fields = (
        'heading',
    )


@register(models.RegionLandingPage)
class RegionLandingPageTranslation(BaseTranslationOptions):
    fields = (
        'heading',
    )


@register(models.InfoPage)
class InfoPageTranslation(BaseTranslationOptions):
    fields = (
        'content',
    )


@register(models.SetupGuidePage)
class SetupGuidePageTranslation(BaseTranslationOptions):
    fields = (
        'description',
        'heading',
        'sub_heading',
        'subsections',
    )


@register(models.SetupGuideLandingPage)
class SetupGuideLandingPageTranslation(BaseTranslationOptions):
    fields = (
        'heading',
        'sub_heading',
        'lead_in',
    )
