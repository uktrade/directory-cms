import pytest

from export_readiness import models


def test_app_models():
    assert models.ExportReadinessApp.allowed_subpage_models() == [
        models.ExportReadinessApp,
        models.TermsAndConditionsPage,
        models.PrivacyAndCookiesPage,
        models.GetFinancePage,
    ]


@pytest.mark.django_db
def test_set_slug():
    instance = models.ExportReadinessApp.objects.create(
        title_en_gb='the app',
        depth=2,
        path='/thing',
    )

    assert instance.slug_en_gb == 'the-app'
