from directory_constants import cms
from django.core.management import BaseCommand
from django.core.management.base import no_translations
from wagtail.core.models import Page

from core import filters


SERVICES_MAPPING = {
    'international': cms.GREAT_INTERNATIONAL,
    'domestic': cms.GREAT_DOMESTIC
}


class Command(BaseCommand):
    help = 'Enable the tree based routing flag on pages. ' \
           'If --servicename is not specified, the flag is enabled on ' \
           'ALL the pages.'

    def add_arguments(self, parser):
        parser.add_argument(
            '--servicename',
            help='Select international or domestic',
            choices=['international', 'domestic']
        )

    @no_translations
    def handle(self, *args, **options):
        queryset = Page.objects.exclude(title__isnull=True)
        if options['servicename']:
            service_name = SERVICES_MAPPING[options['servicename']]
            queryset = filters.ServiceNameFilter().filter_service_name(
                queryset=queryset,
                name=None,
                value=service_name,
            )
        for page in queryset:
            page.specific.uses_tree_based_routing = True
            page.specific.save()
