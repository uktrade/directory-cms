from django.conf import settings
from django.core.management.commands.migrate import Command as MigrateCommand

from core.management.commands import helpers


class Command(helpers.ExclusiveDistributedHandleMixin, MigrateCommand):
    lock_id = 'migrations'

    def handle(self, *args, **options):
        if not settings.FEATURE_FLAGS['SKIP_MIGRATE']:
            super().handle(*args, **options)
