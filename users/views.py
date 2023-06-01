from django.conf import settings
from django.contrib.auth import get_user_model, update_session_auth_hash
from django.shortcuts import redirect
from django.urls import reverse, reverse_lazy
from django.utils import timezone
from django.utils.translation import gettext as _
from django.views import generic
from wagtail.admin import messages
from wagtail.admin.views.generic import EditView
from wagtail import hooks
from wagtail.users.utils import user_can_delete_user
from wagtail.users.views.users import add_user_perm, change_user_perm

from users.models import UserProfile
from users.notifications import (
    notify_team_leader_of_pending_access_request,
    notify_user_of_access_request_approval,
)
from . import forms, mixins

User = get_user_model()


class WagtailUserActionBaseView(mixins.WagtailAdminPermissionRequiredMixin):
    hook_action = ''
    form_invalid_message = ''
    form_valid_message = ''

    def dispatch(self, request, *args, **kwargs):
        hook_name = 'before_{action}_user'.format(action=self.hook_action)
        for fn in hooks.get_hooks(hook_name):
            result = fn(request)
            if hasattr(result, 'status_code'):
                return result
        return super().dispatch(request, *args, **kwargs)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update(user=self.request.user)
        return kwargs

    def form_invalid(self, form):
        messages.error(self.request, _(self.form_invalid_message))
        return super().form_invalid(form)

    def handle_success_message(self):
        user = self.object
        messages.success(
            self.request,
            _(self.form_valid_message).format(user),
            buttons=[messages.button(reverse('great_users:edit', args=(user.pk,)), _('Edit'))],
        )
        hook_name = 'after_{action}_user'.format(action=self.hook_action)
        for fn in hooks.get_hooks(hook_name):
            result = fn(self.request, user)
            if hasattr(result, 'status_code'):
                return result


class CreateUserView(WagtailUserActionBaseView, generic.CreateView):
    form_class = forms.UserCreationForm
    model = User
    template_name = 'great_users/users/create.html'
    permission_required = add_user_perm
    hook_action = 'create'
    form_invalid_message = 'The user could not be created due to errors.'
    form_valid_message = 'User ' '{0}' ' created.'

    def form_valid(self, form):
        self.object = form.save()
        self.handle_success_message()
        return redirect('great_users:index')


class EditUserView(WagtailUserActionBaseView, generic.UpdateView):
    form_class = forms.UserEditForm
    model = User
    template_name = 'wagtailusers/users/edit.html'
    permission_required = change_user_perm
    hook_action = 'edit'
    form_invalid_message = 'The user could not be saved due to errors.'
    form_valid_message = 'User ' '{0}' ' updated.'

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        profile = self.object.userprofile

        self.is_approval = profile.assignment_status in (
            UserProfile.STATUS_CREATED,
            UserProfile.STATUS_AWAITING_APPROVAL,
        )
        if settings.FEATURE_FLAGS['ENFORCE_STAFF_SSO_ON'] and self.is_approval and request.method == 'GET':
            # Warn the current user that this is an 'approval'
            message_text = (
                "This user is awaiting approval and will be automatically "
                "notified via email if added to a group that grants access "
                "to the Wagtail CMS."
            )
            if profile.self_assigned_group:
                # Preselect the user-selcted group in the form
                self.initial['groups'] = [profile.self_assigned_group.id]
                # Also mention this to the current user
                message_text += (
                    " They requested to be added to the '{}' group, so this "
                    "has been preselected for you under the 'Roles' tab."
                ).format(profile.self_assigned_group.name)

            messages.warning(request, message_text)
        return super().dispatch(request, *args, **kwargs)

    def get_form_kwargs(self):
        editing_self = self.request.user == self.object
        kwargs = super().get_form_kwargs()
        kwargs.update(editing_self=editing_self)
        return kwargs

    def form_valid(self, form):
        self.object = user = form.save()

        if user == self.request.user and 'password1' in form.changed_data:
            # User is changing their own password;
            # need to update their session hash
            update_session_auth_hash(self.request, user)

        if self.is_approval and user.has_perm('wagtailadmin.access_admin'):
            self.mark_user_as_approved()
            self.notify_user()

        self.handle_success_message()
        return redirect('great_users:index')

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        can_delete = user_can_delete_user(self.request.user, self.object)
        ctx.update(can_delete=can_delete)
        return ctx

    def mark_user_as_approved(self):
        profile = self.object.userprofile
        profile.assignment_status = UserProfile.STATUS_APPROVED
        profile.approved_by = self.request.user
        profile.approved_at = timezone.now()
        profile.save()

    def notify_user(self):
        if settings.FEATURE_FLAGS['ENFORCE_STAFF_SSO_ON']:
            notify_user_of_access_request_approval(
                request=self.request,
                user_email=self.object.email,
                user_name=self.object.first_name,
                reviewer_name=self.request.user.get_full_name(),
            )


class SSORequestAccessView(EditView):
    model = UserProfile
    form_class = forms.SSORequestAccessForm
    permission_required = None
    error_message = 'There was a problem with your submission'
    template_name = "sso/request_access.html"
    success_url = reverse_lazy('great_sso:request_access_success')
    edit_url_name = 'wagtailadmin_workflows:edit'
    delete_url_name = 'wagtailadmin_workflows:disable'
    delete_item_label = _('Disable')

    def dispatch(self, request):
        self.get_object()
        if settings.USERS_REQUEST_ACCESS_PREVENT_RESUBMISSION:
            # Toggling behaviour here to aid local testing
            if self.object.assignment_status == UserProfile.STATUS_APPROVED:
                return redirect('wagtailadmin_home')
            if self.object.assignment_status == UserProfile.STATUS_AWAITING_APPROVAL:  # noqa
                return redirect(self.success_url)
        return super().dispatch(request)

    def get_object(self):
        if hasattr(self, 'object'):
            return self.object
        self.object = self.request.user.userprofile
        return self.object

    def save_instance(self):
        self.object = super().save_instance()
        self.object.assignment_status = UserProfile.STATUS_AWAITING_APPROVAL
        self.object.save()
        self.notify_team_leader()
        return self.object

    def get_success_url(self):
        return self.success_url

    def notify_team_leader(self):
        notify_team_leader_of_pending_access_request(
            request=self.request,
            team_leader_email=self.object.team_leader.email,
            team_leader_name=self.object.team_leader.first_name,
            user_id=self.request.user.id,
            user_name=self.request.user.get_full_name(),
            user_email=self.request.user.email,
            user_role=self.object.self_assigned_group.info.name_singular,
        )
