from django.contrib.auth.mixins import PermissionRequiredMixin
from django.shortcuts import redirect
from django.utils.translation import gettext as _
from wagtail.admin import messages


class WagtailAdminPermissionRequiredMixin(PermissionRequiredMixin):

    def handle_no_permission(self):
        messages.error(
            self.request,
            _('Sorry, you do not have permission to access this area.')
        )
        return redirect('wagtailadmin_home')
