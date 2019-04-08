import pytest

from find_a_supplier import models


@pytest.mark.django_db
def test_industries_page_published_url_field():
    instance = models.IndustryLandingPage()

    assert instance.get_url() == (
        'http://supplier.trade.great:8005/industries/'
    )


def test_app_models():
    assert models.FindASupplierApp.allowed_subpage_models() == [
        models.FindASupplierApp,
        models.IndustryPage,
        models.IndustryLandingPage,
        models.IndustryArticlePage,
        models.LandingPage,
        models.IndustryContactPage
    ]
