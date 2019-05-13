from django import forms
from django.conf import settings
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


class UserEditForm(
    EntryPointAwareUserActionForm,
    wagtail_forms.UserEditForm
):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        """
        Prevents personal details from being update when
        when SSO is enforced.
        """
        if settings.FEATURE_FLAGS['ENFORCE_STAFF_SSO_ON']:
            # Disable the fields
            self.fields['username'].disabled = True
            self.fields['email'].disabled = True
            self.fields['first_name'].disabled = True
            self.fields['last_name'].disabled = True


class UserCreationForm(
    EntryPointAwareUserActionForm,
    wagtail_forms.UserCreationForm
):
    pass
