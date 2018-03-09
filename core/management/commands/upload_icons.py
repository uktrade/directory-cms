import json
import os

from django.core.management import BaseCommand
from django.conf import settings
from django.core.files.storage import default_storage

from core import constants

class Command(BaseCommand):

    def handle(self, *args, **options):
        icon_paths = [
            constants.NETWORK_ICON_PATH,
            constants.INNOVATION_ICON_PATH,
            constants.INVESTMENT_ICON_PATH,
            constants.QUALITY_ICON_PATH,
            constants.RESEARCH_ICON_PATH,
            constants.SKILLS_ICON_PATH,
        ]
        for icon_path in icon_paths:
            with open(os.path.join('core/static', icon_path), 'rb') as f:
                default_storage.save(icon_path, f)
