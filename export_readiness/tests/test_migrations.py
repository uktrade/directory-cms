import pytest

from core.models import HistoricSlug
from export_readiness.tests import factories
from export_readiness import models


@pytest.mark.skip('slow')
@pytest.mark.django_db
def test_populate_breadcrumb(migration, settings):
    page = factories.DeprecatedGetFinancePageFactory.create(
        breadcrumbs_label='breadcrumb',
    )
    historic_apps = migration.before([
        ('core', '0016_auto_20180823_2014'),
    ])

    historic_apps.get_model('core', 'Breadcrumb').objects.all().delete()

    apps = migration.apply('core', '0017_auto_20180823_1545')
    HistoricBreadcrumb = apps.get_model('core', 'Breadcrumb')
    HistoricContentType = apps.get_model('contenttypes', 'ContentType')
    content_type = HistoricContentType.objects.get_for_model(page)

    breadcrumb = HistoricBreadcrumb.objects.get(
        object_id=page.pk, content_type=content_type
    )

    assert breadcrumb.service_name == page.service_name
    assert breadcrumb.object_id == page.pk
    assert breadcrumb.label == 'breadcrumb'


@pytest.mark.skip(reason='slow')
@pytest.mark.django_db
def test_populate_service_name(migration, settings):
    page = factories.DeprecatedGetFinancePageFactory.create()
    models.GetFinancePage.objects.filter(pk=page.pk).update(service_name=None)
    HistoricSlug.objects.all().delete()

    page.refresh_from_db()

    assert page.service_name is None
    assert page.historicslug_set.all().count() == 0

    migration.before([('export_readiness', '0014_auto_20180829_1027')])

    apps = migration.apply('export_readiness', '0015_auto_20180830_0632')

    page = apps.get_model(
        'export_readiness', 'GetFinancePage'
    ).objects.get(pk=page.pk)

    assert page.service_name == 'EXPORT_READINESS'
    assert apps.get_model('core', 'HistoricSlug').objects.filter(
        page=page, service_name='EXPORT_READINESS'
    ).count() == 1


@pytest.mark.skip(reason='slow')
@pytest.mark.django_db
def test_deprecated_get_finance_page(migration, settings):
    page = factories.DeprecatedGetFinancePageFactory.create()
    HistoricSlug.objects.all().delete()
    page.slug = 'get-finance'
    page.save()

    migration.before(
        [('export_readiness', '0016_auto_20180905_1020')]
    )

    apps = migration.apply('export_readiness', '0017_auto_20180905_1022')

    page = apps.get_model(
        'export_readiness', 'DeprecatedGetFinancePage'
    ).objects.get(pk=page.pk)

    assert page.slug == 'get-finance-deprecated'
    assert apps.get_model('core', 'HistoricSlug').objects.filter(
        page=page,
        service_name='EXPORT_READINESS',
        slug='get-finance-deprecated'
    ).count() == 1
