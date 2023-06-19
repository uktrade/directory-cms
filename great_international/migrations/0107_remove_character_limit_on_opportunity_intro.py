# Generated by Django 2.2.24 on 2021-09-08 17:00

import core.model_fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('great_international', '0106_update_related_sector_model_to_use_new_models'),
    ]

    operations = [
        migrations.AlterField(
            model_name='investmentopportunitypage',
            name='introduction',
            field=core.model_fields.MarkdownField(help_text='A single paragraph to introduce the opportunity – what is the vision / ambition of the opportunity, timeline and where relevant, procurement method. What type of investor is this suitable for? Where is it and why is that important? Further detail can be provided in the “The Opportunity” section.'),
        ),
        migrations.AlterField(
            model_name='investmentopportunitypage',
            name='introduction_ar',
            field=core.model_fields.MarkdownField(help_text='A single paragraph to introduce the opportunity – what is the vision / ambition of the opportunity, timeline and where relevant, procurement method. What type of investor is this suitable for? Where is it and why is that important? Further detail can be provided in the “The Opportunity” section.', null=True),
        ),
        migrations.AlterField(
            model_name='investmentopportunitypage',
            name='introduction_de',
            field=core.model_fields.MarkdownField(help_text='A single paragraph to introduce the opportunity – what is the vision / ambition of the opportunity, timeline and where relevant, procurement method. What type of investor is this suitable for? Where is it and why is that important? Further detail can be provided in the “The Opportunity” section.', null=True),
        ),
        migrations.AlterField(
            model_name='investmentopportunitypage',
            name='introduction_en_gb',
            field=core.model_fields.MarkdownField(help_text='A single paragraph to introduce the opportunity – what is the vision / ambition of the opportunity, timeline and where relevant, procurement method. What type of investor is this suitable for? Where is it and why is that important? Further detail can be provided in the “The Opportunity” section.', null=True),
        ),
        migrations.AlterField(
            model_name='investmentopportunitypage',
            name='introduction_es',
            field=core.model_fields.MarkdownField(help_text='A single paragraph to introduce the opportunity – what is the vision / ambition of the opportunity, timeline and where relevant, procurement method. What type of investor is this suitable for? Where is it and why is that important? Further detail can be provided in the “The Opportunity” section.', null=True),
        ),
        migrations.AlterField(
            model_name='investmentopportunitypage',
            name='introduction_fr',
            field=core.model_fields.MarkdownField(help_text='A single paragraph to introduce the opportunity – what is the vision / ambition of the opportunity, timeline and where relevant, procurement method. What type of investor is this suitable for? Where is it and why is that important? Further detail can be provided in the “The Opportunity” section.', null=True),
        ),
        migrations.AlterField(
            model_name='investmentopportunitypage',
            name='introduction_ja',
            field=core.model_fields.MarkdownField(help_text='A single paragraph to introduce the opportunity – what is the vision / ambition of the opportunity, timeline and where relevant, procurement method. What type of investor is this suitable for? Where is it and why is that important? Further detail can be provided in the “The Opportunity” section.', null=True),
        ),
        migrations.AlterField(
            model_name='investmentopportunitypage',
            name='introduction_pt',
            field=core.model_fields.MarkdownField(help_text='A single paragraph to introduce the opportunity – what is the vision / ambition of the opportunity, timeline and where relevant, procurement method. What type of investor is this suitable for? Where is it and why is that important? Further detail can be provided in the “The Opportunity” section.', null=True),
        ),
        migrations.AlterField(
            model_name='investmentopportunitypage',
            name='introduction_zh_hans',
            field=core.model_fields.MarkdownField(help_text='A single paragraph to introduce the opportunity – what is the vision / ambition of the opportunity, timeline and where relevant, procurement method. What type of investor is this suitable for? Where is it and why is that important? Further detail can be provided in the “The Opportunity” section.', null=True),
        ),
    ]