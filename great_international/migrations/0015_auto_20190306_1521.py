# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-03-06 15:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('great_international', '0014_auto_20190304_1215'),
    ]

    operations = [
        migrations.AlterField(
            model_name='internationalsectorpage',
            name='sub_heading',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
