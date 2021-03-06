# Generated by Django 2.2.2 on 2019-07-18 11:51

import core.models
from django.db import migrations, models
import django.db.models.deletion
import great_international.panels.invest


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0041_group_collection_permissions_verbose_name_plural'),
        ('great_international', '0049_aboutditlandingpage_aboutditservicesfields_aboutditservicespage'),
    ]

    operations = [
        migrations.CreateModel(
            name='InvestHighPotentialOpportunitiesPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('service_name', models.CharField(choices=[('FIND_A_SUPPLIER', 'Find a Supplier'), ('EXPORT_READINESS', 'Export Readiness'), ('INVEST', 'Invest'), ('COMPONENTS', 'Components'), ('GREAT_INTERNATIONAL', 'Great International')], db_index=True, max_length=100, null=True)),
                ('uses_tree_based_routing', models.BooleanField(default=False, help_text="Allow this page's URL to be determined by its slug, and the slugs of its ancestors in the page tree.", verbose_name='tree-based routing enabled')),
            ],
            options={
                'abstract': False,
            },
            bases=(core.models.ExclusivePageMixin, 'wagtailcore.page', great_international.panels.invest.InvestHighPotentialOpportunitiesPagePanels),
        ),
    ]
