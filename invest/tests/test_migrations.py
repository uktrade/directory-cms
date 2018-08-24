import pytest

from invest.tests import factories


@pytest.mark.skip(rason='slow')
@pytest.mark.django_db
def test_populate_historic_slug_service_name(migration, settings):
    page = factories.InfoPageFactory.create()

    migration.before([
        ('core', '0010_auto_20180815_1304'),
        ('invest', '0007_auto_20180719_1414'),
    ])

    # create the new `service_name` field
    apps = migration.apply('invest', '0008_auto_20180817_1630')

    page = apps.get_model('invest', 'InfoPage').objects.get(pk=page.pk)

    assert page.service_name is None

    # populate the `service_name field`
    migration.apply('core', '0011_auto_20180817_1631')

    page.refresh_from_db()

    assert page.service_name == 'INVEST'
