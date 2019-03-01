from django.apps import AppConfig
from django.db.models.signals import m2m_changed, post_save


class GreatInternationalConfig(AppConfig):
    name = 'great_international'

    def ready(self):
        from great_international import cache, models, signals
        cache.InternationalSectorPageSubscriber.subscribe()
        cache.InternationalHomePageSubscriber.subscribe()
        cache.InternationalArticlePageSubscriber.subscribe()
        cache.InternationalCampaignPageSubscriber.subscribe()
        cache.InternationalArticleListingPageSubscriber()
        cache.InternationalTopicLandingPageSubscriber()
        # tags inheritance signals
        post_save.connect(
            receiver=signals.inherit_tags_from_parent(),
            sender=models.InternationalSectorPage
        )
        post_save.connect(
            receiver=signals.inherit_tags_from_parent,
            sender=models.InternationalArticlePage
        )
        post_save.connect(
            receiver=signals.inherit_tags_from_parent,
            sender=models.InternationalCampaignPage
        )
        # tags propagation signals
        m2m_changed.connect(
            receiver=signals.tags_propagate_to_descendants,
            sender=models.InternationalTopicLandingPage.tags.through
        )
        m2m_changed.connect(
            receiver=signals.tags_propagate_to_descendants,
            sender=models.InternationalArticleListingPage.tags.through
        )
        m2m_changed.connect(
            receiver=signals.tags_propagate_to_descendants,
            sender=models.InternationalRegionPage.tags.through
        )
        m2m_changed.connect(
            receiver=signals.tags_propagate_to_descendants,
            sender=models.InternationalCampaignPage.tags.through
        )
