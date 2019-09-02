import pytest
from unittest import mock

from modeltranslation.utils import build_localized_fieldname

from django.conf import settings
from django.contrib.contenttypes.models import ContentType
from django.utils import translation
from wagtail.core.models import Page, Site

from core.models import BasePage, ExclusivePageMixin, RoutingSettings
from tests.great_international.factories import InternationalSectorPageFactory
from tests.export_readiness.factories import HomePageFactory


from tests.export_readiness.factories import (
    HomePageFactory, TopicLandingPageFactory,
    ArticleListingPageFactory, ArticlePageFactory,
    PrivacyAndCookiesPageFactory, SitePolicyPagesFactory,
)
from tests.great_international.factories import (
    InternationalTopicLandingPageFactory,
    InternationalArticleListingPageFactory,
    InternationalArticlePageFactory,
)


@pytest.mark.django_db
def test_page_paths(root_page, international_root_page):
    domestic_homepage = HomePageFactory(parent=root_page)
    domestic_page_one = TopicLandingPageFactory(
        parent=domestic_homepage, slug='topic')
    domestic_page_two = ArticleListingPageFactory(
        parent=domestic_page_one, slug='list')
    domestic_page_three = ArticlePageFactory(
        parent=domestic_page_two, slug='article')

    assert domestic_page_two.full_path == '/topic/list/'
    assert domestic_page_three.full_path == '/topic/list/article/'

    domestice_site_policy = SitePolicyPagesFactory(parent=domestic_homepage)
    domestic_cookies_one = PrivacyAndCookiesPageFactory(
        slug='privacy', parent=domestice_site_policy)
    domestic_cookies_two = PrivacyAndCookiesPageFactory(
        slug='cookies', parent=domestic_cookies_one)

    assert domestic_cookies_one.full_path == '/privacy/'
    assert domestic_cookies_two.full_path == '/privacy/cookies/'

    international_page_one = InternationalTopicLandingPageFactory(
        parent=international_root_page, slug='topic')
    international_page_two = InternationalArticleListingPageFactory(
        parent=international_page_one, slug='list')
    international_page_three = InternationalArticlePageFactory(
        parent=international_page_two, slug='article')

    assert international_page_two.full_path == 'topic/list/'
    assert international_page_three.full_path == 'topic/list/article/'


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

    domain = f'http://localhost/{translated_page.slug}'

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
def test_translated_localised_urls_untranslated_page():
    page = HomePageFactory()

    assert page.get_localized_urls() == [
        ('en-gb', 'http://exred.trade.great:8007'),
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
def test_get_tree_based_url(root_page):
    domestic_homepage = HomePageFactory(parent=root_page)
    domestic_page_one = TopicLandingPageFactory(
        parent=domestic_homepage, slug='topic')
    domestic_page_two = ArticleListingPageFactory(
        parent=domestic_page_one, slug='list')
    domestic_page_three = ArticlePageFactory(
        parent=domestic_page_two, slug='article')

    Site.objects.all().delete()
    site = Site.objects.create(
        site_name='Great Domestic',
        hostname='domestic.trade.great',
        port=8007,
        root_page=domestic_homepage,
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
def test_get_site_returns_none_when_page_not_routable(root_page):
    Site.objects.all().delete()  # ensures pages are not routable
    page = InternationalSectorPageFactory(parent=root_page, slug='industry')
    result = page.get_site()
    assert result is None


@pytest.mark.django_db
def test_get_site_fetches_routing_settings_if_they_exist(root_page, django_assert_num_queries):
    page = InternationalSectorPageFactory(parent=root_page, slug='industry')
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
    page = InternationalSectorPageFactory(parent=root_page, slug='industry')
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
def test_url_methods_use_tree_based_routing(root_page):
    # Checks that the full_path and full_url methods call get_tree_based_url
    # when uses_tree_based_routing is True
    domestic_homepage = HomePageFactory(parent=root_page)
    domestic_page_one = TopicLandingPageFactory(
        parent=domestic_homepage, slug='topic')
    domestic_page_two = ArticleListingPageFactory(
        parent=domestic_page_one, slug='list')
    domestic_page_three = ArticlePageFactory(
        parent=domestic_page_two, slug='article')

    Site.objects.all().delete()
    site = Site.objects.create(
        site_name='Great Domestic',
        hostname='domestic.trade.great',
        port=8007,
        root_page=domestic_homepage,
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


@pytest.mark.django_db
def test_basepage_can_exist_under(root_page):
    page = InternationalSectorPageFactory(parent=root_page)
    assert isinstance(page, BasePage)
    dummy_ctype = ContentType.objects.create(app_label='blah', model='blah')
    test_parent = Page(slug='basic', title='Page')
    test_parent.content_type = dummy_ctype
    assert page.can_exist_under(test_parent) is False


@pytest.mark.django_db
def test_exclusivepagemixin_can_create_at(root_page):
    page = SitePolicyPagesFactory(parent=root_page)
    assert isinstance(page, ExclusivePageMixin)
    assert page.can_create_at(root_page) is False
