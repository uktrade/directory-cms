import pytest

from find_a_supplier import models
from find_a_supplier.tests import factories


@pytest.mark.django_db
def test_industries_page_published_url_field():
    instance = models.IndustryLandingPage()

    assert instance.get_url() == (
        'http://supplier.trade.great:8005/industries/'
    )


def test_app_models():
    assert models.FindASupplierApp.allowed_subpage_models() == [
        models.FindASupplierApp,
        models.IndustryLandingPage,
        models.IndustryArticlePage,
        models.LandingPage,
        models.IndustryContactPage
    ]


@pytest.mark.django_db
def test_industry_contact_page_url():
    page = factories.IndustryContactPageFactory()

    assert page.get_url() == (
        'http://supplier.trade.great:8005/industries/contact/'
    )
