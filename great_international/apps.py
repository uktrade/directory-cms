from django.apps import AppConfig
from django.db.models.signals import m2m_changed, post_save


class GreatInternationalConfig(AppConfig):
    name = 'great_international'

    def ready(self):
        from great_international import cache, signals
        from great_international.models import great_international
        cache.InternationalSectorPageSubscriber.subscribe()
        cache.InternationalSubSectorPageSubscriber.subscribe()
        cache.InternationalHomePageSubscriber.subscribe()
        cache.InternationalHomePageOldSubscriber.subscribe()
        cache.InternationalArticlePageSubscriber.subscribe()
        cache.InternationalCampaignPageSubscriber.subscribe()
        cache.InternationalArticleListingPageSubscriber.subscribe()
        cache.InternationalTopicLandingPageSubscriber.subscribe()
        cache.InternationalCuratedTopicLandingPageSubscriber.subscribe()
        cache.InternationalGuideLandingPageSubscriber.subscribe()
        cache.InternationalEUExitFormPageSubscriber.subscribe()
        cache.InternationalEUExitFormSuccessPageSubscriber.subscribe()
        cache.InternationalCapitalInvestLandingPageSubscriber.subscribe()
        cache.CapitalInvestRegionPageSubscriber.subscribe()
        cache.CapitalInvestOpportunityPageSubscriber.subscribe()
        cache.CapitalInvestOpportunityListingPageSubscriber.subscribe()
        cache.InvestInternationalHomePageSubscriber.subscribe()
        cache.InvestHighPotentialOpportunityDetailPageSubscriber.subscribe()
        cache.InvestHighPotentialOpportunityFormPageSubscriber.subscribe()
        cache.InvestHighPotentialOpportunityFormSuccessPageSubscriber.subscribe()  # noqa
        cache.InvestRegionLandingPageSubscriber.subscribe()
        cache.InvestRegionPageSubscriber.subscribe()
        cache.InternationalTradeHomePageSubscriber.subscribe()
        cache.InternationalTradeIndustryContactPageSubscriber.subscribe()
        cache.AboutDitLandingPageSubscriber.subscribe()
        cache.AboutDitServicesPageSubscriber.subscribe()
        cache.AboutUkLandingPageSubscriber.subscribe()
        cache.AboutUkWhyChooseTheUkPageSubscriber.subscribe()
        cache.CapitalInvestContactFormPageSubscriber.subscribe()
        # tags inheritance signals
        post_save.connect(
            receiver=signals.inherit_tags_from_parent,
            sender=great_international.InternationalSectorPage
        )
        post_save.connect(
            receiver=signals.inherit_tags_from_parent,
            sender=great_international.InternationalArticlePage
        )
        post_save.connect(
            receiver=signals.inherit_tags_from_parent,
            sender=great_international.InternationalCampaignPage
        )
        # tags propagation signals
        m2m_changed.connect(
            receiver=signals.tags_propagate_to_descendants,
            sender=(
                great_international.InternationalTopicLandingPage.tags.through)
        )
        m2m_changed.connect(
            receiver=signals.tags_propagate_to_descendants,
            sender=great_international.InternationalArticleListingPage.tags.through  # noqa
        )
        m2m_changed.connect(
            receiver=signals.tags_propagate_to_descendants,
            sender=great_international.InternationalRegionPage.tags.through
        )
        m2m_changed.connect(
            receiver=signals.tags_propagate_to_descendants,
            sender=great_international.InternationalCampaignPage.tags.through
        )
