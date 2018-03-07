from django.conf import settings
from django.core.files.storage import default_storage


FIND_A_SUPPLIER = 'FIND_A_SUPPLIER'
EXPORT_READINESS = 'EXPORT_READINESS'
APP_CHOICES = [
    (FIND_A_SUPPLIER, 'Find a Supplier'),
    (EXPORT_READINESS, 'Export Readiness'),
]
APP_URLS = {
    FIND_A_SUPPLIER: settings.APP_URL_FIND_A_SUPPLIER,
    EXPORT_READINESS: settings.APP_URL_EXPORT_READINESS,
}
PREOPPULATE_PARAM = 'prepopulate'
ICONS = [
    (default_storage.url('core/icons/infrastructure.png'), 'Network'),
    (default_storage.url('core/icons/innovation.png'), 'Light bulb'),
    (default_storage.url('core/icons/investment.png'), 'Money'),
    (default_storage.url('core/icons/quality.png'), 'Rosette'),
    (default_storage.url('core/icons/research.png'), 'Magnifying glass'),
    (default_storage.url('core/icons/skills.png'), 'Cogs'),
]
