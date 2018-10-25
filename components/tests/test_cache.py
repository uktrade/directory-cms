from core.cache import is_registered_for_cache
from components import models


def test_cache_registration():
    for model in [
        models.BannerComponent,
    ]:
        assert is_registered_for_cache(model)
