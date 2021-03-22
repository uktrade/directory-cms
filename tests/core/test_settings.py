import pytest
from django.conf import settings

pytestmark = pytest.mark.django_db


def test_cookie_language_name_is_custom():
    assert settings.LANGUAGE_COOKIE_NAME == 'cms_language'
