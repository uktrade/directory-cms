from directory_constants.constants import cms
from django.core.management import BaseCommand
from wagtail.core.models import Page

from core.filters import ServiceNameFilter


class Command(BaseCommand):

    def handle(self, *args, **options):
        queryset = ServiceNameFilter().filter_service_name(
            queryset=Page.objects.all(),
            name=None,
            value=cms.INVEST,
        )
        for page in queryset.specific():
            if page.slug_en_gb.startswith('invest-'):
                page.slug_en_gb = page.slug_en_gb[7:]
                page.save()
