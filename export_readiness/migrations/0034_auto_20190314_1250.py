# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-03-14 12:50
from __future__ import unicode_literals

import core.model_fields
import core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0021_image_file_hash'),
        ('export_readiness', '0033_auto_20190312_1557'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='countryguidepage',
            name='accordion_1_hero_image',
        ),
        migrations.RemoveField(
            model_name='countryguidepage',
            name='accordion_2_hero_image',
        ),
        migrations.RemoveField(
            model_name='countryguidepage',
            name='accordion_3_hero_image',
        ),
        migrations.RemoveField(
            model_name='countryguidepage',
            name='accordion_4_hero_image',
        ),
        migrations.RemoveField(
            model_name='countryguidepage',
            name='accordion_5_hero_image',
        ),
        migrations.RemoveField(
            model_name='countryguidepage',
            name='accordion_6_hero_image',
        ),
        migrations.AddField(
            model_name='countryguidepage',
            name='accordion_1_case_study_button_link',
            field=models.CharField(blank=True, max_length=255, verbose_name='Case study button link'),
        ),
        migrations.AddField(
            model_name='countryguidepage',
            name='accordion_1_case_study_button_text',
            field=models.CharField(blank=True, max_length=255, verbose_name='Case study button text'),
        ),
        migrations.AddField(
            model_name='countryguidepage',
            name='accordion_1_case_study_description',
            field=models.CharField(blank=True, max_length=255, verbose_name='Case study description'),
        ),
        migrations.AddField(
            model_name='countryguidepage',
            name='accordion_1_case_study_hero_image',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image', verbose_name='Case study hero'),
        ),
        migrations.AddField(
            model_name='countryguidepage',
            name='accordion_1_case_study_title',
            field=models.CharField(blank=True, max_length=255, verbose_name='Case study title'),
        ),
        migrations.AddField(
            model_name='countryguidepage',
            name='accordion_1_cta_1_link',
            field=models.CharField(blank=True, max_length=255, verbose_name='CTA link 1'),
        ),
        migrations.AddField(
            model_name='countryguidepage',
            name='accordion_1_cta_1_title',
            field=models.CharField(blank=True, max_length=255, verbose_name='CTA title 1'),
        ),
        migrations.AddField(
            model_name='countryguidepage',
            name='accordion_1_cta_2_link',
            field=models.CharField(blank=True, max_length=255, verbose_name='CTA link 2'),
        ),
        migrations.AddField(
            model_name='countryguidepage',
            name='accordion_1_cta_2_title',
            field=models.CharField(blank=True, max_length=255, verbose_name='CTA title 2'),
        ),
        migrations.AddField(
            model_name='countryguidepage',
            name='accordion_1_cta_3_link',
            field=models.CharField(blank=True, max_length=255, verbose_name='CTA link 3'),
        ),
        migrations.AddField(
            model_name='countryguidepage',
            name='accordion_1_cta_3_title',
            field=models.CharField(blank=True, max_length=255, verbose_name='CTA title 3'),
        ),
        migrations.AddField(
            model_name='countryguidepage',
            name='accordion_2_case_study_button_link',
            field=models.CharField(blank=True, max_length=255, verbose_name='Case study button link'),
        ),
        migrations.AddField(
            model_name='countryguidepage',
            name='accordion_2_case_study_button_text',
            field=models.CharField(blank=True, max_length=255, verbose_name='Case study button text'),
        ),
        migrations.AddField(
            model_name='countryguidepage',
            name='accordion_2_case_study_description',
            field=models.CharField(blank=True, max_length=255, verbose_name='Case study description'),
        ),
        migrations.AddField(
            model_name='countryguidepage',
            name='accordion_2_case_study_hero_image',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image', verbose_name='Case study hero'),
        ),
        migrations.AddField(
            model_name='countryguidepage',
            name='accordion_2_case_study_title',
            field=models.CharField(blank=True, max_length=255, verbose_name='Case study title'),
        ),
        migrations.AddField(
            model_name='countryguidepage',
            name='accordion_2_cta_1_link',
            field=models.CharField(blank=True, max_length=255, verbose_name='CTA link 1'),
        ),
        migrations.AddField(
            model_name='countryguidepage',
            name='accordion_2_cta_1_title',
            field=models.CharField(blank=True, max_length=255, verbose_name='CTA title 1'),
        ),
        migrations.AddField(
            model_name='countryguidepage',
            name='accordion_2_cta_2_link',
            field=models.CharField(blank=True, max_length=255, verbose_name='CTA link 2'),
        ),
        migrations.AddField(
            model_name='countryguidepage',
            name='accordion_2_cta_2_title',
            field=models.CharField(blank=True, max_length=255, verbose_name='CTA title 2'),
        ),
        migrations.AddField(
            model_name='countryguidepage',
            name='accordion_2_cta_3_link',
            field=models.CharField(blank=True, max_length=255, verbose_name='CTA link 3'),
        ),
        migrations.AddField(
            model_name='countryguidepage',
            name='accordion_2_cta_3_title',
            field=models.CharField(blank=True, max_length=255, verbose_name='CTA title 3'),
        ),
        migrations.AddField(
            model_name='countryguidepage',
            name='accordion_3_case_study_button_link',
            field=models.CharField(blank=True, max_length=255, verbose_name='Case study button link'),
        ),
        migrations.AddField(
            model_name='countryguidepage',
            name='accordion_3_case_study_button_text',
            field=models.CharField(blank=True, max_length=255, verbose_name='Case study button text'),
        ),
        migrations.AddField(
            model_name='countryguidepage',
            name='accordion_3_case_study_description',
            field=models.CharField(blank=True, max_length=255, verbose_name='Case study description'),
        ),
        migrations.AddField(
            model_name='countryguidepage',
            name='accordion_3_case_study_hero_image',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image', verbose_name='Case study hero'),
        ),
        migrations.AddField(
            model_name='countryguidepage',
            name='accordion_3_case_study_title',
            field=models.CharField(blank=True, max_length=255, verbose_name='Case study title'),
        ),
        migrations.AddField(
            model_name='countryguidepage',
            name='accordion_3_cta_1_link',
            field=models.CharField(blank=True, max_length=255, verbose_name='CTA link 1'),
        ),
        migrations.AddField(
            model_name='countryguidepage',
            name='accordion_3_cta_1_title',
            field=models.CharField(blank=True, max_length=255, verbose_name='CTA title 1'),
        ),
        migrations.AddField(
            model_name='countryguidepage',
            name='accordion_3_cta_2_link',
            field=models.CharField(blank=True, max_length=255, verbose_name='CTA link 2'),
        ),
        migrations.AddField(
            model_name='countryguidepage',
            name='accordion_3_cta_2_title',
            field=models.CharField(blank=True, max_length=255, verbose_name='CTA title 2'),
        ),
        migrations.AddField(
            model_name='countryguidepage',
            name='accordion_3_cta_3_link',
            field=models.CharField(blank=True, max_length=255, verbose_name='CTA link 3'),
        ),
        migrations.AddField(
            model_name='countryguidepage',
            name='accordion_3_cta_3_title',
            field=models.CharField(blank=True, max_length=255, verbose_name='CTA title 3'),
        ),
        migrations.AddField(
            model_name='countryguidepage',
            name='accordion_4_case_study_button_link',
            field=models.CharField(blank=True, max_length=255, verbose_name='Case study button link'),
        ),
        migrations.AddField(
            model_name='countryguidepage',
            name='accordion_4_case_study_button_text',
            field=models.CharField(blank=True, max_length=255, verbose_name='Case study button text'),
        ),
        migrations.AddField(
            model_name='countryguidepage',
            name='accordion_4_case_study_description',
            field=models.CharField(blank=True, max_length=255, verbose_name='Case study description'),
        ),
        migrations.AddField(
            model_name='countryguidepage',
            name='accordion_4_case_study_hero_image',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image', verbose_name='Case study hero'),
        ),
        migrations.AddField(
            model_name='countryguidepage',
            name='accordion_4_case_study_title',
            field=models.CharField(blank=True, max_length=255, verbose_name='Case study title'),
        ),
        migrations.AddField(
            model_name='countryguidepage',
            name='accordion_4_cta_1_link',
            field=models.CharField(blank=True, max_length=255, verbose_name='CTA link 1'),
        ),
        migrations.AddField(
            model_name='countryguidepage',
            name='accordion_4_cta_1_title',
            field=models.CharField(blank=True, max_length=255, verbose_name='CTA title 1'),
        ),
        migrations.AddField(
            model_name='countryguidepage',
            name='accordion_4_cta_2_link',
            field=models.CharField(blank=True, max_length=255, verbose_name='CTA link 2'),
        ),
        migrations.AddField(
            model_name='countryguidepage',
            name='accordion_4_cta_2_title',
            field=models.CharField(blank=True, max_length=255, verbose_name='CTA title 2'),
        ),
        migrations.AddField(
            model_name='countryguidepage',
            name='accordion_4_cta_3_link',
            field=models.CharField(blank=True, max_length=255, verbose_name='CTA link 3'),
        ),
        migrations.AddField(
            model_name='countryguidepage',
            name='accordion_4_cta_3_title',
            field=models.CharField(blank=True, max_length=255, verbose_name='CTA title 3'),
        ),
        migrations.AddField(
            model_name='countryguidepage',
            name='accordion_5_case_study_button_link',
            field=models.CharField(blank=True, max_length=255, verbose_name='Case study button link'),
        ),
        migrations.AddField(
            model_name='countryguidepage',
            name='accordion_5_case_study_button_text',
            field=models.CharField(blank=True, max_length=255, verbose_name='Case study button text'),
        ),
        migrations.AddField(
            model_name='countryguidepage',
            name='accordion_5_case_study_description',
            field=models.CharField(blank=True, max_length=255, verbose_name='Case study description'),
        ),
        migrations.AddField(
            model_name='countryguidepage',
            name='accordion_5_case_study_hero_image',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image', verbose_name='Case study hero'),
        ),
        migrations.AddField(
            model_name='countryguidepage',
            name='accordion_5_case_study_title',
            field=models.CharField(blank=True, max_length=255, verbose_name='Case study title'),
        ),
        migrations.AddField(
            model_name='countryguidepage',
            name='accordion_5_cta_1_link',
            field=models.CharField(blank=True, max_length=255, verbose_name='CTA link 1'),
        ),
        migrations.AddField(
            model_name='countryguidepage',
            name='accordion_5_cta_1_title',
            field=models.CharField(blank=True, max_length=255, verbose_name='CTA title 1'),
        ),
        migrations.AddField(
            model_name='countryguidepage',
            name='accordion_5_cta_2_link',
            field=models.CharField(blank=True, max_length=255, verbose_name='CTA link 2'),
        ),
        migrations.AddField(
            model_name='countryguidepage',
            name='accordion_5_cta_2_title',
            field=models.CharField(blank=True, max_length=255, verbose_name='CTA title 2'),
        ),
        migrations.AddField(
            model_name='countryguidepage',
            name='accordion_5_cta_3_link',
            field=models.CharField(blank=True, max_length=255, verbose_name='CTA link 3'),
        ),
        migrations.AddField(
            model_name='countryguidepage',
            name='accordion_5_cta_3_title',
            field=models.CharField(blank=True, max_length=255, verbose_name='CTA title 3'),
        ),
        migrations.AddField(
            model_name='countryguidepage',
            name='accordion_6_case_study_button_link',
            field=models.CharField(blank=True, max_length=255, verbose_name='Case study button link'),
        ),
        migrations.AddField(
            model_name='countryguidepage',
            name='accordion_6_case_study_button_text',
            field=models.CharField(blank=True, max_length=255, verbose_name='Case study button text'),
        ),
        migrations.AddField(
            model_name='countryguidepage',
            name='accordion_6_case_study_description',
            field=models.CharField(blank=True, max_length=255, verbose_name='Case study description'),
        ),
        migrations.AddField(
            model_name='countryguidepage',
            name='accordion_6_case_study_hero_image',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image', verbose_name='Case study hero'),
        ),
        migrations.AddField(
            model_name='countryguidepage',
            name='accordion_6_case_study_title',
            field=models.CharField(blank=True, max_length=255, verbose_name='Case study title'),
        ),
        migrations.AddField(
            model_name='countryguidepage',
            name='accordion_6_cta_1_link',
            field=models.CharField(blank=True, max_length=255, verbose_name='CTA link 1'),
        ),
        migrations.AddField(
            model_name='countryguidepage',
            name='accordion_6_cta_1_title',
            field=models.CharField(blank=True, max_length=255, verbose_name='CTA title 1'),
        ),
        migrations.AddField(
            model_name='countryguidepage',
            name='accordion_6_cta_2_link',
            field=models.CharField(blank=True, max_length=255, verbose_name='CTA link 2'),
        ),
        migrations.AddField(
            model_name='countryguidepage',
            name='accordion_6_cta_2_title',
            field=models.CharField(blank=True, max_length=255, verbose_name='CTA title 2'),
        ),
        migrations.AddField(
            model_name='countryguidepage',
            name='accordion_6_cta_3_link',
            field=models.CharField(blank=True, max_length=255, verbose_name='CTA link 3'),
        ),
        migrations.AddField(
            model_name='countryguidepage',
            name='accordion_6_cta_3_title',
            field=models.CharField(blank=True, max_length=255, verbose_name='CTA title 3'),
        ),
        migrations.AddField(
            model_name='countryguidepage',
            name='fact_sheet_column_1_body',
            field=core.model_fields.MarkdownField(blank=True, validators=[core.validators.slug_hyperlinks]),
        ),
        migrations.AddField(
            model_name='countryguidepage',
            name='fact_sheet_column_1_teaser',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='countryguidepage',
            name='fact_sheet_column_1_title',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='countryguidepage',
            name='fact_sheet_column_2_body',
            field=core.model_fields.MarkdownField(blank=True, validators=[core.validators.slug_hyperlinks]),
        ),
        migrations.AddField(
            model_name='countryguidepage',
            name='fact_sheet_column_2_teaser',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='countryguidepage',
            name='fact_sheet_column_2_title',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='countryguidepage',
            name='fact_sheet_teaser',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='countryguidepage',
            name='fact_sheet_title',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='countryguidepage',
            name='help_market_guide_cta_link',
            field=models.CharField(blank=True, max_length=255, verbose_name='Help CTA market guide link'),
        ),
        migrations.AddField(
            model_name='countryguidepage',
            name='help_market_guide_cta_title',
            field=models.CharField(blank=True, max_length=255, verbose_name='Help CTA market guide title'),
        ),
    ]
