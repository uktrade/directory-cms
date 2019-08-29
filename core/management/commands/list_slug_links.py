from django.core.management import BaseCommand
from django.core.management.base import no_translations
from wagtail.core.models import Page

from django.forms.models import model_to_dict
from django.urls import reverse


class Command(BaseCommand):
    help = 'List pages that contain hyperlinks using slugs to identify the target page'

    @no_translations
    def handle(self, *args, **options):
        for instance in Page.objects.all().specific():
            for value in model_to_dict(instance).values():
                if isinstance(value, str) and 'slug:' in value:
                    url = reverse('wagtailadmin_pages:edit', args=(instance.pk,))
                    self.stdout.write(self.style.WARNING(url))
                    break
