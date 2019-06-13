# -*- coding: utf-8 -*-
# Generated by Django 1.11.21 on 2019-06-13 13:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('great_international', '0040_auto_20190612_1521'),
    ]

    operations = [
        migrations.AddField(
            model_name='capitalinvestopportunitylistingpage',
            name='hero_title',
            field=models.CharField(default='Opportunities', max_length=255),
        ),
        migrations.AddField(
            model_name='capitalinvestopportunitylistingpage',
            name='hero_title_ar',
            field=models.CharField(default='Opportunities', max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='capitalinvestopportunitylistingpage',
            name='hero_title_de',
            field=models.CharField(default='Opportunities', max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='capitalinvestopportunitylistingpage',
            name='hero_title_en_gb',
            field=models.CharField(default='Opportunities', max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='capitalinvestopportunitylistingpage',
            name='hero_title_es',
            field=models.CharField(default='Opportunities', max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='capitalinvestopportunitylistingpage',
            name='hero_title_fr',
            field=models.CharField(default='Opportunities', max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='capitalinvestopportunitylistingpage',
            name='hero_title_ja',
            field=models.CharField(default='Opportunities', max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='capitalinvestopportunitylistingpage',
            name='hero_title_pt',
            field=models.CharField(default='Opportunities', max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='capitalinvestopportunitylistingpage',
            name='hero_title_zh_hans',
            field=models.CharField(default='Opportunities', max_length=255, null=True),
        ),
    ]
