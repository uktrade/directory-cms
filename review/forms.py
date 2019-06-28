from django import forms
from wagtail.admin.widgets import AdminDateInput

from .models import ModerationRequest


class SubmitForm(forms.ModelForm):
    class Meta:
        fields = [
            'due_date',
            'comment',
        ]
        model = ModerationRequest
        widgets = {
            'due_date': AdminDateInput,
        }
