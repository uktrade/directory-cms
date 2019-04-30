from django.conf import settings
from django.http import HttpResponse
from django.middleware.locale import LocaleMiddleware
from django.utils import translation

from core import helpers


class LocaleQuerystringMiddleware(LocaleMiddleware):

    def process_request(self, request):
        super().process_request(request)
        language_code = helpers.get_language_from_querystring(request)
        if language_code:
            translation.activate(language_code)
            request.LANGUAGE_CODE = translation.get_language()


class StubSiteMiddleware(LocaleMiddleware):
    """ Even though wagtail site middleware is not useful for this service,
    wagtail expects `request.site` to be present - so we populate it with None
    """

    def process_request(self, request):
        request.site = None


class MaintenanceModeMiddleware:

    def process_request(self, request):
        if settings.FEATURE_FLAGS['MAINTENANCE_MODE_ON']:
            return HttpResponse('CMS is offline for maintenance', status=503)
