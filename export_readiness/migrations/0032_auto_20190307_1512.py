# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-03-07 15:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('export_readiness', '0031_internationallandingpage_squashed_0050_auto_20190219_1633'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articlepage',
            name='article_teaser',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
