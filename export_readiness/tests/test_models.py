import pytest

from export_readiness import models as exred_models
from find_a_supplier import models as fas_models


def test_app_models():
    assert exred_models.ExportReadinessApp.allowed_subpage_models() == [
        exred_models.ExportReadinessApp,
        exred_models.TermsAndConditionsPage,
        exred_models.PrivacyAndCookiesPage,
        exred_models.GetFinancePage,
        exred_models.PerformanceDashboardPage
    ]


@pytest.mark.parametrize('model', [
    exred_models.ExportReadinessApp,
    fas_models.FindASupplierApp,
    ]
)
def test_app_required_translatable_fields(model):
    assert model.get_required_translatable_fields() == []


@pytest.mark.django_db
def test_set_slug():
    instance = exred_models.ExportReadinessApp.objects.create(
        title_en_gb='the app',
        depth=2,
        path='/thing',
    )

    assert instance.slug_en_gb == 'the-app'
