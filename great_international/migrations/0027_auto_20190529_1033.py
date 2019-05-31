# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-05-29 10:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('great_international', '0026_auto_20190528_0826'),
    ]

    operations = [
        migrations.AlterField(
            model_name='capitalinvestopportunitypage',
            name='project_background_intro',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='capitalinvestopportunitypage',
            name='project_background_intro_ar',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='capitalinvestopportunitypage',
            name='project_background_intro_de',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='capitalinvestopportunitypage',
            name='project_background_intro_en_gb',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='capitalinvestopportunitypage',
            name='project_background_intro_es',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='capitalinvestopportunitypage',
            name='project_background_intro_fr',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='capitalinvestopportunitypage',
            name='project_background_intro_ja',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='capitalinvestopportunitypage',
            name='project_background_intro_pt',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='capitalinvestopportunitypage',
            name='project_background_intro_zh_hans',
            field=models.TextField(blank=True, null=True),
        ),
    ]
