import components.models
import components.serializers
import export_readiness.models
import export_readiness.serializers
import find_a_supplier.models
import find_a_supplier.serializers
import invest.models
import invest.serializers


MODELS_SERIALIZERS_MAPPING = {
    # export readiness
    export_readiness.models.TermsAndConditionsPage: export_readiness.serializers.GenericBodyOnlyPageSerializer,  # NOQA
    export_readiness.models.PrivacyAndCookiesPage: export_readiness.serializers.GenericBodyOnlyPageSerializer,  # NOQA
    export_readiness.models.GetFinancePage: export_readiness.serializers.GetFinancePageSerializer,  # NOQA
    export_readiness.models.PerformanceDashboardPage: export_readiness.serializers.PerformanceDashboardPageSerializer,  # NOQA
    export_readiness.models.PerformanceDashboardNotesPage: export_readiness.serializers.GenericBodyOnlyPageSerializer,  # NOQA
    export_readiness.models.ArticlePage: export_readiness.serializers.ArticlePageSerializer,  # NOQA
    export_readiness.models.HomePage: export_readiness.serializers.HomePageSerializer,  # NOQA
    export_readiness.models.ArticleListingPage: export_readiness.serializers.ArticleListingPageSerializer,  # NOQA
    export_readiness.models.TopicLandingPage: export_readiness.serializers.TopicLandingPageSerializer,  # NOQA
    export_readiness.models.InternationalLandingPage: export_readiness.serializers.InternationalLandingPageSerializer,  # NOQA
    export_readiness.models.CampaignPage: export_readiness.serializers.CampaignPageSerializer,  # NOQA
    export_readiness.models.EUExitInternationalFormPage: export_readiness.serializers.EUExitInternationalFormPageSerializer,  # NOQA
    export_readiness.models.EUExitDomesticFormPage: export_readiness.serializers.EUExitDomesticFormPageSerializer,  # NOQA
    export_readiness.models.EUExitFormSuccessPage: export_readiness.serializers.EUExitFormSuccessPageSerializer,  # NOQA
    export_readiness.models.ContactUsGuidancePage: export_readiness.serializers.ContactUsGuidancePageSerializer,  # NOQA
    export_readiness.models.ContactSuccessPage: export_readiness.serializers.ContactSuccessPageSerializer,  # NOQA
    # invest
    invest.models.SectorLandingPage: invest.serializers.SectorLandingPageGenericSerializer,  # NOQA
    invest.models.RegionLandingPage: invest.serializers.SectorLandingPageGenericSerializer,  # NOQA
    invest.models.SectorPage: invest.serializers.SectorPageSerializer,
    invest.models.SetupGuideLandingPage: invest.serializers.SetupGuideLandingPageSerializer,  # NOQA
    invest.models.SetupGuidePage: invest.serializers.SetupGuidePageSerializer,
    invest.models.InvestHomePage: invest.serializers.InvestHomePageSerializer,
    invest.models.InfoPage: invest.serializers.InfoPageSerializer,
    invest.models.HighPotentialOpportunityFormPage: invest.serializers.HighPotentialOpportunityFormPageSerializer,  # NOQA
    invest.models.HighPotentialOpportunityDetailPage: invest.serializers.HighPotentialOpportunityDetailPageSerializer,  # NOQA
    invest.models.HighPotentialOpportunityFormSuccessPage: invest.serializers.HighPotentialOpportunityFormSuccessPageSerializer,  # NOQA
    # find a supplier
    find_a_supplier.models.IndustryPage: find_a_supplier.serializers.IndustryPageSerializer,  # NOQA
    find_a_supplier.models.IndustryLandingPage: find_a_supplier.serializers.IndustryLandingPageSerializer,  # NOQA
    find_a_supplier.models.IndustryArticlePage: find_a_supplier.serializers.IndustryArticlePageSerializer,  # NOQA
    find_a_supplier.models.LandingPage: find_a_supplier.serializers.LandingPageSerializer,  # NOQA
    find_a_supplier.models.IndustryContactPage: find_a_supplier.serializers.IndustryContactPageSerializer,  # NOQA
    # components
    components.models.BannerComponent: components.serializers.BannerComponentPageSerializer  # NOQA
}
