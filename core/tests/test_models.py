import pytest
from unittest import mock

from modeltranslation.utils import build_localized_fieldname

from django.conf import settings
from django.core.exceptions import ValidationError
from django.utils import translation
from wagtail.core.models import Page, Site

from core.models import RoutingSettings
from find_a_supplier.tests.factories import (
    FindASupplierAppFactory, IndustryPageFactory, IndustryLandingPageFactory,
    IndustryArticlePageFactory,
)
from invest.tests.factories import (
    InvestAppFactory, SectorLandingPageFactory, SectorPageFactory,
)
from export_readiness.tests.factories import (
    ExportReadinessAppFactory, TopicLandingPageFactory,
    ArticleListingPageFactory, ArticlePageFactory,
    PrivacyAndCookiesPageFactory, SitePolicyPagesFactory,
)
from great_international.tests.factories import (
    GreatInternationalAppFactory, InternationalTopicLandingPageFactory,
    InternationalArticleListingPageFactory, InternationalArticlePageFactory,
)
from invest.models import InvestApp


@pytest.mark.django_db
def test_slugs_are_unique_in_the_same_service():
    IndustryPageFactory(slug='foo')
    with pytest.raises(ValidationError) as excinfo:
        IndustryPageFactory(slug='foo')
    assert 'This slug is already in use' in str(excinfo.value)


@pytest.mark.django_db
def test_slugs_are_not_unique_across_services(root_page):
    page_one = IndustryPageFactory(slug='foo', parent=root_page)
    page_two = SectorPageFactory(slug='foo', parent=root_page)
    assert page_one.slug == 'foo'
    assert page_two.slug == 'foo'


@pytest.mark.django_db
def test_delete_same_slug_different_services(root_page):
    """
    Deleting a page results in ancestor pages being re-saved.
    Thus ancestor page (root_page) has to have title & title_en_gb.
    """
    root_page.title = 'ancestor page has to have a title'
    root_page.title_en_gb = 'ancestor page has to have a title'
    root_page.save()
    page_one = IndustryPageFactory(slug='foo', parent=root_page)
    page_two = SectorPageFactory(slug='foo', parent=root_page)
    assert page_one.slug == 'foo'
    assert page_two.slug == 'foo'
    page_one.delete()
    assert Page.objects.filter(pk=page_one.pk).exists() is False


@pytest.mark.django_db
def test_page_paths(root_page):
    invest_app = InvestAppFactory(parent=root_page)
    invest_page_one = SectorLandingPageFactory(parent=invest_app)
    invest_page_two = SectorPageFactory(slug='foo', parent=invest_page_one)
    invest_page_three = SectorPageFactory(slug='bar', parent=invest_page_two)

    assert invest_page_two.full_path == '/industries/foo/'
    assert invest_page_three.full_path == '/industries/foo/bar/'

    fas_app = FindASupplierAppFactory(parent=root_page)
    fas_industry_landing_page = IndustryLandingPageFactory(parent=fas_app)
    fas_industry_one = IndustryPageFactory(
        slug='foo', parent=fas_industry_landing_page)
    fas_industry_two = IndustryPageFactory(
        slug='bar', parent=fas_industry_landing_page)
    fas_industry_article = IndustryArticlePageFactory(
        slug='article', parent=fas_industry_two)

    assert fas_industry_one.full_path == '/industries/foo/'
    assert fas_industry_two.full_path == '/industries/bar/'
    assert fas_industry_article.full_path == '/industry-articles/article/'

    domestic_app = ExportReadinessAppFactory(parent=root_page)
    domestic_page_one = TopicLandingPageFactory(
        parent=domestic_app, slug='topic')
    domestic_page_two = ArticleListingPageFactory(
        parent=domestic_page_one, slug='list')
    domestic_page_three = ArticlePageFactory(
        parent=domestic_page_two, slug='article')

    assert domestic_page_two.full_path == '/topic/list/'
    assert domestic_page_three.full_path == '/topic/list/article/'

    domestice_site_policy = SitePolicyPagesFactory(parent=domestic_app)
    domestic_cookies_one = PrivacyAndCookiesPageFactory(
        slug='privacy', parent=domestice_site_policy)
    domestic_cookies_two = PrivacyAndCookiesPageFactory(
        slug='cookies', parent=domestic_cookies_one)

    assert domestic_cookies_one.full_path == '/privacy/'
    assert domestic_cookies_two.full_path == '/privacy/cookies/'

    international_app = GreatInternationalAppFactory(parent=root_page)
    international_page_one = InternationalTopicLandingPageFactory(
        parent=international_app, slug='topic')
    international_page_two = InternationalArticleListingPageFactory(
        parent=international_page_one, slug='list')
    international_page_three = InternationalArticlePageFactory(
        parent=international_page_two, slug='article')

    assert international_page_two.full_path == '/topic/list/'
    assert international_page_three.full_path == '/topic/list/article/'


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
        expected = [language_code, settings.LANGUAGE_CODE]
    assert sorted(page.translated_languages) == sorted(expected)


@pytest.mark.django_db
def test_translated_languages_no_fields(settings):
    assert InvestApp().translated_languages == [settings.LANGUAGE_CODE]


@pytest.mark.django_db
def test_translated_localised_urls(translated_page):
    translated_page.slug = 'slug'
    translated_page.pk = 3

    domain = 'http://supplier.trade.great:8005'

    assert sorted(translated_page.get_localized_urls()) == [
        ('ar', domain + '/slug/?lang=ar'),
        ('de', domain + '/slug/?lang=de'),
        ('en-gb', domain + '/slug/'),
        ('es', domain + '/slug/?lang=es'),
        ('fr', domain + '/slug/?lang=fr'),
        ('ja', domain + '/slug/?lang=ja'),
        ('pt', domain + '/slug/?lang=pt'),
        ('zh-hans', domain + '/slug/?lang=zh-hans')
    ]


@pytest.mark.django_db
def test_translated_localised_urls_untranslated_page(page):
    page.slug = 'slug'
    page.pk = 3

    assert page.get_localized_urls() == [
        ('en-gb', 'http://supplier.trade.great:8005/slug/'),
    ]


@pytest.mark.django_db
def test_language_names_translated(translated_page):
    assert translated_page.language_names == (
        'Translated to German, Japanese, Simplified Chinese, '
        'French, Spanish, Portuguese, Arabic'
    )


@pytest.mark.django_db
def test_language_names_untranslated(page):
    assert page.language_names == ''


@pytest.mark.django_db
def test_base_app_slugs_are_created_in_all_languages(root_page):
    app = InvestAppFactory(title='foo', parent=root_page)
    assert app.slug == InvestApp.slug_identity


@pytest.mark.django_db
def test_get_tree_based_url(root_page):
    domestic_app = ExportReadinessAppFactory(parent=root_page)
    domestic_page_one = TopicLandingPageFactory(
        parent=domestic_app, slug='topic')
    domestic_page_two = ArticleListingPageFactory(
        parent=domestic_page_one, slug='list')
    domestic_page_three = ArticlePageFactory(
        parent=domestic_page_two, slug='article')

    Site.objects.all().delete()
    site = Site.objects.create(
        site_name='Great Domestic',
        hostname='domestic.trade.great',
        port=8007,
        root_page=domestic_app,
    )

    routing_settings = RoutingSettings.objects.create(
        site=site,
        root_path_prefix='/domestic/c',
        include_port_in_urls=False,
    )

    assert domestic_page_two.get_tree_based_url() == '/domestic/c/topic/list/'
    assert (
        domestic_page_three.get_tree_based_url() ==
        '/domestic/c/topic/list/article/'
    )

    # Test include_site_url
    assert (
        domestic_page_two.get_tree_based_url(include_site_url=True) ==
        'http://domestic.trade.great/domestic/c/topic/list/'
    )

    # Test RoutingSettings.include_port_in_urls
    routing_settings.include_port_in_urls = True
    routing_settings.save()

    assert (
        domestic_page_two.get_tree_based_url(include_site_url=True) ==
        'http://domestic.trade.great:8007/domestic/c/topic/list/'
    )


@pytest.mark.django_db
def test_get_tree_based_url_without_routing_settings(root_page):
    # This time, call without RoutingSettings configured for the site
    # and check that an instance is created
    domestic_app = ExportReadinessAppFactory(parent=root_page)
    domestic_page_one = TopicLandingPageFactory(
        parent=domestic_app, slug='topic')
    domestic_page_two = ArticleListingPageFactory(
        parent=domestic_page_one, slug='list')

    Site.objects.all().delete()
    site = Site.objects.create(
        site_name='Great Domestic',
        hostname='domestic.trade.great',
        port=8007,
        root_page=domestic_app,
    )

    domestic_page_two.get_tree_based_url()

    # Check routing settings were created
    routing_settings = RoutingSettings.objects.get()
    assert routing_settings.site == site
    assert routing_settings.root_path_prefix == ''
    assert routing_settings.include_port_in_urls is True


@pytest.mark.django_db
def test_url_methods_use_tree_based_routing(root_page):
    # Checks that the full_path and full_url methods call get_tree_based_url
    # when uses_tree_based_routing is True
    domestic_app = ExportReadinessAppFactory(parent=root_page)
    domestic_page_one = TopicLandingPageFactory(
        parent=domestic_app, slug='topic')
    domestic_page_two = ArticleListingPageFactory(
        parent=domestic_page_one, slug='list')
    domestic_page_three = ArticlePageFactory(
        parent=domestic_page_two, slug='article')

    Site.objects.all().delete()
    site = Site.objects.create(
        site_name='Great Domestic',
        hostname='domestic.trade.great',
        port=8007,
        root_page=domestic_app,
    )

    RoutingSettings.objects.create(
        site=site,
        root_path_prefix='/domestic/c',
        include_port_in_urls=False,
    )

    domestic_page_three.get_tree_based_url = mock.MagicMock(
        side_effect=domestic_page_three.get_tree_based_url
    )

    # First check without tree based routing
    domestic_page_three.uses_tree_based_routing = False
    assert domestic_page_three.full_path == '/topic/list/article/'
    assert (
        domestic_page_three.full_url ==
        'http://exred.trade.great:8007/topic/list/article/'
    )
    domestic_page_three.get_tree_based_url.assert_not_called()

    domestic_page_three.get_tree_based_url.reset_mock()

    # Now check with tree based routing
    domestic_page_three.uses_tree_based_routing = True
    assert domestic_page_three.full_path == '/domestic/c/topic/list/article/'
    assert (
        domestic_page_three.full_url ==
        'http://domestic.trade.great/domestic/c/topic/list/article/'
    )
    domestic_page_three.get_tree_based_url.assert_called()
