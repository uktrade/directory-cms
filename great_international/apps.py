from django.apps import AppConfig
from django.db.models.signals import m2m_changed, post_save


class GreatInternationalConfig(AppConfig):
    name = 'great_international'

    def ready(self):
        from great_international import cache, models, signals
        cache.InternationalHomePageSubscriber.subscribe()
        cache.InternationalArticlePageSubscriber.subscribe()
        cache.InternationalCampaignPageSubscriber.subscribe()
        cache.InternationalArticleListingPageSubscriber()
        cache.InternationalTopicLandingPageSubscriber()
        # signals
        post_save.connect(
            receiver=signals.inherit_tags_from_parent,
            sender=models.InternationalArticlePage
        )
        post_save.connect(
            receiver=signals.inherit_tags_from_parent,
            sender=models.InternationalCampaignPage
        )
        m2m_changed.connect(
            receiver=signals.tags_propagate_to_descendants,
            sender=models.InternationalArticleListingPage.tags.through
        )
        m2m_changed.connect(
            receiver=signals.tags_propagate_to_descendants,
            sender=models.InternationalArticleListingPage.tags.through
        )
        m2m_changed.connect(
            receiver=signals.tags_propagate_to_descendants,
            sender=models.InternationalArticleListingPage.tags.through
        )
        m2m_changed.connect(
            receiver=signals.tags_propagate_to_descendants,
            sender=models.InternationalMarketingPages.tags.through
        )
        m2m_changed.connect(
            receiver=signals.tags_propagate_to_descendants,
            sender=models.InternationalRegionPage.tags.through
        )
        m2m_changed.connect(
            receiver=signals.tags_propagate_to_descendants,
            sender=models.InternationalTopicLandingPage.tags.through
        )
