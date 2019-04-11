# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-04-11 10:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('great_international', '0017_merge_20190411_1027'),
    ]

    operations = [
        migrations.AddField(
            model_name='internationalhomepage',
            name='hero_cta_link_ar',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='internationalhomepage',
            name='hero_cta_link_de',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='internationalhomepage',
            name='hero_cta_link_en_gb',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='internationalhomepage',
            name='hero_cta_link_es',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='internationalhomepage',
            name='hero_cta_link_fr',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='internationalhomepage',
            name='hero_cta_link_ja',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='internationalhomepage',
            name='hero_cta_link_pt',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='internationalhomepage',
            name='hero_cta_link_pt_br',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='internationalhomepage',
            name='hero_cta_link_ru',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='internationalhomepage',
            name='hero_cta_link_zh_hans',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]