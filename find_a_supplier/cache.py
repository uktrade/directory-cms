from core.cache import CacheDatabaseSubscriber
from core.models import Breadcrumb

from find_a_supplier import models


class IndustryPageSubscriber(CacheDatabaseSubscriber):
    model = models.IndustryPage
    subscriptions = [
        Breadcrumb,
    ]


class IndustryLandingPageSubscriber(CacheDatabaseSubscriber):
    model = models.IndustryLandingPage
    subscriptions = [
        Breadcrumb,
        models.IndustryPage,
    ]


class IndustryArticlePageSubscriber(CacheDatabaseSubscriber):
    model = models.IndustryArticlePage
    subscriptions = [
        Breadcrumb,
    ]


class LandingPageSubscriber(CacheDatabaseSubscriber):
    model = models.LandingPage
    subscriptions = [
        models.IndustryPage
    ]


class IndustryContactPageSubscriber(CacheDatabaseSubscriber):
    model = models.IndustryContactPage
    subscriptions = [
        Breadcrumb,
        models.IndustryPage,
    ]
