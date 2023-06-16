from directory_constants import cms
from django.core.management import BaseCommand
from django.core.management.base import no_translations
from wagtail.models import Page
from django.db.migrations.recorder import MigrationRecorder

from core import filters


APPS_MAPPING = {
    'great_international': 'great_international',
    'core': 'core',
}


class Command(BaseCommand):
    help = 'Zero App Migrations.'

    @no_translations
    def handle(self, *args, **options):
        MigrationRecorder.Migration.objects.filter(app='core').delete()
        MigrationRecorder.Migration.objects.filter(app='great_international').delete()
        MigrationRecorder.Migration.objects.filter(app='export_readiness').delete()
