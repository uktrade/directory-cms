import pytest

from export_readiness.tests import factories


@pytest.mark.skip('slow')
@pytest.mark.django_db
def test_populate_breadcrumb(migration, settings):
    page = factories.GetFinancePageFactory.create(
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
