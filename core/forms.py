from django import forms
from django.conf import settings


class CopyToEnvironmentForm(forms.Form):

    environment = forms.ChoiceField(
        label='Website',
        help_text='The website you would like to copy the page to',
        choices=[(url, url) for url in settings.COPY_DESTINATION_URLS]
    )
