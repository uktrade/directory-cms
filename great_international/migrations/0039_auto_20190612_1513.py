# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-06-12 15:13
from __future__ import unicode_literals

import core.model_fields
import core.validators
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('great_international', '0038_merge_20190611_1253'),
    ]

    operations = [
        migrations.AlterField(
            model_name='capitalinvestopportunitypage',
            name='project_background_intro',
            field=core.model_fields.MarkdownField(validators=[core.validators.slug_hyperlinks]),
        ),
        migrations.AlterField(
            model_name='capitalinvestopportunitypage',
            name='project_background_intro_ar',
            field=core.model_fields.MarkdownField(null=True, validators=[core.validators.slug_hyperlinks]),
        ),
        migrations.AlterField(
            model_name='capitalinvestopportunitypage',
            name='project_background_intro_de',
            field=core.model_fields.MarkdownField(null=True, validators=[core.validators.slug_hyperlinks]),
        ),
        migrations.AlterField(
            model_name='capitalinvestopportunitypage',
            name='project_background_intro_en_gb',
            field=core.model_fields.MarkdownField(null=True, validators=[core.validators.slug_hyperlinks]),
        ),
        migrations.AlterField(
            model_name='capitalinvestopportunitypage',
            name='project_background_intro_es',
            field=core.model_fields.MarkdownField(null=True, validators=[core.validators.slug_hyperlinks]),
        ),
        migrations.AlterField(
            model_name='capitalinvestopportunitypage',
            name='project_background_intro_fr',
            field=core.model_fields.MarkdownField(null=True, validators=[core.validators.slug_hyperlinks]),
        ),
        migrations.AlterField(
            model_name='capitalinvestopportunitypage',
            name='project_background_intro_ja',
            field=core.model_fields.MarkdownField(null=True, validators=[core.validators.slug_hyperlinks]),
        ),
        migrations.AlterField(
            model_name='capitalinvestopportunitypage',
            name='project_background_intro_pt',
            field=core.model_fields.MarkdownField(null=True, validators=[core.validators.slug_hyperlinks]),
        ),
        migrations.AlterField(
            model_name='capitalinvestopportunitypage',
            name='project_background_intro_zh_hans',
            field=core.model_fields.MarkdownField(null=True, validators=[core.validators.slug_hyperlinks]),
        ),
    ]