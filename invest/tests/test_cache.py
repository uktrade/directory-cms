from core.cache import is_registered_for_cache

from invest import models


def test_cache_registration():
    for model in [
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
    ]:
        assert not is_registered_for_cache(model)
