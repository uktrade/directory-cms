import json
import pytest

from django.conf import settings
from django.core.files.temp import NamedTemporaryFile
from django.core.files import File

from great_international.serializers import (
    InternationalArticlePageSerializer,
    InternationalCampaignPageSerializer,
    InternationalHomePageSerializer,
    AboutUkRegionPageSerializer,
    ForeignDirectInvestmentFormPageSerializer,
    ForeignDirectInvestmentFormSuccessPageSerializer,
    AboutDitServicesPageSerializer,
    AboutUkRegionListingPageSerializer,
    InvestmentOpportunityPageSerializer,
    InvestmentOpportunityListingPageSerializer,
    InvestmentOpportunityForListPageSerializer,
    InternationalInvestmentSectorPageSerializer,
    InternationalInvestmentSubSectorPageSerializer,
)
from tests.core.helpers import make_test_video
from tests.great_international.factories import (
    InternationalArticlePageFactory,
    InternationalCampaignPageFactory,
    InternationalHomePageFactory,
    AboutUkRegionPageFactory,
    ForeignDirectInvestmentFormPageFactory,
    ForeignDirectInvestmentFormSuccessPageFactory,
    InternationalTopicLandingPageFactory,
    AboutDitServicesPageFactory,
    AboutUkRegionListingPageFactory,
    InvestmentOpportunityPageFactory,
    InvestmentOpportunityRelatedSectorsFactory,
    InvestmentOpportunityListingPageFactory,
    PlanningStatusFactory,
    InvestmentTypeFactory,
    InternationalInvestmentSectorPageFactory,
    InternationalInvestmentSubSectorPageFactory
)

from great_international.models.great_international import (
    AboutDitServicesFields,
    InternationalInvestmentSectorPage,
)
from great_international.models.investment_atlas import (
    InvestmentOpportunityPage,
    InvestmentOpportunityRelatedSubSectors,
)


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
def test_about_uk_region_page_has_related_opportunities(international_root_page, rf):
    region_1 = AboutUkRegionPageFactory(
        slug='region-1-slug',
        hero_title="Region 1",
        parent=international_root_page
    )
    region_2 = AboutUkRegionPageFactory(
        slug='region-2-slug',
        hero_title="Region 2",
        parent=international_root_page
    )
    region_3 = AboutUkRegionPageFactory(
        slug='region-3-slug',
        hero_title="Region 2",
        parent=international_root_page
    )

    opp_1 = InvestmentOpportunityPageFactory(
        slug='opp_1',
        title='opp_1',
        parent=international_root_page
    )
    opp_2 = InvestmentOpportunityPageFactory(
        slug='opp_2',
        title='opp_2',
        parent=international_root_page
    )
    opp_3 = InvestmentOpportunityPageFactory(
        slug='opp_3',
        title='opp_3',
        priority_weighting='9',  # should come first in a list
        parent=international_root_page
    )
    opp_4 = InvestmentOpportunityPageFactory(
        slug='opp_4',
        title='opp_4',
        parent=international_root_page
    )
    opp_5 = InvestmentOpportunityPageFactory(
        slug='opp_5',
        title='opp_5',
        parent=international_root_page
    )
    opp_6 = InvestmentOpportunityPageFactory(
        slug='opp_6',
        title='opp_6',
        parent=international_root_page
    )
    opp_7 = InvestmentOpportunityPageFactory(
        slug='opp_7',
        title='opp_7',
        parent=international_root_page
    )

    opp_1.regions_with_locations = json.dumps(
        [
            {
                "type": "location",
                "value": {
                    "region": region_1.id,
                    "map_coordinate": "0,0"
                }
            },
            {
                "type": "location",
                "value": {
                    "region": region_2.id,
                    "map_coordinate": "0,0"
                }
            }

        ]
    )

    opp_2.regions_with_locations = json.dumps(
        [
            {
                "type": "location",
                "value": {
                    "region": region_1.id,
                    "map_coordinate": "0,0"
                }
            }
        ]
    )
    opp_3.regions_with_locations = json.dumps(
        [
            {
                "type": "location",
                "value": {
                    "region": region_2.id,
                    "map_coordinate": "0,0"
                }
            }
        ]
    )
    opp_4.regions_with_locations = json.dumps(
        [
            {
                "type": "location",
                "value": {
                    "region": region_1.id,
                    "map_coordinate": "0,0"
                }
            }
        ]
    )
    opp_5.regions_with_locations = json.dumps(
        [
            {
                "type": "location",
                "value": {
                    "region": region_1.id,
                    "map_coordinate": "0,0"
                }
            }
        ]
    )
    opp_6.regions_with_locations = json.dumps(
        [
            {
                "type": "location",
                "value": {
                    "region": region_1.id,
                    "map_coordinate": "0,0"
                }
            }
        ]
    )
    opp_7.regions_with_locations = json.dumps(
        [
            {
                "type": "location",
                "value": {
                    "region": region_1.id,
                    "map_coordinate": "0,0"
                }
            }
        ]
    )

    opp_1.save()
    opp_2.save()
    opp_3.save()
    opp_4.save()
    opp_5.save()
    opp_6.save()
    opp_7.save()

    def _get_regions(opp_instance):
        return [item.value['region'] for item in opp_instance.regions_with_locations]

    assert len(_get_regions(opp_1)) == 2
    assert len(_get_regions(opp_2)) == 1
    assert len(_get_regions(opp_3)) == 1
    assert len(_get_regions(opp_4)) == 1
    assert len(_get_regions(opp_5)) == 1
    assert len(_get_regions(opp_6)) == 1
    assert len(_get_regions(opp_7)) == 1

    region_1_serializer = AboutUkRegionPageSerializer(
        instance=region_1,
        context={'request': rf.get('/')}
    )
    region_1_related_opportunities = region_1_serializer.data['related_opportunities']

    assert len(region_1_related_opportunities) == 3
    assert [x['meta']['slug'] for x in region_1_related_opportunities] == [
        'opp_7',  # newest with default priority
        'opp_6',  # next newest with default priority
        'opp_5',  # next newest with default priority
    ]

    region_2_serializer = AboutUkRegionPageSerializer(
        instance=region_2,
        context={'request': rf.get('/')}
    )
    region_2_related_opportunities = region_2_serializer.data['related_opportunities']
    assert len(region_2_related_opportunities) == 2
    assert [x['meta']['slug'] for x in region_2_related_opportunities] == [
        'opp_3',  # higher pri than opp_1
        'opp_1',
    ]

    region_3_serializer = AboutUkRegionPageSerializer(
        instance=region_3,
        context={'request': rf.get('/')}
    )
    region_3_related_opportunities = region_3_serializer.data['related_opportunities']
    assert len(region_3_related_opportunities) == 0


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
def test_about_uk_region_listing_page_has_regions(rf, international_root_page):
    scotland = AboutUkRegionPageFactory(
        slug="scotland",
        featured_description="Scotland lorem ipsum",
        parent=international_root_page
    )

    midlands = AboutUkRegionPageFactory(
        slug="midlands",
        featured_description="Midlands lorem ipsum",
        parent=international_root_page
    )

    regions = AboutUkRegionListingPageFactory(
        slug='regions',
        parent=international_root_page
    )

    serializer = AboutUkRegionListingPageSerializer(
        instance=regions,
        context={'request': rf.get('/')}
    )

    assert len(serializer.data['mapped_regions']) == 2
    for field in serializer.data['mapped_regions']:
        assert 'region' in field
        assert 'text' in field

    scotland_image_path_stub = scotland.hero_image.file.name.replace('.jpg', '').replace('original_', '/media/')
    midlands_image_path_stub = midlands.hero_image.file.name.replace('.jpg', '').replace('original_', '/media/')

    assert serializer.data['mapped_regions'][0]['text'] == 'Scotland lorem ipsum'
    assert serializer.data['mapped_regions'][0]['region']['meta']['slug'] == 'scotland'
    assert scotland_image_path_stub in serializer.data['mapped_regions'][0]['region']['hero_image_thumbnail']['url']
    assert serializer.data['mapped_regions'][1]['text'] == 'Midlands lorem ipsum'
    assert serializer.data['mapped_regions'][1]['region']['meta']['slug'] == 'midlands'
    assert midlands_image_path_stub in serializer.data['mapped_regions'][1]['region']['hero_image_thumbnail']['url']


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
def test_international_homepage_serializer(rf, international_root_page, image):
    home_page = InternationalHomePageFactory(
        slug='international',
        parent=international_root_page,  # This is tautological, but irrelevant here
    )
    home_page.hero_subtitle = "THIS LEGACY FIELD SHOULD NOT BE USED"
    fake_video = make_test_video(duration=70, transcript='Test transcript note')
    with NamedTemporaryFile(delete=True) as img_tmp:
        fake_video.thumbnail.save('test.jpg', File(img_tmp))
        fake_video.save()
    home_page.hero_video = fake_video
    home_page.hero_video.save()

    home_page.homepage_link_panels = [
        (
            'link_panel',
            {
                'title': 'panel one',
                'supporting_text': 'panel one supporting text',
                'link': {
                    'internal_link': home_page,  # Circular link but doesn't matter in this test
                }
            }
        ),
        (
            'link_panel',
            {
                'title': 'panel two',
                'supporting_text': 'panel two supporting text',
                'link': {
                    'external_link': 'http://example.com/two/',
                }
            }
        ),
    ]
    home_page.save()

    assert home_page.hero_subtitle is not None

    serializer = InternationalHomePageSerializer(
        instance=home_page,
        context={'request': rf.get('/')}
    )

    assert serializer.data['hero_title'] == home_page.hero_title
    homepage_link_panels = serializer.data['homepage_link_panels']
    assert homepage_link_panels[0]['type'] == 'link_panel'
    assert homepage_link_panels[0]['value'] == {
        'title': 'panel one',
        'supporting_text': 'panel one supporting text',
        'link': home_page.url,
    }
    assert homepage_link_panels[1]['type'] == 'link_panel'
    assert homepage_link_panels[1]['value'] == {
        'title': 'panel two',
        'supporting_text': 'panel two supporting text',
        'link': 'http://example.com/two/',
    }
    assert serializer.data['hero_video']['title'] == 'Test file'
    assert serializer.data['hero_video']['transcript'] == 'Test transcript note'
    assert serializer.data['hero_video']['thumbnail'] == fake_video.thumbnail.url
    assert serializer.data['hero_video']['sources'][0]['src'] == fake_video.url

    # confirm the legacy fields are not exposed:
    for example_field_name in [
        'hero_subtitle',
        'hero_cta_text',
        'hero_cta_link',
        'hero_image',
        'brexit_banner_text',
        'invest_title',
        'invest_content',
        'invest_image',
        # there are more, but these are useful smoke tests
        'case_study_image',
        'case_study_title',
        'case_study_text',
        'case_study_cta_text',
        'case_study_cta_link',
    ]:
        assert example_field_name not in serializer.data


# Investment Atlas Serializer tests

@pytest.mark.django_db
def test_atlas_opportunity_page_can_add_sector_as_related(rf, international_root_page):
    # Based on test_opportunity_page_can_add_sector_as_related

    topic_landing_page = InternationalTopicLandingPageFactory(
        parent=international_root_page,
        slug='page-slug',
    )

    sector = InternationalInvestmentSectorPageFactory(
        parent=topic_landing_page,
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
    # Unlike with the old CapInvest opps, Atlas ones are associated by Sector.
    # Regions and Sub-sector do not matter

    # make a landing page
    topic_landing_page = InternationalTopicLandingPageFactory(
        parent=international_root_page,
        slug='page-slug',
    )

    # set up some sectors and subsectors, to help show they don't influence results
    sector_a = InternationalInvestmentSectorPageFactory(
        parent=topic_landing_page,
        slug='sectorA'
    )
    sector_b = InternationalInvestmentSectorPageFactory(
        parent=topic_landing_page,
        slug='sectorB'
    )
    sector_c = InternationalInvestmentSectorPageFactory(
        parent=topic_landing_page,
        slug='sectorC'
    )
    subsector_a1 = InternationalInvestmentSubSectorPageFactory(
        parent=sector_a,
        heading='sub_sector_a1_heading',
        slug='sub_sector_a1'
    )
    subsector_b2 = InternationalInvestmentSubSectorPageFactory(
        parent=sector_b,
        heading='sub_sector_b2_heading',
        slug='sub_sector_b2'
    )
    subsector_b3 = InternationalInvestmentSubSectorPageFactory(
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

    related_subsector_a1 = InvestmentOpportunityRelatedSubSectors(
        related_sub_sector=subsector_a1
    )

    related_subsector_b2 = InvestmentOpportunityRelatedSubSectors(
        related_sub_sector=subsector_b2
    )

    related_subsector_b3 = InvestmentOpportunityRelatedSubSectors(
        related_sub_sector=subsector_b3
    )

    # Make eight opportunities:
    # 1. Sector A, Subsector A1 -> Related to Sector A, show show for sector A
    # 2. Sector A, no subsector -> Related to Sector A, show show for sector A
    # 3. Sector B, Subsector B2 -> Related to Sector B, show show for sector B
    # 4. Sector B, Subsector B3 -> Related to Sector B, show show for sector B
    # 5. Sector A, -> Related to Sector A, show show for sector A
    # 6. Sector A, Subsector A1 -> Related to Sector A, show show for sector A
    # 7. Sector C -> Related to Sector C, show show for sector C
    # 8. Sector C -> Related to Sector C, show show for sector C
    # 9. Sector C -> Related to Sector C, show show for sector A
    # 10 with no sector -> No related to any sector - shouldnt shown

    # Also note that priority_weighting is used here to order which ones are shown first

    # 1. Sector A, Subsector A1 -> Related to Sector A, show show for sector A
    opportunity_1 = InvestmentOpportunityPageFactory(
        parent=international_root_page,
        slug='opp_one',
        related_sectors=[InvestmentOpportunityRelatedSectorsFactory(related_sector=sector_a)],
        related_sub_sectors=[related_subsector_a1],
        priority_weighting="0.9"
    )
    opportunity_1.regions_with_locations = json.dumps(
        [
            {
                "type": "location",
                "value": {
                    "region": region_a.id,
                    "map_coordinate": "0,0"
                }
            }
        ]
    )
    opportunity_1.save()

    # 2. Sector A, no subsector -> Related to Sector A, show show for sector A
    opportunity_2 = InvestmentOpportunityPageFactory(
        parent=international_root_page,
        slug='opp_two',
        related_sectors=[InvestmentOpportunityRelatedSectorsFactory(related_sector=sector_a)],
        related_sub_sectors=[],
        priority_weighting="1.0"
    )
    opportunity_2.regions_with_locations = json.dumps(
        [
            {
                "type": "location",
                "value": {
                    "region": region_a.id,
                    "map_coordinate": "0,0"
                }
            }
        ]
    )
    opportunity_2.save()

    # 3. Sector B, Subsector B2 -> Related to Sector B, show show for sector B
    opportunity_3 = InvestmentOpportunityPageFactory(
        parent=international_root_page,
        slug='opp_three',
        related_sectors=[InvestmentOpportunityRelatedSectorsFactory(related_sector=sector_b)],
        related_sub_sectors=[related_subsector_b2],
        priority_weighting="2.0"
    )

    opportunity_3.regions_with_locations = json.dumps(
        [
            {
                "type": "location",
                "value": {
                    "region": region_a.id,
                    "map_coordinate": "0,0"
                }
            }
        ]
    )
    opportunity_3.save()

    # 4. Sector B, Subsector B3 -> Related to Sector B, show show for sector B
    opportunity_4 = InvestmentOpportunityPageFactory(
        parent=international_root_page,
        slug='opp_four',
        related_sectors=[InvestmentOpportunityRelatedSectorsFactory(related_sector=sector_b)],
        related_sub_sectors=[related_subsector_b3],
        priority_weighting="1.5"
    )
    opportunity_4.regions_with_locations = json.dumps(
        [
            {
                "type": "location",
                "value": {
                    "region": region_a.id,
                    "map_coordinate": "0,0"
                }
            }
        ]
    )
    opportunity_4.save()

    # 5. Sector A, -> Related to Sector A, show show for sector A
    opportunity_5 = InvestmentOpportunityPageFactory(
        parent=international_root_page,
        slug='opp_five',
        related_sectors=[InvestmentOpportunityRelatedSectorsFactory(related_sector=sector_a)],
        related_sub_sectors=[],
        priority_weighting="4.2"
    )
    opportunity_5.regions_with_locations = json.dumps(
        [
            {
                "type": "location",
                "value": {
                    "region": region_b.id,
                    "map_coordinate": "0,0"
                }
            }
        ]
    )
    opportunity_5.save()

    # 6. Sector A, Subsector A1 -> Related to Sector A, show show for sector A
    opportunity_6 = InvestmentOpportunityPageFactory(
        parent=international_root_page,
        slug='opp_six',
        related_sectors=[InvestmentOpportunityRelatedSectorsFactory(related_sector=sector_a)],
        related_sub_sectors=[related_subsector_a1],
        priority_weighting="6.2"
    )
    opportunity_6.regions_with_locations = json.dumps(
        [
            {
                "type": "location",
                "value": {
                    "region": region_b.id,
                    "map_coordinate": "0,0"
                }
            }
        ]
    )
    opportunity_6.save()

    # 7. Sector C -> Related to Sector C, show show for sector C
    opportunity_7 = InvestmentOpportunityPageFactory(
        parent=international_root_page,
        slug='opp_seven',
        related_sectors=[InvestmentOpportunityRelatedSectorsFactory(related_sector=sector_c)],
        related_sub_sectors=[],
        priority_weighting="7.2"

    )

    opportunity_7.regions_with_locations = json.dumps(
        [
            {
                "type": "location",
                "value": {
                    "region": region_c.id,
                    "map_coordinate": "0,0"
                }
            }
        ]
    )
    opportunity_7.save()

    # 8. Sector C -> Related to Sector C, show show for sector C
    opportunity_8 = InvestmentOpportunityPageFactory(
        parent=international_root_page,
        slug='opp_eight',
        related_sectors=[InvestmentOpportunityRelatedSectorsFactory(related_sector=sector_c)],
        related_sub_sectors=[],
        priority_weighting="5.2"
    )

    opportunity_8.regions_with_locations = json.dumps(
        [
            {
                "type": "location",
                "value": {
                    "region": region_c.id,
                    "map_coordinate": "0,0"
                }
            }
        ]
    )
    opportunity_8.save()

    # 9. Sector C -> Related to Sector C, show show for sector A
    opportunity_9 = InvestmentOpportunityPageFactory(
        parent=international_root_page,
        slug='opp_nine',
        related_sectors=[InvestmentOpportunityRelatedSectorsFactory(related_sector=sector_c)],
        related_sub_sectors=[]
        # Has default priority_wieghting (ie, 0.0)
    )
    opportunity_9.regions_with_locations = json.dumps(
        [
            {
                "type": "location",
                "value": {
                    "region": region_a.id,
                    "map_coordinate": "0,0"
                }
            },
            {
                "type": "location",
                "value": {
                    "region": region_c.id,
                    "map_coordinate": "0,0"
                }
            }
        ]
    )
    opportunity_9.save()

    # 10 with no sector -> No related to any sector - shouldnt shown
    opportunity_10 = InvestmentOpportunityPageFactory(
        parent=international_root_page,
        slug='opp_nine',
        related_sectors=[],
        related_sub_sectors=[]
        # Has default priority_wieghting (ie, 0.0)
    )
    opportunity_10.regions_with_locations = json.dumps(
        [
            {
                "type": "location",
                "value": {
                    "region": region_a.id,
                    "map_coordinate": "0,0"
                }
            },
            {
                "type": "location",
                "value": {
                    "region": region_c.id,
                    "map_coordinate": "0,0"
                }
            }
        ]
    )
    opportunity_10.save()

    # now grab the results for the opp
    opportunity_1_serializer = InvestmentOpportunityPageSerializer(
        instance=opportunity_1,
        context={'request': rf.get('/')}
    )

    expected_slugs = [
        x.slug for x in [
            # these are ordered by priority
            opportunity_2,
            opportunity_5,
            opportunity_6,
        ]
    ]

    unexpected_slugs = [
        x.slug for x in [
            # priority doesn't matter here, because we're testing for absence
            opportunity_1,
            opportunity_3,
            opportunity_4,
            opportunity_7,
            opportunity_8,
            opportunity_9,
            opportunity_10,
        ]
    ]

    seen_slugs = []

    for idx, page in enumerate(opportunity_1_serializer.data['related_opportunities']):
        slug = page['meta']['slug']
        expected_slugs[idx] == slug  # ie, ordering check
        assert slug not in unexpected_slugs
        assert slug not in seen_slugs
        seen_slugs.append(slug)

    assert sorted(seen_slugs) == sorted(expected_slugs)

    # Also show the number of related opps varies according to mutual sectors
    # 1. Sector A, Subsector A1 -> Related to Sector A, show show for sector A
    # 2. Sector A, no subsector -> Related to Sector A, show show for sector A
    # 3. Sector B, Subsector B2 -> Related to Sector B, show show for sector B
    # 4. Sector B, Subsector B3 -> Related to Sector B, show show for sector B
    # 5. Sector A, -> Related to Sector A, show show for sector A
    # 6. Sector A, Subsector A1 -> Related to Sector A, show show for sector A
    # 7. Sector C -> Related to Sector C, show show for sector C
    # 8. Sector C -> Related to Sector C, show show for sector C
    # 9. Sector C -> Related to Sector C, show show for sector A
    # 10 with no sector -> No related to any sector - shouldnt shown

    # Expected related_opps
    # Sector A - 3 Related opps
    # Sector B - 1 Related opp
    # Sector C - 2 Related opps

    # Each Sector A Opps should link to three other
    for sector_a_opp in [opportunity_5, opportunity_6]:
        serializer = InvestmentOpportunityPageSerializer(
            instance=sector_a_opp,
            context={'request': rf.get('/')}
        )
        assert len(serializer.data['related_opportunities']) == 3
        assert sector_a_opp.slug not in [x['meta']['slug'] for x in serializer.data['related_opportunities']]

    # These Sector C Opps should link to two others
    for sector_c_opp in [opportunity_7, opportunity_8, opportunity_9]:
        serializer = InvestmentOpportunityPageSerializer(
            instance=sector_c_opp,
            context={'request': rf.get('/')}
        )
        assert len(serializer.data['related_opportunities']) == 2
        assert sector_c_opp.slug not in [x['meta']['slug'] for x in serializer.data['related_opportunities']]

    # And this sector C opp shoud link to 2 in total
    serializer = InvestmentOpportunityPageSerializer(
        instance=opportunity_9,
        context={'request': rf.get('/')}
    )
    assert len(serializer.data['related_opportunities']) == 2
    assert opportunity_9.slug not in [x['meta']['slug'] for x in serializer.data['related_opportunities']]

    # And opportunity with no sector  shoud link to 0 in total
    serializer = InvestmentOpportunityPageSerializer(
        instance=opportunity_10,
        context={'request': rf.get('/')}
    )
    assert len(serializer.data['related_opportunities']) == 0
    assert opportunity_10.slug not in [x['meta']['slug'] for x in serializer.data['related_opportunities']]


@pytest.mark.django_db
def test_atlas_opportunity_list_page_related_opportunities__no_opportunities(rf, international_root_page):
    opportunity = InvestmentOpportunityPageFactory(
        parent=international_root_page,
        slug='opp_one',
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
    topic_landing_page = InternationalTopicLandingPageFactory(
        parent=international_root_page,
        slug='page-slug',
    )

    sector = InternationalInvestmentSectorPageFactory(
        parent=topic_landing_page,
        slug='sector'
    )

    sub_sector = InternationalInvestmentSubSectorPageFactory(
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

    automotive_sector = InternationalInvestmentSectorPageFactory(
        parent=topic_landing_page,
        slug='automotive'
    )
    InternationalInvestmentSectorPageSerializer(
        instance=automotive_sector,
        context={'request': rf.get('/')}
    )

    real_estate_sector = InternationalInvestmentSectorPageFactory(
        parent=topic_landing_page,
        slug='real-estate'
    )
    InternationalInvestmentSectorPageSerializer(
        instance=real_estate_sector,
        context={'request': rf.get('/')}
    )

    housing_sub_sector = InternationalInvestmentSubSectorPageFactory(
        parent=real_estate_sector,
        heading='Housing',
        slug='housing'
    )
    InternationalInvestmentSubSectorPageSerializer(
        instance=housing_sub_sector,
        context={'request': rf.get('/')}
    )

    mixed_use_sub_sector = InternationalInvestmentSubSectorPageFactory(
        parent=automotive_sector,
        heading='Mixed Use',
        slug='mixed-use'
    )
    InternationalInvestmentSubSectorPageSerializer(
        instance=mixed_use_sub_sector,
        context={'request': rf.get('/')}
    )

    energy_sub_sector = InternationalInvestmentSubSectorPageFactory(
        parent=automotive_sector,
        heading='Energy',
        slug='energy'
    )
    InternationalInvestmentSubSectorPageSerializer(
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
        sub_sector for sub_sectors in
        opportunity_listing_serializer.data['sector_with_sub_sectors'].values() for sub_sector in sub_sectors
    ]

    assert len(all_sub_sectors) == 3


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


@pytest.mark.django_db
def test_atlas_opportunity_listing_page_serializer__planning_status__is_none(
        international_root_page,
):
    planning_status = None
    opportunity = InvestmentOpportunityPageFactory(
        parent=international_root_page,
        slug='opp_one',
        planning_status=planning_status,
    )

    opportunity_for_list_serializer = InvestmentOpportunityForListPageSerializer(
        instance=opportunity
    )
    assert opportunity_for_list_serializer.data['planning_status'] is None


@pytest.fixture
def sector_pages_with_related_opportunities(international_root_page):
    # make a landing page
    topic_landing_page = InternationalTopicLandingPageFactory(
        parent=international_root_page,
        slug='page-slug',
    )

    # Add three Sector Pages, one will have no opportunities associated with it
    sector_a = InternationalInvestmentSectorPageFactory(
        parent=topic_landing_page,
        slug='sectorA'
    )
    InternationalInvestmentSectorPageFactory(
        parent=topic_landing_page,
        slug='sectorB'
    )
    sector_c = InternationalInvestmentSectorPageFactory(
        parent=topic_landing_page,
        slug='sectorC'
    )

    # Add six opportunities, map four to SectorA, none to SectorB, two to SectorC
    InvestmentOpportunityPageFactory(
        parent=international_root_page,
        slug='opp_1',
        related_sectors=[InvestmentOpportunityRelatedSectorsFactory(related_sector=sector_a)],
        related_sub_sectors=[],
        priority_weighting="0.0"
    )

    InvestmentOpportunityPageFactory(
        parent=international_root_page,
        slug='opp_2',
        related_sectors=[InvestmentOpportunityRelatedSectorsFactory(related_sector=sector_a)],
        related_sub_sectors=[],
        priority_weighting="0.0"
    )

    InvestmentOpportunityPageFactory(
        parent=international_root_page,
        slug='opp_3',
        related_sectors=[InvestmentOpportunityRelatedSectorsFactory(related_sector=sector_a)],
        related_sub_sectors=[],
        priority_weighting="100"  # Note, highest weighting
    )

    InvestmentOpportunityPageFactory(
        parent=international_root_page,
        slug='opp_4',
        related_sectors=[InvestmentOpportunityRelatedSectorsFactory(related_sector=sector_a)],
        related_sub_sectors=[],
        priority_weighting="10.1"
    )

    InvestmentOpportunityPageFactory(
        parent=international_root_page,
        slug='opp_5',
        related_sectors=[InvestmentOpportunityRelatedSectorsFactory(related_sector=sector_c)],
        related_sub_sectors=[],
        priority_weighting="0.0"
    )

    InvestmentOpportunityPageFactory(
        parent=international_root_page,
        slug='opp_6',
        related_sectors=[InvestmentOpportunityRelatedSectorsFactory(related_sector=sector_c)],
        related_sub_sectors=[],
        priority_weighting="1.0"
    )


@pytest.mark.django_db
def test_international_investment_sector_page_serializer__get_related_opportunities__manually_selected(
        sector_pages_with_related_opportunities
):
    sector_a = InternationalInvestmentSectorPage.objects.get(slug='sectorA')
    sector_b = InternationalInvestmentSectorPage.objects.get(slug='sectorB')

    opp_1 = InvestmentOpportunityPage.objects.get(slug='opp_1')
    opp_2 = InvestmentOpportunityPage.objects.get(slug='opp_2')
    opp_3 = InvestmentOpportunityPage.objects.get(slug='opp_3')
    opp_5 = InvestmentOpportunityPage.objects.get(slug='opp_5')

    # manually spec some related_opportunities. NB: doesn't enforce that their sectors match - nice-to-do
    sector_a.manually_selected_related_opportunities = [
        ('related_opportunity', opp_5),
        ('related_opportunity', opp_1),
        ('related_opportunity', opp_3),
    ]
    sector_a.save()

    sector_b.manually_selected_related_opportunities = [
        ('related_opportunity', opp_2),
        ('related_opportunity', opp_1),
    ]
    sector_b.save()

    serialized_sector_a = InternationalInvestmentSectorPageSerializer(sector_a)
    serialized_sector_b = InternationalInvestmentSectorPageSerializer(sector_b)

    assert len(serialized_sector_a.data['related_opportunities']) == 3

    assert [x['meta']['slug'] for x in serialized_sector_a.data['related_opportunities']] == [
        'opp_5',
        'opp_1',
        'opp_3',
    ]

    assert len(serialized_sector_b.data['related_opportunities']) == 2

    assert [x['meta']['slug'] for x in serialized_sector_b.data['related_opportunities']] == [
        'opp_2',
        'opp_1',
    ]

    # sector C has none manually configured but two auto-associated, covered in the test below


@pytest.mark.django_db
def test_international_investment_sector_page_serializer__get_related_opportunities__auto_selected(
        sector_pages_with_related_opportunities
):
    sector_a = InternationalInvestmentSectorPage.objects.get(slug='sectorA')
    sector_b = InternationalInvestmentSectorPage.objects.get(slug='sectorB')
    sector_c = InternationalInvestmentSectorPage.objects.get(slug='sectorC')

    serialized_sector_a = InternationalInvestmentSectorPageSerializer(sector_a)
    serialized_sector_b = InternationalInvestmentSectorPageSerializer(sector_b)
    serialized_sector_c = InternationalInvestmentSectorPageSerializer(sector_c)

    assert len(serialized_sector_a.data['related_opportunities']) == 3  # even though four are configured, limited to 3
    assert [x['meta']['slug'] for x in serialized_sector_a.data['related_opportunities']] == [
        'opp_3',  # highest weighted
        'opp_4',  # next highest weighted
        'opp_2',  # no weighting, but newer than opp_1
    ]

    assert len(serialized_sector_b.data['related_opportunities']) == 0  # none configured
    assert [x['meta']['slug'] for x in serialized_sector_b.data['related_opportunities']] == []

    assert len(serialized_sector_c.data['related_opportunities']) == 2
    assert [x['meta']['slug'] for x in serialized_sector_c.data['related_opportunities']] == [
        'opp_6',
        'opp_5',
    ]


def make_fdi_opportunity_mix(international_root_page):
    # make a mix of opps, including some with FDIs

    fdi_type = InvestmentTypeFactory(
        name=settings.FOREIGN_DIRECT_INVESTMENT_SNIPPET_LABEL_DEFAULT
    )
    non_fdi_type = InvestmentTypeFactory(
        name=f'Not {settings.FOREIGN_DIRECT_INVESTMENT_SNIPPET_LABEL_DEFAULT}'
    )
    InvestmentOpportunityPageFactory(
        slug='opp_1__fdi',
        investment_type=fdi_type,
        parent=international_root_page
    )
    InvestmentOpportunityPageFactory(
        slug='opp_2__non_fdi',
        investment_type=non_fdi_type,
        parent=international_root_page
    )
    InvestmentOpportunityPageFactory(
        slug='opp_3__fdi',
        investment_type=fdi_type,
        parent=international_root_page
    )
    InvestmentOpportunityPageFactory(
        slug='opp_4__non_fdi',
        investment_type=non_fdi_type,
        parent=international_root_page
    )


@pytest.mark.django_db
def test_foreign_direct_investment_form_page_serializer(international_root_page):
    make_fdi_opportunity_mix(international_root_page)

    instance = ForeignDirectInvestmentFormPageFactory(
        parent=international_root_page
    )

    serializer = ForeignDirectInvestmentFormPageSerializer(
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

    assert len(serializer.data['opportunity_list']) == 2
    assert serializer.data['opportunity_list'][0]['meta']['slug'] == 'opp_1__fdi'
    assert serializer.data['opportunity_list'][1]['meta']['slug'] == 'opp_3__fdi'


@pytest.mark.django_db
def test_foreign_direct_investment_form_sucess_page_serializer(
        international_root_page,
):
    make_fdi_opportunity_mix(international_root_page)

    parent_form_page = ForeignDirectInvestmentFormPageFactory(
        parent=international_root_page
    )

    instance = ForeignDirectInvestmentFormSuccessPageFactory(
        parent=parent_form_page
    )

    serializer = ForeignDirectInvestmentFormSuccessPageSerializer(
        instance
    )

    assert len(serializer.data['opportunity_list']) == 2
    assert serializer.data['opportunity_list'][0]['meta']['slug'] == 'opp_1__fdi'
    assert serializer.data['opportunity_list'][1]['meta']['slug'] == 'opp_3__fdi'
