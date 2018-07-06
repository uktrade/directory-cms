import itertools
import json
import os
from django.conf import settings
from modeltranslation.utils import build_localized_fieldname

from invest import models


class PageContentLoader:
    languages_codes = ('de', 'es', 'fr', 'pt', 'ar', 'ja', 'zh_hans')
    filename = None
    fields = None
    stream_fields = None
    model_class = None
    filtering_field_name = None

    def __init__(self):
        self.json_all_data = self.load_json_file(self.filename)
        self.translated_fields = self.generate_translated_fields_names(
            self.fields
        )

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

        value = getattr(page, self.filtering_field_name + '_en_gb')
        return list(filter(
            lambda x: x[self.filtering_field_name].encode().decode(
                'utf-8') == value,
            self.json_all_data
        ))[0]

    def generate_translated_fields_names(self, fields):
        return (build_localized_fieldname(field, lang) for field, lang in
                itertools.product(fields, self.languages_codes))

    def load_fields(self, page):
        json_data = self.get_filtered_content(page)
        for field_name in self.translated_fields:
            value = json_data[field_name]
            if value:
                value = value.encode().decode('utf-8')
            setattr(page, field_name, value)
        self.save_revision_and_publish(page)

    def load_streamfields(self, page):
        pass

    @staticmethod
    def save_revision_and_publish(page):
        page.save()

    @staticmethod
    def get_streamfield_content_in_english(page, field_name):
        field_name = field_name + '_en_gb'
        return getattr(page, field_name)

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
    model_class = models.InvestHomePage

    def load_streamfields(self, page):

        for field_name in self.stream_fields:
            streamfield_in_english = self.get_streamfield_content_in_english(
                page=page,
                field_name=field_name
            )
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
            self.save_revision_and_publish(page)


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


class SectorPageLoader(PageContentLoader):
    filename = 'sector.json'
    model_class = models.SectorPage
    fields = (
        'description',
        'heading',
        'pullout',
        'subsections'
    )
    filtering_field_name = 'heading'
    stream_fields = ('pullout', 'subsections')


    def load_streamfields(self, page):
        for field_name in self.stream_fields:
            streamfield_in_english = self.get_streamfield_content_in_english(
                page=page,
                field_name=field_name
            )
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
                        block_type = content['type']
                        content = content['value']
                        if block_type == 'markdown':
                            block.value['content'] = content['content']\
                                .encode().decode('utf-8')
                            block.value['title'] = content['title']\
                                .encode().decode('utf-8')
                        else:
                            block.value['info'] = content['info'] \
                                .encode().decode('utf-8')
                            block.value['title'] = content['title'] \
                                .encode().decode('utf-8')
                    else:
                        content = content['value']
                        block.value['text'] = content['text'].encode() \
                            .decode('utf-8')
                        block.value['stat'] = content['stat'].encode() \
                            .decode('utf-8')
                        block.value['stat_text'] = content['stat_text'].encode() \
                            .decode('utf-8')
            self.save_revision_and_publish(page)


class SetupGuidePageLoader(PageContentLoader):
    filename = 'setup_guide.json'
    model_class = models.SetupGuidePage
    fields = (
        'description',
        'heading',
        'sub_heading',
        'subsections',
    )
    filtering_field_name = 'heading'
    stream_fields = ('subsections', )

    def load_streamfields(self, page):
        import pudb; pu.db
        field_name = 'subsections'
        streamfield_in_english = self.get_streamfield_content_in_english(
            page=page,
            field_name=field_name
        )
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
                content = content['value']
                block.value['content'] = content['content'].encode()\
                    .decode('utf-8')
                block.value['title'] = content['title'].encode()\
                    .decode('utf-8')
        self.save_revision_and_publish(page)


class InfoPageLoader(PageContentLoader):
    filename = 'info.json'
    model_class = models.InfoPage
    fields = (
        'content',
    )
    filtering_field_name = 'content'




def load_all():
    HomePageLoader().run()
    SetupGuideLandingPageLoader().run()
    SectorLandingPageLoader().run()
    RegionLandingPageLoader().run()
    SectorPageLoader().run()
    SetupGuidePageLoader().run()
    InfoPageLoader().run()


if __name__ == '__main__':
    load_all()


