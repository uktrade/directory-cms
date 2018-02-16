from django.core.management.commands.migrate import Command as MigrateCommand

from core.management.commands import helpers


class Command(helpers.ExclusiveDistributedHandleMixin, MigrateCommand):
    lock_id = 'migrations'
