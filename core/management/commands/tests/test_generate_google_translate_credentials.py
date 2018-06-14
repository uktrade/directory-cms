from unittest.mock import call, patch, mock_open

from django.core.management import call_command


def test_generate_google_translate_credentials(settings):
    settings.GOOGLE_TRANSLATE_PRIVATE_KEY_ID = '1'
    settings.GOOGLE_TRANSLATE_PRIVATE_KEY = '2'
    settings.GOOGLE_TRANSLATE_CLIENT_EMAIL = '3'
    settings.GOOGLE_TRANSLATE_CLIENT_ID = '4'
    settings.GOOGLE_TRANSLATE_CERT_URL = '5'
    settings.GOOGLE_APPLICATION_CREDENTIALS = 'config/6.json'

    mock = mock_open()
    path = (
        'core.management.commands.generate_google_translate_credentials.open'
    )
    with patch(path, mock, create=False):
        call_command('generate_google_translate_credentials')

    assert mock.call_count == 1
    assert mock.mock_calls == [
        call('config/6.json', 'w'),
        call().__enter__(),
        call().write(
            '{'
            '"type": "service_account", "project_id": "directory-cms", '
            '"private_key_id": "1", "private_key": "2", "client_email": "3", '
            '"client_id": "4", '
            '"auth_uri": "https://accounts.google.com/o/oauth2/auth", '
            '"token_uri": "https://accounts.google.com/o/oauth2/token", '
            '"auth_provider_x509_cert_url": '
            '"https://www.googleapis.com/oauth2/v1/certs", '
            '"client_x509_cert_url": "5"'
            '}'
        ),
        call().__exit__(None, None, None)
    ]
