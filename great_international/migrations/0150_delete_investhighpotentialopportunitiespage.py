# Generated by Django 2.2.24 on 2021-12-14 11:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0059_apply_collection_ordering'),
        ('wagtailforms', '0004_add_verbose_name_plural'),
        ('great_international', '0149_delete_investhighpotentialopportunitydetailpage'),
    ]

    operations = [
        migrations.DeleteModel(
            name='InvestHighPotentialOpportunitiesPage',
        ),
    ]