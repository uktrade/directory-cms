from django import forms
from django.contrib.auth.models import Group
from django.utils.translation import ugettext_lazy as _

from wagtail.users import forms as wagtail_forms


class EntryPointAwareUserActionForm(forms.Form):
    """
    Does two things:

    1) Changes the label of is_superuser from administrator to superuser
    2) Makes group selection entry point aware/filtered

    """
    is_superuser = forms.BooleanField(
        label=_('Superuser'),
        required=False,
        help_text=_('Superusers have full access to manage any object '
                    'or setting.'))

    def __init__(self, user, *args, **kwargs):
        """Creating user (session user) should only see the groups
        that have the same tree entry point of their own group(s).
        """
        super().__init__(*args, **kwargs)
        self.fields['groups'].queryset = self.get_groups_queryset(user)

    def get_groups_queryset(self, user):
        """Return the groups with the same entrypoint(s) of the the user in
        the request (not the one being created)."""
        if user.is_superuser:
            # superusers can see everything
            return Group.objects.all()
        if user.groups.count() == 0:
            # normal users with no tree entry point shouldn't exist but...
            return Group.objects.none()
        else:
            entry_points_ids = user.groups.all().values_list(
                'page_permissions__page_id', flat=True
            ).distinct()
            return Group.objects.filter(
                page_permissions__page_id=entry_points_ids
            ).distinct('id')


class DisableUserFieldsMixin(forms.Form):
    """
    Disables all user fields except for roles
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        instance = getattr(self, 'instance', None)
        if instance and instance.pk:
            # Disable the fields
            self.fields['username'].widget.attrs['readonly'] = True
            self.fields['email'].widget.attrs['readonly'] = True
            self.fields['first_name'].widget.attrs['readonly'] = True
            self.fields['last_name'].widget.attrs['readonly'] = True

            # Note: When editing self, the 'is_active' field doesn't exist
            if 'is_active' in self.fields:
                # Note: checkboxes don't support "readonly" so disable instead
                self.fields['is_active'].widget.attrs['disabled'] = True

            # Make sure the values haven't been changed
            data = self.data.copy()
            data['username'] = instance.username
            data['email'] = instance.email
            data['first_name'] = instance.first_name
            data['last_name'] = instance.last_name

            if instance.is_active:
                data['is_active'] = 'on'
            elif 'is_active' in data:
                del data['is_active']

            self.data = data


class UserEditForm(EntryPointAwareUserActionForm, DisableUserFieldsMixin,
                   wagtail_forms.UserEditForm):
    pass


class UserCreationForm(EntryPointAwareUserActionForm, DisableUserFieldsMixin,
                       wagtail_forms.UserCreationForm):
    pass
