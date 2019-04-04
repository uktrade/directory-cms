from core import constants


class ServiceHomepageMixin:
    full_path = '/'

    @property
    def full_url(self):
        return dict(constants.APP_URLS)[self.service_name_value]
