from core.models import BasePage

from directory_constants import cms


class BaseInternationalPage(BasePage):
    service_name_value = cms.GREAT_INTERNATIONAL

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        self.uses_tree_based_routing = True
        return super().save(*args, **kwargs)
