from urllib.parse import urljoin
from django.core import signing

from wagtail.core.models import Page

from core import constants

from django.shortcuts import redirect


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
        return urljoin(app_url, self.view_path)

    @property
    def preview_url(self):
        return self.published_url + '?draft_token=' + self.get_draft_token()

    def serve(self, request, *args, **kwargs):
        if getattr(request, 'is_preview', False):
            url = self.preview_url
        else:
            url = self.published_url
        return redirect(url)
