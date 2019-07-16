import pytest

from great_international.serializers import (
    AbstractInternationalSectorPageSerializer,
    InternationalArticlePageSerializer,
    InternationalCampaignPageSerializer, InternationalHomePageSerializer,
    InternationalCuratedTopicLandingPageSerializer,
    InternationalGuideLandingPageSerializer,
    CapitalInvestRegionPageSerializer,
    InternationalCapitalInvestLandingPageSerializer,
    InvestHighPotentialOpportunityFormPageSerializer,
    CapitalInvestOpportunityPageSerializer,
    CapitalInvestOpportunityListingSerializer)
from great_international.tests.factories import (
    InternationalSectorPageFactory, InternationalArticlePageFactory,
    InternationalCampaignPageFactory, InternationalHomePageFactory,
    InternationalHomePageOldFactory,
    InternationalCuratedTopicLandingPageFactory,
    InternationalGuideLandingPageFactory,
    CapitalInvestRegionPageFactory,
    InternationalCapitalInvestLandingPageFactory,
    CapitalInvestOpportunityPageFactory,
    InvestHighPotentialOpportunityFormPageFactory,
    CapitalInvestOpportunityListingPageFactory,
    InternationalSubSectorPageFactory, InternationalTopicLandingPageFactory)

from great_international.models import CapitalInvestRelatedRegions, \
    CapitalInvestHomesInEnglandCardFieldsSummary, \
    CapitalInvestRegionCardFieldsSummary, CapitalInvestRelatedSectors, \
    CapitalInvestRelatedSubSectors


@pytest.mark.django_db
def test_sector_page_has_section_three_subsections(root_page, rf):
    article = InternationalSectorPageFactory(
        parent=root_page,
        slug='article-slug'
    )

    serializer = AbstractInternationalSectorPageSerializer(
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

    serializer = AbstractInternationalSectorPageSerializer(
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

    serializer = AbstractInternationalSectorPageSerializer(
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

    serializer = AbstractInternationalSectorPageSerializer(
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
def test_consistent_page_type_for_old_and_new_home_pages(root_page, rf):
    context = {'request': rf.get('/')}
    expected_page_type = 'InternationalHomePage'

    page1 = InternationalHomePageFactory(parent=root_page, slug='one')
    page1_serializer = InternationalHomePageSerializer(
        instance=page1, context=context)
    assert page1_serializer.data['page_type'] == expected_page_type

    page2 = InternationalHomePageOldFactory(parent=root_page, slug='two')
    page2_serializer = InternationalHomePageSerializer(
        instance=page2, context=context)
    assert page2_serializer.data['page_type'] == expected_page_type


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
def test_capital_invest_landing_page_gets_added_related_regions(rf):

    region = CapitalInvestRegionPageFactory(
        parent=None,
        slug='region'
    )

    related_page = CapitalInvestRelatedRegions(
        related_region=region
    )
    capital_invest_landing_page = InternationalCapitalInvestLandingPageFactory(
        parent=None,
        slug='sector',
        added_regions=[related_page]
    )

    serializer = InternationalCapitalInvestLandingPageSerializer(
        instance=capital_invest_landing_page,
        context={'request': rf.get('/')}
    )

    for page in serializer.data['added_regions']:
        assert page['related_region']['meta']['slug'] == 'region'


@pytest.mark.django_db
def test_capital_invest_landing_page_gets_added_related_region_card_fields(rf):

    region_fields = CapitalInvestRegionCardFieldsSummary(
        region_card_title="title"
    )

    capital_invest_landing_page = InternationalCapitalInvestLandingPageFactory(
        parent=None,
        slug='sector',
        added_region_card_fields=[region_fields]
    )

    serializer = InternationalCapitalInvestLandingPageSerializer(
        instance=capital_invest_landing_page,
        context={'request': rf.get('/')}
    )

    for page in serializer.data['added_region_card_fields']:
        assert page['region_card_title'] == 'title'


@pytest.mark.django_db
def test_capital_invest_landing_page_gets_added_homes_in_england_card_fields(
        rf
):

    homes_in_england_fields = CapitalInvestHomesInEnglandCardFieldsSummary(
        homes_in_england_card_title="title",
    )

    capital_invest_landing_page = InternationalCapitalInvestLandingPageFactory(
        parent=None,
        slug='sector',
        added_homes_in_england_card_fields=[homes_in_england_fields]
    )

    serializer = InternationalCapitalInvestLandingPageSerializer(
        instance=capital_invest_landing_page,
        context={'request': rf.get('/')}
    )

    for page in serializer.data['added_homes_in_england_card_fields']:
        assert page['homes_in_england_card_title'] == 'title'


@pytest.mark.django_db
def test_capital_invest_landing_page_returns_empty_when_no_related_regions(rf):

    related_page = CapitalInvestRelatedRegions()

    capital_invest_landing_page = InternationalCapitalInvestLandingPageFactory(
        parent=None,
        slug='sector',
        added_regions=[related_page]
    )

    serializer = InternationalCapitalInvestLandingPageSerializer(
        instance=capital_invest_landing_page,
        context={'request': rf.get('/')}
    )

    assert serializer.data['added_region_card_fields'] == []


@pytest.mark.django_db
def test_high_potential_opportunity_form_page_serializer():
    instance = InvestHighPotentialOpportunityFormPageFactory()

    serializer = InvestHighPotentialOpportunityFormPageSerializer(
        instance
    )

    assert serializer.data['full_name'] == {
        'label': instance.full_name_label,
        'help_text': instance.full_name_help_text,
    }
    assert serializer.data['role_in_company'] == {
        'label': instance.role_in_company_label,
        'help_text': instance.role_in_company_help_text,
    }
    assert serializer.data['email_address'] == {
        'label': instance.email_address_label,
        'help_text': instance.email_address_help_text,
    }
    assert serializer.data['phone_number'] == {
        'label': instance.phone_number_label,
        'help_text': instance.phone_number_help_text,
    }
    assert serializer.data['company_name'] == {
        'label': instance.company_name_label,
        'help_text': instance.company_name_help_text,
    }
    assert serializer.data['website_url'] == {
        'label': instance.website_url_label,
        'help_text': instance.website_url_help_text,
    }
    assert serializer.data['country'] == {
        'label': instance.country_label,
        'help_text': instance.country_help_text,
    }
    assert serializer.data['company_size'] == {
        'label': instance.company_size_label,
        'help_text': instance.company_size_help_text,
    }
    assert serializer.data['opportunities'] == {
        'label': instance.opportunities_label,
        'help_text': instance.opportunities_help_text,
    }
    assert serializer.data['comment'] == {
        'label': instance.comment_label,
        'help_text': instance.comment_help_text,
    }


@pytest.mark.django_db
def test_capital_invest_landing_page_has_how_we_help(rf):
    region = InternationalCapitalInvestLandingPageFactory(
        slug='region-slug',
        parent=None
    )

    serializer = InternationalCapitalInvestLandingPageSerializer(
        instance=region,
        context={'request': rf.get('/')}
    )

    assert len(serializer.data['how_we_help_icon_and_text']) == 4
    for statistic in serializer.data['how_we_help_icon_and_text']:
        assert 'text' in statistic
        assert 'icon' in statistic


@pytest.mark.django_db
def test_opportunity_page_can_add_sector_as_related(rf):

    guide_landing_page = InternationalGuideLandingPageFactory(
        parent=None,
        slug='page-slug',
    )

    sector = InternationalSectorPageFactory(
        parent=guide_landing_page,
        slug='sector'
    )

    related_sector = CapitalInvestRelatedSectors(
        related_sector=sector
    )

    opportunity = CapitalInvestOpportunityPageFactory(
        parent=None,
        slug='opp',
        related_sectors=[related_sector]
    )

    opportunity_serializer = CapitalInvestOpportunityPageSerializer(
        instance=opportunity,
        context={'request': rf.get('/')}
    )

    for page in opportunity_serializer.data['related_sectors']:
        assert page['related_sector']['meta']['slug'] == 'sector'


@pytest.mark.django_db
def test_international_sector_page_gets_opps_with_sector_as_related(rf):

    guide_landing_page = InternationalTopicLandingPageFactory(
        parent=None,
        slug='page-slug',
    )
    print('\n\n\n\n guide landing page ', guide_landing_page)

    sector = InternationalSectorPageFactory(
        parent=guide_landing_page,
        slug='sector'
    )
    print('\n\n\n\n\n\n sector ', sector)

    related_sector = CapitalInvestRelatedSectors(
        related_sector=sector
    )
    print('\n\n\n\n\n\n related sector ', related_sector)

    opportunity = CapitalInvestOpportunityPageFactory(
        parent=None,
        slug='opp',
        related_sectors=[related_sector]
    )
    print('\n\n\n\n\n\n opportunity ', opportunity)

    opportunity_serializer = CapitalInvestOpportunityPageSerializer(
        instance=opportunity,
        context={'request': rf.get('/')}
    )
    print('\n\n\n\n\n\n opportunity serializer data ', opportunity_serializer.data)  # NOQA

    for page in opportunity_serializer.data['related_sectors']:
        assert page['related_sector']['meta']['slug'] == 'sector'

    sector_serializer = AbstractInternationalSectorPageSerializer(
        instance=sector,
        context={'request': rf.get('/')}
    )

    print('\n\n\n\n\n sector serializer ', sector_serializer.data)

    for page in sector_serializer.data['related_opportunities']:
        assert page['meta']['slug'] == 'opp'


@pytest.mark.django_db
def test_opp_page_null_case_related_sector(rf):

    related_sector = CapitalInvestRelatedSectors()

    opportunity = CapitalInvestOpportunityPageFactory(
        parent=None,
        slug='opp',
        related_sectors=[related_sector]
    )

    opportunity_serializer = CapitalInvestOpportunityPageSerializer(
        instance=opportunity,
        context={'request': rf.get('/')}
    )

    for page in opportunity_serializer.data['related_sectors']:
        assert page['related_sector'] == []


@pytest.mark.django_db
def test_opp_page_null_case_related_sector2(rf):

    opportunity = CapitalInvestOpportunityPageFactory(
        parent=None,
        slug='opp',
        related_sectors=[]
    )

    opportunity_serializer = CapitalInvestOpportunityPageSerializer(
        instance=opportunity,
        context={'request': rf.get('/')}
    )

    assert opportunity_serializer.data['related_sectors'] == []


@pytest.mark.django_db
def test_international_sector_opportunity_null_case(rf):

    guide_landing_page = InternationalGuideLandingPageFactory(
        parent=None,
        slug='page-slug',
    )

    sector_a = InternationalSectorPageFactory(
        parent=guide_landing_page,
        slug='sectorA'
    )

    sector_b = InternationalSectorPageFactory(
        parent=guide_landing_page,
        slug='sectorB'
    )

    related_sector = CapitalInvestRelatedSectors(
        related_sector=sector_a
    )

    opportunity = CapitalInvestOpportunityPageFactory(
        parent=None,
        slug='opp',
        related_sectors=[related_sector]
    )

    opportunity_serializer = CapitalInvestOpportunityPageSerializer(
        instance=opportunity,
        context={'request': rf.get('/')}
    )

    for page in opportunity_serializer.data['related_sectors']:
        assert page['related_sector']['meta']['slug'] == 'sectorA'

    sector_serializer = AbstractInternationalSectorPageSerializer(
        instance=sector_b,
        context={'request': rf.get('/')}
    )

    assert sector_serializer.data['related_opportunities'] == []


@pytest.mark.django_db
def test_international_sector_opportunity_null_case2(rf):

    guide_landing_page = InternationalGuideLandingPageFactory(
        parent=None,
        slug='page-slug',
    )

    sector = InternationalSectorPageFactory(
        parent=guide_landing_page,
        slug='sector'
    )

    related_sector = CapitalInvestRelatedSectors()

    opportunity = CapitalInvestOpportunityPageFactory(
        parent=None,
        slug='opp',
        related_sectors=[related_sector]
    )

    opportunity_serializer = CapitalInvestOpportunityPageSerializer(
        instance=opportunity,
        context={'request': rf.get('/')}
    )
    for page in opportunity_serializer.data['related_sectors']:
        assert page['related_sector'] == []

    sector_serializer = AbstractInternationalSectorPageSerializer(
        instance=sector,
        context={'request': rf.get('/')}
    )
    assert sector_serializer.data['related_opportunities'] == []


@pytest.mark.django_db
def test_opportunity_listing_page_gets_opportunities(rf):

    opportunity_listing_page = CapitalInvestOpportunityListingPageFactory(
        parent=None,
        slug='opp-listing'
    )

    opportunity_page = CapitalInvestOpportunityPageFactory(
        parent=opportunity_listing_page,
        slug='opportunity'
    )

    opportunity_serializer = CapitalInvestOpportunityPageSerializer(
        instance=opportunity_page,
        context={'request': rf.get('/')}
    )

    opportunity_listing_serializer = CapitalInvestOpportunityListingSerializer(
        instance=opportunity_listing_page,
        context={'request': rf.get('/')}
    )

    assert opportunity_serializer.data['meta']['slug'] == 'opportunity'
    for opp in opportunity_listing_serializer.data['opportunity_list']:
        assert opp['meta']['slug'] == 'opportunity'


@pytest.mark.django_db
def test_opportunity_listing_page_getting_opportunities_null_case(rf):

    opportunity_listing_page = CapitalInvestOpportunityListingPageFactory(
        parent=None,
        slug='opp-listing'
    )

    opportunity_listing_serializer = CapitalInvestOpportunityListingSerializer(
        instance=opportunity_listing_page,
        context={'request': rf.get('/')}
    )

    assert opportunity_listing_serializer.data['opportunity_list'] == []


@pytest.mark.django_db
def test_opportunity_page_can_add_sub_sector_as_related(rf):

    guide_landing_page = InternationalTopicLandingPageFactory(
        parent=None,
        slug='page-slug',
    )

    sector = InternationalSectorPageFactory(
        parent=guide_landing_page,
        slug='sector'
    )

    sub_sector = InternationalSubSectorPageFactory(
        parent=sector,
        heading='sub_sector',
        slug='sub_sector'
    )

    related_sub_sector = CapitalInvestRelatedSubSectors(
        related_sub_sector=sub_sector
    )

    opportunity = CapitalInvestOpportunityPageFactory(
        parent=None,
        slug='opp',
        related_sub_sectors=[related_sub_sector]
    )

    opportunity_serializer = CapitalInvestOpportunityPageSerializer(
        instance=opportunity,
        context={'request': rf.get('/')}
    )

    for sector in opportunity_serializer.data['sub_sectors']:
        assert sector['sub_sectors'] == 'sub_sector'


@pytest.mark.django_db
def test_opportunity_page_can_add_sub_sector_as_related_null_case(rf):

    related_sub_sector = CapitalInvestRelatedSubSectors()

    opportunity = CapitalInvestOpportunityPageFactory(
        parent=None,
        slug='opp',
        related_sub_sectors=[related_sub_sector]
    )

    opportunity_serializer = CapitalInvestOpportunityPageSerializer(
        instance=opportunity,
        context={'request': rf.get('/')}
    )

    assert opportunity_serializer.data['sub_sectors'] == [[]]
