# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-02-14 20:04
from __future__ import unicode_literals

from django.core.management import call_command
from django.db import migrations


def sync_page_translation_fields(apps, schema_editor):
    call_command('sync_page_translation_fields', '--noinput')


class Migration(migrations.Migration):

    dependencies = [
        ('find_a_supplier', '0012_auto_20180313_1155'),
    ]

    operations = [
        migrations.RunPython(
            sync_page_translation_fields, migrations.RunPython.noop
        )
    ]
