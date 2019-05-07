from django.shortcuts import redirect, reverse_lazy


class RedirectAdminUsersToRequestAccessViewsMiddleware:

    admin_root_url = reverse_lazy('wagtailadmin_home')
    permitted_admin_urls = (
        reverse_lazy('wagtailusers_users:request_access'),
        reverse_lazy('wagtailusers_users:request_access_success'),
    )

    def process_request(self, request):

        user = self.request.user

        # allow the view to handle this as necessary
        if not user.is_authenticated() or user.is_superuser:
            return

        # not an 'admin' url, no need to intervene
        if not request.url.startswith(self.admin_root_url):
            return

        # no need to redirect if these views are being accessed
        for url in self.permitted_admin_urls:
            if request.url.startswith(url):
                return

        # redirect to request_access view
        if user.profile.assignment_status == 'created':
            return redirect('wagtailusers_users:request_access')

        # redirect to request_access_success view
        if user.profile.assignment_status == 'unassigned':
            return redirect('wagtailusers_users:request_access_success')
