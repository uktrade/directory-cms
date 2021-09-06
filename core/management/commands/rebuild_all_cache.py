from django.core.management import BaseCommand
from core.cache import rebuild_all_cache


class Command(BaseCommand):
    help = 'Rebuild the redis cache'

    def handle(self, *args, **options):
        rebuild_all_cache()
