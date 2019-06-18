from django import forms
from wagtail.admin.widgets import AdminDateInput

from .models import ModerationRequest


class SubmitForm(forms.ModelForm):
    class Meta:
        fields = [
            'publish_at',
            'comment',
        ]
        model = ModerationRequest
        widgets = {
            'publish_at': AdminDateInput,
        }
