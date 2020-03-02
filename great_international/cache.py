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
        great_international.InternationalCampaignPage,
        capital_invest.CapitalInvestOpportunityListingPage,
        great_international.InternationalSubSectorPage,
        great_international.InternationalCuratedTopicLandingPage,
    ]


class InternationalSubSectorPageSubscriber(AbstractDatabaseCacheSubscriber):
    model = great_international.InternationalSubSectorPage
    subscriptions = [
        great_international.InternationalArticlePage,
        great_international.InternationalCampaignPage,
        capital_invest.CapitalInvestOpportunityListingPage,
        great_international.InternationalTopicLandingPage,
    ]


class InternationalHomePageSubscriber(AbstractDatabaseCacheSubscriber):
    model = great_international.InternationalHomePage
    subscriptions = [
        great_international.InternationalArticlePage,
    ]


class InternationalArticlePageSubscriber(AbstractDatabaseCacheSubscriber):
    model = great_international.InternationalArticlePage
    subscriptions = [
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
        great_international.InternationalArticleListingPage,
        great_international.InternationalCampaignPage,
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
    ]


class CapitalInvestOpportunityPageSubscriber(AbstractDatabaseCacheSubscriber):
    model = capital_invest.CapitalInvestOpportunityPage
    subscriptions = [
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
    ]


class InvestHighPotentialOpportunityFormPageSubscriber(
    AbstractDatabaseCacheSubscriber
):
    model = invest.InvestHighPotentialOpportunityFormPage
    subscriptions = [
    ]


class InvestHighPotentialOpportunityDetailPageSubscriber(
    AbstractDatabaseCacheSubscriber
):
    model = invest.InvestHighPotentialOpportunityDetailPage
    subscriptions = [
    ]


class InvestHighPotentialOpportunityFormSuccessPageSubscriber(
    AbstractDatabaseCacheSubscriber
):
    model = invest.InvestHighPotentialOpportunityFormSuccessPage
    subscriptions = [
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
    ]


class AboutDitServicesPageSubscriber(
    AbstractDatabaseCacheSubscriber
):
    model = great_international.AboutDitServicesPage
    subscriptions = [
        capital_invest.InternationalCapitalInvestLandingPage,
    ]


class AboutUkLandingPageSubscriber(
    AbstractDatabaseCacheSubscriber
):
    model = great_international.AboutUkLandingPage
    subscriptions = [
        great_international.InternationalSectorPage,
    ]


class AboutUkRegionListingPageSubscriber(AbstractDatabaseCacheSubscriber):
    model = great_international.AboutUkRegionListingPage
    subscriptions = [
    ]


class AboutUkRegionPageSubscriber(AbstractDatabaseCacheSubscriber):
    model = great_international.AboutUkRegionPage
    subscriptions = [
        great_international.AboutUkRegionListingPage
    ]


class AboutUkWhyChooseTheUkPageSubscriber(
    AbstractDatabaseCacheSubscriber
):
    model = great_international.AboutUkWhyChooseTheUkPage
    subscriptions = [
        great_international.AboutDitServicesPage
    ]


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
