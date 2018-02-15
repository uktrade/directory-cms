import functools
from urllib.parse import urljoin

from wagtail.wagtailcore.models import Page

from django.core import signing
from django.shortcuts import redirect

from core import constants


class BasePage(Page):

    class Meta:
        abstract = True

    def __init__(self, *args, **kwargs):
        self.signer = signing.Signer()
        super().__init__(*args, **kwargs)

    def get_draft_token(self):
        return self.signer.sign(self.pk)

    def is_draft_token_valid(self, draft_token):
        try:
            value = self.signer.unsign(draft_token)
        except signing.BadSignature:
            return False
        else:
            return str(self.pk) == str(value)

    @property
    def published_url(self):
        app_url = dict(constants.APP_URLS)[self.view_app]
        url_parts = [
            app_url, self.view_path, str(self.pk) + '/', self.slug + '/'
        ]
        return functools.reduce(urljoin, url_parts)

    @property
    def draft_url(self):
        return self.published_url + '?draft_token=' + self.get_draft_token()

    def serve(self, request, *args, **kwargs):
        return redirect(self.published_url)
