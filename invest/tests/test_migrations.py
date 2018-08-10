import pytest

from . import factories


@pytest.mark.django_db
def test_update_invest_slugs(migration, root_page):
    migration.before([('invest', '0007_auto_20180719_1414')])

    page_one = factories.InfoPageFactory(
        slug='invest-foo-bar',
        slug_en_gb='invest-foo-bar'
    )
    page_two = factories.SetupGuideLandingPageFactory(parent=root_page)

    assert page_one.slug == 'invest-foo-bar'
    assert page_two.slug == 'invest-setup-guide-landing-page'

    migration.apply('invest', '0008_auto_20180809_1609')

    page_one.refresh_from_db()
    page_two.refresh_from_db()

    assert page_one.slug == 'foo-bar'
    assert page_two.slug == 'setup-guide-landing-page'
