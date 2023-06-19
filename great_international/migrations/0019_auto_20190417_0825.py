# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-04-17 08:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('great_international', '0018_auto_20190411_1028'),
    ]

    operations = [
        migrations.AddField(
            model_name='greatinternationalapp',
            name='uses_tree_based_routing',
            field=models.BooleanField(default=False, help_text="Allow this page's URL to be determined by its slug, and the slugs of its ancestors in the page tree.", verbose_name='tree-based routing enabled'),
        ),
        migrations.AddField(
            model_name='internationalarticlelistingpage',
            name='uses_tree_based_routing',
            field=models.BooleanField(default=False, help_text="Allow this page's URL to be determined by its slug, and the slugs of its ancestors in the page tree.", verbose_name='tree-based routing enabled'),
        ),
        migrations.AddField(
            model_name='internationalarticlepage',
            name='uses_tree_based_routing',
            field=models.BooleanField(default=False, help_text="Allow this page's URL to be determined by its slug, and the slugs of its ancestors in the page tree.", verbose_name='tree-based routing enabled'),
        ),
        migrations.AddField(
            model_name='internationalcampaignpage',
            name='uses_tree_based_routing',
            field=models.BooleanField(default=False, help_text="Allow this page's URL to be determined by its slug, and the slugs of its ancestors in the page tree.", verbose_name='tree-based routing enabled'),
        ),
        migrations.AddField(
            model_name='internationalcuratedtopiclandingpage',
            name='uses_tree_based_routing',
            field=models.BooleanField(default=False, help_text="Allow this page's URL to be determined by its slug, and the slugs of its ancestors in the page tree.", verbose_name='tree-based routing enabled'),
        ),
        migrations.AddField(
            model_name='internationalguidelandingpage',
            name='uses_tree_based_routing',
            field=models.BooleanField(default=False, help_text="Allow this page's URL to be determined by its slug, and the slugs of its ancestors in the page tree.", verbose_name='tree-based routing enabled'),
        ),
        migrations.AddField(
            model_name='internationalhomepage',
            name='uses_tree_based_routing',
            field=models.BooleanField(default=False, help_text="Allow this page's URL to be determined by its slug, and the slugs of its ancestors in the page tree.", verbose_name='tree-based routing enabled'),
        ),
        migrations.AddField(
            model_name='internationallocalisedfolderpage',
            name='uses_tree_based_routing',
            field=models.BooleanField(default=False, help_text="Allow this page's URL to be determined by its slug, and the slugs of its ancestors in the page tree.", verbose_name='tree-based routing enabled'),
        ),
        migrations.AddField(
            model_name='internationalregionpage',
            name='uses_tree_based_routing',
            field=models.BooleanField(default=False, help_text="Allow this page's URL to be determined by its slug, and the slugs of its ancestors in the page tree.", verbose_name='tree-based routing enabled'),
        ),
        migrations.AddField(
            model_name='internationalsectorpage',
            name='uses_tree_based_routing',
            field=models.BooleanField(default=False, help_text="Allow this page's URL to be determined by its slug, and the slugs of its ancestors in the page tree.", verbose_name='tree-based routing enabled'),
        ),
        migrations.AddField(
            model_name='internationaltopiclandingpage',
            name='uses_tree_based_routing',
            field=models.BooleanField(default=False, help_text="Allow this page's URL to be determined by its slug, and the slugs of its ancestors in the page tree.", verbose_name='tree-based routing enabled'),
        ),
    ]