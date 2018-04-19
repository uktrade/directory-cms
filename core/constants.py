from django.conf import settings


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
RICH_TEXT_FEATURES = [
    'h2',
    'h3',
    'h4',
    'h5',
    'h6',
    'link',
    'ol',
    'ul',
    # image removed to prevent breaking page layout.
    # bold and italic removed as per styleguide guidelines:
    # export-elements-dev.herokuapp.com/typography/#typography-body-copy
]
