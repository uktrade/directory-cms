# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-09-20 09:41
from __future__ import unicode_literals

import core.fields
import core.validators
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('invest', '0024_highpotentialopportunitydetailpage_testimonial_background'),
    ]

    operations = [
        migrations.AlterField(
            model_name='highpotentialopportunitydetailpage',
            name='testimonial',
            field=core.fields.MarkdownField(blank=True, validators=[core.validators.slug_hyperlinks]),
        ),
    ]
