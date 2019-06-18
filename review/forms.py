from django import forms
from wagtail.admin.widgets import AdminDateInput

from .models import Moderation


class SubmitForm(forms.ModelForm):
    class Meta:
        fields = [
            'publish_at',
            'comment',
        ]
        model = Moderation
        widgets = {
            'publish_at': AdminDateInput,
        }
