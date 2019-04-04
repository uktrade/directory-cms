from modeltranslation.decorators import register

from core.translation import BaseTranslationOptions
from . import models


@register(models.InvestHomePage)
class InvestHomePageTranslation(BaseTranslationOptions):
    fields = (
        'breadcrumbs_label',
        'heading',
        'sub_heading',
        'hero_call_to_action_text',

        'benefits_section_title',
        'benefits_section_intro',
        'benefits_section_content',
        'benefits_section_img',
        'benefits_section_img_caption',

        'capital_invest_section_title',
        'capital_invest_section_content',
        'capital_invest_section_cta_text',
        'capital_invest_section_background_image',

        'eu_exit_section_title',
        'eu_exit_section_content',
        'eu_exit_section_call_to_action_text',
        'eu_exit_section_img',
        'eu_exit_section_img_caption',

        # subsections
        'subsection_title_one',
        'subsection_content_one',

        'subsection_title_two',
        'subsection_content_two',

        'subsection_title_three',
        'subsection_content_three',

        'subsection_title_four',
        'subsection_content_four',

        'subsection_title_five',
        'subsection_content_five',

        'subsection_title_six',
        'subsection_content_six',

        'subsection_title_seven',
        'subsection_content_seven',

        'sector_title',
        'sector_intro',
        'hpo_title',
        'hpo_intro',
        'setup_guide_title',
        'setup_guide_content',
        'setup_guide_img',
        'setup_guide_img_caption',
        'setup_guide_call_to_action_text',
        'setup_guide_lead_in',
        'how_we_help_title',
        'how_we_help_lead_in',
        # how we help
        'how_we_help_text_one',
        'how_we_help_icon_one',

        'how_we_help_text_two',
        'how_we_help_icon_two',

        'how_we_help_text_three',
        'how_we_help_icon_three',

        'how_we_help_text_four',
        'how_we_help_icon_four',

        'how_we_help_text_five',
        'how_we_help_icon_five',

        'how_we_help_text_six',
        'sector_button_text',
        'contact_section_title',
        'contact_section_content',
        'contact_section_call_to_action_text'
    )


@register(models.SectorPage)
class SectorPageTranslation(BaseTranslationOptions):
    fields = (
        'description',
        'heading',
        'pullout_text',
        'pullout_stat',
        'pullout_stat_text',
        # subsections
        'subsection_title_one',
        'subsection_content_one',
        'subsection_map_one',

        'subsection_title_two',
        'subsection_content_two',
        'subsection_map_two',

        'subsection_title_three',
        'subsection_content_three',
        'subsection_map_three',

        'subsection_title_four',
        'subsection_content_four',
        'subsection_map_four',

        'subsection_title_five',
        'subsection_content_five',
        'subsection_map_five',

        'subsection_title_six',
        'subsection_content_six',
        'subsection_map_six',

        'subsection_title_seven',
        'subsection_content_seven',
        'subsection_map_seven'
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
        # subsections
        'subsection_title_one',
        'subsection_content_one',

        'subsection_title_two',
        'subsection_content_two',

        'subsection_title_three',
        'subsection_content_three',

        'subsection_title_four',
        'subsection_content_four',

        'subsection_title_five',
        'subsection_content_five',

        'subsection_title_six',
        'subsection_content_six',

        'subsection_title_seven',
        'subsection_content_seven',
    )


@register(models.SetupGuideLandingPage)
class SetupGuideLandingPageTranslation(BaseTranslationOptions):
    fields = (
        'heading',
        'sub_heading',
        'lead_in',
    )


@register(models.HighPotentialOpportunityFormPage)
class HighPotentialOpportunityFormPageTranslationOptions(
    BaseTranslationOptions
):
    fields = []


@register(models.HighPotentialOpportunityDetailPage)
class HighPotentialOpportunityDetailPageTranslationOptions(
    BaseTranslationOptions
):
    fields = []


@register(models.InvestApp)
class InvestAppTranslationOptions(BaseTranslationOptions):
    fields = []


@register(models.HighPotentialOpportunityFormSuccessPage)
class HighPotentialOpportunityFormSuccessPageTranslationOptions(
    BaseTranslationOptions
):
    fields = []
