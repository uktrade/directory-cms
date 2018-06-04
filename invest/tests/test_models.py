from invest import models


def test_app_models():
    assert models.InvestApp.allowed_subpage_models() == [
        models.InvestApp,
        models.SectorLandingPage,
        models.SectorPage,
        models.InvestHomePage,
        models.InfoPage,
        models.SetupGuideLandingPage,
        models.SetupGuidePage
    ]
