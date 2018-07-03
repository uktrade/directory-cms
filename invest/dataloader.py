import itertools
import json
import os

from django.conf import settings

from invest import models


class PageContentLoader:
    languages_codes = ('de', 'es', 'fr', 'pt', 'ar', 'ja', 'zh_cn')
    filename = None
    fields = None
    stream_fields = None
    model_class = None
    filtering_field_name = None

    def __init__(self):
        self.json_all_data = self.load_json_file(self.filename)
        self.translated_fields = self.generate_translated_fields_names(self.fields)

    @staticmethod
    def load_json_file(filename):
        file_full_path = os.path.join(
            settings.BASE_DIR,
            'invest/old_data',
            filename
        )
        with open(file_full_path) as json_file:
            data = json.load(json_file)
        return data

    def get_filtered_content(self, page):
        """Get the right content for page."""
        if len(self.json_all_data) == 1:
            return self.json_all_data[0]

        value = getattr(page, self.filtering_field_name)
        return list(filter(
            lambda x: x[self.filtering_field_name] == value,
            self.json_all_data
        ))[0]

    def generate_translated_fields_names(self, fields):
        return ('_'.join(language_field) for language_field in
                itertools.product(fields, self.languages_codes))

    def load_fields(self, page):
        for field_name in self.translated_fields:
            json_data = self.get_filtered_content(page)
            value = json_data[field_name]
            if value:
                value = value.encode().decode('utf-8')
            setattr(page, field_name, value)
        page.save()

    def load_streamfields(self, page):
        pass

    def run(self):
        pages = self.model_class.objects.all()
        for page in pages:
            self.load_fields(page)
            self.load_streamfields(page)


class HomePageLoader(PageContentLoader):
    filename = 'home.json'
    fields = (
        'heading',
        'sub_heading',
        'sector_title',
        'setup_guide_title',
        'setup_guide_lead_in',
        'how_we_help_title',
        'how_we_help_lead_in',
        'sector_button_text',
    )
    stream_fields = ('subsections', 'how_we_help')
    page = models.InvestHomePage

    def load_streamfields(self, page):

        for field_name in self.stream_fields:
            streamfield_in_english = getattr(page, field_name)
            for translated_field_name in self.generate_translated_fields_names(
                    (field_name,)
            ):

                # set the translated content to the English content first,
                # so we have a reference to images and pages
                setattr(page, translated_field_name, streamfield_in_english)

                # now modify the streamfield with the translated content
                # this assumes that the streamfield blocks and the json blocks
                # are in the same order
                json_data = self.get_filtered_content(page)
                translated_content = json.loads(
                    json_data[translated_field_name]
                )
                translated_streamfield = getattr(page, translated_field_name)
                for block, content in zip(translated_streamfield,
                                          translated_content):
                    if field_name == 'subsections':
                        content = content['value']
                        block.value['content'] = content['content'].encode()\
                            .decode('utf-8')
                        block.value['title'] = content['title'].encode()\
                            .decode('utf-8')
                    else:
                        content = content['value']
                        block.value['text'] = content['text'].encode() \
                            .decode('utf-8')
        page.save()


class SetupGuideLandingPageLoader(PageContentLoader):
    filename = 'setup_guide_landing.json'
    model_class = models.SetupGuideLandingPage
    fields = (
        'heading',
        'sub_heading',
        'lead_in'
    )


class SectorLandingPageLoader(PageContentLoader):
    filename = 'sector_landing.json'
    model_class = models.SectorLandingPage
    fields = (
        'heading',
    )


class RegionLandingPageLoader(PageContentLoader):
    filename = 'region_landing.json'
    model_class = models.RegionLandingPage
    fields = (
        'heading',
    )


def load_all():
    HomePageLoader().run()
    SetupGuideLandingPageLoader().run()
    SectorLandingPageLoader().run()
    RegionLandingPageLoader().run()


if __name__ == '__main__':
    load_all()
