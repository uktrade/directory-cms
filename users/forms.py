from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.utils.functional import cached_property
from django.utils.translation import ugettext_lazy as _

from wagtail.users import forms as wagtail_forms

from core.widgets import Select2Widget
from groups.models import GroupInfo
from groups.widgets import RadioSelectWithGroupInfoModal

from users.models import UserProfile


class EntryPointAwareUserActionForm(forms.Form):
    """
    Does two things:

    1) Changes the label of is_superuser from administrator to superuser
    2) Makes group selection entry point aware/filtered

    """

    is_superuser = forms.BooleanField(
        label=_("Superuser"),
        required=False,
        help_text=_(
            "Superusers have full access to manage any object " "or setting."),
    )

    def __init__(self, user, *args, **kwargs):
        """Creating user (session user) should only see the groups
        that have the same tree entry point of their own group(s).
        """
        super().__init__(*args, **kwargs)
        self.fields["groups"].queryset = self.get_groups_queryset(user)

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
            entry_points_ids = (
                user.groups.all()
                .values_list("page_permissions__page_id", flat=True)
                .distinct()
            )
            return Group.objects.filter(
                page_permissions__page_id=entry_points_ids
            ).distinct("id")


class UserEditForm(EntryPointAwareUserActionForm, wagtail_forms.UserEditForm):
    pass


class UserCreationForm(EntryPointAwareUserActionForm, wagtail_forms.UserCreationForm):
    pass


class UserChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return "{name} <{email}>".format(name=obj.get_full_name(), email=obj.email)


class SSORequestAccessForm(forms.ModelForm):

    self_assigned_group = forms.ModelChoiceField(
        label="Which best describes your content role?",
        queryset=GroupInfo.objects.none(),
        empty_label=None,
        widget=RadioSelectWithGroupInfoModal,
    )

    team_leader = UserChoiceField(
        label="Who is your content team leader?",
        queryset=get_user_model().objects.none(),
        widget=Select2Widget,
    )

    class Meta:
        model = UserProfile
        fields = ["self_assigned_group", "team_leader"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        group_queryset = GroupInfo.objects.visibile_to_anyone()
        self.fields["self_assigned_group"].queryset = group_queryset
        self.fields["team_leader"].queryset = self.team_leader_queryset

    @property
    def team_leader_queryset(self):
        group = GroupInfo.objects.team_leaders_group.group
        return group.user_set.all()
