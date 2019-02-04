import pytest
from great_domestic.serializers import (
    ArticlePageSerializer, CountryGuidePageSerializer, CampaignPageSerializer)
from great_domestic.tests.factories import (
    ArticlePageFactory, CountryGuidePageFactory, CampaignPageFactory)


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
