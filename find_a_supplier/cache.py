from core.cache import AbstractPageCache
from core.models import Breadcrumb

from find_a_supplier import models


class IndustryContactPageCache(AbstractPageCache):

    model = models.PageCacher
    external_change_subscriptions = [
        Breadcrumb,
        models.Industry,
    ]


class IndustryPagePageCache(AbstractPageCache):
	model = models.IndustryPage
