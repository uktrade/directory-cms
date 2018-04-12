from itertools import product
import pytest

from modeltranslation.utils import build_localized_fieldname
from wagtail.wagtailcore.models import Page

from find_a_supplier.tests.factories import IndustryPageFactory


@pytest.fixture
def page():
    return IndustryPageFactory(
        parent=Page.objects.get(pk=1),
    )


@pytest.fixture
def translated_page(settings):
    page = IndustryPageFactory(
        parent=Page.objects.get(pk=1),
        title_en_gb='ENGLISH',
        title_de='GERMAN',
        title_ja='JAPANESE',
        title_zh_hans='SIMPLIFIED CHINESE',
        title_fr='FRENCH',
        title_es='SPANISH',
        title_pt='PORTUGUESE',
        title_pt_br='BRAZILIAN',
        title_ar='ARABIC',
        breadcrumbs_label_en_gb='label',
        introduction_text_en_gb='lede',
        search_description_en_gb='description',
        hero_text_en_gb='hero text',
        introduction_column_one_text_en_gb='lede column one',
        introduction_column_two_text_en_gb='lede column two',
        introduction_column_three_text_en_gb='lede column three',
        company_list_call_to_action_text_en_gb='view all',
        company_list_text_en_gb='the title',
    )
    field_names = page.get_required_translatable_fields()
    language_codes = settings.LANGUAGES
    for field_name, (language_code, _) in product(field_names, language_codes):
        localized_name = build_localized_fieldname(field_name, language_code)
        if not getattr(page, localized_name):
            setattr(page, localized_name, localized_name + '-value')
    page.save()
    return page


@pytest.fixture
def page_with_reversion(admin_user, translated_page):
    translated_page.title = 'published-title',
    translated_page.title_en_gb = 'published-title'
    translated_page.save()

    translated_page.title_en_gb = 'draft-title'
    translated_page.save_revision(
        user=admin_user,
        submitted_for_moderation=False,
    )
    return translated_page
