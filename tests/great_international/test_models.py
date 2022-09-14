import pytest
from wagtail.core.models import Page

from great_international.models import (
    capital_invest,
    find_a_supplier,
    great_international,
    investment_atlas,
)
from . import factories


@pytest.mark.django_db
def test_models_hierarchy():
    # homepage / app root
    assert great_international.InternationalHomePage.allowed_subpage_models() == [
        great_international.InternationalArticleListingPage,
        great_international.InternationalTopicLandingPage,
        investment_atlas.InvestmentAtlasLandingPage,
        find_a_supplier.InternationalTradeHomePage,
    ]
    assert great_international.InternationalHomePage.allowed_parent_page_models() == [Page]
    # topic landing
    assert great_international.InternationalTopicLandingPage.allowed_subpage_models() == [
            great_international.InternationalArticleListingPage,
            great_international.InternationalCampaignPage,
            great_international.InternationalInvestmentSectorPage,
        ]
    # article listing
    assert great_international.InternationalArticleListingPage.allowed_subpage_models() == [
            great_international.InternationalArticlePage,
            great_international.InternationalCampaignPage
        ]
    # campaign
    assert great_international.InternationalCampaignPage.allowed_subpage_models() == [
            great_international.InternationalArticlePage,
        ]
    assert capital_invest.CapitalInvestContactFormPage.allowed_subpage_models() == [
            capital_invest.CapitalInvestContactFormSuccessPage
        ]
    assert capital_invest.CapitalInvestContactFormSuccessPage.allowed_subpage_models() == []
    assert great_international.AboutUkRegionListingPage.allowed_subpage_models() == [
            great_international.AboutUkRegionPage
        ]
    assert great_international.AboutUkRegionPage.allowed_subpage_models() == []
    assert investment_atlas.ForeignDirectInvestmentFormPage.allowed_subpage_models() == [
        investment_atlas.ForeignDirectInvestmentFormSuccessPage,
    ]


@pytest.mark.django_db
def test_uses_tree_base_routing_always_true(international_root_page):
    page = factories.InternationalArticleListingPageFactory(
        parent=international_root_page
    )
    assert page.uses_tree_based_routing is True


@pytest.mark.django_db
def test_url_for_investment_opportunity_listing_page(international_root_page):
    atlas_home = factories.InvestmentAtlasLandingPageFactory(
        parent=international_root_page,
        slug='investment',
    )
    opportunities = factories.InvestmentOpportunityListingPageFactory(
        parent=atlas_home,
        slug='opportunities',
    )

    assert 'content' not in opportunities.url.split('/')
    assert opportunities.get_url() == 'http://great.gov.uk/international/investment/opportunities/'
    assert opportunities.url == 'http://great.gov.uk/international/investment/opportunities/'


@pytest.mark.django_db
def test_url_for_investment_atlas_landing_page(international_root_page):
    atlas_home = factories.InvestmentAtlasLandingPageFactory(
        parent=international_root_page,
        slug='investment',
    )
    assert 'content' not in atlas_home.url.split('/')
    assert atlas_home.get_url() == 'http://great.gov.uk/international/investment/'
    assert atlas_home.url == 'http://great.gov.uk/international/investment/'


@pytest.mark.django_db
def test_planning_status__str__method():
    # Just to keep coverage happy...

    planning_status = factories.PlanningStatusFactory(
        name="Planning Status One",
        verbose_description="Verbose description for the first planning status type"
    )

    assert f"{planning_status}" == "Planning Status One"


@pytest.mark.django_db
def test_reusable_content_snippet__str_method():
    snippet = factories.ReusableContentSectionFactory()
    # Quick coverage appeasement for the __str__ method
    assert f'{snippet}' == f'Reusable content: {snippet.title}'
