# Generated by Django 2.2.24 on 2021-11-17 15:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0059_apply_collection_ordering'),
        ('wagtailforms', '0004_add_verbose_name_plural'),
        ('export_readiness', '0076_delete_performancedashboardpage'),
    ]

    operations = [
        migrations.DeleteModel(
            name='GetFinancePage',
        ),
    ]