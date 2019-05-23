import pytest

from great_international.serializers import (
    InternationalSectorPageSerializer, InternationalArticlePageSerializer,
    InternationalCampaignPageSerializer, InternationalHomePageSerializer,
    InternationalCuratedTopicLandingPageSerializer,
    InternationalGuideLandingPageSerializer,
    CapitalInvestRegionPageSerializer,
    InternationalCapitalInvestLandingPageSerializer,
    CapitalInvestRegionalSectorPageSerializer)
from great_international.tests.factories import (
    InternationalSectorPageFactory, InternationalArticlePageFactory,
    InternationalCampaignPageFactory, InternationalHomePageFactory,
    InternationalCuratedTopicLandingPageFactory,
    InternationalGuideLandingPageFactory,
    CapitalInvestRegionPageFactory,
    InternationalCapitalInvestLandingPageFactory,
    CapitalInvestRegionalSectorPageFactory,
    CapitalInvestOpportunityPageFactory,
    CapitalInvestOpportunityListingPageFactory)

from great_international.models import CapitalInvestSectorRelatedPageSummary


@pytest.mark.django_db
def test_sector_page_has_section_three_subsections(root_page, rf):
    article = InternationalSectorPageFactory(
        parent=root_page,
        slug='article-slug'
    )

    serializer = InternationalSectorPageSerializer(
        instance=article,
        context={'request': rf.get('/')}
    )

    assert len(serializer.data['section_three_subsections']) == 2
    for section in serializer.data['section_three_subsections']:
        assert 'heading' in section
        assert 'teaser' in section
        assert 'body' in section


@pytest.mark.django_db
def test_sector_page_has_section_two_subsections(root_page, rf):
    article = InternationalSectorPageFactory(
        parent=root_page,
        slug='article-slug'
    )

    serializer = InternationalSectorPageSerializer(
        instance=article,
        context={'request': rf.get('/')}
    )

    assert len(serializer.data['section_two_subsections']) == 3
    for section in serializer.data['section_two_subsections']:
        assert 'icon' in section
        assert 'heading' in section
        assert 'body' in section


@pytest.mark.django_db
def test_sector_page_has_statistics(root_page, rf):
    article = InternationalSectorPageFactory(
        parent=root_page,
        slug='article-slug'
    )

    serializer = InternationalSectorPageSerializer(
        instance=article,
        context={'request': rf.get('/')}
    )

    assert len(serializer.data['statistics']) == 6
    for statistic in serializer.data['statistics']:
        assert 'number' in statistic
        assert 'heading' in statistic
        assert 'smallprint' in statistic


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


@pytest.mark.django_db
def test_curated_topic_landing_page_has_features(root_page, rf):
    page = InternationalCuratedTopicLandingPageFactory(
        parent=root_page,
        slug='page-slug'
    )

    serializer = InternationalCuratedTopicLandingPageSerializer(
        instance=page,
        context={'request': rf.get('/')}
    )

    assert len(serializer.data['features_large']) == 2
    for item in serializer.data['features_large']:
        assert 'heading' in item
        assert 'image' in item
        assert 'content' in item

    assert len(serializer.data['features_small']) == 3
    for item in serializer.data['features_small']:
        assert 'heading' in item
        assert 'image' in item
        assert 'url' in item


@pytest.mark.django_db
def test_guide_landing_page_serializer_guide_list(root_page, image, rf):
    """
    The serializer for InternationalGuideLandingPage should include a list
    of decendants of type InternationalArticlePage only
    """
    page = InternationalGuideLandingPageFactory(
        parent=root_page,
        slug='page-slug',
        section_one_image=image,
        section_two_image=image,
    )

    InternationalArticlePageFactory(parent=page, slug='one')
    InternationalArticlePageFactory(parent=page, slug='two')
    # This page in not an InternationalArticlePage, so should not be included
    InternationalSectorPageFactory(parent=page, slug='three')

    serializer = InternationalGuideLandingPageSerializer(
        instance=page,
        context={'request': rf.get('/')}
    )

    assert len(serializer.data['guides']) == 2
    for item in serializer.data['guides']:
        assert 'title' in item
        assert 'teaser' in item
        assert 'thumbnail' in item


@pytest.mark.django_db
def test_capital_invest_landing_page_related_regions(root_page, rf):
    related_region_one = CapitalInvestRegionPageFactory(
        parent=root_page,
        slug='one'
    )

    home_page = InternationalCapitalInvestLandingPageFactory(
        parent=root_page,
        slug='home-page',
        related_region_one=related_region_one
    )

    serializer = InternationalCapitalInvestLandingPageSerializer(
        instance=home_page,
        context={'request': rf.get('/')}
    )

    assert len(serializer.data['related_regions']) == 1
    for page in serializer.data['related_regions']:
        assert 'title' in page
        assert 'image' in page
        assert 'featured_description' in page


@pytest.mark.django_db
def test_capital_invest_region_page_has_statistics(rf):
    region = CapitalInvestRegionPageFactory(
        slug='region-slug',
        parent=None
    )

    serializer = CapitalInvestRegionPageSerializer(
        instance=region,
        context={'request': rf.get('/')}
    )

    assert len(serializer.data['location_stats']) == 4
    assert len(serializer.data['economics_stats']) == 4
    for statistic in serializer.data['location_stats']:
        assert 'number' in statistic
        assert 'heading' in statistic
        assert 'smallprint' in statistic
    for statistic in serializer.data['economics_stats']:
        assert 'number' in statistic
        assert 'heading' in statistic
        assert 'smallprint' in statistic


@pytest.mark.django_db
def test_capital_invest_regional_sector_gets_added_related_page(
        rf
):
    opportunity_listing_page = CapitalInvestOpportunityListingPageFactory(
        parent=None,
        slug='listing-opps'
    )
    opportunity = CapitalInvestOpportunityPageFactory(
        parent=opportunity_listing_page,
        slug='opp'
    )

    related_page = CapitalInvestSectorRelatedPageSummary(
        added_related_pages=opportunity
    )
    region_page = CapitalInvestRegionPageFactory(
        parent=None,
        slug='region'
    )
    sector_page = CapitalInvestRegionalSectorPageFactory(
        parent=region_page,
        slug='sector',
        added_related_pages=[related_page]
    )

    serializer = CapitalInvestRegionalSectorPageSerializer(
        instance=sector_page,
        context={'request': rf.get('/')}
    )

    print('\n\n\n serializer.data in the test => ', serializer.data['added_related_pages'])
    for page in serializer.data['added_related_pages']:
        assert page['added_related_page']['meta']['slug'] == 'opp'


@pytest.mark.django_db
def test_capital_invest_regional_sector_page_gets_parent(
        root_page, rf
):
    page = CapitalInvestRegionPageFactory(
        parent=root_page,
        slug='page-slug',
    )

    sector = CapitalInvestRegionalSectorPageFactory(parent=page, slug='one')

    serializer = CapitalInvestRegionalSectorPageSerializer(
        instance=sector,
        context={'request': rf.get('/')}
    )

    assert serializer.data['parent']['meta']['slug'] == 'page-slug'


@pytest.mark.django_db
def test_capital_invest_landing_page_has_region_cards_in_list(rf):
    home_page = InternationalCapitalInvestLandingPageFactory(
        slug='some-slug',
        parent=None
    )

    serializer = InternationalCapitalInvestLandingPageSerializer(
        instance=home_page,
        context={'request': rf.get('/')}
    )

    assert len(serializer.data['region_cards'][0]) == 5
    for field in serializer.data['region_cards']:
        assert 'image' in field
        assert 'title' in field
        assert 'summary' in field
        assert 'cta_text' in field
        assert 'pdf_document' in field
