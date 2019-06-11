import jwt
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.db import transaction
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.utils.translation import ugettext as _
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import CreateView, ListView, View
from rest_framework.generics import CreateAPIView
from wagtail.admin import messages
from wagtail.admin.utils import send_notification
from wagtail.core.models import PageRevision

from .forms import SubmitForm
from .models import Moderation, ModeratorReview
from .serializers import ModeratorReviewSerializer


# FIXME: replace with review.api.views.ReviewTokenMixin once merged with the
# review-poc branch
class ReviewTokenMixin:
    authentication_classes = []

    @method_decorator(csrf_exempt)
    def dispatch(self, *args, **kwargs):
        review_token = self.request.GET.get('review_token')
        data = jwt.decode(
            review_token,
            settings.SECRET_KEY,
            algorithms=['HS256'],
        )
        self.reviewer_id = data['reviewer_id']
        self.page_revision_id = data['page_revision_id']

        return super().dispatch(*args, **kwargs)


@method_decorator(login_required, name='dispatch')
class Review(ListView):
    template_name = "moderation_queue/review.html"

    def get_context_data(self, **kwargs):
        pending_reviews = ModeratorReview.objects.filter(
            moderation__revision__user=self.request.user,
        ).order_by('created_at').select_related(
            'moderation',
            'moderation__revision',
            'moderation__revision__user',
            'user',
        )

        context = super().get_context_data(**kwargs)
        context['pending_reviews'] = pending_reviews
        return context

    def get_queryset(self):
        return (Moderation.objects.filter(revision__user=self.request.user)
                                  .accepted())


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
        page = moderation.revision.page
        revision = moderation.revision

        if not page.permissions_for_user(request.user).can_publish():
            raise PermissionDenied

        if not revision.submitted_for_moderation:
            page_title = moderation.revision.page.get_admin_display_title()
            messages.error(
                request,
                _(f"The page '{page_title}' is not currently awaiting moderation."),  # noqa: E501
            )
            return redirect('wagtailadmin_home')

        with transaction.atomic():
            revision.approve_moderation()
            moderation.reviews.create(user=request.user, is_accepted=True)

        admin_display_title = page.get_admin_display_title()
        message = _(f"Page '{admin_display_title}' published.")
        buttons = []
        if page.url is not None:
            buttons.append(messages.button(
                page.url,
                _('View live'),
                new_window=True,
            ))
        buttons.append(
            messages.button(
                reverse('wagtailadmin_pages:edit', args=(page.id,)),
                _('Edit'),
            ),
        )
        messages.success(request, message, buttons=buttons)

        if not send_notification(revision.id, 'approved', request.user.pk):
            messages.error(request, _("Failed to send approval notifications"))

        return redirect('wagtailadmin_home')


@method_decorator(login_required, name='dispatch')
class ModerationQueue(ListView):
    ordering = '-publish_at'
    paginate_by = 20
    queryset = Moderation.objects.pending()
    template_name = 'moderation_queue/all.html'


@method_decorator(login_required, name='dispatch')
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
        page = moderation.revision.page
        if not page.permissions_for_user(request.user).can_publish():
            raise PermissionDenied

        page = moderation.revision.as_page_object()

        # pass in the real user request rather than page.dummy_request(), so
        # that request.user and request.revision_id will be picked up by the
        # wagtail user bar
        return page.serve_preview(request, page.default_preview_mode)


@method_decorator(csrf_exempt, name='post')
class ReviewModeration(ReviewTokenMixin, CreateAPIView):
    queryset = ModeratorReview.objects.all()
    serializer_class = ModeratorReviewSerializer

    def create(self, request, *args, **kwargs):
        """

        """
        moderation = (Moderation.objects.filter(revision__page__pk=self.kwargs['pk'])  # noqa: E501
                                        .order_by('-created_at')
                                        .first())
        if moderation is None:
            raise Http404

        data = {
            'comment': request.data.get('comment'),
            'is_accepted': request.data.get('is_accepted'),
            'moderation': moderation.pk,
        }
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        return HttpResponseRedirect(request.META['HTTP_REFERER'])

        # TODO: use JS on the frontend so we can handle errors and not ping a
        # user between sites.
        # headers = self.get_success_headers(serializer.data)
        # from rest_framework import status
        # from rest_framework.response import Response
        # return Response(
        #     serializer.data,
        #     status=status.HTTP_201_CREATED,
        #     headers=headers,
        # )


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
        page = moderation.revision.page
        revision = moderation.revision

        if not page.permissions_for_user(request.user).can_publish():
            raise PermissionDenied

        if not revision.submitted_for_moderation:
            page_title = moderation.revision.page.get_admin_display_title()
            messages.error(
                request,
                _(f"The page '{page_title}' is not currently awaiting moderation."),  # noqa: E501
            )
            return redirect('wagtailadmin_home')

        with transaction.atomic():
            revision.reject_moderation()
            moderation.reviews.create(user=request.user, is_accepted=False)

        page_title = page.get_admin_display_title()
        buttons = [
            messages.button(
                reverse('wagtailadmin_pages:edit', args=(page.id,)),
                _('Edit'),
            ),
        ],
        messages.success(
            request,
            _(f"Page '{page_title}' rejected for publication."),
            buttons=buttons,
        )
        if not send_notification(revision.id, 'rejected', request.user.pk):
            messages.error(
                request,
                _("Failed to send rejection notifications"),
            )

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
