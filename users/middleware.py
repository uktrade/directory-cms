from django.shortcuts import redirect
from django.urls import reverse_lazy
from .models import UserProfile


class RedirectAdminUsersToRequestAccessViewsMiddleware:

    admin_root_url = reverse_lazy('wagtailadmin_home')
    permitted_admin_urls = (
        reverse_lazy('wagtailusers_users:sso_request_access'),
        reverse_lazy('wagtailusers_users:sso_request_access_success'),
    )

    def process_request(self, request):

        user = request.user

        # allow the view to handle these
        if not user.is_authenticated() or user.is_superuser:
            return

        # not an 'admin' url, so no need to intervene
        if not request.url.startswith(self.admin_root_url):
            return

        # no need to redirect if these views are being accessed
        for url in self.permitted_admin_urls:
            if request.url == url:
                return

        if user.profile.assignment_status == UserProfile.ASSIGNMENT_STATUS_CREATED: # noqa
            return redirect('wagtailusers_users:sso_request_access')

        if user.profile.assignment_status == UserProfile.ASSIGNMENT_STATUS_AWAITING_APPROVAL: # noqa
            return redirect('wagtailusers_users:sso_request_access_success')
