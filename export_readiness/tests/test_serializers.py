import pytest
from export_readiness.serializers import (
    ArticlePageSerializer, CountryGuidePageSerializer, CampaignPageSerializer)
from export_readiness.tests.factories import (
    ExportReadinessAppFactory, ArticlePageFactory, CountryGuidePageFactory,
    CampaignPageFactory, TopicLandingPageFactory)


@pytest.mark.django_db
@pytest.mark.parametrize('ParentPage,Serializer', (
    (ArticlePageFactory, ArticlePageSerializer),
    (CountryGuidePageFactory, CountryGuidePageSerializer),
    (CampaignPageFactory, CampaignPageSerializer),
))
def test_related_article_page_serializer_has_pages(
    ParentPage, Serializer, root_page, rf
):
    related_page_one = ArticlePageFactory(
        parent=root_page,
        slug='one'
    )
    related_page_two = ArticlePageFactory(
        parent=root_page,
        slug='two'
    )
    related_page_three = ArticlePageFactory(
        parent=root_page,
        slug='three'
    )
    article = ParentPage(
        parent=root_page,
        slug='article-slug',
        related_page_one=related_page_one,
        related_page_two=related_page_two,
        related_page_three=related_page_three,
    )

    serializer = Serializer(
        instance=article,
        context={'request': rf.get('/')}
    )

    assert len(serializer.data['related_pages']) == 3


@pytest.mark.django_db
@pytest.mark.parametrize('ParentPage,Serializer', (
    (ArticlePageFactory, ArticlePageSerializer),
    (CountryGuidePageFactory, CountryGuidePageSerializer),
    (CampaignPageFactory, CampaignPageSerializer),
))
def test_related_article_page_serializer_no_pages(
    ParentPage, Serializer, root_page, rf
):
    article = ParentPage(
        parent=root_page,
        slug='article-slug',
        related_page_one=None,
        related_page_two=None,
        related_page_three=None,
    )

    serializer = Serializer(
        instance=article,
        context={'request': rf.get('/')}
    )

    assert len(serializer.data['related_pages']) == 0


@pytest.mark.django_db
def test_country_guide_page_serializer(root_page, rf):
    markets_page = TopicLandingPageFactory(parent=root_page)
    country_guide = CountryGuidePageFactory(
        parent=markets_page,
        intro_cta_one_title='',
        intro_cta_one_link='',
        intro_cta_two_title='',
        intro_cta_two_link='',
        intro_cta_three_title='',
        intro_cta_three_link='',
    )

    serializer = CountryGuidePageSerializer(
        instance=country_guide,
        context={'request': rf.get('/')}
    )

    assert len(serializer.data['intro_ctas']) == 0


@pytest.mark.django_db
def test_breadcrumbs_serializer(root_page, rf):
    app_page = ExportReadinessAppFactory(parent=root_page)
    markets_page = TopicLandingPageFactory(
        title_en_gb='topic',
        slug='topic',
        parent=app_page)
    country_guide = CountryGuidePageFactory(
        title_en_gb='country',
        slug='country',
        parent=markets_page)

    serializer = CountryGuidePageSerializer(
        instance=country_guide,
        context={'request': rf.get('/')}
    )

    breadcrumbs = serializer.data['tree_based_breadcrumbs']

    assert len(breadcrumbs) == 2
    assert breadcrumbs[0]['title'] == 'topic'
    assert breadcrumbs[1]['title'] == 'country'
    assert breadcrumbs[0]['url'] == 'http://exred.trade.great:8007/topic/'
    assert breadcrumbs[1]['url'] == (
        'http://exred.trade.great:8007/topic/country/')
