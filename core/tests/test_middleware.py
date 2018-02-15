from django.conf import settings
from django.utils import translation

from core import middleware


def test_locale_middleware_installed():
    expected = 'core.middleware.LocaleQuerystringMiddleware'
    assert expected in settings.MIDDLEWARE_CLASSES


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
