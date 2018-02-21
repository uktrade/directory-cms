from django.core.management import BaseCommand
from django.conf import settings
from django.template.loader import render_to_string


class Command(BaseCommand):

    help = 'Generate the credentials for google translate'

    def handle(self, *args, **options):
        template_name = 'core/google-cloud-credentials.html'
        context = {
            'private_key_id': settings.GOOGLE_TRANSLATE_PRIVATE_KEY_ID,
            'private_key': settings.GOOGLE_TRANSLATE_PRIVATE_KEY,
            'client_email': settings.GOOGLE_TRANSLATE_CLIENT_EMAIL,
            'client_id': settings.GOOGLE_TRANSLATE_CLIENT_ID,
            'client_x509_cert_url': settings.GOOGLE_TRANSLATE_CERT_URL,
        }
        with open(settings.GOOGLE_APPLICATION_CREDENTIALS, 'w') as f:
            f.write(render_to_string(template_name, context))
