import pytest

from export_readiness.tests import factories


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
def test_deprecated_get_finance_page(migration, settings):
    page = factories.DeprecatedGetFinancePageFactory.create()
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
