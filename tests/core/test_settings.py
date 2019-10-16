from django.conf import settings


def test_cookie_language_name_is_custom():
    assert settings.LANGUAGE_COOKIE_NAME == 'cms_language'
