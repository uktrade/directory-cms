import wagtail

import components.models
import components.serializers
import core.serializers
import great_international.models
import great_international.serializers


MODELS_SERIALIZERS_MAPPING = {
    # core page
    wagtail.core.models.Page: core.serializers.WagtailPageSerializer,

    # Atlas core
    # ----------
    great_international.models.great_international.InternationalHomePage: great_international.serializers.InternationalHomePageSerializer,  # NOQA
    great_international.models.great_international.InternationalInvestmentSectorPage: great_international.serializers.InternationalInvestmentSectorPageSerializer,  # NOQA
    great_international.models.great_international.InternationalInvestmentSubSectorPage: great_international.serializers.InternationalInvestmentSubSectorPageSerializer,  # NOQA
    great_international.models.great_international.InternationalArticlePage: great_international.serializers.InternationalArticlePageSerializer,  # NOQA
    great_international.models.great_international.InternationalCampaignPage: great_international.serializers.InternationalCampaignPageSerializer,  # NOQA
    great_international.models.great_international.AboutUkRegionPage: great_international.serializers.AboutUkRegionPageSerializer,  # NOQA
    great_international.models.great_international.AboutUkRegionListingPage: great_international.serializers.AboutUkRegionListingPageSerializer,  # NOQA
    great_international.models.great_international.InternationalTopicLandingPage: great_international.serializers.InternationalTopicLandingPageSerializer,  # NOQA
    great_international.models.investment_atlas.InvestmentOpportunityPage: great_international.serializers.InvestmentOpportunityPageSerializer,  # NOQA
    great_international.models.investment_atlas.InvestmentOpportunityListingPage: great_international.serializers.InvestmentOpportunityListingPageSerializer,  # NOQA
    great_international.models.investment_atlas.InvestmentAtlasLandingPage: great_international.serializers.InvestmentAtlasLandingPageSerializer,  # NOQA
    great_international.models.great_international.WhyInvestInTheUKPage: great_international.serializers.WhyInvestInTheUKPageSerializer,  # NOQA
    great_international.models.investment_atlas.InvestmentGeneralContentPage: great_international.serializers.InvestmentGeneralContentPageSerializer,  # NOQA
    great_international.models.investment_atlas.ForeignDirectInvestmentFormPage: great_international.serializers.ForeignDirectInvestmentFormPageSerializer,  # NOQA
    great_international.models.investment_atlas.ForeignDirectInvestmentFormSuccessPage: great_international.serializers.ForeignDirectInvestmentFormSuccessPageSerializer,  # NOQA


    # Still used but old styles for content
    # -------------------------------------
    great_international.models.great_international.InternationalEUExitFormPage: great_international.serializers.InternationalEUExitFormPageSerializer,  # NOQA
    great_international.models.great_international.InternationalEUExitFormSuccessPage: great_international.serializers.InternationalEUExitFormSuccessPageSerializer,  # NOQA
    # 2 pages redirected, 1 with old style:
    great_international.models.great_international.AboutDitServicesPage: great_international.serializers.AboutDitServicesPageSerializer,  # NOQA

    great_international.models.capital_invest.CapitalInvestContactFormPage: great_international.serializers.CapitalInvestContactFormPageSerializer,  # NOQA
    great_international.models.capital_invest.CapitalInvestContactFormSuccessPage: great_international.serializers.CapitalInvestContactFormSuccessPageSerializer,  # NOQA
    great_international.models.find_a_supplier.InternationalTradeHomePage: great_international.serializers.InternationalTradeHomePageSerializer,  # NOQA
    great_international.models.find_a_supplier.InternationalTradeIndustryContactPage: great_international.serializers.InternationalTradeIndustryContactPageSerializer,  # NOQA


    # Pages using these exist in Wagtail but are draft or redirected
    # --------------------------------------------------------------
    great_international.models.invest.InvestInternationalHomePage: great_international.serializers.InvestInternationalHomePageSerializer,  # NOQA

    # Not sure!
    # ---------
    # The following only has one page which exists as a draft, but does have children pages...
    great_international.models.great_international.InternationalArticleListingPage: great_international.serializers.InternationalArticleListingPageSerializer,  # NOQA


    # components
    components.models.BannerComponent: components.serializers.BannerComponentPageSerializer  # NOQA
}
