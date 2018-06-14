from collections import OrderedDict
import json

from django.core.management import BaseCommand
from django.conf import settings


class Command(BaseCommand):

    help = 'Generate the credentials for google translate'

    def handle(self, *args, **options):
        context = OrderedDict([
            ('type', 'service_account'),
            ('project_id', 'directory-cms'),
            ('private_key_id', settings.GOOGLE_TRANSLATE_PRIVATE_KEY_ID),
            ('private_key', settings.GOOGLE_TRANSLATE_PRIVATE_KEY),
            ('client_email', settings.GOOGLE_TRANSLATE_CLIENT_EMAIL),
            ('client_id', settings.GOOGLE_TRANSLATE_CLIENT_ID),
            ('auth_uri', 'https://accounts.google.com/o/oauth2/auth'),
            ('token_uri', 'https://accounts.google.com/o/oauth2/token'),
            (
                'auth_provider_x509_cert_url',
                'https://www.googleapis.com/oauth2/v1/certs'
            ),
            ('client_x509_cert_url', settings.GOOGLE_TRANSLATE_CERT_URL),
        ])
        with open(settings.GOOGLE_APPLICATION_CREDENTIALS, 'w') as f:
            f.write(json.dumps(context))
