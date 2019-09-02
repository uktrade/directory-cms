import pytest
from wagtail.core.models import Page

from great_international.models import (
    great_international, invest, capital_invest, find_a_supplier
)
from . import factories
from tests.export_readiness import factories as exread_factories


def test_models_hierarchy():
    # homepage / app root
    assert great_international.InternationalHomePage.allowed_subpage_models() \
        == [
        great_international.InternationalArticleListingPage,
        great_international.InternationalTopicLandingPage,
        great_international.InternationalCuratedTopicLandingPage,
        great_international.InternationalGuideLandingPage,
        great_international.InternationalRegionPage,
        great_international.InternationalEUExitFormPage,
        great_international.InternationalEUExitFormSuccessPage,
        great_international.AboutDitLandingPage,
        great_international.AboutUkLandingPage,
        capital_invest.InternationalCapitalInvestLandingPage,
        capital_invest.CapitalInvestOpportunityListingPage,
        capital_invest.CapitalInvestRegionPage,
        invest.InvestInternationalHomePage,
        find_a_supplier.InternationalTradeHomePage
    ]
    assert invest.InvestInternationalHomePage.allowed_subpage_models() == [
        invest.InvestHighPotentialOpportunitiesPage,
        invest.InvestRegionLandingPage,
    ]
    assert invest.InvestHighPotentialOpportunitiesPage.allowed_subpage_models() == [
        invest.InvestHighPotentialOpportunityDetailPage,
        invest.InvestHighPotentialOpportunityFormPage,
    ]
    assert invest.InvestHighPotentialOpportunityFormPage.allowed_subpage_models() == [
        invest.InvestHighPotentialOpportunityFormSuccessPage,
    ]
    assert great_international.InternationalHomePage.allowed_parent_page_models() == [Page]
    # region page
    assert great_international.InternationalRegionPage.allowed_subpage_models() == []
    # regional folder page
    assert great_international.InternationalLocalisedFolderPage.allowed_subpage_models() == []
    # topic landing
    assert great_international.InternationalTopicLandingPage.allowed_subpage_models() == [
            great_international.InternationalArticleListingPage,
            great_international.InternationalCampaignPage,
            great_international.InternationalSectorPage,
        ]
    # curated topic landing
    assert great_international.InternationalCuratedTopicLandingPage.allowed_subpage_models() == []
    # guide landing
    assert great_international.InternationalGuideLandingPage.allowed_subpage_models() == [
            great_international.InternationalArticlePage,
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
    # EU Exit forms
    assert great_international.InternationalEUExitFormPage.allowed_subpage_models() == [
            great_international.InternationalEUExitFormSuccessPage,
        ]
    assert great_international.InternationalEUExitFormSuccessPage.allowed_parent_page_models() == [
            great_international.InternationalEUExitFormPage,
        ]
    assert capital_invest.InternationalCapitalInvestLandingPage.allowed_subpage_models() == [
            capital_invest.CapitalInvestContactFormPage,
        ]
    assert capital_invest.CapitalInvestOpportunityListingPage.allowed_subpage_models() == [
            capital_invest.CapitalInvestOpportunityPage,
        ]
    assert capital_invest.CapitalInvestContactFormPage.allowed_subpage_models() == [
            capital_invest.CapitalInvestContactFormSuccessPage
        ]
    assert capital_invest.CapitalInvestContactFormSuccessPage.allowed_subpage_models() == []
    assert great_international.InternationalSectorPage.allowed_subpage_models() == [
            great_international.InternationalSubSectorPage,
            great_international.InternationalArticlePage
        ]
    assert great_international.AboutDitLandingPage.allowed_subpage_models() == [
            great_international.AboutDitServicesPage
        ]
    assert great_international.AboutUkLandingPage.allowed_subpage_models() == [
            great_international.AboutUkWhyChooseTheUkPage,
            great_international.AboutUkRegionListingPage
        ]
    assert great_international.AboutUkRegionListingPage.allowed_subpage_models() == [
            great_international.AboutUkRegionPage
        ]
    assert great_international.AboutUkRegionPage.allowed_subpage_models() == []


@pytest.mark.django_db
def test_uses_tree_base_routing_always_true(international_root_page):
    page = factories.InternationalArticleListingPageFactory(
        parent=international_root_page
    )
    assert page.uses_tree_based_routing is True


@pytest.mark.django_db
def test_hpo_folder_page(international_root_page):
    int_home = factories.InternationalHomePageFactory(
        parent=international_root_page
    )
    invest_home = factories.InvestInternationalHomePageFactory(
        parent=int_home
    )
    invest_hpo_folder = factories.InvestHighPotentialOpportunitiesPageFactory(
        parent=invest_home
    )

    assert invest_hpo_folder.title == 'High potential opportunities'
