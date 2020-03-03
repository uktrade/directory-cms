from great_international.models import great_international
from great_international.models import invest
from great_international.models import find_a_supplier
from great_international.models import capital_invest

from core.cache import DatabaseCacheSubscriber, RegionAwareCachePopulator


subscribers = [
    DatabaseCacheSubscriber([
        capital_invest.CapitalInvestContactFormPage,
        capital_invest.CapitalInvestContactFormSuccessPage,
        capital_invest.CapitalInvestOpportunityListingPage,
        capital_invest.CapitalInvestOpportunityPage,
        capital_invest.InternationalCapitalInvestLandingPage,
        find_a_supplier.InternationalTradeHomePage,
        find_a_supplier.InternationalTradeIndustryContactPage,
        great_international.AboutDitLandingPage,
        great_international.AboutDitServicesPage,
        great_international.AboutUkLandingPage,
        great_international.AboutUkRegionListingPage,
        great_international.AboutUkRegionPage,
        great_international.AboutUkWhyChooseTheUkPage,
        great_international.InternationalArticlePage,
        great_international.InternationalCampaignPage,
        great_international.InternationalCuratedTopicLandingPage,
        great_international.InternationalEUExitFormPage,
        great_international.InternationalEUExitFormSuccessPage,
        great_international.InternationalGuideLandingPage,
        great_international.InternationalHomePage,
        great_international.InternationalSectorPage,
        great_international.InternationalSubSectorPage,
        great_international.InternationalTopicLandingPage,
        invest.InvestHighPotentialOpportunityDetailPage,
        invest.InvestHighPotentialOpportunityFormPage,
        invest.InvestHighPotentialOpportunityFormSuccessPage,
        invest.InvestInternationalHomePage,
        invest.InvestRegionLandingPage,
        invest.InvestRegionPage,
    ]),
    DatabaseCacheSubscriber(
        page_classes=[great_international.InternationalArticleListingPage],
        cache_populator=RegionAwareCachePopulator,
    )
]