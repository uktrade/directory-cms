import pytest

from invest import models
from . import factories


def test_invest_app_models():
    assert models.InvestApp.allowed_subpage_models() == [
        models.InvestApp,
        models.SectorLandingPage,
        models.RegionLandingPage,
        models.SectorPage,
        models.SetupGuideLandingPage,
        models.SetupGuidePage,
        models.InvestHomePage,
        models.InfoPage,
        models.HighPotentialOpportunityFormPage,
        models.HighPotentialOpportunityDetailPage,
        models.HighPotentialOpportunityFormSuccessPage,
    ]


@pytest.mark.django_db
def test_high_potential_opportunity_form_get_url():
    page = factories.HighPotentialOpportunityFormPageFactory()

    assert page.get_url() == (
        'http://invest.trade.great:8011/high-potential-opportunities/rail/'
        'contact/'
    )
