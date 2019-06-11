import pytest
from export_readiness.serializers import (
    ArticlePageSerializer, CountryGuidePageSerializer, CampaignPageSerializer,
    HomePageSerializer
)
from export_readiness.tests.factories import (
    ArticlePageFactory, CountryGuidePageFactory, CampaignPageFactory,
    HomePagFactory, HomePageOldFactory, TopicLandingPageFactory
)


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
def test_consistent_page_type_for_old_and_new_home_pages(root_page, rf):
    context = {'request': rf.get('/')}
    expected_page_type = 'HomePage'

    page1 = HomePageFactory(parent=root_page, slug='page1',)
    page1_serializer = HomePageSerializer(instance=page1, context=context)
    assert page1_serializer.data['page_type'] == expected_page_type

    page2 = HomePageOldFactory(parent=root_page, slug='page2')
    page2_serializer = HomePageSerializer(instance=page2, context=context)
    assert page2_serializer.data['page_type'] == expected_page_type
