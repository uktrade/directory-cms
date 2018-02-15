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
