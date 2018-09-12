import pytest

from export_readiness.models import ExportReadinessApp
from find_a_supplier.models import FindASupplierApp
from invest.models import InvestApp


@pytest.mark.skip('slow')
@pytest.mark.django_db
def test_populate_slug(migration, settings):
    ExportReadinessApp.objects.create(title='exred', path='0', depth=2)
    FindASupplierApp.objects.create(title='fas', path='01', depth=2)
    InvestApp.objects.create(title='invest', path='02', depth=2)

    ExportReadinessApp.objects.all().update(slug='a')
    FindASupplierApp.objects.all().update(slug='b')
    InvestApp.objects.all().update(slug='c')

    migration.before([
        ('core', '0022_auto_20180906_1344'),
    ])

    apps = migration.apply('core', '0023_auto_20180912_0758')
    HistoricExportReadinessApp = apps.get_model(
        'export_readiness', 'ExportReadinessApp'
    )
    HistoricFindASupplierApp = apps.get_model(
        'find_a_supplier', 'FindASupplierApp'
    )
    HistoricInvestApp = apps.get_model('invest', 'InvestApp')

    assert HistoricExportReadinessApp.objects.first().slug == (
        'export-readiness-app'
    )
    assert HistoricFindASupplierApp.objects.first().slug == (
        'find-a-supplier-app'
    )
    assert HistoricInvestApp.objects.first().slug == 'invest-app'
