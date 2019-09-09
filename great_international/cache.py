from core.cache import (
    AbstractDatabaseCacheSubscriber, RegionAwareCachePopulator
)

from great_international.models import great_international
from great_international.models import invest
from great_international.models import find_a_supplier
from great_international.models import capital_invest


class InternationalSectorPageSubscriber(AbstractDatabaseCacheSubscriber):
    model = great_international.InternationalSectorPage
    subscriptions = [
        great_international.InternationalArticlePage,
        great_international.InternationalCampaignPage,
        capital_invest.CapitalInvestOpportunityPage,
        capital_invest.CapitalInvestOpportunityListingPage,
        great_international.InternationalSubSectorPage,
        great_international.InternationalTopicLandingPage,
        great_international.InternationalCuratedTopicLandingPage,
        great_international.AboutUkLandingPage,
        great_international.InternationalHomePage
    ]


class InternationalSubSectorPageSubscriber(AbstractDatabaseCacheSubscriber):
    model = great_international.InternationalSubSectorPage
    subscriptions = [
        great_international.InternationalArticlePage,
        great_international.InternationalCampaignPage,
        capital_invest.CapitalInvestOpportunityPage,
        capital_invest.CapitalInvestOpportunityListingPage,
        great_international.InternationalTopicLandingPage,
        great_international.InternationalSubSectorPage
    ]


class InternationalHomePageSubscriber(AbstractDatabaseCacheSubscriber):
    model = great_international.InternationalHomePage
    subscriptions = [
        great_international.InternationalArticlePage,
        invest.InvestInternationalHomePage,
        capital_invest.InternationalCapitalInvestLandingPage,
        find_a_supplier.InternationalTradeHomePage,
        great_international.InternationalSectorPage
    ]


class InternationalHomePageOldSubscriber(AbstractDatabaseCacheSubscriber):
    model = great_international.InternationalHomePageOld
    subscriptions = [
        great_international.InternationalArticlePage,
    ]


class InternationalArticlePageSubscriber(AbstractDatabaseCacheSubscriber):
    model = great_international.InternationalArticlePage
    subscriptions = [
        great_international.InternationalTopicLandingPage,
        great_international.InternationalSectorPage,
    ]


class InternationalCampaignPageSubscriber(AbstractDatabaseCacheSubscriber):
    model = great_international.InternationalCampaignPage
    subscriptions = []


class InternationalArticleListingPageSubscriber(
    AbstractDatabaseCacheSubscriber
):
    cache_populator = RegionAwareCachePopulator
    model = great_international.InternationalArticleListingPage
    subscriptions = [
        great_international.InternationalArticlePage,
        great_international.InternationalCampaignPage
    ]


class InternationalTopicLandingPageSubscriber(AbstractDatabaseCacheSubscriber):
    model = great_international.InternationalTopicLandingPage
    subscriptions = [
        great_international.InternationalArticlePage,
        great_international.InternationalArticleListingPage,
        great_international.InternationalSectorPage,
        great_international.InternationalCampaignPage,
        great_international.AboutUkLandingPage
    ]


class InternationalCuratedTopicLandingPageSubscriber(
    AbstractDatabaseCacheSubscriber
):
    model = great_international.InternationalCuratedTopicLandingPage
    subscriptions = []


class InternationalGuideLandingPageSubscriber(AbstractDatabaseCacheSubscriber):
    model = great_international.InternationalGuideLandingPage
    subscriptions = [
        great_international.InternationalArticlePage,
        invest.InvestInternationalHomePage,
        capital_invest.InternationalCapitalInvestLandingPage
    ]


class InternationalEUExitFormPageSubscriber(
    AbstractDatabaseCacheSubscriber
):
    model = great_international.InternationalEUExitFormPage
    subscriptions = []


class InternationalEUExitFormSuccessPageSubscriber(
    AbstractDatabaseCacheSubscriber
):
    model = great_international.InternationalEUExitFormSuccessPage
    subscriptions = []


class InternationalCapitalInvestLandingPageSubscriber(
    AbstractDatabaseCacheSubscriber
):
    model = capital_invest.InternationalCapitalInvestLandingPage
    subscriptions = [
        capital_invest.CapitalInvestRegionPage,
        great_international.AboutUkRegionPage,
        great_international.InternationalGuideLandingPage,
        great_international.InternationalHomePage
    ]


class CapitalInvestRegionPageSubscriber(AbstractDatabaseCacheSubscriber):
    model = capital_invest.CapitalInvestRegionPage
    subscriptions = []


class CapitalInvestOpportunityPageSubscriber(AbstractDatabaseCacheSubscriber):
    model = capital_invest.CapitalInvestOpportunityPage
    subscriptions = [
        capital_invest.CapitalInvestOpportunityPage,
        great_international.InternationalSectorPage,
        great_international.InternationalSubSectorPage,
        capital_invest.CapitalInvestOpportunityListingPage,
    ]


class CapitalInvestOpportunityListingPageSubscriber(
    AbstractDatabaseCacheSubscriber
):
    model = capital_invest.CapitalInvestOpportunityListingPage
    subscriptions = [
        capital_invest.CapitalInvestOpportunityPage
    ]


class InvestInternationalHomePageSubscriber(AbstractDatabaseCacheSubscriber):
    model = invest.InvestInternationalHomePage
    subscriptions = [
        great_international.InternationalSectorPage,
        invest.InvestHighPotentialOpportunityDetailPage,
        great_international.InternationalGuideLandingPage,
        great_international.InternationalHomePage
    ]


class InvestHighPotentialOpportunityFormPageSubscriber(
    AbstractDatabaseCacheSubscriber
):
    model = invest.InvestHighPotentialOpportunityFormPage
    subscriptions = [
        invest.InvestHighPotentialOpportunityDetailPage,
        invest.InvestHighPotentialOpportunityFormPage,
        invest.InvestHighPotentialOpportunityFormSuccessPage,
    ]


class InvestHighPotentialOpportunityDetailPageSubscriber(
    AbstractDatabaseCacheSubscriber
):
    model = invest.InvestHighPotentialOpportunityDetailPage
    subscriptions = [
        invest.InvestHighPotentialOpportunityDetailPage,
        invest.InvestHighPotentialOpportunityFormPage,
        invest.InvestHighPotentialOpportunityFormSuccessPage,
    ]


class InvestHighPotentialOpportunityFormSuccessPageSubscriber(
    AbstractDatabaseCacheSubscriber
):
    model = invest.InvestHighPotentialOpportunityFormSuccessPage
    subscriptions = [
        invest.InvestHighPotentialOpportunityDetailPage,
        invest.InvestHighPotentialOpportunityFormPage,
    ]


class InvestRegionLandingPageSubscriber(AbstractDatabaseCacheSubscriber):
    model = invest.InvestRegionLandingPage
    subscriptions = [
        invest.InvestRegionPage,
    ]


class InvestRegionPageSubscriber(AbstractDatabaseCacheSubscriber):
    model = invest.InvestRegionPage
    subscriptions = [
        # not a typo: each sector page contains a list of other sector pages
        invest.InvestRegionPage,
    ]


class InternationalTradeHomePageSubscriber(AbstractDatabaseCacheSubscriber):
    model = find_a_supplier.InternationalTradeHomePage
    subscriptions = [
        great_international.InternationalSectorPage,
        great_international.InternationalHomePage
    ]


class InternationalTradeIndustryContactPageSubscriber(
    AbstractDatabaseCacheSubscriber
):
    model = find_a_supplier.InternationalTradeIndustryContactPage
    subscriptions = [
        great_international.InternationalSectorPage,
    ]


class AboutDitLandingPageSubscriber(
    AbstractDatabaseCacheSubscriber
):
    model = great_international.AboutDitLandingPage
    subscriptions = [
        great_international.AboutDitServicesPage
    ]


class AboutDitServicesPageSubscriber(
    AbstractDatabaseCacheSubscriber
):
    model = great_international.AboutDitServicesPage
    subscriptions = [
        great_international.AboutDitLandingPage
    ]


class AboutUkLandingPageSubscriber(
    AbstractDatabaseCacheSubscriber
):
    model = great_international.AboutUkLandingPage
    subscriptions = [
        great_international.InternationalSectorPage,
        great_international.AboutUkRegionListingPage,
        great_international.AboutUkRegionPage,
        great_international.InternationalTopicLandingPage
    ]


class AboutUkRegionListingPageSubscriber(AbstractDatabaseCacheSubscriber):
    model = great_international.AboutUkRegionListingPage
    subscriptions = [
        great_international.AboutUkLandingPage
    ]


class AboutUkRegionPageSubscriber(AbstractDatabaseCacheSubscriber):
    model = great_international.AboutUkRegionPage
    subscriptions = [
        great_international.AboutUkLandingPage,
        great_international.AboutUkRegionListingPage
    ]


class AboutUkWhyChooseTheUkPageSubscriber(
    AbstractDatabaseCacheSubscriber
):
    model = great_international.AboutUkWhyChooseTheUkPage
    subscriptions = []


class CapitalInvestContactFormPageSubscriber(
    AbstractDatabaseCacheSubscriber
):
    model = capital_invest.CapitalInvestContactFormPage
    subscriptions = [
        capital_invest.InternationalCapitalInvestLandingPage
    ]


class CapitalInvestContactFormSuccessPageSubscriber(
    AbstractDatabaseCacheSubscriber
):
    model = capital_invest.CapitalInvestContactFormSuccessPage
    subscriptions = [
        capital_invest.InternationalCapitalInvestLandingPage,
        capital_invest.CapitalInvestContactFormPage
    ]
