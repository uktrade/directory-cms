from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.db import transaction
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.utils.translation import ugettext as _
from django.views.generic import CreateView, ListView, View
from wagtail.admin import messages
from wagtail.admin.utils import send_notification
from wagtail.core.models import PageRevision

from .forms import SubmitForm
from .models import Moderation


@method_decorator(login_required, name='dispatch')
class PendingModerations(ListView):
    model = Moderation
    template_name = "moderation_queue/list.html"


@method_decorator(login_required, name='dispatch')
class ApproveModeration(View):
    """
    Approve moderation requests.

    This is a modified version of wagtail.admin.views.pages.approve_moderation
    to handle Moderation objects in lock step with
    PageRevision.submitted_for_moderation.
    """
    http_method_names = ['post']

    def post(self, request, *args, **kwargs):
        moderation = get_object_or_404(Moderation, id=self.kwargs['pk'])

        if not moderation.revision.page.permissions_for_user(request.user).can_publish():
            raise PermissionDenied

        if not moderation.revision.submitted_for_moderation:
            page_title = moderation.revision.page.get_admin_display_title()
            messages.error(request, _(f"The page '{page_title}' is not currently awaiting moderation."))
            return redirect('wagtailadmin_home')

        page = moderation.revision.page
        revision = moderation.revision

        with transaction.atomic():
            revision.approve_moderation()
            moderation.reviews.create(user=request.user, is_accepted=True)

        message = _("Page '{0}' published.").format(page.get_admin_display_title())
        buttons = []
        if page.url is not None:
            buttons.append(messages.button(page.url, _('View live'), new_window=True))
        buttons.append(messages.button(reverse('wagtailadmin_pages:edit', args=(page.id,)), _('Edit')))
        messages.success(request, message, buttons=buttons)

        if not send_notification(revision.id, 'approved', request.user.pk):
            messages.error(request, _("Failed to send approval notifications"))

        return redirect('wagtailadmin_home')


class PreviewModeration(View):
    """
    Preview a moderation request.

    This is based on wagtail.admin.views.page.preview_for_moderation but looks
    at Modreation objects instead of PageReivews.  It doesn't check the status
    of PageReview.submitted_for_moderation since it is expected this view will
    be used for previewing Pages which are pending or have passed moderation.
    """
    http_method_names = ['get']

    def get(self, request, *args, **kwargs):
        moderation = get_object_or_404(Moderation, id=self.kwargs['pk'])
        if not moderation.revision.page.permissions_for_user(request.user).can_publish():
            raise PermissionDenied

        page = moderation.revision.as_page_object()

        # pass in the real user request rather than page.dummy_request(), so that request.user
        # and request.revision_id will be picked up by the wagtail user bar
        return page.serve_preview(request, page.default_preview_mode)


@method_decorator(login_required, name='dispatch')
class RejectModeration(View):
    """
    Reject moderation requests.

    This is a modified version of wagtail.admin.views.pages.reject_moderation
    to handle Moderation objects in lock step with
    PageRevision.submitted_for_moderation.
    """
    http_method_names = ['post']

    def post(self, request, *args, **kwargs):
        moderation = get_object_or_404(Moderation, id=self.kwargs['pk'])

        if not moderation.revision.page.permissions_for_user(request.user).can_publish():
            raise PermissionDenied

        if not moderation.revision.submitted_for_moderation:
            page_title = moderation.revision.page.get_admin_display_title()
            messages.error(request, _(f"The page '{page_title}' is not currently awaiting moderation."))
            return redirect('wagtailadmin_home')

        page = moderation.revision.page
        revision = moderation.revision

        with transaction.atomic():
            revision.reject_moderation()
            moderation.reviews.create(user=request.user, is_accepted=False)

        page_title = page.get_admin_display_title()
        messages.success(request, _(f"Page '{page_title}' rejected for publication."), buttons=[
            messages.button(reverse('wagtailadmin_pages:edit', args=(page.id,)), _('Edit'))
        ])
        if not send_notification(revision.id, 'rejected', request.user.pk):
            messages.error(request, _("Failed to send rejection notifications"))

        return redirect('wagtailadmin_home')


@method_decorator(login_required, name='dispatch')
class SubmitModeration(CreateView):
    form_class = SubmitForm
    model = Moderation
    success_url = reverse_lazy('wagtailadmin_explore_root')
    template_name = 'moderation_queue/submit.html'

    def form_valid(self, form):
        revision = get_object_or_404(PageRevision, id=self.kwargs['pk'])

        # TODO: should we remove exiting Moderation rows for the given page?
        self.object = Moderation.objects.create(
            revision=revision,
            publish_at=form.cleaned_data['publish_at'],
            comment=form.cleaned_data['comment'],
        )

        return redirect(self.get_success_url())
