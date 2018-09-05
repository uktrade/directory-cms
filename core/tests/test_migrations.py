import pytest

from core.models import HistoricSlug
from export_readiness.tests.factories import DeprecatedGetFinancePageFactory


@pytest.mark.skip(reason='slow')
@pytest.mark.django_db
def test_populate_historic_slug_service_name(migration, settings):
    page = DeprecatedGetFinancePageFactory.create()

    historic_slug = HistoricSlug.objects.get(page=page)
    historic_slug.service_name = None
    historic_slug.save()

    migration.before([('core', '0019_merge_20180829_0939')])
    apps = migration.apply('core', '0020_auto_20180830_1737')

    HistoricHistoricSlug = apps.get_model('core', 'HistoricSlug')
    assert HistoricHistoricSlug.objects.filter(
        page_id=page.pk, service_name='EXPORT_READINESS'
    ).count() == 1
