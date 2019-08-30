from django.conf import settings

from directory_constants import cms

APP_URLS = {
    cms.FIND_A_SUPPLIER: settings.APP_URL_FIND_A_SUPPLIER,
    cms.EXPORT_READINESS: settings.APP_URL_EXPORT_READINESS,
    cms.INVEST: settings.APP_URL_INVEST,
    cms.COMPONENTS: settings.APP_URL_COMPONENTS,
    cms.GREAT_INTERNATIONAL: settings.APP_URL_GREAT_INTERNATIONAL
}

ARTICLE_TYPES = [
    ('Blog', 'Blog'),
    ('Advice', 'Advice'),
    ('Case study', 'Case study'),
    ('Campaign', 'Campaign'),
]
