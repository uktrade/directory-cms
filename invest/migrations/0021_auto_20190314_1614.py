# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-03-14 16:14
from __future__ import unicode_literals

import core.model_fields
import core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0021_image_file_hash'),
        ('invest', '0020_auto_20190314_1532'),
    ]

    operations = [
        migrations.AddField(
            model_name='investhomepage',
            name='eu_exit_section_call_to_action_text',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='investhomepage',
            name='eu_exit_section_call_to_action_text_ar',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='investhomepage',
            name='eu_exit_section_call_to_action_text_de',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='investhomepage',
            name='eu_exit_section_call_to_action_text_en_gb',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='investhomepage',
            name='eu_exit_section_call_to_action_text_es',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='investhomepage',
            name='eu_exit_section_call_to_action_text_fr',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='investhomepage',
            name='eu_exit_section_call_to_action_text_ja',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='investhomepage',
            name='eu_exit_section_call_to_action_text_pt',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='investhomepage',
            name='eu_exit_section_call_to_action_text_pt_br',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='investhomepage',
            name='eu_exit_section_call_to_action_text_ru',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='investhomepage',
            name='eu_exit_section_call_to_action_text_zh_hans',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='investhomepage',
            name='eu_exit_section_content',
            field=core.model_fields.MarkdownField(blank=True, validators=[core.validators.slug_hyperlinks]),
        ),
        migrations.AddField(
            model_name='investhomepage',
            name='eu_exit_section_content_ar',
            field=core.model_fields.MarkdownField(blank=True, null=True, validators=[core.validators.slug_hyperlinks]),
        ),
        migrations.AddField(
            model_name='investhomepage',
            name='eu_exit_section_content_de',
            field=core.model_fields.MarkdownField(blank=True, null=True, validators=[core.validators.slug_hyperlinks]),
        ),
        migrations.AddField(
            model_name='investhomepage',
            name='eu_exit_section_content_en_gb',
            field=core.model_fields.MarkdownField(blank=True, null=True, validators=[core.validators.slug_hyperlinks]),
        ),
        migrations.AddField(
            model_name='investhomepage',
            name='eu_exit_section_content_es',
            field=core.model_fields.MarkdownField(blank=True, null=True, validators=[core.validators.slug_hyperlinks]),
        ),
        migrations.AddField(
            model_name='investhomepage',
            name='eu_exit_section_content_fr',
            field=core.model_fields.MarkdownField(blank=True, null=True, validators=[core.validators.slug_hyperlinks]),
        ),
        migrations.AddField(
            model_name='investhomepage',
            name='eu_exit_section_content_ja',
            field=core.model_fields.MarkdownField(blank=True, null=True, validators=[core.validators.slug_hyperlinks]),
        ),
        migrations.AddField(
            model_name='investhomepage',
            name='eu_exit_section_content_pt',
            field=core.model_fields.MarkdownField(blank=True, null=True, validators=[core.validators.slug_hyperlinks]),
        ),
        migrations.AddField(
            model_name='investhomepage',
            name='eu_exit_section_content_pt_br',
            field=core.model_fields.MarkdownField(blank=True, null=True, validators=[core.validators.slug_hyperlinks]),
        ),
        migrations.AddField(
            model_name='investhomepage',
            name='eu_exit_section_content_ru',
            field=core.model_fields.MarkdownField(blank=True, null=True, validators=[core.validators.slug_hyperlinks]),
        ),
        migrations.AddField(
            model_name='investhomepage',
            name='eu_exit_section_content_zh_hans',
            field=core.model_fields.MarkdownField(blank=True, null=True, validators=[core.validators.slug_hyperlinks]),
        ),
        migrations.AddField(
            model_name='investhomepage',
            name='eu_exit_section_img',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image'),
        ),
        migrations.AddField(
            model_name='investhomepage',
            name='eu_exit_section_img_ar',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image'),
        ),
        migrations.AddField(
            model_name='investhomepage',
            name='eu_exit_section_img_caption',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='investhomepage',
            name='eu_exit_section_img_caption_ar',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='investhomepage',
            name='eu_exit_section_img_caption_de',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='investhomepage',
            name='eu_exit_section_img_caption_en_gb',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='investhomepage',
            name='eu_exit_section_img_caption_es',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='investhomepage',
            name='eu_exit_section_img_caption_fr',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='investhomepage',
            name='eu_exit_section_img_caption_ja',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='investhomepage',
            name='eu_exit_section_img_caption_pt',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='investhomepage',
            name='eu_exit_section_img_caption_pt_br',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='investhomepage',
            name='eu_exit_section_img_caption_ru',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='investhomepage',
            name='eu_exit_section_img_caption_zh_hans',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='investhomepage',
            name='eu_exit_section_img_de',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image'),
        ),
        migrations.AddField(
            model_name='investhomepage',
            name='eu_exit_section_img_en_gb',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image'),
        ),
        migrations.AddField(
            model_name='investhomepage',
            name='eu_exit_section_img_es',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image'),
        ),
        migrations.AddField(
            model_name='investhomepage',
            name='eu_exit_section_img_fr',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image'),
        ),
        migrations.AddField(
            model_name='investhomepage',
            name='eu_exit_section_img_ja',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image'),
        ),
        migrations.AddField(
            model_name='investhomepage',
            name='eu_exit_section_img_pt',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image'),
        ),
        migrations.AddField(
            model_name='investhomepage',
            name='eu_exit_section_img_pt_br',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image'),
        ),
        migrations.AddField(
            model_name='investhomepage',
            name='eu_exit_section_img_ru',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image'),
        ),
        migrations.AddField(
            model_name='investhomepage',
            name='eu_exit_section_img_zh_hans',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image'),
        ),
        migrations.AddField(
            model_name='investhomepage',
            name='eu_exit_section_title',
            field=models.CharField(default='EU Exit', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='investhomepage',
            name='eu_exit_section_title_ar',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='investhomepage',
            name='eu_exit_section_title_de',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='investhomepage',
            name='eu_exit_section_title_en_gb',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='investhomepage',
            name='eu_exit_section_title_es',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='investhomepage',
            name='eu_exit_section_title_fr',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='investhomepage',
            name='eu_exit_section_title_ja',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='investhomepage',
            name='eu_exit_section_title_pt',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='investhomepage',
            name='eu_exit_section_title_pt_br',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='investhomepage',
            name='eu_exit_section_title_ru',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='investhomepage',
            name='eu_exit_section_title_zh_hans',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
