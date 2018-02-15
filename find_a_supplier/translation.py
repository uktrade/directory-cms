from find_a_supplier import models
from modeltranslation.translator import TranslationOptions
from modeltranslation.decorators import register


@register(models.Company)
class CompanyTranslationOptions(TranslationOptions):
    fields = (
        'image_alt',
        'name',
        'description',
        'url',
    )


@register(models.Showcase)
class ShowcaseTranslationOptions(TranslationOptions):
    fields = (
        'image_alt',
        'image_caption',
        'title',
        'synopsis',
        'testimonial',
        'testimonial_name',
        'testimonial_company',
        'company_name',
    )


@register(models.CaseStudyPage)
class CaseStudyPageTranslationOptions(TranslationOptions):
    fields = (
        'footer_text',
        'footer_title',
        'companies_section_title',
        'lede',
        'body',
        'key_facts',
        'read_more_text',
        'seo_description',
    )
