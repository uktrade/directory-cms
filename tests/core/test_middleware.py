import pytest

from django.conf import settings
from django.utils import translation

from core import middleware

pytestmark = pytest.mark.django_db


def test_locale_middleware_installed():
    expected = 'core.middleware.LocaleQuerystringMiddleware'
    assert expected in settings.MIDDLEWARE


def test_locale_middleware_sets_querystring_language(rf):
    request = rf.get('/', {'lang': 'en-gb'})
    instance = middleware.LocaleQuerystringMiddleware()

    instance.process_request(request)

    expected = 'en-gb'
    assert request.LANGUAGE_CODE == expected == translation.get_language()


def test_locale_middleware_ignored_invalid_querystring_language(rf):
    request = rf.get('/', {'lang': 'plip'})
    instance = middleware.LocaleQuerystringMiddleware()

    instance.process_request(request)

    expected = settings.LANGUAGE_CODE
    assert request.LANGUAGE_CODE == expected == translation.get_language()


def test_locale_middleware_handles_missing_querystring_language(rf):
    request = rf.get('/')
    instance = middleware.LocaleQuerystringMiddleware()

    instance.process_request(request)

    expected = settings.LANGUAGE_CODE
    assert request.LANGUAGE_CODE == expected == translation.get_language()


def test_maintenance_mode_middleware_installed():
    expected = 'core.middleware.MaintenanceModeMiddleware'
    assert expected in settings.MIDDLEWARE


def test_maintenance_mode_middleware_feature_flag_on(rf, settings):
    settings.FEATURE_FLAGS['MAINTENANCE_MODE_ON'] = True
    request = rf.get('/')

    response = middleware.MaintenanceModeMiddleware().process_request(request)

    assert response.status_code == 503
    assert response.content == b'CMS is offline for maintenance'


def test_maintenance_mode_middleware_feature_flag_off(rf, settings):
    settings.FEATURE_FLAGS['MAINTENANCE_MODE_ON'] = False

    request = rf.get('/')

    response = middleware.MaintenanceModeMiddleware().process_request(request)

    assert response is None
