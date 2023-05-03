import pytest

from modeltranslation.utils import build_localized_fieldname
from django.urls import reverse
from django.conf import settings
from django.contrib.contenttypes.models import ContentType
from django.utils import translation
from django.test import TestCase

from wagtail.models import Page, Site
from tests.core.helpers import make_test_video


from core.models import BasePage, RoutingSettings
from tests.great_international.factories import InternationalArticlePageFactory


@pytest.mark.django_db
def test_base_model_check_valid_draft_token(international_root_page):
    draft_token = international_root_page.get_draft_token()

    assert international_root_page.is_draft_token_valid(draft_token) is True


@pytest.mark.django_db
def test_base_model_check_invalid_draft_token(international_root_page):
    assert international_root_page.is_draft_token_valid('asdf') is False


@pytest.mark.django_db
def test_base_model_sets_service_name_on_save(international_root_page):
    assert international_root_page.service_name == international_root_page.service_name_value


@pytest.mark.django_db
def test_base_model_redirect_published_url(rf, international_root_page):
    request = rf.get('/')

    response = international_root_page.serve(request)

    assert response.status_code == 302
    assert response.url == international_root_page.get_url()


@pytest.mark.parametrize('languaue_code,expected', (
    ('en-gb', 'ENGLISH'),
    ('de', 'GERMAN'),
    ('ja', 'JAPANESE'),
    ('zh-hans', 'SIMPLIFIED CHINESE'),
    ('fr', 'FRENCH'),
    ('es', 'SPANISH'),
    ('pt', 'PORTUGUESE'),
    ('ar', 'ARABIC'),
))
@pytest.mark.django_db
def test_translations_broker_fields(translated_page, languaue_code, expected):
    with translation.override(languaue_code):
        assert translated_page.title == expected


@pytest.mark.django_db
@pytest.mark.parametrize(
    'language_code', [code for code, _ in settings.LANGUAGES]
)
def test_translated_languages(international_root_page, language_code):
    field_names = international_root_page.get_required_translatable_fields()
    for field_name in field_names:
        localized_name = build_localized_fieldname(field_name, language_code)
        setattr(international_root_page, localized_name, localized_name + ' value')
    if language_code == 'en-gb':
        expected = ['en-gb']
    else:
        expected = [language_code, settings.LANGUAGE_CODE]
    assert sorted(international_root_page.translated_languages) == sorted(expected)


@pytest.mark.django_db
def test_translated_localised_urls(translated_page):

    domain = f'http://great.gov.uk/international/content/{translated_page.slug}'

    assert sorted(translated_page.get_localized_urls()) == [
        ('ar', domain + '/?lang=ar'),
        ('de', domain + '/?lang=de'),
        ('en-gb', domain + '/'),
        ('es', domain + '/?lang=es'),
        ('fr', domain + '/?lang=fr'),
        ('ja', domain + '/?lang=ja'),
        ('pt', domain + '/?lang=pt'),
        ('zh-hans', domain + '/?lang=zh-hans')
    ]


@pytest.mark.django_db
def test_language_names_translated(translated_page):
    assert translated_page.language_names == (
        'Translated to German, Japanese, Simplified Chinese, '
        'French, Spanish, Portuguese, Arabic'
    )


@pytest.mark.django_db
def test_language_names_untranslated(international_root_page):
    assert international_root_page.language_names == ''


@pytest.mark.django_db
def test_get_site_returns_none_when_page_not_routable(root_page):
    Site.objects.all().delete()  # ensures pages are not routable
    page = InternationalArticlePageFactory(parent=root_page, slug='industry')
    result = page.get_site()
    assert result is None


@pytest.mark.django_db
def test_get_site_fetches_routing_settings_if_they_exist(root_page, django_assert_num_queries):
    page = InternationalArticlePageFactory(parent=root_page, slug='industry')
    site = Site.objects.create(hostname='example.org', root_page=page)
    RoutingSettings.objects.create(site=site)

    # running this first so that the query doesn't count toward
    # the total query count (the value is usually cached)
    page._get_site_root_paths()

    with django_assert_num_queries(1):
        # site and routing settings should be fetched in one query
        result_site = page.get_site()

        # Check the correct site was returned
        assert result_site == site

        # This attribute is set to reference the newly created object,
        # so this shouldn't result in another query
        result_site.routingsettings


@pytest.mark.django_db
def test_get_site_creates_routing_settings_if_none_exist(root_page, django_assert_num_queries):
    page = InternationalArticlePageFactory(parent=root_page, slug='industry')
    site = Site.objects.create(hostname='example.gov', root_page=page)

    # running this first so that the query doesn't count toward
    # the total query count (the value is usually cached)
    page._get_site_root_paths()

    with django_assert_num_queries(2):
        # 1 query to get the site, 1 to create routing settings
        result_site = page.get_site()

        # Check the correct site was returned
        assert result_site == site

        # This attribute is set to reference the newly created object,
        # so this shouldn't result in another query
        result_site.routingsettings


@pytest.mark.django_db
def test_basepage_can_exist_under(root_page):
    page = InternationalArticlePageFactory(parent=root_page)
    assert isinstance(page, BasePage)
    dummy_ctype = ContentType.objects.create(app_label='blah', model='blah')
    test_parent = Page(slug='basic', title='Page')
    test_parent.content_type = dummy_ctype
    assert page.can_exist_under(test_parent) is False


class TestGreatMedia(TestCase):
    def test_sources_mp4_with_no_transcript(self):
        media = make_test_video()
        self.assertEqual(
            media.sources,
            [
                {
                    'src': '/media/movie.mp4',
                    'type': 'video/mp4',
                    'transcript': None,
                }
            ],
        )

    def test_sources_mp4_with_transcript(self):
        media = make_test_video(transcript='A test transcript text')

        self.assertEqual(
            media.sources,
            [
                {
                    'src': '/media/movie.mp4',
                    'type': 'video/mp4',
                    'transcript': 'A test transcript text',
                }
            ],
        )

    def test_subtitles__present(self):
        media = make_test_video()
        media.subtitles_en = 'Dummy subtitles content'
        media.save()
        self.assertTrue(media.subtitles_en)
        expected = [
            {
                'srclang': 'en',
                'label': 'English',
                'url': reverse('subtitles-serve', args=[media.id, 'en']),
                'default': False,
            },
        ]
        self.assertEqual(media.subtitles, expected)

    def test_subtitles__not_present(self):
        media = make_test_video()
        self.assertFalse(media.subtitles_en)
        self.assertEqual(media.subtitles, [])
