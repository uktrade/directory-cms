import pytest

import find_a_supplier.models
from export_readiness import models
from export_readiness.tests import factories


def test_app_models():
    assert models.ExportReadinessApp.allowed_subpage_models() == [
        models.ExportReadinessApp,
        models.TermsAndConditionsPage,
        models.PrivacyAndCookiesPage,
        models.GetFinancePage,
        models.PerformanceDashboardPage,
        models.PerformanceDashboardNotesPage,
        models.HighPotentialOfferFormPage,
    ]


@pytest.mark.parametrize('model', [
    models.ExportReadinessApp,
    find_a_supplier.models.FindASupplierApp,
])
def test_app_required_translatable_fields(model):
    assert model.get_required_translatable_fields() == []


@pytest.mark.django_db
def test_set_slug():
    instance = models.ExportReadinessApp.objects.create(
        title_en_gb='the app',
        depth=2,
        path='/thing',
    )

    assert instance.slug_en_gb == 'the-app'


@pytest.mark.django_db
def test_get_finance_breadcrumbs():
    page = factories.GetFinancePageFactory.create()
    assert page.breadcrumb.first().label == page.breadcrumbs_label
