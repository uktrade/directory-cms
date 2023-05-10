import requests
from wagtail.models import Locale
from django.core.files.base import ContentFile
from django.core.files import File
from wagtail.models import Collection
from wagtailmedia import models as wagtailmedia_models


def clean_post_data(post_data):
    """
    Removes None values from data, so that it can posted to Django's test
    client without TypeError being raised in Django 2.2+
    """
    return {
        key: value for key, value in post_data.items()
        if value is not None
    }


def create_response(status_code, json_body={}, content=None):
    response = requests.Response()
    response.status_code = status_code
    response.json = lambda: json_body
    response._content = content
    return response


class SetUpLocaleMixin:
    """Ensures a default locale is in the database
    pytest equivalent is the `en_locale` fixture
    """

    def _fixture_setup(self):
        Locale.objects.get_or_create(language_code='en-gb')
        return super()._fixture_setup()


def make_test_video(
    title='Test file',
    content=b'An example movie file',
    filename='movie.mp4',
    duration=120,
    transcript=None,
    subtitles=None,
    collection_name='Root',
):
    fake_file = ContentFile(content)
    fake_file.name = filename
    root_collection, _ = Collection.objects.get_or_create(name=collection_name, depth=0)
    media_model = wagtailmedia_models.get_media_model()
    media = media_model(collection=root_collection)
    media.title = title
    media.file = File(fake_file)
    media.duration = duration
    media.transcript = transcript
    media.subtitles_en = subtitles
    return media
