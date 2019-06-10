from directory_constants.constants import cms
from modeltranslation.utils import build_localized_fieldname
from wagtail.core.models import Page

from django.conf import settings
from django.core.management.base import BaseCommand

from core import filters


class Command(BaseCommand):

    # Look for translated field value in this order
    preferred_source_fields = (
        'article_title',
        'landing_page_title',
        'campaign_heading',
        'display_title',
        'heading',
        'hero_title',
    )

    def add_arguments(self, parser):
        parser.add_argument(
            '--dryrun', action='store_true', dest='dryrun', default=False,
            help="Dry run -- don't change anything.")

    def handle(self, *args, **options):
        dryrun = False
        if options['dryrun']:
            self.stdout.write("Will do a dry run.")
            dryrun = True

        queryset = filters.ServiceNameFilter().filter_service_name(
            queryset=Page.objects.all(),
            name=None,
            value=cms.GREAT_INTERNATIONAL,
        )
        for page in queryset.specific():
            print('--------------------------------------------------------')
            print("{}: {} (ID:{})".format(
                 page.__class__.__name__, page, page.id
            ))
            print('--------------------------------------------------------\n')
            for language_code, language_name in settings.LANGUAGES:
                title_field_for_language = build_localized_fieldname(
                    'title', language_code)
                try:
                    title_value = getattr(page, title_field_for_language)
                except AttributeError:
                    continue

                if title_value:
                    print("{} title already set to: '{}'\n".format(
                        language_name, title_value))
                    continue

                print("Looking for {} title value...".format(language_name))
                no_fields_found = True
                for fieldname in self.preferred_source_fields:
                    fieldname_for_language = build_localized_fieldname(
                        fieldname, language_code)
                    try:
                        value = getattr(page, fieldname_for_language)
                        no_fields_found = False
                        if value:
                            print("'{}' value looks usable: '{}'".format(
                                fieldname_for_language, value))
                            title_value = value
                            setattr(page, title_field_for_language, value)
                            if not dryrun:
                                page.save()
                                print('Page saved')
                            break
                        else:
                            print("'{}' value is blank :(".format(
                                fieldname_for_language))
                    except AttributeError:
                        pass
                if no_fields_found:
                    print('No suitable fields could be found')
                print()
