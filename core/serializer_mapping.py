import wagtail

import components.models
import components.serializers
import core.serializers
import export_readiness.models
import export_readiness.serializers
import great_international.models
import great_international.serializers


MODELS_SERIALIZERS_MAPPING = {
    # core page
    wagtail.core.models.Page: core.serializers.WagtailPageSerializer,
    # export_readiness
    export_readiness.models.TermsAndConditionsPage: export_readiness.serializers.GenericBodyOnlyPageSerializer,  # NOQA
    export_readiness.models.PrivacyAndCookiesPage: export_readiness.serializers.GenericBodyOnlyPageSerializer,  # NOQA
    export_readiness.models.GetFinancePage: export_readiness.serializers.GetFinancePageSerializer,  # NOQA
    export_readiness.models.PerformanceDashboardPage: export_readiness.serializers.PerformanceDashboardPageSerializer,  # NOQA
    export_readiness.models.PerformanceDashboardNotesPage: export_readiness.serializers.GenericBodyOnlyPageSerializer,  # NOQA
    export_readiness.models.ArticlePage: export_readiness.serializers.ArticlePageSerializer,  # NOQA
    export_readiness.models.MarketingArticlePage: export_readiness.serializers.MarketingArticlePageSerializer,  # NOQA
    export_readiness.models.HomePage: export_readiness.serializers.HomePageSerializer,  # NOQA
    export_readiness.models.ArticleListingPage: export_readiness.serializers.ArticleListingPageSerializer,  # NOQA
    export_readiness.models.TopicLandingPage: export_readiness.serializers.TopicLandingPageSerializer,  # NOQA
    export_readiness.models.CampaignPage: export_readiness.serializers.CampaignPageSerializer,  # NOQA
    export_readiness.models.EUExitDomesticFormPage: export_readiness.serializers.EUExitDomesticFormPageSerializer,  # NOQA
    export_readiness.models.EUExitFormSuccessPage: export_readiness.serializers.EUExitFormSuccessPageSerializer,  # NOQA
    export_readiness.models.ContactUsGuidancePage: export_readiness.serializers.ContactUsGuidancePageSerializer,  # NOQA
    export_readiness.models.ContactSuccessPage: export_readiness.serializers.ContactSuccessPageSerializer,  # NOQA
    export_readiness.models.SuperregionPage: export_readiness.serializers.SuperregionPageSerializer,  # NOQA
    export_readiness.models.CountryGuidePage: export_readiness.serializers.CountryGuidePageSerializer,  # NOQA
    export_readiness.models.SellingOnlineOverseasHomePage: export_readiness.serializers.SellingOnlineOverseasHomePageSerializer,  # NOQA
    # great international
    great_international.models.great_international.InternationalSectorPage: great_international.serializers.InternationalSectorPageSerializer,  # NOQA
    great_international.models.great_international.InternationalSubSectorPage: great_international.serializers.InternationalSubSectorPageSerializer,  # NOQA
    great_international.models.great_international.InternationalInvestmentSectorPage: great_international.serializers.InternationalInvestmentSectorPageSerializer,  # NOQA
    great_international.models.great_international.InternationalInvestmentSubSectorPage: great_international.serializers.InternationalInvestmentSubSectorPageSerializer,  # NOQA
    great_international.models.great_international.InternationalHomePage: great_international.serializers.InternationalHomePageSerializer,  # NOQA
    great_international.models.great_international.InternationalArticlePage: great_international.serializers.InternationalArticlePageSerializer,  # NOQA
    great_international.models.great_international.InternationalCampaignPage: great_international.serializers.InternationalCampaignPageSerializer,  # NOQA
    great_international.models.great_international.InternationalArticleListingPage: great_international.serializers.InternationalArticleListingPageSerializer,  # NOQA
    great_international.models.great_international.InternationalTopicLandingPage: great_international.serializers.InternationalTopicLandingPageSerializer,  # NOQA
    great_international.models.great_international.InternationalCuratedTopicLandingPage: great_international.serializers.InternationalCuratedTopicLandingPageSerializer,  # NOQA
    great_international.models.great_international.InternationalGuideLandingPage: great_international.serializers.InternationalGuideLandingPageSerializer,  # NOQA
    great_international.models.great_international.InternationalEUExitFormPage: great_international.serializers.InternationalEUExitFormPageSerializer,  # NOQA
    great_international.models.great_international.InternationalEUExitFormSuccessPage: great_international.serializers.InternationalEUExitFormSuccessPageSerializer,  # NOQA
    great_international.models.great_international.AboutDitLandingPage: great_international.serializers.AboutDitLandingPageSerializer,  # NOQA
    great_international.models.great_international.AboutDitServicesPage: great_international.serializers.AboutDitServicesPageSerializer,  # NOQA
    great_international.models.great_international.AboutUkLandingPage: great_international.serializers.AboutUkLandingPageSerializer,  # NOQA
    great_international.models.great_international.AboutUkRegionPage: great_international.serializers.AboutUkRegionPageSerializer,  # NOQA
    great_international.models.great_international.AboutUkRegionListingPage: great_international.serializers.AboutUkRegionListingPageSerializer,  # NOQA
    great_international.models.great_international.AboutUkWhyChooseTheUkPage: great_international.serializers.AboutUkWhyChooseTheUkPageSerializer,  # NOQA
    great_international.models.capital_invest.InternationalCapitalInvestLandingPage: great_international.serializers.InternationalCapitalInvestLandingPageSerializer,  # NOQA
    great_international.models.capital_invest.CapitalInvestRegionPage: great_international.serializers.CapitalInvestRegionPageSerializer,  # NOQA
    great_international.models.capital_invest.CapitalInvestOpportunityListingPage: great_international.serializers.CapitalInvestOpportunityListingSerializer,  # NOQA
    great_international.models.capital_invest.CapitalInvestOpportunityPage: great_international.serializers.CapitalInvestOpportunityPageSerializer,  # NOQA
    great_international.models.capital_invest.CapitalInvestContactFormPage: great_international.serializers.CapitalInvestContactFormPageSerializer,  # NOQA
    great_international.models.capital_invest.CapitalInvestContactFormSuccessPage: great_international.serializers.CapitalInvestContactFormSuccessPageSerializer,  # NOQA
    great_international.models.invest.InvestInternationalHomePage: great_international.serializers.InvestInternationalHomePageSerializer,  # NOQA
    great_international.models.invest.InvestHighPotentialOpportunityFormSuccessPage: great_international.serializers.InvestHighPotentialOpportunityFormSuccessPageSerializer,  # NOQA
    great_international.models.invest.InvestHighPotentialOpportunityFormPage: great_international.serializers.InvestHighPotentialOpportunityFormPageSerializer,  # NOQA
    great_international.models.invest.InvestHighPotentialOpportunityDetailPage: great_international.serializers.InvestHighPotentialOpportunityDetailPageSerializer,   # NOQA
    great_international.models.find_a_supplier.InternationalTradeHomePage: great_international.serializers.InternationalTradeHomePageSerializer,  # NOQA
    great_international.models.find_a_supplier.InternationalTradeIndustryContactPage: great_international.serializers.InternationalTradeIndustryContactPageSerializer,  # NOQA
    great_international.models.invest.InvestRegionPage: great_international.serializers.InvestRegionPageSerializer,  # NOQA
    great_international.models.invest.InvestRegionLandingPage: great_international.serializers.InvestRegionLandingPageSerializer,  # NOQA
    great_international.models.investment_atlas.InvestmentOpportunityPage: great_international.serializers.InvestmentOpportunityPageSerializer,  # NOQA
    great_international.models.investment_atlas.InvestmentOpportunityListingPage: great_international.serializers.InvestmentOpportunityListingPageSerializer,  # NOQA
    great_international.models.investment_atlas.InvestmentAtlasLandingPage: great_international.serializers.InvestmentAtlasLandingPageSerializer,  # NOQA
    # components
    components.models.BannerComponent: components.serializers.BannerComponentPageSerializer  # NOQA
}
