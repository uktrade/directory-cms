# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-06-05 15:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0021_image_file_hash'),
        ('great_international', '0031_investhighpotentialopportunitydetailpage_investhighpotentialopportunityformpage_investhighpotentialo'),
    ]

    operations = [
        migrations.AddField(
            model_name='investinternationalhomepage',
            name='how_we_help_icon_six',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image'),
        ),
    ]
