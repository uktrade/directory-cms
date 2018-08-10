from directory_constants.constants import cms
from django.core.management import BaseCommand
from wagtail.core.models import Page

from core.models import Service


class Command(BaseCommand):

    def handle(self, *args, **options):
        pages = Page.objects.filter(
                service__in=Service.objects.filter(name=cms.INVEST)
            )
        for page in pages:
            if page.slug_en_gb.startswith('invest-'):
                page.slug_en_gb = page.slug_en_gb[7:]
                page.save()
