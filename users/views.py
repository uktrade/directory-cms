from django.contrib.auth import get_user_model, update_session_auth_hash
from django.shortcuts import redirect
from django.urls import reverse
from django.utils.translation import ugettext as _
from django.views import generic

from wagtail.admin import messages
from wagtail.core import hooks
from wagtail.users.utils import user_can_delete_user
from wagtail.users.views.users import add_user_perm, change_user_perm

from . import forms, mixins

User = get_user_model()


class WagtailUserActionBaseView(mixins.WagtailAdminPermissionRequiredMixin):
    hook_action = ''
    form_invalid_message = ''

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
            _("User '{0}' created.").format(user),
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
        self.handle_success_message()
        return redirect('wagtailusers_users:index')

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        can_delete = user_can_delete_user(self.request.user, self.object)
        ctx.update(can_delete=can_delete)
        return ctx
