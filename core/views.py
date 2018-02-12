from wagtail.api.v2.endpoints import BaseAPIEndpoint, PagesAPIEndpoint
from wagtail.core.models import Page

from django.shortcuts import redirect
from django.views.generic import TemplateView

from config.signature import SignatureCheckPermission
from core.permissions import DraftTokenPermisison


class HelloWorldView(TemplateView):
    template_name = 'core/hello-world.html'


class PagesOptionalDraftAPIEndpoint(PagesAPIEndpoint):
    meta_fields = []

    @property
    def permission_classes(self):
        permissions = [SignatureCheckPermission]
        if DraftTokenPermisison.TOKEN_PARAM in self.request.GET:
            permissions.append(DraftTokenPermisison)
        return permissions

    def get_object(self):
        instance = super().get_object()
        if self.request.GET.get(DraftTokenPermisison.TOKEN_PARAM):
            instance = instance.get_latest_revision_as_page()
        return instance


class DraftRedirectView(BaseAPIEndpoint):
    permission_classes = []
    model = Page

    def get(self, request, *args, **kwargs):
        return redirect(self.get_object().specific.draft_url)
