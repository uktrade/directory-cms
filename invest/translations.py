from modeltranslation.decorators import register

from core.translation import BaseTranslationOptions
from .models import InvestHomePage


@register(InvestHomePage)
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
