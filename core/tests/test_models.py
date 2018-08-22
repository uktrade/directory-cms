import pytest

from modeltranslation.utils import build_localized_fieldname

from django.conf import settings
from django.core.exceptions import ValidationError
from django.utils import translation

from find_a_supplier.tests.factories import IndustryPageFactory
from invest.tests.factories import InvestAppFactory, SectorPageFactory


@pytest.mark.django_db
def test_slugs_are_unique_in_the_same_service():
    IndustryPageFactory(slug_en_gb='foo')
    with pytest.raises(ValidationError) as excinfo:
        IndustryPageFactory(slug_en_gb='foo')
    assert 'This slug is already in use' in str(excinfo.value)


@pytest.mark.django_db
def test_slugs_are_not_unique_across_services(root_page):
    page_one = IndustryPageFactory(slug_en_gb='foo', parent=root_page)
    page_two = SectorPageFactory(slug_en_gb='foo', parent=root_page)
    assert page_one.slug == 'foo'
    assert page_two.slug == 'foo'


@pytest.mark.django_db
def test_base_model_check_valid_draft_token(page):
    draft_token = page.get_draft_token()

    assert page.is_draft_token_valid(draft_token) is True


@pytest.mark.django_db
def test_base_model_check_invalid_draft_token(page):
    assert page.is_draft_token_valid('asdf') is False


@pytest.mark.django_db
def test_base_model_sets_service_name_on_save(page):
    assert page.service_name == page.service_name_value


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
        ('en-gb', domain + '/industries/slug/'),
        ('de', domain + '/industries/slug/?lang=de'),
        ('ja', domain + '/industries/slug/?lang=ja'),
        ('ru', domain + '/industries/slug/?lang=ru'),
        ('zh-hans', domain + '/industries/slug/?lang=zh-hans'),
        ('fr', domain + '/industries/slug/?lang=fr'),
        ('es', domain + '/industries/slug/?lang=es'),
        ('pt', domain + '/industries/slug/?lang=pt'),
        ('pt-br', domain + '/industries/slug/?lang=pt-br'),
        ('ar', domain + '/industries/slug/?lang=ar')
    ]


@pytest.mark.django_db
def test_translated_localised_urls_untranslated_page(page):
    page.slug = 'slug'
    page.pk = 3

    assert page.get_localized_urls() == [
        ('en-gb', 'http://supplier.trade.great:8005/industries/slug/'),
    ]


@pytest.mark.django_db
def test_get_admin_display_title_translated(translated_page):
    assert translated_page.get_admin_display_title() == (
        'ENGLISH\n\n<br>\n<i>Translated to German, Japanese, Russian, '
        'Simplified Chinese, French, Spanish, Portuguese, '
        'Portuguese (Brazilian), Arabic</i>\n\n'
    )


@pytest.mark.django_db
def test_get_admin_display_title_untranslated(page):
    page.draft_title = 'Untranslated page'
    assert page.get_admin_display_title() == 'Untranslated page\n\n'


@pytest.mark.django_db
def test_historically_unique_slug():
    page_one = IndustryPageFactory.create(
        slug_en_gb='slug-one',
        title_en_gb='1',
        depth=2,
        path='/thing0',
    )
    page_one.save()
    page_one.slug_en_gb = 'slug-two'
    page_one.save()

    expected = 'This slug is already in use'
    with pytest.raises(ValidationError, match=expected):
        IndustryPageFactory.create(
            slug_en_gb='slug-one',
            title_en_gb='2',
            depth=2,
            path='/thing1',
        )

    with pytest.raises(ValidationError, match=expected):
        IndustryPageFactory.create(
            slug_en_gb='slug-two',
            title_en_gb='3',
            depth=2,
            path='/thing2',
        )
        assert error.value.message_dict == expected


@pytest.mark.xfail
@pytest.mark.django_db
def test_base_app_slugs_are_created_in_all_languages(root_page):
    app = InvestAppFactory(title='foo', parent=root_page)
    assert app.slug_de == 'foo'
    assert app.slug_en_gb == 'foo'
    