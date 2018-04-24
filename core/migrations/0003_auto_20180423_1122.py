# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-04-23 11:22
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0040_page_draft_title'),
        ('core', '0002_auto_20180307_1748'),
    ]

    operations = [
        migrations.CreateModel(
            name='HistoricSlug',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField()),
                ('page', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wagtailcore.Page')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='historicslug',
            unique_together=set([('slug', 'page')]),
        ),
    ]
