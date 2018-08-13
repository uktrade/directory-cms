import pytest
from django.core.management import call_command

from . import factories


@pytest.mark.django_db
def test_update_invest_slugs(migration, root_page):
    page_one = factories.InfoPageFactory(
        slug='invest-foo-bar',
        slug_en_gb='invest-foo-bar',
        content='whatever',
        content_en_gb='whatever'
    )

    assert page_one.slug == 'invest-foo-bar'

    call_command('remove_invest_prefix_from_slugs')

    page_one.refresh_from_db()

    assert page_one.slug == 'foo-bar'
