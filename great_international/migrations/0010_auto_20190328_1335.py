# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-03-28 13:35
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0021_image_file_hash'),
        ('great_international', '0009_auto_20190328_1237'),
    ]

    operations = [
        migrations.AddField(
            model_name='internationalcapitalinvestlandingpage',
            name='hero_image',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image'),
        ),
        migrations.AlterField(
            model_name='internationalcapitalinvestlandingpage',
            name='region_ops_section_intro',
            field=models.CharField(blank=True, max_length=255, verbose_name='Region opportunities section intro'),
        ),
        migrations.AlterField(
            model_name='internationalcapitalinvestlandingpage',
            name='region_ops_section_title',
            field=models.CharField(max_length=255, verbose_name='Region opportunities section title'),
        ),
    ]
