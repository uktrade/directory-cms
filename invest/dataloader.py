import itertools
import json
import os
from django.conf import settings
from django.core.exceptions import ValidationError
from modeltranslation.utils import build_localized_fieldname

from invest import models


class PageContentLoader:
    languages_codes = ('de', 'es', 'fr', 'pt', 'ar', 'ja', 'zh_hans')
    number_mapping = {
        1: 'one',
        2: 'two',
        3: 'three',
        4: 'four',
        5: 'five',
        6: 'six',
        7: 'seven'
    }
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
        content = list(filter(
            lambda x: x[self.filtering_field_name].encode().decode(
                'utf-8') == value,
            self.json_all_data
        ))
        if content:
            return content[0]

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
        try:
            page.save()
        except ValidationError:
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
    model_class = models.InvestHomePage

    def load_streamfields(self, page):

        for lang_code in self.languages_codes:
            streamfield_name = 'subsections_{lang_code}'.format(
                lang_code=lang_code
            )
            json_data = self.get_filtered_content(page)
            translated_content = json.loads(json_data[streamfield_name])
            for index, content in enumerate(translated_content, 1):
                content = content['value']
                field = 'subsection_content_{number}_{lang_code}'.format(
                    number=self.number_mapping[index],
                    lang_code=lang_code
                )
                setattr(
                    page,
                    field,
                    content['content'].encode().decode('utf-8')
                )
                field = 'subsection_title_{number}_{lang_code}'.format(
                    number=self.number_mapping[index],
                    lang_code=lang_code
                )
                setattr(
                    page,
                    field,
                    content['title'].encode().decode('utf-8')
                )
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
    )
    filtering_field_name = 'heading'

    def load_streamfields(self, page):
        for lang_code in self.languages_codes:
            json_data = self.get_filtered_content(page)
            if json_data:
                # pullout
                streamfield_name = 'pullout_{lang_code}'.format(
                    lang_code=lang_code
                )
                translated_content = json.loads(json_data[streamfield_name])
                if translated_content:
                    content = translated_content[0]['value']
                    setattr(
                        page,
                        'pullout_text_{}'.format(lang_code),
                        content['text'].encode().decode('utf-8')
                    )
                    setattr(
                        page,
                        'pullout_stat_{}'.format(lang_code),
                        content['stat'].encode().decode('utf-8')
                    )
                    setattr(
                        page,
                        'pullout_stat_text_{}'.format(lang_code),
                        content['stat_text'].encode().decode('utf-8')
                    )

                # subsections
                streamfield_name = 'subsections_{lang_code}'.format(
                    lang_code=lang_code
                )
                translated_content = json.loads(json_data[streamfield_name])
                for index, content in enumerate(translated_content, 1):
                    block_type = content['type']
                    content = content['value']
                    field = 'subsection_title_{number}_{lang_code}'.format(
                        number=self.number_mapping[index],
                        lang_code=lang_code
                    )
                    setattr(
                        page,
                        field,
                        content['title'].encode().decode('utf-8')
                    )
                    if block_type == 'markdown':
                        field = 'subsection_content_' \
                                '{number}_{lang_code}'.format(
                                    number=self.number_mapping[index],
                                    lang_code=lang_code
                                )
                        setattr(
                            page,
                            field,
                            content['content'].encode().decode('utf-8')
                        )
                    else:
                        field = 'subsection_content_' \
                                '{number}_{lang_code}'.format(
                                    number=self.number_mapping[index],
                                    lang_code=lang_code
                                )
                        setattr(
                            page,
                            field,
                            content['info'].encode().decode('utf-8')
                        )
                        # image
                        image = getattr(
                            page,
                            'subsection_map_{number}_en_gb_id'.format(
                                number=self.number_mapping[index],
                            )
                        )
                        setattr(
                            page,
                            'subsection_map_{number}_{lang_code}_id'.format(
                                number=self.number_mapping[index],
                                lang_code=lang_code
                            ),
                            image
                        )
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

    def load_streamfields(self, page):
        for lang_code in self.languages_codes:
            streamfield_name = 'subsections_{lang_code}'.format(
                lang_code=lang_code
            )
            json_data = self.get_filtered_content(page)
            translated_content = json.loads(json_data[streamfield_name])
            for index, content in enumerate(translated_content, 1):
                content = content['value']
                field = 'subsection_content_{number}_{lang_code}'.format(
                    number=self.number_mapping[index],
                    lang_code=lang_code
                )
                setattr(
                    page,
                    field,
                    content['content'].encode().decode('utf-8')
                )
                field = 'subsection_title_{number}_{lang_code}'.format(
                    number=self.number_mapping[index],
                    lang_code=lang_code
                )
                setattr(
                    page,
                    field,
                    content['title'].encode().decode('utf-8')
                )
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
