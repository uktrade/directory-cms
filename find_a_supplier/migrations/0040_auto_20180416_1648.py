# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-04-16 16:48
from __future__ import unicode_literals

from django.db import migrations


def sync_page_translation_fields(apps, schema_editor):
    IndustryPage = apps.get_model('find_a_supplier', 'IndustryPage')
    for page in IndustryPage.objects.all():
        page.search_filter_sector = [page.sector_value]
        page.save()


class Migration(migrations.Migration):

    dependencies = [
        ('find_a_supplier', '0039_auto_20180416_1648'),
    ]

    operations = [
        migrations.RunPython(
            sync_page_translation_fields, migrations.RunPython.noop,
            elidable=True
        )
    ]
