# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-07-17 08:56
from __future__ import unicode_literals

from django.db import migrations


NUMBER_MAPPING = {
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six',
    7: 'seven'
}


def migrate_sector_pages_streamfields(apps, schema_editor):

    SectorPage = apps.get_model('invest', 'SectorPage')
    for page in SectorPage.objects.all():
        if page.pullout:
            page.pullout_text = page.pullout[0].value['text']
            page.pullout_stat = page.pullout[0].value['stat']
            page.pullout_stat_text = page.pullout[0].value['stat_text']

        for index, subsection in enumerate(page.subsections, 1):
            # title is always present
            field_name = 'subsection_title_{}_en_gb'.format(
                NUMBER_MAPPING[index]
            )
            setattr(page, field_name, subsection.value['title'])
            if 'content' in subsection.value:
                field_name = 'subsection_content_{}_en_gb'.format(
                    NUMBER_MAPPING[index]
                )
                setattr(page, field_name, subsection.value['content'])
            else:
                field_name = 'subsection_info_{}_en_gb'.format(
                    NUMBER_MAPPING[index]
                )
                setattr(page, field_name, subsection.value['info'])
                field_name = 'subsection_map_{}_en_gb_id'.format(
                    NUMBER_MAPPING[index]
                )
                setattr(page, field_name, subsection.value['map'])
        page.save()


def migrate_setup_guide_pages_streamfields(apps, schema_editor):

    SetupGuidePage = apps.get_model('invest', 'SetupGuidePage')
    for page in SetupGuidePage.objects.all():
        for index, subsection in enumerate(page.subsections, 1):
            field_name = 'subsection_title_{}_en_gb'.format(
                NUMBER_MAPPING[index]
            )
            setattr(page, field_name, subsection.value['title'])
            field_name = 'subsection_content_{}_en_gb'.format(
                NUMBER_MAPPING[index]
            )
            setattr(page, field_name, subsection.value['content'])
        page.save()


def migrate_home_page_streamfields(apps, schema_editor):

    InvestHomePage = apps.get_model('invest', 'InvestHomePage')
    page = InvestHomePage.objects.first()
    if page:
        for index, subsection in enumerate(page.subsections, 1):
            field_name = 'subsection_title_{}_en_gb'.format(
                NUMBER_MAPPING[index]
            )
            setattr(page, field_name, subsection.value['title'])
            field_name = 'subsection_content_{}_en_gb'.format(
                NUMBER_MAPPING[index]
            )
            setattr(page, field_name, subsection.value['content'])
        page.save()


class Migration(migrations.Migration):

    dependencies = [
        ('invest', '0003_auto_20180717_1814'),
    ]

    operations = [
        migrations.RunPython(
            migrate_sector_pages_streamfields,
            reverse_code=migrations.RunPython.noop
        ),
        migrations.RunPython(
            migrate_setup_guide_pages_streamfields,
            reverse_code=migrations.RunPython.noop
        ),
        migrations.RunPython(
            migrate_home_page_streamfields,
            reverse_code=migrations.RunPython.noop
        )
    ]
