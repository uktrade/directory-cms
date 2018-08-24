import pytest

from wagtail_factories import PageFactory
from modeltranslation.utils import build_localized_fieldname


@pytest.mark.skip(rason='slow')
@pytest.mark.django_db
def test_update_url_path(migration, settings):
    migration.before([('core', '0005_auto_20180423_1803')])

    field_names = (
        build_localized_fieldname('url_path', code)
        for code, _ in settings.LANGUAGES
    )

    page_one = PageFactory.build(path='0', depth=2)
    page_two = PageFactory.build(path='1', depth=2)

    for field_name in field_names:
        setattr(page_one, field_name, None)
        setattr(page_two, field_name, '/hello')

    page_one.save()
    page_two.save()

    migration.apply('core', '0006_auto_20180508_1331')

    page_one.refresh_from_db()
    page_two.refresh_from_db()

    for field_name in field_names:
        assert getattr(page_one, field_name) == '/'
        assert getattr(page_two, field_name) == '/hello'
