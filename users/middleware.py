from django.shortcuts import redirect
from django.urls import reverse_lazy
from .models import UserProfile


class SSORedirectUsersToRequestAccessViews:

    admin_root_url = reverse_lazy('wagtailadmin_home')
    ignore_admin_urls = (
        reverse_lazy('wagtailusers_users:sso_request_access'),
        reverse_lazy('wagtailusers_users:sso_request_access_success'),
    )

    def process_request(self, request):

        user = request.user

        if not user.is_authenticated() or user.is_superuser:
            # allow the view to handle these
            return

        if not request.url.startswith(self.admin_root_url):
            # not an 'admin' url, so no need to intervene
            return

        # no need to intervene if these views are already being accessed
        for url in self.ignore_admin_urls:
            if request.url == url:
                return

        if user.profile.assignment_status == UserProfile.CREATED:
            return redirect('wagtailusers_users:sso_request_access')

        if user.profile.assignment_status == UserProfile.AWAITING_APPROVAL:
            return redirect('wagtailusers_users:sso_request_access_success')
