from core.cache import AbstractDatabaseCacheSubscriber
from core.models import Breadcrumb

from find_a_supplier import models


class IndustryPageSubscriber(AbstractDatabaseCacheSubscriber):
    model = models.IndustryPage
    subscriptions = [
        Breadcrumb,
    ]


class IndustryLandingPageSubscriber(AbstractDatabaseCacheSubscriber):
    model = models.IndustryLandingPage
    subscriptions = [
        Breadcrumb,
        models.IndustryPage,
    ]


class IndustryArticlePageSubscriber(AbstractDatabaseCacheSubscriber):
    model = models.IndustryArticlePage
    subscriptions = [
        Breadcrumb,
    ]


class LandingPageSubscriber(AbstractDatabaseCacheSubscriber):
    model = models.LandingPage
    subscriptions = [
        models.IndustryPage
    ]


class IndustryContactPageSubscriber(AbstractDatabaseCacheSubscriber):
    model = models.IndustryContactPage
    subscriptions = [
        Breadcrumb,
        models.IndustryPage,
    ]
