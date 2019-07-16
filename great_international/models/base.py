from core.models import BasePage

from directory_constants import cms


class BaseInternationalPage(BasePage):
    service_name_value = cms.GREAT_INTERNATIONAL

    class Meta:
        abstract = True
