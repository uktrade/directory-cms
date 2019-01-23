from django import forms
from django.contrib.auth.models import Group
from django.utils.translation import ugettext_lazy as _

from wagtail.users.forms import UserEditForm, UserCreationForm


class CustomUserEditForm(UserEditForm):
    is_superuser = forms.BooleanField(
        label=_('Superuser'), required=False,
        help_text=_('Superusers have full access to manage any object '
                    'or setting.'))
    groups = forms.ModelChoiceField(
        queryset=Group.objects.all(),
        required=True
    )


class CustomUserCreationForm(UserCreationForm):
    is_superuser = forms.BooleanField(
        label=_('Superuser'), required=False,
        help_text=_('Superusers have full access to manage any object '
                    'or setting.'))
    groups = forms.ModelChoiceField(
        queryset=Group.objects.all(),
        required=True
    )
