from unittest import mock
import pytest

from great_international.serializers import (
    BaseInternationalSectorPageSerializer,
    InternationalArticlePageSerializer,
    InternationalCampaignPageSerializer,
    InternationalHomePageSerializer,
    InternationalCuratedTopicLandingPageSerializer,
    InternationalGuideLandingPageSerializer,
    AboutUkRegionPageSerializer,
    InternationalCapitalInvestLandingPageSerializer,
    InvestHighPotentialOpportunityFormPageSerializer,
    CapitalInvestOpportunityPageSerializer,
    CapitalInvestOpportunityListingSerializer,
    InternationalSectorPageSerializer,
    AboutDitServicesPageSerializer,
    AboutUkWhyChooseTheUkPageSerializer,
    AboutUkLandingPageSerializer,
    InvestInternationalHomePageSerializer,
    CapitalInvestRegionPageSerializer,
    AboutUkRegionListingPageSerializer,
    InvestmentOpportunityPageSerializer,
    InvestmentOpportunityListingPageSerializer,
    InvestmentOpportunityForListPageSerializer,
    RelatedInvestmentOpportunityPageSerializer,
)
from tests.great_international.factories import (
    InternationalSectorPageFactory,
    InternationalArticlePageFactory,
    InternationalCampaignPageFactory,
    InternationalHomePageFactory,
    InternationalCuratedTopicLandingPageFactory,
    InternationalGuideLandingPageFactory,
    AboutUkRegionPageFactory,
    InternationalCapitalInvestLandingPageFactory,
    CapitalInvestOpportunityPageFactory,
    InvestHighPotentialOpportunityFormPageFactory,
    CapitalInvestOpportunityListingPageFactory,
    InternationalSubSectorPageFactory,
    InternationalTopicLandingPageFactory,
    AboutDitServicesPageFactory,
    AboutUkWhyChooseTheUkPageFactory,
    AboutUkLandingPageFactory,
    InvestInternationalHomePageFactory,
    CapitalInvestRegionPageFactory,
    AboutUkRegionListingPageFactory,
    InvestRegionPageFactory,
    InternationalTradeHomePageFactory,
    CapitalInvestRelatedSectorsFactory,
    InvestmentOpportunityPageFactory,
    InvestmentOpportunityRelatedSectorsFactory,
    InvestmentOpportunityListingPageFactory,
    PlanningStatusFactory,
)

from great_international.models.capital_invest import (
    CapitalInvestRelatedRegions,
    CapitalInvestHomesInEnglandCardFieldsSummary,
    CapitalInvestRegionCardFieldsSummary,
    CapitalInvestRelatedSubSectors,
)
from great_international.models.great_international import (
    AboutDitServicesFields,
    AboutUkArticlesFields
)
from great_international.models.investment_atlas import (
    InvestmentOpportunityRelatedSubSectors,
)


@pytest.mark.django_db
def test_sector_page_has_section_three_subsections(international_root_page,
                                                   rf):
    article = InternationalSectorPageFactory(
        parent=international_root_page,
        slug='article-slug'
    )

    serializer = BaseInternationalSectorPageSerializer(
        instance=article,
        context={'request': rf.get('/')}
    )

    assert len(serializer.data['section_three_subsections']) == 2
    for section in serializer.data['section_three_subsections']:
        assert 'heading' in section
        assert 'teaser' in section
        assert 'body' in section


@pytest.mark.django_db
def test_sector_page_has_section_two_subsections(international_root_page, rf):
    article = InternationalSectorPageFactory(
        parent=international_root_page,
        slug='article-slug'
    )

    serializer = BaseInternationalSectorPageSerializer(
        instance=article,
        context={'request': rf.get('/')}
    )

    assert len(serializer.data['section_two_subsections']) == 3
    for section in serializer.data['section_two_subsections']:
        assert 'icon' in section
        assert 'heading' in section
        assert 'body' in section


@pytest.mark.django_db
def test_sector_page_has_statistics(international_root_page, rf):
    article = InternationalSectorPageFactory(
        parent=international_root_page,
        slug='article-slug'
    )

    serializer = BaseInternationalSectorPageSerializer(
        instance=article,
        context={'request': rf.get('/')}
    )

    assert len(serializer.data['statistics']) == 6
    for statistic in serializer.data['statistics']:
        assert 'number' in statistic
        assert 'heading' in statistic
        assert 'smallprint' in statistic


@pytest.mark.django_db
def test_sector_page_related_pages_serializer_has_pages(
        international_root_page, rf
):
    related_page_one = InternationalArticlePageFactory(
        parent=international_root_page,
        slug='one'
    )

    related_page_two = InternationalArticlePageFactory(
        parent=international_root_page,
        slug='two'
    )
    related_page_three = InternationalArticlePageFactory(
        parent=international_root_page,
        slug='three'
    )
    case_study_cta_page = InternationalArticlePageFactory(
        parent=international_root_page,
        slug="case_study"
    )
    article = InternationalSectorPageFactory(
        parent=international_root_page,
        slug='article-slug',
        related_page_one=related_page_one,
        related_page_two=related_page_two,
        related_page_three=related_page_three,
        case_study_cta_page=case_study_cta_page
    )

    serializer = BaseInternationalSectorPageSerializer(
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
        parent_page_class, serializer_class, international_root_page, rf
):
    related_page_one = InternationalArticlePageFactory(
        parent=international_root_page,
        slug='one'
    )
    related_page_two = InternationalArticlePageFactory(
        parent=international_root_page,
        slug='two'
    )
    related_page_three = InternationalArticlePageFactory(
        parent=international_root_page,
        slug='three'
    )
    article = parent_page_class(
        parent=international_root_page,
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
def test_home_page_related_pages(international_root_page, rf):
    related_page_one = InternationalArticlePageFactory(
        parent=international_root_page,
        slug='one'
    )
    related_page_two = InternationalCampaignPageFactory(
        parent=international_root_page,
        slug='two'
    )

    home_page = InternationalHomePageFactory(
        parent=international_root_page,
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
    parent_page_class, serializer_class, international_root_page, rf
):
    article = parent_page_class(
        parent=international_root_page,
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
def test_curated_topic_landing_page_has_features(international_root_page, rf):
    page = InternationalCuratedTopicLandingPageFactory(
        parent=international_root_page,
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
def test_guide_landing_page_serializer_guide_list(international_root_page, image, rf):
    """
    The serializer for InternationalGuideLandingPage should include a list
    of decendants of type InternationalArticlePage only
    """
    page = InternationalGuideLandingPageFactory(
        parent=international_root_page,
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
def test_capital_invest_region_page_has_statistics(international_root_page, rf):
    region = CapitalInvestRegionPageFactory(
        slug='region-slug',
        parent=international_root_page
    )

    serializer = CapitalInvestRegionPageSerializer(
        instance=region,
        context={'request': rf.get('/')}
    )

    assert len(serializer.data['location_stats']) == 6
    assert len(serializer.data['economics_stats']) == 6
    for statistic in serializer.data['location_stats']:
        assert 'number' in statistic
        assert 'heading' in statistic
        assert 'smallprint' in statistic
    for statistic in serializer.data['economics_stats']:
        assert 'number' in statistic
        assert 'heading' in statistic
        assert 'smallprint' in statistic


@pytest.mark.django_db
def test_about_uk_region_page_has_statistics(international_root_page, rf):
    region = AboutUkRegionPageFactory(
        slug='region-slug',
        parent=international_root_page
    )

    serializer = AboutUkRegionPageSerializer(
        instance=region,
        context={'request': rf.get('/')}
    )

    assert len(serializer.data['location_stats']) == 6
    assert len(serializer.data['economics_stats']) == 6
    for statistic in serializer.data['location_stats']:
        assert 'number' in statistic
        assert 'heading' in statistic
        assert 'smallprint' in statistic
    for statistic in serializer.data['economics_stats']:
        assert 'number' in statistic
        assert 'heading' in statistic
        assert 'smallprint' in statistic


@pytest.mark.django_db
def test_capital_invest_landing_page_gets_added_related_regions(
        rf, international_root_page
):

    region = AboutUkRegionPageFactory(
        parent=international_root_page,
        slug='region'
    )

    related_page = CapitalInvestRelatedRegions(
        related_region=region
    )
    capital_invest_landing_page = InternationalCapitalInvestLandingPageFactory(
        parent=international_root_page,
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
def test_capital_invest_landing_page_gets_added_related_region_card_fields(
        rf, international_root_page):

    region_fields = CapitalInvestRegionCardFieldsSummary(
        region_card_title="title"
    )

    capital_invest_landing_page = InternationalCapitalInvestLandingPageFactory(
        parent=international_root_page,
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
        rf, international_root_page
):

    homes_in_england_fields = CapitalInvestHomesInEnglandCardFieldsSummary(
        homes_in_england_card_title="title",
    )

    capital_invest_landing_page = InternationalCapitalInvestLandingPageFactory(
        parent=international_root_page,
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
def test_capital_invest_landing_page_returns_empty_when_no_related_regions(
        rf, international_root_page):

    related_page = CapitalInvestRelatedRegions()

    capital_invest_landing_page = InternationalCapitalInvestLandingPageFactory(
        parent=international_root_page,
        slug='sector',
        added_regions=[related_page]
    )

    serializer = InternationalCapitalInvestLandingPageSerializer(
        instance=capital_invest_landing_page,
        context={'request': rf.get('/')}
    )

    assert serializer.data['added_region_card_fields'] == []


@pytest.mark.django_db
def test_high_potential_opportunity_form_page_serializer(
    international_root_page
):
    instance = InvestHighPotentialOpportunityFormPageFactory(
        parent=international_root_page
    )

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
def test_capital_invest_landing_page_has_how_we_help(
        rf, international_root_page
):
    region = InternationalCapitalInvestLandingPageFactory(
        slug='region-slug',
        parent=international_root_page
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
def test_opportunity_page_can_add_sector_as_related(rf, international_root_page):

    guide_landing_page = InternationalGuideLandingPageFactory(
        parent=international_root_page,
        slug='page-slug',
    )

    sector = InternationalSectorPageFactory(
        parent=guide_landing_page,
        slug='sector'
    )

    opportunity = CapitalInvestOpportunityPageFactory(
        parent=international_root_page,
        slug='opp',
        related_sectors=[]
    )
    related_sector = CapitalInvestRelatedSectorsFactory(related_sector=sector, page=opportunity)
    opportunity.related_sector = related_sector

    opportunity_serializer = CapitalInvestOpportunityPageSerializer(
        instance=opportunity,
        context={'request': rf.get('/')}
    )

    for page in opportunity_serializer.data['related_sectors']:
        assert page['related_sector']['meta']['slug'] == 'sector'


@pytest.mark.django_db
def test_international_sector_page_gets_opps_with_sector_as_related(
        rf, international_root_page
):

    guide_landing_page = InternationalGuideLandingPageFactory(
        parent=international_root_page,
        slug='page-slug',
    )

    sector = InternationalSectorPageFactory(
        parent=guide_landing_page,
        slug='sector'
    )

    opportunity = CapitalInvestOpportunityPageFactory(
        parent=international_root_page,
        slug='opp',
        related_sectors=[]
    )
    related_sector = CapitalInvestRelatedSectorsFactory(related_sector=sector, page=opportunity)
    opportunity.related_sector = related_sector

    opportunity_serializer = CapitalInvestOpportunityPageSerializer(
        instance=opportunity,
        context={'request': rf.get('/')}
    )

    for page in opportunity_serializer.data['related_sectors']:
        assert page['related_sector']['meta']['slug'] == 'sector'

    sector_serializer = BaseInternationalSectorPageSerializer(
        instance=sector,
        context={'request': rf.get('/')}
    )

    for page in sector_serializer.data['related_opportunities']:
        assert page['meta']['slug'] == 'opp'


@pytest.mark.django_db
def test_opp_page_null_case_related_sector(rf, international_root_page):

    opportunity = CapitalInvestOpportunityPageFactory(
        parent=international_root_page,
        slug='opp',
        related_sectors=[]
    )
    related_sector = CapitalInvestRelatedSectorsFactory(page=opportunity)
    opportunity.related_sector = related_sector

    opportunity_serializer = CapitalInvestOpportunityPageSerializer(
        instance=opportunity,
        context={'request': rf.get('/')}
    )

    for page in opportunity_serializer.data['related_sectors']:
        assert page['related_sector'] == []


@pytest.mark.django_db
def test_opp_page_related_random_opps(rf, international_root_page):

    guide_landing_page = InternationalGuideLandingPageFactory(
        parent=international_root_page,
        slug='page-slug',
    )

    sector = InternationalSectorPageFactory(
        parent=guide_landing_page,
        slug='sector'
    )

    opportunity = CapitalInvestOpportunityPageFactory(
        parent=international_root_page,
        slug='opp',
        related_sectors=[]
    )

    related_sector = CapitalInvestRelatedSectorsFactory(related_sector=sector, page=opportunity)
    opportunity.related_sectors = [related_sector]

    for i in range(3):
        opp = CapitalInvestOpportunityPageFactory(
            parent=international_root_page,
            slug=f'opp{i}',
            related_sectors=[related_sector]
        )
        related_sector = CapitalInvestRelatedSectorsFactory(related_sector=sector, page=opp)
        opp.related_sectors = [related_sector]

    serializer = CapitalInvestOpportunityPageSerializer(
        instance=opportunity,
        context={'request': rf.get('/')}
    )

    assert len(serializer.data['related_opportunities']) == 3


@pytest.mark.django_db
def test_opp_page_null_case_related_sector2(rf, international_root_page):

    opportunity = CapitalInvestOpportunityPageFactory(
        parent=international_root_page,
        slug='opp',
        related_sectors=[]
    )

    opportunity_serializer = CapitalInvestOpportunityPageSerializer(
        instance=opportunity,
        context={'request': rf.get('/')}
    )

    assert opportunity_serializer.data['related_sectors'] == []


@pytest.mark.django_db
def test_international_sector_opportunity_null_case(
        rf, international_root_page
):

    guide_landing_page = InternationalGuideLandingPageFactory(
        parent=international_root_page,
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

    opportunity = CapitalInvestOpportunityPageFactory(
        parent=international_root_page,
        slug='opp',
        related_sectors=[]
    )
    related_sector = CapitalInvestRelatedSectorsFactory(related_sector=sector_a, page=opportunity)
    opportunity.related_sector = related_sector

    opportunity_serializer = CapitalInvestOpportunityPageSerializer(
        instance=opportunity,
        context={'request': rf.get('/')}
    )

    for page in opportunity_serializer.data['related_sectors']:
        assert page['related_sector']['meta']['slug'] == 'sectorA'

    sector_serializer = BaseInternationalSectorPageSerializer(
        instance=sector_b,
        context={'request': rf.get('/')}
    )

    assert sector_serializer.data['related_opportunities'] == []


@pytest.mark.django_db
def test_international_sector_opportunity_null_case2(
        rf, international_root_page
):

    guide_landing_page = InternationalGuideLandingPageFactory(
        parent=international_root_page,
        slug='page-slug',
    )

    sector = InternationalSectorPageFactory(
        parent=guide_landing_page,
        slug='sector'
    )

    opportunity = CapitalInvestOpportunityPageFactory(
        parent=international_root_page,
        slug='opp',
        related_sectors=[]
    )

    opportunity_serializer = CapitalInvestOpportunityPageSerializer(
        instance=opportunity,
        context={'request': rf.get('/')}
    )
    for page in opportunity_serializer.data['related_sectors']:
        assert page['related_sector'] == []

    sector_serializer = BaseInternationalSectorPageSerializer(
        instance=sector,
        context={'request': rf.get('/')}
    )
    assert sector_serializer.data['related_opportunities'] == []


@pytest.mark.django_db
def test_opportunity_listing_page_gets_opportunities(
        rf, international_root_page
):

    opportunity_listing_page = CapitalInvestOpportunityListingPageFactory(
        parent=international_root_page,
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
def test_opportunity_listing_page_getting_opportunities_null_case(
        rf, international_root_page
):

    opportunity_listing_page = CapitalInvestOpportunityListingPageFactory(
        parent=international_root_page,
        slug='opp-listing'
    )

    opportunity_listing_serializer = CapitalInvestOpportunityListingSerializer(
        instance=opportunity_listing_page,
        context={'request': rf.get('/')}
    )

    assert opportunity_listing_serializer.data['opportunity_list'] == []


@pytest.mark.django_db
def test_opportunity_page_can_add_sub_sector_as_related(
        rf, international_root_page):

    guide_landing_page = InternationalTopicLandingPageFactory(
        parent=international_root_page,
        slug='page-slug',
    )

    sector = InternationalSectorPageFactory(
        parent=guide_landing_page,
        slug='sector'
    )

    sub_sector = InternationalSubSectorPageFactory(
        parent=sector,
        heading='sub_sector_heading',
        slug='sub_sector'
    )

    related_sub_sector = CapitalInvestRelatedSubSectors(
        related_sub_sector=sub_sector
    )

    opportunity = CapitalInvestOpportunityPageFactory(
        parent=international_root_page,
        slug='opp',
        related_sub_sectors=[related_sub_sector]
    )

    opportunity_serializer = CapitalInvestOpportunityPageSerializer(
        instance=opportunity,
        context={'request': rf.get('/')}
    )

    for sub_sector in opportunity_serializer.data['sub_sectors']:
        assert sub_sector == 'sub_sector_heading'


@pytest.mark.django_db
def test_opportunity_page_can_add_sub_sector_as_related_null_case(
        rf, international_root_page
):

    related_sub_sector = CapitalInvestRelatedSubSectors()

    opportunity = CapitalInvestOpportunityPageFactory(
        parent=international_root_page,
        slug='opp',
        related_sub_sectors=[related_sub_sector]
    )

    opportunity_serializer = CapitalInvestOpportunityPageSerializer(
        instance=opportunity,
        context={'request': rf.get('/')}
    )

    assert opportunity_serializer.data['sub_sectors'] == ['']


@pytest.mark.django_db
def test_opportunity_listing_page_gets_sectors_with_sub_sectors(
        rf, international_root_page
):
    topic_landing_page = InternationalTopicLandingPageFactory(
        parent=international_root_page,
        slug='page-slug',
    )

    automotive_sector = InternationalSectorPageFactory(
        parent=topic_landing_page,
        slug='automotive'
    )
    InternationalSectorPageSerializer(
        instance=automotive_sector,
        context={'request': rf.get('/')}
    )

    real_estate_sector = InternationalSectorPageFactory(
        parent=topic_landing_page,
        slug='real-estate'
    )
    InternationalSectorPageSerializer(
        instance=real_estate_sector,
        context={'request': rf.get('/')}
    )

    housing_sub_sector = InternationalSubSectorPageFactory(
        parent=real_estate_sector,
        heading='Housing',
        slug='housing'
    )
    BaseInternationalSectorPageSerializer(
        instance=housing_sub_sector,
        context={'request': rf.get('/')}
    )

    mixed_use_sub_sector = InternationalSubSectorPageFactory(
        parent=automotive_sector,
        heading='Mixed Use',
        slug='mixed-use'
    )
    BaseInternationalSectorPageSerializer(
        instance=mixed_use_sub_sector,
        context={'request': rf.get('/')}
    )

    energy_sub_sector = InternationalSubSectorPageFactory(
        parent=automotive_sector,
        heading='Energy',
        slug='energy'
    )
    BaseInternationalSectorPageSerializer(
        instance=energy_sub_sector,
        context={'request': rf.get('/')}
    )

    opportunity_listing_page = CapitalInvestOpportunityListingPageFactory(
        parent=international_root_page,
        slug='opp-listing'
    )

    opportunity_listing_serializer = CapitalInvestOpportunityListingSerializer(
        instance=opportunity_listing_page,
        context={'request': rf.get('/')}
    )

    assert len(
        opportunity_listing_serializer.data['sector_with_sub_sectors']) == 2

    all_sub_sectors = [
        sub_sector for sub_sectors in opportunity_listing_serializer
        .data['sector_with_sub_sectors'].values() for sub_sector in sub_sectors
    ]

    assert len(all_sub_sectors) == 3


@pytest.mark.django_db
def test_about_dit_services_page_gets_added_related_services_fields(
        rf, international_root_page
):
    services_fields = AboutDitServicesFields(
        title="title"
    )

    about_dit_services_page = AboutDitServicesPageFactory(
        parent=international_root_page,
        slug='services',
        about_dit_services_fields=[services_fields]
    )

    serializer = AboutDitServicesPageSerializer(
        instance=about_dit_services_page,
        context={'request': rf.get('/')}
    )

    for page in serializer.data['about_dit_services_fields']:
        assert page['title'] == 'title'


@pytest.mark.django_db
def test_about_uk_why_choose_the_uk_page_gets_added_related_articles_fields(
        rf, international_root_page
):
    services_fields = AboutUkArticlesFields(
        title="title"
    )

    about_uk_why_choose_the_uk_page = AboutUkWhyChooseTheUkPageFactory(
        parent=international_root_page,
        slug='services',
        about_uk_articles_fields=[services_fields]
    )

    serializer = AboutUkWhyChooseTheUkPageSerializer(
        instance=about_uk_why_choose_the_uk_page,
        context={'request': rf.get('/')}
    )

    for page in serializer.data['about_uk_articles_fields']:
        assert page['title'] == 'title'


@pytest.mark.django_db
def test_opportunity_page_gets_opportunities_with_same_sector(rf, international_root_page):

    topic_landing_page = InternationalGuideLandingPageFactory(
        parent=international_root_page,
        slug='page-slug',
    )

    sector = InternationalSectorPageFactory(
        parent=topic_landing_page,
        slug='sector',
        title='sector_title'
    )

    ashton_green = CapitalInvestOpportunityPageFactory(
        parent=international_root_page,
        slug='ashton-green',
        title_en_gb='Ashton Green',
        related_sectors=[]
    )
    related_sector = CapitalInvestRelatedSectorsFactory(related_sector=sector, page=ashton_green)
    ashton_green.related_sector = related_sector

    birmingham = CapitalInvestOpportunityPageFactory(
        parent=international_root_page,
        slug='birimingham-curzon',
        title_en_gb='Birmingham Curzon',
        related_sectors=[]
    )
    related_sector = CapitalInvestRelatedSectorsFactory(related_sector=sector, page=birmingham)
    ashton_green.related_sector = related_sector

    serializer = CapitalInvestOpportunityPageSerializer(
        instance=birmingham,
        context={'request': rf.get('/')}
    )

    related_opps = serializer.data['related_opportunities']

    assert len(related_opps) == 1

    assert related_opps[0]['meta']['slug'] == 'ashton-green'


@pytest.mark.django_db
def test_opportunity_page_null_case_gets_opportunities_with_same_sector(rf, international_root_page):
    topic_landing_page = InternationalGuideLandingPageFactory(
        parent=international_root_page,
        slug='page-slug',
    )

    sector = InternationalSectorPageFactory(
        parent=topic_landing_page,
        slug='sector',
        title='sector_title'
    )

    related_sector = CapitalInvestRelatedSectorsFactory(related_sector=sector)

    opportunity = CapitalInvestOpportunityPageFactory(
        parent=international_root_page,
        slug='birimingham-curzon',
        title_en_gb='Birmingham Curzon',
        related_sectors=[related_sector]
    )

    opportunity_serializer = CapitalInvestOpportunityPageSerializer(
        instance=opportunity,
        context={'request': rf.get('/')}
    )

    assert len(opportunity_serializer.data['related_opportunities']) == 0


@pytest.mark.django_db
def test_about_uk_landing_page_has_how_we_help(
        rf, international_root_page
):
    about_uk = AboutUkLandingPageFactory(
        slug='about-uk',
        parent=international_root_page
    )

    serializer = AboutUkLandingPageSerializer(
        instance=about_uk,
        context={'request': rf.get('/')}
    )

    assert len(serializer.data['how_we_help']) == 6
    for how_we_help in serializer.data['how_we_help']:
        assert 'text' in how_we_help
        assert 'icon' in how_we_help
        assert 'title' in how_we_help


@pytest.mark.django_db
def test_about_uk_landing_page_has_all_sectors(
        rf, international_root_page
):
    InternationalSectorPageFactory(
        parent=international_root_page,
        slug='sector-one',
    )

    about_uk = AboutUkLandingPageFactory(
        slug='about-uk',
        parent=international_root_page
    )

    serializer = AboutUkLandingPageSerializer(
        instance=about_uk,
        context={'request': rf.get('/')}
    )

    assert len(serializer.data['all_sectors']) == 1
    assert serializer.data['all_sectors'][0]['meta']['slug'] == 'sector-one'


@pytest.mark.django_db
def test_invest_international_homepage_featured_industries(international_root_page, rf):
    featured_industry_one = InternationalSectorPageFactory(
        parent=international_root_page,
        slug='one'
    )
    featured_industry_two = InternationalSectorPageFactory(
        parent=international_root_page,
        slug='two'
    )
    featured_industry_three = InternationalSectorPageFactory(
        parent=international_root_page,
        slug='three'
    )
    homepage = InvestInternationalHomePageFactory(
        parent=international_root_page,
        slug='invest',
        featured_industry_one=featured_industry_one,
        featured_industry_two=featured_industry_two,
        featured_industry_three=featured_industry_three,
    )

    serializer = InvestInternationalHomePageSerializer(
        instance=homepage,
        context={'request': rf.get('/')}
    )

    serialized_pages = serializer.data['sectors']

    assert len(serialized_pages) == 3
    assert serialized_pages[0]['meta']['slug'] == 'one'
    assert serialized_pages[1]['meta']['slug'] == 'two'
    assert serialized_pages[2]['meta']['slug'] == 'three'


@pytest.mark.django_db
def test_about_uk_landing_page_has_regions(rf, international_root_page):
    scotland = AboutUkRegionPageFactory(
        slug="scotland",
        parent=international_root_page
    )

    midlands = AboutUkRegionPageFactory(
        slug="midlands",
        parent=international_root_page
    )

    about_uk = AboutUkLandingPageFactory(
        slug='about-uk',
        parent=international_root_page,
        scotland=scotland,
        scotland_text="Lorem ipsum",
        midlands=midlands,
        midlands_text="Lorem ipsum",
    )

    serializer = AboutUkLandingPageSerializer(
        instance=about_uk,
        context={'request': rf.get('/')}
    )

    assert len(serializer.data['regions']) == 6
    for field in serializer.data['regions']:
        assert 'region' in field
        assert 'text' in field
    assert serializer.data['regions'][0]['text'] == 'Lorem ipsum'
    assert serializer.data['regions'][0]['region']['meta']['slug'] == 'scotland'
    assert serializer.data['regions'][4]['text'] == 'Lorem ipsum'
    assert serializer.data['regions'][4]['region']['meta']['slug'] == 'midlands'


@pytest.mark.django_db
def test_about_uk_region_listing_page_has_regions(rf, international_root_page):
    scotland = InvestRegionPageFactory(
        slug="scotland",
        parent=international_root_page
    )

    midlands = AboutUkRegionPageFactory(
        slug="midlands",
        parent=international_root_page
    )

    AboutUkLandingPageFactory(
        slug='about-uk',
        parent=international_root_page,
        scotland=scotland,
        scotland_text="Lorem ipsum",
        midlands=midlands,
        midlands_text="Lorem ipsum",
    )

    regions = AboutUkRegionListingPageFactory(
        slug='regions',
        parent=international_root_page
    )

    serializer = AboutUkRegionListingPageSerializer(
        instance=regions,
        context={'request': rf.get('/')}
    )

    assert len(serializer.data['mapped_regions']) == 6
    for field in serializer.data['mapped_regions']:
        assert 'region' in field
        assert 'text' in field
    assert serializer.data['mapped_regions'][0]['text'] == 'Lorem ipsum'
    assert serializer.data['mapped_regions'][0]['region']['meta']['slug'] == 'scotland'
    assert serializer.data['mapped_regions'][4]['text'] == 'Lorem ipsum'
    assert serializer.data['mapped_regions'][4]['region']['meta']['slug'] == 'midlands'


@pytest.mark.django_db
def test_about_uk_region_listing_page_has_empty_regions_if_no_parent(rf, international_root_page):

    regions = AboutUkRegionListingPageFactory(
        slug='regions',
        parent=international_root_page
    )

    serializer = AboutUkRegionListingPageSerializer(
        instance=regions,
        context={'request': rf.get('/')}
    )

    assert serializer.data['mapped_regions'] == []


@pytest.mark.django_db
def test_new_int_home_page_has_ready_to_trade_stories(rf, international_root_page):
    home = InternationalHomePageFactory(
        slug='international',
        parent=international_root_page,
        ready_to_trade_story_one='some story',
        ready_to_trade_story_two='some story',
        ready_to_trade_story_three='',
    )

    serializer = InternationalHomePageSerializer(
        instance=home,
        context={'request': rf.get('/')}
    )

    assert len(serializer.data['ready_to_trade_stories']) == 2
    for story in serializer.data['ready_to_trade_stories']:
        assert 'story' in story


@pytest.mark.django_db
def test_new_int_home_page_has_featured_links_one(rf, international_root_page, image):
    home = InternationalHomePageFactory(
        slug='international',
        parent=international_root_page,
        featured_link_one_image=image,
        featured_link_one_url='/foo',
        featured_link_one_heading='Foo',
        featured_link_two_image=None,
        featured_link_two_url=None,
        featured_link_two_heading=None,
        featured_link_three_image=None,
        featured_link_three_url=None,
        featured_link_three_heading=None,
    )

    serializer = InternationalHomePageSerializer(
        instance=home,
        context={'request': rf.get('/')}
    )

    assert len(serializer.data['featured_links']) == 1


@pytest.mark.django_db
def test_new_int_home_page_has_featured_links_all(rf, international_root_page, image):
    home = InternationalHomePageFactory(
        slug='international',
        parent=international_root_page,
        featured_link_one_image=image,
        featured_link_one_url='/one',
        featured_link_one_heading='One',
        featured_link_two_image=image,
        featured_link_two_url='/two',
        featured_link_two_heading='Two',
        featured_link_three_image=image,
        featured_link_three_url='/three',
        featured_link_three_heading='Three',
    )

    serializer = InternationalHomePageSerializer(
        instance=home,
        context={'request': rf.get('/')}
    )

    assert len(serializer.data['featured_links']) == 3
    assert serializer.data['featured_links'][0]['heading'] == 'One'
    assert serializer.data['featured_links'][1]['heading'] == 'Two'
    assert serializer.data['featured_links'][2]['heading'] == 'Three'


@pytest.mark.django_db
def test_new_int_home_page_has_benefits_ok_uk(rf, international_root_page):
    home = InternationalHomePageFactory(
        slug='international',
        parent=international_root_page,
        benefits_of_uk_one='',
        benefits_of_uk_two='some text',
        benefits_of_uk_three='',
        benefits_of_uk_four='',
        benefits_of_uk_five='some text',
        benefits_of_uk_six='some text',
    )

    serializer = InternationalHomePageSerializer(
        instance=home,
        context={'request': rf.get('/')}
    )

    assert len(serializer.data['benefits_of_uk']) == 3
    for benefit in serializer.data['benefits_of_uk']:
        assert 'benefits_of_uk_text' in benefit


@pytest.mark.django_db
def test_new_int_home_page_has_how_we_help(rf, international_root_page, image):
    home = InternationalHomePageFactory(
        slug='international',
        parent=international_root_page,
        how_we_help_one_icon=image,
        how_we_help_one_text='How we help',
        how_we_help_two_icon=image,
        how_we_help_two_text='How we help',
        how_we_help_three_icon=image,
        how_we_help_three_text='',
    )

    serializer = InternationalHomePageSerializer(
        instance=home,
        context={'request': rf.get('/')}
    )

    assert len(serializer.data['how_we_help']) == 2
    for how_we_help in serializer.data['how_we_help']:
        assert 'text' in how_we_help
        assert 'icon' in how_we_help


@pytest.mark.django_db
def test_new_int_home_page_has_link_to_section_links(rf, international_root_page):
    home = InternationalHomePageFactory(
        slug='international',
        parent=international_root_page,
        link_to_section_one='Some markdown',
        link_to_section_one_cta_text='Get in touch',
        link_to_section_one_cta_link='',
        link_to_section_two='Some markdown',
        link_to_section_two_cta_text='Get in touch',
        link_to_section_two_cta_link='/international',
        link_to_section_three='',
        link_to_section_three_cta_text='Get in touch',
        link_to_section_three_cta_link='/international',
    )

    serializer = InternationalHomePageSerializer(
        instance=home,
        context={'request': rf.get('/')}
    )

    assert len(serializer.data['link_to_section_links']) == 1
    for link in serializer.data['link_to_section_links']:
        assert 'text' in link
        assert 'cta_text' in link
        assert 'cta_link' in link


@pytest.mark.django_db
def test_new_int_home_page_has_all_sectors(rf, international_root_page):
    InternationalSectorPageFactory(
        parent=international_root_page,
        slug='sector-one',
        featured_description='some description'
    )

    home = InternationalHomePageFactory(
        slug='international',
        parent=international_root_page
    )

    serializer = InternationalHomePageSerializer(
        instance=home,
        context={'request': rf.get('/')}
    )

    assert len(serializer.data['all_sectors']) == 1
    assert serializer.data['all_sectors'][0]['meta']['slug'] == 'sector-one'


@pytest.mark.django_db
def test_new_int_home_page_has_related_expand(rf, international_root_page, image):
    expand = InvestInternationalHomePageFactory(
        parent=international_root_page,
        slug='expand',
        heading="Some title",
        hero_image=image
    )

    home = InternationalHomePageFactory(
        slug='international',
        related_page_expand=expand,
        parent=international_root_page
    )

    serializer = InternationalHomePageSerializer(
        instance=home,
        context={'request': rf.get('/')}
    )

    assert serializer.data['related_page_expand']['meta']['slug'] == 'expand'


@pytest.mark.django_db
def test_new_int_home_page_has_related_capital_invest(rf, international_root_page, image):
    capital_invest = InternationalCapitalInvestLandingPageFactory(
        parent=international_root_page,
        slug='capital-invest',
        hero_title='Hero title',
        hero_image=image
    )

    home = InternationalHomePageFactory(
        slug='international',
        related_page_invest_capital=capital_invest,
        parent=international_root_page
    )

    serializer = InternationalHomePageSerializer(
        instance=home,
        context={'request': rf.get('/')}
    )

    assert serializer.data['related_page_invest_capital']['meta']['slug'] == 'capital-invest'


@pytest.mark.django_db
def test_capital_invest_landing_page_has_cta(rf, international_root_page, image):
    capital_invest_landing_page = InternationalCapitalInvestLandingPageFactory(
        parent=international_root_page,
        slug='capital-invest',
        hero_title='Hero title',
        hero_image=image,
        hero_subheading='Hero subheading',
        hero_subtitle='Hero subtitle',
        hero_cta_text='click here',
        hero_cta_link='/hero/cta/link',
    )

    serializer = InternationalCapitalInvestLandingPageSerializer(
        instance=capital_invest_landing_page,
        context={'request': rf.get('/')},
    )

    assert serializer.data['hero_title'] == 'Hero title'
    assert serializer.data['hero_subheading'] == 'Hero subheading'
    assert serializer.data['hero_subtitle'] == 'Hero subtitle'
    assert serializer.data['hero_cta_text'] == 'click here'
    assert serializer.data['hero_cta_link'] == '/hero/cta/link'


@pytest.mark.django_db
def test_new_int_home_page_has_related_trade(rf, international_root_page, image):
    trade = InternationalTradeHomePageFactory(
        parent=international_root_page,
        slug='trade',
        title='the title',
        hero_image=image
    )

    home = InternationalHomePageFactory(
        slug='international',
        related_page_buy=trade,
        parent=international_root_page
    )

    serializer = InternationalHomePageSerializer(
        instance=home,
        context={'request': rf.get('/')}
    )

    assert serializer.data['related_page_buy']['meta']['slug'] == 'trade'


@pytest.mark.django_db
def test_new_int_home_page_has_related_how_dit_help_pages(rf, international_root_page, image):
    how_we_help_one = AboutDitServicesPageFactory(
        parent=international_root_page,
        slug='how-we-help-buy',
        title='the title',
        hero_image=image
    )
    how_we_help_two = AboutDitServicesPageFactory(
        parent=international_root_page,
        slug='how-we-help-invest',
        title='the title',
        hero_image=image
    )

    home = InternationalHomePageFactory(
        slug='international',
        related_how_dit_help_page_one=how_we_help_one,
        related_how_dit_help_page_two=how_we_help_two,
        parent=international_root_page
    )

    serializer = InternationalHomePageSerializer(
        instance=home,
        context={'request': rf.get('/')}
    )

    assert serializer.data['related_how_dit_help_pages'][0]['meta']['slug'] == 'how-we-help-buy'
    assert serializer.data['related_how_dit_help_pages'][1]['meta']['slug'] == 'how-we-help-invest'


@pytest.mark.django_db
def test_new_int_home_page_related_how_dit_help_pages_null(rf, international_root_page, image):

    home = InternationalHomePageFactory(
        slug='international',
        parent=international_root_page
    )

    serializer = InternationalHomePageSerializer(
        instance=home,
        context={'request': rf.get('/')}
    )

    assert serializer.data['related_how_dit_help_pages'] == []


@pytest.mark.django_db
def test_invest_international_landing_page_how_to_expand(international_root_page, rf):

    homepage = InvestInternationalHomePageFactory(
        parent=international_root_page,
        slug='expand',
    )

    serializer = InvestInternationalHomePageSerializer(
        instance=homepage,
        context={'request': rf.get('/')}
    )

    serialized_pages = serializer.data

    assert len(serialized_pages['how_to_expand']) == 4
    for how_to in serialized_pages['how_to_expand']:
        assert 'title' in how_to
        assert 'text' in how_to


# Investment Atlas Serializer tests

@pytest.mark.django_db
def test_atlas_opportunity_page_can_add_sector_as_related(rf, international_root_page):
    # Based on test_opportunity_page_can_add_sector_as_related

    guide_landing_page = InternationalGuideLandingPageFactory(
        parent=international_root_page,
        slug='page-slug',
    )

    sector = InternationalSectorPageFactory(
        parent=guide_landing_page,
        slug='sector-a-test'
    )

    opportunity = InvestmentOpportunityPageFactory(
        parent=international_root_page,
        slug='opp',
        related_sectors=[]
    )
    related_sector = InvestmentOpportunityRelatedSectorsFactory(
        related_sector=sector,
        page=opportunity,
    )

    opportunity.related_sector = related_sector  # How this works is not apparent, but it seems to.

    opportunity_serializer = InvestmentOpportunityPageSerializer(
        instance=opportunity,
        context={'request': rf.get('/')}
    )

    for page in opportunity_serializer.data['related_sectors']:
        assert page['related_sector']['meta']['slug'] == 'sector-a-test'


@pytest.mark.django_db
def test_atlas_opportunity_page_null_case_related_sector(rf, international_root_page):
    # based on test_opp_page_null_case_related_sector

    opportunity = InvestmentOpportunityPageFactory(
        parent=international_root_page,
        slug='opp',
        related_sectors=[]
    )
    related_sector = InvestmentOpportunityRelatedSectorsFactory(
        page=opportunity,
        # NB: related_sector kwarg here is null/not set
    )
    opportunity.related_sector = related_sector

    opportunity_serializer = InvestmentOpportunityPageSerializer(
        instance=opportunity,
        context={'request': rf.get('/')}
    )

    for page in opportunity_serializer.data['related_sectors']:
        assert page['related_sector'] == []


@pytest.mark.django_db
def test_atlas_opportunity_page_null_case_related_sector__alt(rf, international_root_page):
    # Based on test_opp_page_null_case_related_sector2

    opportunity = InvestmentOpportunityPageFactory(
        parent=international_root_page,
        slug='opp',
        related_sectors=[]
    )

    # Note, no related sectors set up

    opportunity_serializer = InvestmentOpportunityPageSerializer(
        instance=opportunity,
        context={'request': rf.get('/')}
    )

    assert opportunity_serializer.data['related_sectors'] == []


@pytest.mark.django_db
def test_atlas_opportunity_list_page_related_opportunities(rf, international_root_page):

    # Unlike with the old CapInvest opps, Atlas ones are associated by Region.
    # Sectors do not matter

    # make a landing page
    guide_landing_page = InternationalGuideLandingPageFactory(
        parent=international_root_page,
        slug='page-slug',
    )

    # set up some sectors and subsectors, to help show they don't influence results
    sector_a = InternationalSectorPageFactory(
        parent=guide_landing_page,
        slug='sectorA'
    )
    sector_b = InternationalSectorPageFactory(
        parent=guide_landing_page,
        slug='sectorB'
    )
    sector_c = InternationalSectorPageFactory(
        parent=guide_landing_page,
        slug='sectorB'
    )

    subsector_a1 = InternationalSubSectorPageFactory(
        parent=sector_a,
        heading='sub_sector_a1_heading',
        slug='sub_sector_a1'
    )
    subsector_b2 = InternationalSubSectorPageFactory(
        parent=sector_b,
        heading='sub_sector_b2_heading',
        slug='sub_sector_b2'
    )
    subsector_b3 = InternationalSubSectorPageFactory(
        parent=sector_b,
        heading='sub_sector_b3_heading',
        slug='sub_sector_b3'
    )

    # Add some regions, using the great_international.models.AboutUKRegionPage model,
    # which we'll be adopting use of in the Atlas pages

    region_a = AboutUkRegionPageFactory(
        slug='region-a-slug',
        parent=international_root_page
    )

    region_b = AboutUkRegionPageFactory(
        slug='region-b-slug',
        parent=international_root_page
    )

    region_c = AboutUkRegionPageFactory(
        slug='region-c-slug',
        parent=international_root_page
    )

    related_sector_a = InvestmentOpportunityRelatedSectorsFactory(related_sector=sector_a)
    related_subsector_a1 = InvestmentOpportunityRelatedSubSectors(
        related_sub_sector=subsector_a1
    )

    related_sector_b = InvestmentOpportunityRelatedSectorsFactory(related_sector=sector_b)
    related_subsector_b2 = InvestmentOpportunityRelatedSubSectors(
        related_sub_sector=subsector_b2
    )

    related_subsector_b3 = InvestmentOpportunityRelatedSubSectors(
        related_sub_sector=subsector_b3
    )

    related_sector_c = InvestmentOpportunityRelatedSectorsFactory(related_sector=sector_c)

    # Make eight opportunities:
    # 1. Region A, Sector A, Subsector A1 -> Thing we'll match against
    # 2. Region A, Sector A, no subsector -> valid match
    # 3. Region A, Sector B, Subsector B2 -> valid match
    # 4. Region A, Sector B, Subsector B3 -> valid match
    # 5. Region B, Sector A, no subsector -> should not be shown
    # 6. Region B, Sector A, Subsector A1 -> should not be shown
    # 7. Region C, no sector -> should not be shown
    # 8. Region C, Sector C -> should not be shown
    # 9. Region C and Region A -> valid match

    # Also note that priority_weighting is used here to order which ones are shown first

    # 1. Region A, Sector A, Subsector A1 -> Thing we'll match against
    opportunity_1 = InvestmentOpportunityPageFactory(
        parent=international_root_page,
        slug='opp_one',
        related_regions=[region_a],
        related_sectors=[related_sector_a],
        related_sub_sectors=[related_subsector_a1],
        priority_weighting="0.9"
    )

    # 2. Region A, Sector A, no subsector -> valid match
    opportunity_2 = InvestmentOpportunityPageFactory(
        parent=international_root_page,
        slug='opp_two',
        related_regions=[region_a],
        related_sectors=[related_sector_a],
        related_sub_sectors=[],
        priority_weighting="1.0"
    )

    # 3. Region A, Sector B, Subsector B2 -> valid match
    opportunity_3 = InvestmentOpportunityPageFactory(
        parent=international_root_page,
        slug='opp_three',
        related_regions=[region_a],
        related_sectors=[related_sector_b],
        related_sub_sectors=[related_subsector_b2],
        priority_weighting="2.0"
    )

    # 4. Region A, Sector B, Subsector B3 -> valid match
    opportunity_4 = InvestmentOpportunityPageFactory(
        parent=international_root_page,
        slug='opp_four',
        related_regions=[region_a],
        related_sectors=[related_sector_b],
        related_sub_sectors=[related_subsector_b3],
        priority_weighting="1.5"
    )

    # 5. Region B, Sector A, no subsector -> should not be shown
    opportunity_5 = InvestmentOpportunityPageFactory(
        parent=international_root_page,
        slug='opp_five',
        related_regions=[region_b],
        related_sectors=[related_sector_a],
        related_sub_sectors=[],
        priority_weighting="4.2"
    )

    # 6. Region B, Sector A, Subsector A1 -> should not be shown
    opportunity_6 = InvestmentOpportunityPageFactory(
        parent=international_root_page,
        slug='opp_six',
        related_regions=[region_b],
        related_sectors=[related_sector_a],
        related_sub_sectors=[related_subsector_a1],
        priority_weighting="6.2"
    )

    # 7. Region C, no sector -> should not be shown
    opportunity_7 = InvestmentOpportunityPageFactory(
        parent=international_root_page,
        slug='opp_seven',
        related_regions=[region_c],
        related_sectors=[],
        related_sub_sectors=[],
        priority_weighting="7.2"

    )
    # 8. Region C, Sector C -> should not be shown
    opportunity_8 = InvestmentOpportunityPageFactory(
        parent=international_root_page,
        slug='opp_eight',
        related_regions=[region_c],
        related_sectors=[related_sector_c],
        related_sub_sectors=[],
        priority_weighting="5.2"
    )

    # 9. Region C and Region A -> valid match
    opportunity_9 = InvestmentOpportunityPageFactory(
        parent=international_root_page,
        slug='opp_nine',
        related_regions=[region_a, region_c],
        related_sectors=[related_sector_c],
        related_sub_sectors=[]
        # Has default priority_wieghting (ie, 0.0)
    )

    # now grab the results for the opp
    opportunity_1_serializer = InvestmentOpportunityPageSerializer(
        instance=opportunity_1,
        context={'request': rf.get('/')}
    )

    expected_slugs = [
        x.slug for x in [
            # these are ordered by priority
            opportunity_3,
            opportunity_4,
            opportunity_2,
            opportunity_9,
        ]
    ]

    unexpected_slugs = [
        x.slug for x in [
            # priority doesn't matter here, because we're testing for absence
            opportunity_1,
            opportunity_5,
            opportunity_6,
            opportunity_7,
            opportunity_8,
        ]
    ]

    seen_slugs = []

    for idx, page in enumerate(opportunity_1_serializer.data['related_opportunities']):
        slug = page['meta']['slug']
        expected_slugs[idx] == slug  # ie, ordering check
        assert slug not in unexpected_slugs
        assert slug not in seen_slugs
        seen_slugs.append(slug)

        region_ids = [x['id'] for x in page['regions']]
        assert region_a.id in region_ids

    assert sorted(seen_slugs) == sorted(expected_slugs)

    # Also show the number of related opps varies according to mutual regions
    # 1. Region A, Sector A, Subsector A1 -> Thing we'll match against
    # 2. Region A, Sector A, no subsector -> valid match
    # 3. Region A, Sector B, Subsector B2 -> valid match
    # 4. Region A, Sector B, Subsector B3 -> valid match
    # 5. Region B, Sector A, no subsector -> should not be shown
    # 6. Region B, Sector A, Subsector A1 -> should not be shown
    # 7. Region C, no sector -> should not be shown
    # 8. Region C, Sector C -> should not be shown
    # 9. Region C and Region A -> valid match

    # Each Region C Opp should link to one other
    for region_b_opp in [opportunity_5, opportunity_6]:
        serializer = InvestmentOpportunityPageSerializer(
            instance=region_b_opp,
            context={'request': rf.get('/')}
        )
        assert len(serializer.data['related_opportunities']) == 1
        assert region_b_opp.slug not in [x['meta']['slug'] for x in serializer.data['related_opportunities']]

    # These Region C Opps should link to two others
    for region_c_opp in [opportunity_7, opportunity_8]:
        serializer = InvestmentOpportunityPageSerializer(
            instance=region_c_opp,
            context={'request': rf.get('/')}
        )
        assert len(serializer.data['related_opportunities']) == 2
        assert region_c_opp.slug not in [x['meta']['slug'] for x in serializer.data['related_opportunities']]

    # And this region C and Region A opp shoud link to 6 in total
    serializer = InvestmentOpportunityPageSerializer(
        instance=opportunity_9,
        context={'request': rf.get('/')}
    )
    assert len(serializer.data['related_opportunities']) == 6
    assert opportunity_9.slug not in [x['meta']['slug'] for x in serializer.data['related_opportunities']]


@pytest.mark.django_db
def test_atlas_opportunity_list_page_related_opportunities__no_opportunities(rf, international_root_page):
    opportunity = InvestmentOpportunityPageFactory(
        parent=international_root_page,
        slug='opp_one',
        related_regions=[],
        related_sectors=[],
        related_sub_sectors=[],
        priority_weighting="0.9"
    )
    opportunity_serializer = InvestmentOpportunityPageSerializer(
        instance=opportunity,
        context={'request': rf.get('/')}
    )
    assert opportunity_serializer.data['related_opportunities'] == []


@pytest.mark.django_db
def test_atlas_opportunity_page_can_add_sub_sector_as_related(rf, international_root_page):

    guide_landing_page = InternationalTopicLandingPageFactory(
        parent=international_root_page,
        slug='page-slug',
    )

    sector = InternationalSectorPageFactory(
        parent=guide_landing_page,
        slug='sector'
    )

    sub_sector = InternationalSubSectorPageFactory(
        parent=sector,
        heading='sub_sector_heading',
        slug='sub_sector'
    )

    related_sub_sector = InvestmentOpportunityRelatedSubSectors(
        related_sub_sector=sub_sector
    )

    opportunity = InvestmentOpportunityPageFactory(
        parent=international_root_page,
        slug='opp',
        related_sub_sectors=[related_sub_sector]
    )

    opportunity_serializer = InvestmentOpportunityPageSerializer(
        instance=opportunity,
        context={'request': rf.get('/')}
    )

    for sub_sector in opportunity_serializer.data['sub_sectors']:
        assert sub_sector == 'sub_sector_heading'


@pytest.mark.django_db
def test_atlas_opportunity_page_can_add_sub_sector_as_related__null_case(rf, international_root_page):

    related_sub_sector = InvestmentOpportunityRelatedSubSectors()

    opportunity = InvestmentOpportunityPageFactory(
        parent=international_root_page,
        slug='opp',
        related_sub_sectors=[related_sub_sector]
    )

    opportunity_serializer = InvestmentOpportunityPageSerializer(
        instance=opportunity,
        context={'request': rf.get('/')}
    )

    assert opportunity_serializer.data['sub_sectors'] == ['']


@pytest.mark.django_db
def test_atlas_opportunity_listing_page_gets_opportunities(rf, international_root_page):

    opportunity_listing_page = InvestmentOpportunityListingPageFactory(
        parent=international_root_page,
        slug='opp-listing'
    )

    opportunity_page = InvestmentOpportunityPageFactory(
        parent=opportunity_listing_page,
        slug='opportunity'
    )

    opportunity_serializer = InvestmentOpportunityPageSerializer(
        instance=opportunity_page,
        context={'request': rf.get('/')}
    )

    opportunity_listing_serializer = InvestmentOpportunityListingPageSerializer(
        instance=opportunity_listing_page,
        context={'request': rf.get('/')}
    )

    assert opportunity_serializer.data['meta']['slug'] == 'opportunity'
    for opp in opportunity_listing_serializer.data['opportunity_list']:
        assert opp['meta']['slug'] == 'opportunity'


@pytest.mark.django_db
def test_atlas_opportunity_listing_page_gets_opportunities__null_case(rf, international_root_page):

    opportunity_listing_page = InvestmentOpportunityListingPageFactory(
        parent=international_root_page,
        slug='opp-listing'
    )

    opportunity_listing_serializer = InvestmentOpportunityListingPageSerializer(
        instance=opportunity_listing_page,
        context={'request': rf.get('/')}
    )

    assert opportunity_listing_serializer.data['opportunity_list'] == []


@pytest.mark.django_db
def test_atlas_opportunity_listing_page_gets_sectors_with_sub_sectors(rf, international_root_page):
    topic_landing_page = InternationalTopicLandingPageFactory(
        parent=international_root_page,
        slug='page-slug',
    )

    automotive_sector = InternationalSectorPageFactory(
        parent=topic_landing_page,
        slug='automotive'
    )
    InternationalSectorPageSerializer(
        instance=automotive_sector,
        context={'request': rf.get('/')}
    )

    real_estate_sector = InternationalSectorPageFactory(
        parent=topic_landing_page,
        slug='real-estate'
    )
    InternationalSectorPageSerializer(
        instance=real_estate_sector,
        context={'request': rf.get('/')}
    )

    housing_sub_sector = InternationalSubSectorPageFactory(
        parent=real_estate_sector,
        heading='Housing',
        slug='housing'
    )
    BaseInternationalSectorPageSerializer(
        instance=housing_sub_sector,
        context={'request': rf.get('/')}
    )

    mixed_use_sub_sector = InternationalSubSectorPageFactory(
        parent=automotive_sector,
        heading='Mixed Use',
        slug='mixed-use'
    )
    BaseInternationalSectorPageSerializer(
        instance=mixed_use_sub_sector,
        context={'request': rf.get('/')}
    )

    energy_sub_sector = InternationalSubSectorPageFactory(
        parent=automotive_sector,
        heading='Energy',
        slug='energy'
    )
    BaseInternationalSectorPageSerializer(
        instance=energy_sub_sector,
        context={'request': rf.get('/')}
    )

    opportunity_listing_page = InvestmentOpportunityListingPageFactory(
        parent=international_root_page,
        slug='opp-listing'
    )

    opportunity_listing_serializer = InvestmentOpportunityListingPageSerializer(
        instance=opportunity_listing_page,
        context={'request': rf.get('/')}
    )

    assert len(
        opportunity_listing_serializer.data['sector_with_sub_sectors']) == 2

    all_sub_sectors = [
        sub_sector for sub_sectors in opportunity_listing_serializer
        .data['sector_with_sub_sectors'].values() for sub_sector in sub_sectors
    ]

    assert len(all_sub_sectors) == 3


@pytest.mark.django_db
def test_atlas_opportunity_listing_page_serializer__get_hero_image():

    serializer = InvestmentOpportunityForListPageSerializer()

    mock_instance = mock.Mock()
    mock_image_block_1 = mock.Mock()
    mock_image_block_1.block.get_api_representation.return_value = 'http://example.com/image.jpg'
    mock_image_block_2 = mock.Mock()
    mock_image_block_2.block.get_api_representation.side_effect = Exception('Should not be called!')
    mock_instance.featured_images = [mock_image_block_1, mock_image_block_2]

    output = serializer.get_hero_image(mock_instance)
    assert output == 'http://example.com/image.jpg'


@pytest.mark.django_db
def test_atlas_related_investment_opportunity_page_serializer__get_thumbnail_image():
    serializer = RelatedInvestmentOpportunityPageSerializer()

    mock_instance = mock.Mock()
    mock_image_block_1 = mock.Mock()
    mock_image_block_1.block.get_api_representation.return_value = 'http://example.com/image.jpg'
    mock_image_block_2 = mock.Mock()
    mock_image_block_2.block.get_api_representation.side_effect = Exception('Should not be called!')
    mock_instance.featured_images = [mock_image_block_1, mock_image_block_2]

    output = serializer.get_thumbnail_image(mock_instance)
    assert output == 'http://example.com/image.jpg'


@pytest.mark.django_db
def test_atlas_opportunity_page_serializer__get_planning_status(
    rf,
    international_root_page,
):

    planning_status = PlanningStatusFactory(
        name="Planning Status One",
        verbose_description="Verbose description for the first planning status type"
    )
    opportunity = InvestmentOpportunityPageFactory(
        parent=international_root_page,
        slug='opp_one',
        planning_status=planning_status,
    )
    opportunity_serializer = InvestmentOpportunityPageSerializer(
        instance=opportunity,
        context={'request': rf.get('/')}
    )
    assert opportunity_serializer.data['planning_status'] == dict(
        name="Planning Status One",
        verbose_description="Verbose description for the first planning status type"
    )


@pytest.mark.django_db
def test_atlas_opportunity_page_serializer__get_planning_status__is_null(
    rf,
    international_root_page,
):

    opportunity = InvestmentOpportunityPageFactory(
        parent=international_root_page,
        slug='opp_one',
        planning_status=None,  # deliberately None, so the factory doesn't add one
    )
    opportunity_serializer = InvestmentOpportunityPageSerializer(
        instance=opportunity,
        context={'request': rf.get('/')}
    )
    assert opportunity_serializer.data['planning_status'] == dict()


@pytest.mark.django_db
def test_atlas_opportunity_listing_page_serializer__planning_status__is_not_verbose(
    international_root_page,
):

    planning_status = PlanningStatusFactory(
        name="Planning Status One",
        verbose_description="Verbose description for the first planning status type"
    )
    opportunity = InvestmentOpportunityPageFactory(
        parent=international_root_page,
        slug='opp_one',
        planning_status=planning_status,
    )

    opportunity_for_list_serializer = InvestmentOpportunityForListPageSerializer(
        instance=opportunity
    )
    assert opportunity_for_list_serializer.data['planning_status'] == 'Planning Status One'
