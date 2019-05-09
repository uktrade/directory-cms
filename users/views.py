from django.conf import settings
from django.contrib.auth import get_user_model, update_session_auth_hash
from django.shortcuts import redirect
from django.urls import reverse, reverse_lazy
from django.utils import timezone
from django.utils.translation import ugettext as _
from django.views import generic
from wagtail.admin import messages
from wagtail.admin.views.generic import EditView
from wagtail.core import hooks
from wagtail.users.utils import user_can_delete_user
from wagtail.users.views.users import add_user_perm, change_user_perm

from users.models import UserProfile
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
        messages.error(
            self.request,
            _(self.form_invalid_message)
        )
        return super().form_invalid(form)

    def handle_success_message(self):
        user = self.object
        messages.success(
            self.request,
            _(self.form_valid_message).format(user),
            buttons=[messages.button(
                reverse('wagtailusers_users:edit', args=(user.pk,)),
                _('Edit')
            )])
        hook_name = 'after_{action}_user'.format(action=self.hook_action)
        for fn in hooks.get_hooks(hook_name):
            result = fn(self.request, user)
            if hasattr(result, 'status_code'):
                return result


class CreateUserView(
    WagtailUserActionBaseView,
    generic.CreateView
):
    form_class = forms.UserCreationForm
    model = User
    template_name = 'wagtailusers/users/create.html'
    permission_required = add_user_perm
    hook_action = 'create'
    form_invalid_message = 'The user could not be created due to errors.'
    form_valid_message = 'User ''{0}'' created.'

    def form_valid(self, form):
        self.object = form.save()
        self.handle_success_message()
        return redirect('wagtailusers_users:index')


class EditUserView(
    WagtailUserActionBaseView,
    generic.UpdateView
):
    form_class = forms.UserEditForm
    model = User
    template_name = 'wagtailusers/users/edit.html'
    permission_required = change_user_perm
    hook_action = 'edit'
    form_invalid_message = 'The user could not be saved due to errors.'
    form_valid_message = 'User ''{0}'' updated.'

    def get_form_kwargs(self):
        user = self.object
        profile = user.userprofile
        editing_self = self.request.user == user
        is_approval = profile.assignment_status in (
            UserProfile.STATUS_CREATED,
            UserProfile.STATUS_AWAITING_APPROVAL,
        )
        self.is_approval = is_approval  # to use in form_valid()
        kwargs = super().get_form_kwargs()
        kwargs.update(editing_self=editing_self)
        if is_approval:
            # Let the user know that this is an 'approval' and preselect
            # a group if the user selected on at registration
            message_text = (
                "This user is awaiting approval and will be automatically "
                "notified via email if added to a group that grants access "
                "to the Wagtail CMS."
            )
            if profile.self_assigned_group:
                kwargs['initial']['groups'] = [profile.self_assigned_group.id]
                message_text += (
                    " They requested to be added to the '{}' group, so this "
                    "has been preselected for you under the 'Roles' tab."
                ).format(profile.self_assigned_group.name)

            messages.warning(self.request, message_text)

        return kwargs

    def form_valid(self, form):
        self.object = user = form.save()

        if user == self.request.user and 'password1' in form.changed_data:
            # User is changing their own password;
            # need to update their session hash
            update_session_auth_hash(self.request, user)

        if self.is_approval and user.has_perm('wagtailadmin.access_admin'):
            profile = user.userprofile
            profile.assignment_status = UserProfile.STATUS_APPROVED
            profile.approved_by = self.request.user
            profile.approved_at = timezone.now()
            profile.save()
            self.notify_user_of_approval()

        self.handle_success_message()
        return redirect('wagtailusers_users:index')

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        can_delete = user_can_delete_user(self.request.user, self.object)
        ctx.update(can_delete=can_delete)
        return ctx

    def notify_user_of_approval(self):
        # TODO: connect to gov.notify
        pass


class SSORequestAccessView(EditView):
    model = UserProfile
    form_class = forms.SSORequestAccessForm
    permission_required = None
    error_message = 'There was a problem with your submission'
    template_name = "sso/request_access.html"
    success_url = reverse_lazy('wagtailusers_users:sso_request_access_success')

    def dispatch(self, request):
        self.get_object()
        if settings.USERS_REQUEST_ACCESS_PREVENT_RESUBMISSION:
            # Toggling behaviour here to aid local testing
            if self.object.assignment_status == UserProfile.STATUS_APPROVED:
                return redirect('wagtailadmin_home')
            if self.object.assignment_status == UserProfile.STATUS_AWAITING_APPROVAL: # noqa
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
        self.notify_team_leader_of_pending_approval()
        return self.object

    def get_success_url(self):
        return self.success_url

    def notify_team_leader_of_pending_approval(self):
        # TODO: connect to gov.notify
        pass
