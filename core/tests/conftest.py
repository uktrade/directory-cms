import pytest

from wagtail.wagtailcore.models import Page

from find_a_supplier.tests.factories import IndustryPageFactory


@pytest.fixture
def page():
    return IndustryPageFactory(
        parent=Page.objects.get(pk=1)
    )


@pytest.fixture
def translated_page():
    return IndustryPageFactory(
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
        title="translated",
    )


@pytest.fixture
def page_with_reversion(admin_user):
    page = IndustryPageFactory(
        parent=Page.objects.get(pk=1),
        title="published-title",
        title_en_gb="published-title",
    )
    page.title_en_gb = 'draft-title'
    page.save_revision(
        user=admin_user,
        submitted_for_moderation=False,
    )
    return page
