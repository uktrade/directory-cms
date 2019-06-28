from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.utils.translation import ugettext as _
from django.views.decorators.http import require_POST
from django.views.generic import CreateView, ListView, View
from wagtail.admin import messages
from wagtail.core.models import PageRevision

from .forms import SubmitForm
from .models import ModerationRequest, ModerationResponse


@method_decorator(login_required, name='dispatch')
class Review(ListView):
    template_name = "moderation_queue/review.html"

    def get_context_data(self, **kwargs):
        pending_responses = ModerationResponse.objects.filter(
            request__revision__user=self.request.user,
        ).order_by('created_at').select_related(
            'request',
            'request__revision',
            'request__revision__user',
            'reviewer',
        )

        context = super().get_context_data(**kwargs)
        context['pending_responses'] = pending_responses
        return context

    def get_queryset(self):
        return ModerationRequest.objects.filter(revision__user=self.request.user).accepted()


# TODO: Permission checks
@login_required
@require_POST
@transaction.atomic
def publish(request, moderation_request_id):
    moderation_request = get_object_or_404(ModerationRequest, id=moderation_request_id)
    if not moderation_request.is_2i_moderated or moderation_request.published:
        raise PermissionDenied

    revision = moderation_request.revision
    revision.publish()

    moderation_request.published = True
    moderation_request.save()

    messages.success(
        request,
        _(f"Published '{revision.page.get_admin_display_title()}'"),  # noqa: E501
        buttons=[
            messages.button(
                reverse('wagtailadmin_pages:edit', args=[revision.page_id]),
                _('Edit'),
            ),
            messages.button(
                revision.page.specific.get_url(),
                _('View live')
            ),
        ]
    )

    return redirect('moderation-queue:pending')


@method_decorator(login_required, name='dispatch')
class SubmitModerationRequest(CreateView):
    form_class = SubmitForm
    model = ModerationRequest
    template_name = 'moderation_queue/submit.html'

    @transaction.atomic
    def form_valid(self, form):
        revision = get_object_or_404(PageRevision, id=self.kwargs['pk'])

        # TODO: should we remove exiting ModerationRequest rows for the given page?
        self.object = ModerationRequest.objects.create(
            revision=revision,
            publish_at=form.cleaned_data['publish_at'],
            comment=form.cleaned_data['comment'],
        )

        revision.submitted_for_moderation = True
        revision.save(update_fields=['submitted_for_moderation'])

        messages.success(
            self.request,
            _(f"Successfully submitted '{revision.page.get_admin_display_title()}' for moderation."),  # noqa: E501
            buttons=[
                messages.button(
                    reverse('wagtailadmin_pages:edit', args=[revision.page_id]),
                    _('Edit'),
                ),
            ]
        )

        return redirect(reverse('wagtailadmin_explore', args=[revision.page.get_parent().id]))
