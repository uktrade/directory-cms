from django.conf import settings

from directory_constants.constants import cms

APP_URLS = {
    cms.FIND_A_SUPPLIER: settings.APP_URL_FIND_A_SUPPLIER,
    cms.EXPORT_READINESS: settings.APP_URL_EXPORT_READINESS,
    cms.INVEST: settings.APP_URL_INVEST,
    cms.COMPONENTS: settings.APP_URL_COMPONENTS,
}
