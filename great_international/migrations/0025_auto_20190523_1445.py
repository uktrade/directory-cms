# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-05-23 14:45
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('great_international', '0024_capitalinvestopportunitylistingpage_capitalinvestopportunitypage_capitalinvestregionalsectorpage_cap'),
    ]

    operations = [
        migrations.CreateModel(
            name='SectorRelatedOpportunities',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('opportunity', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='great_international.CapitalInvestOpportunityPage')),
                ('page', modelcluster.fields.ParentalKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='added_opportunities', to='great_international.CapitalInvestRegionalSectorPage')),
                ('page_ar', modelcluster.fields.ParentalKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='added_opportunities', to='great_international.CapitalInvestRegionalSectorPage')),
                ('page_de', modelcluster.fields.ParentalKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='added_opportunities', to='great_international.CapitalInvestRegionalSectorPage')),
                ('page_en_gb', modelcluster.fields.ParentalKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='added_opportunities', to='great_international.CapitalInvestRegionalSectorPage')),
                ('page_es', modelcluster.fields.ParentalKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='added_opportunities', to='great_international.CapitalInvestRegionalSectorPage')),
                ('page_fr', modelcluster.fields.ParentalKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='added_opportunities', to='great_international.CapitalInvestRegionalSectorPage')),
                ('page_ja', modelcluster.fields.ParentalKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='added_opportunities', to='great_international.CapitalInvestRegionalSectorPage')),
                ('page_pt', modelcluster.fields.ParentalKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='added_opportunities', to='great_international.CapitalInvestRegionalSectorPage')),
                ('page_zh_hans', modelcluster.fields.ParentalKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='added_opportunities', to='great_international.CapitalInvestRegionalSectorPage')),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
        ),
        migrations.RemoveField(
            model_name='capitalinvestsectorrelatedpagesummary',
            name='added_related_pages',
        ),
        migrations.RemoveField(
            model_name='capitalinvestsectorrelatedpagesummary',
            name='page',
        ),
        migrations.RemoveField(
            model_name='capitalinvestsectorrelatedpagesummary',
            name='page_ar',
        ),
        migrations.RemoveField(
            model_name='capitalinvestsectorrelatedpagesummary',
            name='page_de',
        ),
        migrations.RemoveField(
            model_name='capitalinvestsectorrelatedpagesummary',
            name='page_en_gb',
        ),
        migrations.RemoveField(
            model_name='capitalinvestsectorrelatedpagesummary',
            name='page_es',
        ),
        migrations.RemoveField(
            model_name='capitalinvestsectorrelatedpagesummary',
            name='page_fr',
        ),
        migrations.RemoveField(
            model_name='capitalinvestsectorrelatedpagesummary',
            name='page_ja',
        ),
        migrations.RemoveField(
            model_name='capitalinvestsectorrelatedpagesummary',
            name='page_pt',
        ),
        migrations.RemoveField(
            model_name='capitalinvestsectorrelatedpagesummary',
            name='page_zh_hans',
        ),
        migrations.DeleteModel(
            name='CapitalInvestSectorRelatedPageSummary',
        ),
    ]
