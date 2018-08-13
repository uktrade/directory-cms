# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-08-13 14:29
from __future__ import unicode_literals

from directory_constants.constants import cms
from django.db import migrations


MODELS_CLASS_NAMES = (
    'SectorLandingPage',
    'RegionLandingPage',
    'SectorPage',
    'SetupGuideLandingPage',
    'SetupGuidePage',
    'InvestHomePage',
    'InfoPage'
)


def add_service_to_pages(apps, schema_editor):
    Service = apps.get_model('core', 'Service')
    for class_name in MODELS_CLASS_NAMES:
        model_class = apps.get_model('invest', class_name)
        for page in model_class.objects.all():
            Service.objects.get_or_create(
                name=cms.INVEST,
                page=page
            )


def remove_service_from_page(apps, schema_editor):
    Service = apps.get_model('core', 'Service')
    Service.objects.filter(name=cms.INVEST).delete()


class Migration(migrations.Migration):

    dependencies = [
        ('invest', '0007_auto_20180719_1414'),
        ('core', '0007_auto_20180809_1215')
    ]

    operations = [
        migrations.RunPython(
            add_service_to_pages,
            reverse_code=remove_service_from_page
        )
    ]
