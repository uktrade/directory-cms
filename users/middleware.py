from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.utils.deprecation import MiddlewareMixin
from .models import UserProfile


class SSORedirectUsersToRequestAccessViews(MiddlewareMixin):

    admin_root_url = reverse_lazy('wagtailadmin_home')
    ignore_admin_urls = (
        reverse_lazy('sso:request_access'),
        reverse_lazy('sso:request_access_success'),
    )

    def process_request(self, request):

        user = request.user

        if not user.is_authenticated or user.is_superuser:
            # allow the view to handle these
            return

        if not request.path.startswith(str(self.admin_root_url)):
            # not an 'admin' url, so no need to intervene
            return

        # no need to intervene if these views are already being accessed
        for url in self.ignore_admin_urls:
            if request.path == str(url):
                return

        profile = user.userprofile

        if profile.assignment_status == UserProfile.STATUS_CREATED:
            return redirect('sso:request_access')

        if profile.assignment_status == UserProfile.STATUS_AWAITING_APPROVAL:
            return redirect('sso:request_access_success')
