from wagtail.api.v2.endpoints import BaseAPIEndpoint, PagesAPIEndpoint
from wagtail.wagtailcore.models import Page

from django.shortcuts import redirect

from config.signature import SignatureCheckPermission
from core import permissions


class PagesOptionalDraftAPIEndpoint(PagesAPIEndpoint):
    queryset = Page.objects.all()
    meta_fields = []

    @property
    def permission_classes(self):
        permission_classes = [SignatureCheckPermission]
        if permissions.DraftTokenPermisison.TOKEN_PARAM in self.request.GET:
            permission_classes.append(permissions.DraftTokenPermisison)
        return permission_classes

    def get_queryset(self):
        return self.queryset

    def get_object(self):
        instance = super().get_object()
        if self.request.GET.get(permissions.DraftTokenPermisison.TOKEN_PARAM):
            instance = instance.get_latest_revision_as_page()
        return instance


class DraftRedirectView(BaseAPIEndpoint):
    permission_classes = []
    model = Page

    def get(self, request, *args, **kwargs):
        return redirect(self.get_object().specific.draft_url)
