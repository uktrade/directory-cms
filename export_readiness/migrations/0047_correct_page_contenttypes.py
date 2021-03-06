# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-05-30 16:20
from __future__ import unicode_literals

from django.db import migrations


def migrate_forwards(apps, schema_editor):
    ContentType = apps.get_model('contenttypes', 'ContentType')
    Page = apps.get_model('wagtailcore', 'Page')

    homepage_ct, _ = ContentType.objects.get_or_create(app_label='export_readiness', model='homepage')
    homepageold_ct, _ = ContentType.objects.get_or_create(app_label='export_readiness', model='homepageold')

    Page.objects.filter(url_path='/export-readiness-app/').update(content_type=homepage_ct)
    Page.objects.filter(url_path='/export-readiness-app/home/').update(content_type=homepageold_ct)


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('export_readiness', '0046_rename_exportreadinessapp_to_homepage'),
    ]

    operations = [
        migrations.RunPython(migrate_forwards, migrations.RunPython.noop),
    ]
