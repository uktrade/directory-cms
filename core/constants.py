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
NETWORK_ICON_PATH = 'core/icons/infrastructure.png'
INNOVATION_ICON_PATH = 'core/icons/innovation.png'
INVESTMENT_ICON_PATH = 'core/icons/investment.png'
QUALITY_ICON_PATH = 'core/icons/quality.png'
RESEARCH_ICON_PATH = 'core/icons/research.png'
SKILLS_ICON_PATH = 'core/icons/skills.png'

ICONS = [
    (default_storage.url(PREOPPULATE_PARAM), 'Network'),
    (default_storage.url(INNOVATION_ICON_PATH), 'Light bulb'),
    (default_storage.url(INVESTMENT_ICON_PATH), 'Money'),
    (default_storage.url(QUALITY_ICON_PATH), 'Rosette'),
    (default_storage.url(RESEARCH_ICON_PATH), 'Magnifying glass'),
    (default_storage.url(SKILLS_ICON_PATH), 'Cogs'),
]
