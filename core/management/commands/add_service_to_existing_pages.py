from directory_constants.constants import cms
from django.apps import apps
from django.core.management import BaseCommand

from core.models import Service

MODELS = (
    {
        'app_name': 'export_readiness',
        'class_name': 'TermsAndConditionsPage',
        'service_name': cms.EXPORT_READINESS
    },
    {
        'app_name': 'export_readiness',
        'class_name': 'PrivacyAndCookiesPage',
        'service_name': cms.EXPORT_READINESS
    },
    {
        'app_name': 'export_readiness',
        'class_name': 'GetFinancePage',
        'service_name': cms.EXPORT_READINESS
    },
    {
        'app_name': 'export_readiness',
        'class_name': 'PerformanceDashboardPage',
        'service_name': cms.EXPORT_READINESS
    },
    {
        'app_name': 'export_readiness',
        'class_name': 'PerformanceDashboardNotesPage',
        'service_name': cms.EXPORT_READINESS
    },
    {
        'app_name': 'find_a_supplier',
        'class_name': 'IndustryPage',
        'service_name': cms.FIND_A_SUPPLIER
    },
    {
        'app_name': 'find_a_supplier',
        'class_name': 'IndustryLandingPage',
        'service_name': cms.FIND_A_SUPPLIER
    },
    {
        'app_name': 'find_a_supplier',
        'class_name': 'IndustryArticlePage',
        'service_name': cms.FIND_A_SUPPLIER
    },
    {
        'app_name': 'find_a_supplier',
        'class_name': 'LandingPage',
        'service_name': cms.FIND_A_SUPPLIER
    },
    {
        'app_name': 'find_a_supplier',
        'class_name': 'IndustryContactPage',
        'service_name': cms.FIND_A_SUPPLIER
    },
    {
        'app_name': 'invest',
        'class_name': 'SectorLandingPage',
        'service_name': cms.INVEST
    },
    {
        'app_name': 'invest',
        'class_name': 'RegionLandingPage',
        'service_name': cms.INVEST
    },
    {
        'app_name': 'invest',
        'class_name': 'SectorPage',
        'service_name': cms.INVEST
    },
    {
        'app_name': 'invest',
        'class_name': 'SetupGuideLandingPage',
        'service_name': cms.INVEST
    },
    {
        'app_name': 'invest',
        'class_name': 'SetupGuidePage',
        'service_name': cms.INVEST
    },
    {
        'app_name': 'invest',
        'class_name': 'InvestHomePage',
        'service_name': cms.INVEST
    },
    {
        'app_name': 'invest',
        'class_name': 'InfoPage',
        'service_name': cms.INVEST
    }
)


class Command(BaseCommand):

    help = 'Add service to existing pages'

    def handle(self, *args, **options):
        for model in MODELS:
            model_class = apps.get_model(model['app_name'],
                                         model['class_name'])
            for page in model_class.objects.all():
                Service.objects.get_or_create(
                    name=model['service_name'],
                    page=page
                )
