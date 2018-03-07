from find_a_supplier import models
from modeltranslation.translator import TranslationOptions
from modeltranslation.decorators import register


@register(models.IndustryPage)
class IndustryPageTranslationOptions(TranslationOptions):
    fields = (
        'hero_text',
        'lede',
        'lede_column_one',
        'lede_column_two',
        'lede_column_three',
        'case_study',
        'sector_label',
        'seo_description',
        'lede_column_one_icon',
        'lede_column_two_icon',
        'lede_column_three_icon',
    )
