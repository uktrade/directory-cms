import pytest
from great_international.serializers import (
    InternationalSectorPageSerializer, InternationalArticlePageSerializer,
    InternationalCampaignPageSerializer, InternationalHomePageSerializer
)
from great_international.tests.factories import (
    InternationalSectorPageFactory, InternationalArticlePageFactory,
    InternationalCampaignPageFactory, InternationalHomePageFactory
)


@pytest.mark.django_db
def test_sector_page_related_pages_serializer_has_pages(root_page, rf):
    related_page_one = InternationalArticlePageFactory(
        parent=root_page,
        slug='one'
    )
    related_page_two = InternationalArticlePageFactory(
        parent=root_page,
        slug='two'
    )
    related_page_three = InternationalArticlePageFactory(
        parent=root_page,
        slug='three'
    )
    case_study_cta_page = InternationalArticlePageFactory(
        parent=root_page,
        slug="case_study"
    )
    article = InternationalSectorPageFactory(
        parent=root_page,
        slug='article-slug',
        related_page_one=related_page_one,
        related_page_two=related_page_two,
        related_page_three=related_page_three,
        case_study_cta_page=case_study_cta_page
    )

    serializer = InternationalSectorPageSerializer(
        instance=article,
        context={'request': rf.get('/')}
    )

    assert len(serializer.data['related_pages']) == 3
    cta_page = serializer.data['case_study_cta_page']
    assert 'title' in cta_page
    assert 'teaser' in cta_page
    assert 'thumbnail' in cta_page


@pytest.mark.django_db
@pytest.mark.parametrize('parent_page_class,serializer_class', [
    (InternationalArticlePageFactory, InternationalArticlePageSerializer)
])
def test_related_article_page_serializer_has_pages(
        parent_page_class, serializer_class, root_page, rf
):
    related_page_one = InternationalArticlePageFactory(
        parent=root_page,
        slug='one'
    )
    related_page_two = InternationalArticlePageFactory(
        parent=root_page,
        slug='two'
    )
    related_page_three = InternationalArticlePageFactory(
        parent=root_page,
        slug='three'
    )
    article = parent_page_class(
        parent=root_page,
        slug='article-slug',
        related_page_one=related_page_one,
        related_page_two=related_page_two,
        related_page_three=related_page_three
    )

    serializer = serializer_class(
        instance=article,
        context={'request': rf.get('/')}
    )

    assert len(serializer.data['related_pages']) == 3


@pytest.mark.django_db
def test_home_page_related_pages(root_page, rf):
    related_page_one = InternationalArticlePageFactory(
        parent=root_page,
        slug='one'
    )
    related_page_two = InternationalCampaignPageFactory(
        parent=root_page,
        slug='two'
    )

    home_page = InternationalHomePageFactory(
        parent=root_page,
        slug='home-page',
        related_page_one=related_page_one,
        related_page_two=related_page_two,
    )

    serializer = InternationalHomePageSerializer(
        instance=home_page,
        context={'request': rf.get('/')}
    )

    assert len(serializer.data['related_pages']) == 2
    for page in serializer.data['related_pages']:
        assert 'title' in page
        assert 'teaser' in page
        assert 'thumbnail' in page


@pytest.mark.django_db
@pytest.mark.parametrize('parent_page_class,serializer_class', (
    (InternationalArticlePageFactory, InternationalArticlePageSerializer),
    (InternationalCampaignPageFactory, InternationalCampaignPageSerializer),
))
def test_related_article_page_serializer_no_pages(
    parent_page_class, serializer_class, root_page, rf
):
    article = parent_page_class(
        parent=root_page,
        slug='article-slug',
        related_page_one=None,
        related_page_two=None,
        related_page_three=None,
    )

    serializer = serializer_class(
        instance=article,
        context={'request': rf.get('/')}
    )

    assert len(serializer.data['related_pages']) == 0
