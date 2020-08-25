# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-02-28 12:34
from __future__ import unicode_literals

import core.model_fields
import core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0040_page_draft_title'),
        ('wagtailimages', '0021_image_file_hash'),
        ('great_international', '0011_auto_20190228_1051'),
    ]

    operations = [
        migrations.CreateModel(
            name='InternationalSectorPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('service_name', models.CharField(choices=[('FIND_A_SUPPLIER', 'Find a Supplier'), ('EXPORT_READINESS', 'Export Readiness'), ('INVEST', 'Invest'), ('COMPONENTS', 'Components'), ('GREAT_INTERNATIONAL', 'Great International')], db_index=True, max_length=100, null=True)),
                ('heading', models.CharField(max_length=255)),
                ('sub_heading', models.CharField(max_length=255)),
                ('heading_teaser', models.CharField(max_length=255)),
                ('section_one_body', core.model_fields.MarkdownField(blank=True, null=True, validators=[core.validators.slug_hyperlinks])),
                ('statistic_1_number', models.CharField(max_length=255)),
                ('statistic_1_heading', models.CharField(max_length=255)),
                ('statistic_1_smallprint', models.CharField(max_length=255)),
                ('statistic_2_number', models.CharField(max_length=255)),
                ('statistic_2_heading', models.CharField(max_length=255)),
                ('statistic_2_smallprint', models.CharField(max_length=255)),
                ('statistic_3_number', models.CharField(blank=True, max_length=255)),
                ('statistic_3_heading', models.CharField(blank=True, max_length=255)),
                ('statistic_3_smallprint', models.CharField(blank=True, max_length=255)),
                ('statistic_4_number', models.CharField(blank=True, max_length=255)),
                ('statistic_4_heading', models.CharField(blank=True, max_length=255)),
                ('statistic_4_smallprint', models.CharField(blank=True, max_length=255)),
                ('statistic_5_number', models.CharField(blank=True, max_length=255)),
                ('statistic_5_heading', models.CharField(blank=True, max_length=255)),
                ('statistic_5_smallprint', models.CharField(blank=True, max_length=255)),
                ('statistic_6_number', models.CharField(blank=True, max_length=255)),
                ('statistic_6_heading', models.CharField(blank=True, max_length=255)),
                ('statistic_6_smallprint', models.CharField(blank=True, max_length=255)),
                ('section_two_heading', models.CharField(max_length=255)),
                ('section_two_teaser', models.CharField(max_length=255)),
                ('section_two_subsection_one_heading', models.CharField(max_length=255)),
                ('section_two_subsection_one_body', models.CharField(max_length=255)),
                ('section_two_subsection_two_heading', models.CharField(max_length=255)),
                ('section_two_subsection_two_body', models.CharField(max_length=255)),
                ('section_two_subsection_three_heading', models.CharField(max_length=255)),
                ('section_two_subsection_three_body', models.CharField(max_length=255)),
                ('case_study_title', models.CharField(max_length=255)),
                ('case_study_description', models.CharField(max_length=255)),
                ('case_study_cta_text', models.CharField(max_length=255)),
                ('case_study_cta_url', models.CharField(max_length=255)),
                ('section_three_heading', models.CharField(max_length=255)),
                ('section_three_teaser', models.CharField(max_length=255)),
                ('section_three_subsection_one_heading', models.CharField(max_length=255)),
                ('section_three_subsection_one_teaser', models.CharField(max_length=255)),
                ('section_three_subsection_one_body', core.model_fields.MarkdownField(blank=True, null=True, validators=[core.validators.slug_hyperlinks])),
                ('section_three_subsection_two_heading', models.CharField(max_length=255)),
                ('section_three_subsection_two_teaser', models.CharField(max_length=255)),
                ('section_three_subsection_two_body', core.model_fields.MarkdownField(blank=True, null=True, validators=[core.validators.slug_hyperlinks])),
                ('next_steps_heading', models.CharField(max_length=255)),
                ('next_steps_description', models.CharField(max_length=255)),
                ('case_study_image', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image')),
                ('hero_image', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image')),
                ('related_page_one', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailcore.Page')),
                ('related_page_three', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailcore.Page')),
                ('related_page_two', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailcore.Page')),
                ('section_one_image', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image')),
                ('section_two_subsection_one_icon', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image')),
                ('section_two_subsection_three_icon', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image')),
                ('section_two_subsection_two_icon', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
    ]
