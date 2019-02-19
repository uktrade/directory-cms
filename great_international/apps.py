from django.apps import AppConfig
from django.db.models.signals import post_save


class GreatInternationalConfig(AppConfig):
    name = 'great_international'

    def ready(self):
        from great_international import cache
        from great_international import signals
        cache.InternationalHomePageSubscriber.subscribe()
        cache.InternationalArticlePageSubscriber.subscribe()
        cache.InternationalCampaignPageSubscriber.subscribe()
        cache.InternationalArticleListingPageSubscriber()
        cache.InternationalTopicLandingPageSubscriber()
        # signals
        post_save.connect(
            receiver=signals.inherit_tags_from_parent,
            sender='great_international.InternationalArticlePage'
        )
        post_save.connect(
            receiver=signals.inherit_tags_from_parent,
            sender='great_international.InternationalCampaignPage'
        )
