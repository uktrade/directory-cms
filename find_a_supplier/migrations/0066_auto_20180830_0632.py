# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-08-30 06:32
from __future__ import unicode_literals

from django.db import migrations


service_name = 'FIND_A_SUPPLIER'

model_names = [
	'IndustryPage',
	'IndustryLandingPage',
	'IndustryArticlePage',
	'LandingPage',
	'IndustryContactPage',
]


def populate_historic_slug_service_name(apps, schema_editor):
    HistoricSlug = apps.get_model('core', 'HistoricSlug')
    for model_name in model_names:
        historic_model = apps.get_model('find_a_supplier', model_name)
        for page in historic_model.objects.all():
            page.service_name = service_name
            page.save()
            HistoricSlug.objects.get_or_create(
                slug=page.slug,
                page=page,
                defaults={
                    'service_name': service_name,
                }
            )


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0019_merge_20180829_0939'),
        ('find_a_supplier', '0065_auto_20180829_1027'),
    ]

    operations = [
        migrations.RunPython(
           populate_historic_slug_service_name,
           reverse_code=migrations.RunPython.noop
        )
    ]
