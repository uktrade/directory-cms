# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-08-23 20:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0015_breadcrumb'),
    ]

    operations = [
        migrations.AddField(
            model_name='breadcrumb',
            name='label_ar',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='breadcrumb',
            name='label_de',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='breadcrumb',
            name='label_en_gb',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='breadcrumb',
            name='label_es',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='breadcrumb',
            name='label_fr',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='breadcrumb',
            name='label_ja',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='breadcrumb',
            name='label_pt',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='breadcrumb',
            name='label_pt_br',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='breadcrumb',
            name='label_ru',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='breadcrumb',
            name='label_zh_hans',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
