from invest import models


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
    ]
