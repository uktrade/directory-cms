import pytest

from modeltranslation.utils import build_localized_fieldname

from django.conf import settings
from django.utils import translation


@pytest.mark.django_db
def test_base_model_check_valid_draft_token(page):
    draft_token = page.get_draft_token()

    assert page.is_draft_token_valid(draft_token) is True


@pytest.mark.django_db
def test_base_model_check_invalid_draft_token(page):
    assert page.is_draft_token_valid('asdf') is False


@pytest.mark.django_db
def test_base_model_redirect_published_url(rf, page):
    request = rf.get('/')

    response = page.serve(request)

    assert response.status_code == 302
    assert response.url == page.get_url()


@pytest.mark.parametrize('languaue_code,expected', (
    ('en-gb', 'ENGLISH'),
    ('de', 'GERMAN'),
    ('ja', 'JAPANESE'),
    ('zh-hans', 'SIMPLIFIED CHINESE'),
    ('fr', 'FRENCH'),
    ('es', 'SPANISH'),
    ('pt', 'PORTUGUESE'),
    ('pt-br', 'BRAZILIAN'),
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
def test_translated_languages(page, language_code):
    field_names = page.get_required_translatable_fields()
    for field_name in field_names:
        localized_name = build_localized_fieldname(field_name, language_code)
        setattr(page, localized_name, localized_name + ' value')
    if language_code == 'en-gb':
        expected = ['en-gb']
    else:
        expected = [settings.LANGUAGE_CODE, language_code]
    assert page.translated_languages == expected


@pytest.mark.django_db
def test_translated_localised_urls(translated_page):
    translated_page.slug = 'slug'
    translated_page.pk = 3

    domain = 'http://supplier.trade.great:8005'

    assert translated_page.get_localized_urls() == [
        ('en-gb', domain + '/industries/3/slug/'),
        ('de', domain + '/industries/3/slug_de-v/?lang=de'),
        ('ja', domain + '/industries/3/slug_ja-v/?lang=ja'),
        ('ru', domain + '/industries/3/slug_ru-v/?lang=ru'),
        ('zh-hans', domain + '/industries/3/slug_zh_hans-v/?lang=zh-hans'),
        ('fr', domain + '/industries/3/slug_fr-v/?lang=fr'),
        ('es', domain + '/industries/3/slug_es-v/?lang=es'),
        ('pt', domain + '/industries/3/slug_pt-v/?lang=pt'),
        ('pt-br', domain + '/industries/3/slug_pt_br-v/?lang=pt-br'),
        ('ar', domain + '/industries/3/slug_ar-v/?lang=ar')
    ]


@pytest.mark.django_db
def test_translated_localised_urls_untranslated_page(page):
    page.slug = 'slug'
    page.pk = 3

    assert page.get_localized_urls() == [
        ('en-gb', 'http://supplier.trade.great:8005/industries/3/slug/'),
    ]
