# Generated by Django 2.2.24 on 2021-09-16 15:24

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0059_apply_collection_ordering'),
        ('contenttypes', '0002_remove_content_type_name'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('great_international', '0117_refactor_atlas_general_content_text_block'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='InvestHighPotentialOpportunityFormPage',
            new_name='ForeignDirectInvestmentFormPage',
        ),
        migrations.RenameModel(
            old_name='InvestHighPotentialOpportunityFormSuccessPage',
            new_name='ForeignDirectInvestmentFormSuccessPage',
        ),
    ]
