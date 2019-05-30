from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.db import transaction
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.utils.translation import ugettext as _
from django.views.generic import ListView, View
from wagtail.admin import messages
from wagtail.admin.utils import send_notification

from .models import PagePendingModeration


@method_decorator(login_required, name='dispatch')
class PendingModerations(ListView):
    model = PagePendingModeration
    template_name = "moderation_queue/list.html"


@method_decorator(login_required, name='dispatch')
class ApproveModeration(View):
    """
    Approve moderation requests.

    This is a modified version of wagtail.admin.views.pages.approve_moderation
    to handle PagePendingModeration objects in lock step with
    PageRevision.submitted_for_moderation.
    """
    http_method_names = ['post']

    def post(self, request, *args, **kwargs):
        pending_moderation = get_object_or_404(PagePendingModeration, id=self.kwargs['pk'])

        if not pending_moderation.revision.page.permissions_for_user(request.user).can_publish():
            raise PermissionDenied

        if not pending_moderation.revision.submitted_for_moderation:
            page_title = pending_moderation.revision.page.get_admin_display_title()
            messages.error(request, _(f"The page '{page_title}' is not currently awaiting moderation."))
            return redirect('wagtailadmin_home')

        page = pending_moderation.revision.page
        revision = pending_moderation.revision

        with transaction.atomic():
            revision.approve_moderation()
            pending_moderation.delete()

        message = _("Page '{0}' published.").format(page.get_admin_display_title())
        buttons = []
        if page.url is not None:
            buttons.append(messages.button(page.url, _('View live'), new_window=True))
        buttons.append(messages.button(reverse('wagtailadmin_pages:edit', args=(page.id,)), _('Edit')))
        messages.success(request, message, buttons=buttons)

        if not send_notification(revision.id, 'approved', request.user.pk):
            messages.error(request, _("Failed to send approval notifications"))

        return redirect('wagtailadmin_home')


@method_decorator(login_required, name='dispatch')
class RejectModeration(View):
    """
    Reject moderation requests.

    This is a modified version of wagtail.admin.views.pages.reject_moderation
    to handle PagePendingModeration objects in lock step with
    PageRevision.submitted_for_moderation.
    """
    http_method_names = ['post']

    def post(self, request, *args, **kwargs):
        pending_moderation = get_object_or_404(PagePendingModeration, id=self.kwargs['pk'])

        if not pending_moderation.revision.page.permissions_for_user(request.user).can_publish():
            raise PermissionDenied

        if not pending_moderation.revision.submitted_for_moderation:
            page_title = pending_moderation.revision.page.get_admin_display_title()
            messages.error(request, _(f"The page '{page_title}' is not currently awaiting moderation."))
            return redirect('wagtailadmin_home')

        page = pending_moderation.revision.page
        revision = pending_moderation.revision

        with transaction.atomic():
            revision.reject_moderation()
            pending_moderation.delete()

        page_title = page.get_admin_display_title()
        messages.success(request, _(f"Page '{page_title}' rejected for publication."), buttons=[
            messages.button(reverse('wagtailadmin_pages:edit', args=(page.id,)), _('Edit'))
        ])
        if not send_notification(revision.id, 'rejected', request.user.pk):
            messages.error(request, _("Failed to send rejection notifications"))

        return redirect('wagtailadmin_home')
