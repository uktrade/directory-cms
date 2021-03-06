# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-04-08 16:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('great_international', '0015_auto_20190404_1712'),
    ]

    operations = [
        migrations.AlterField(
            model_name='internationalarticlepage',
            name='article_subheading',
            field=models.CharField(blank=True, help_text='This is a subheading that displays below the main title on the article page', max_length=255),
        ),
        migrations.AlterField(
            model_name='internationalarticlepage',
            name='article_subheading_ar',
            field=models.CharField(blank=True, help_text='This is a subheading that displays below the main title on the article page', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='internationalarticlepage',
            name='article_subheading_de',
            field=models.CharField(blank=True, help_text='This is a subheading that displays below the main title on the article page', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='internationalarticlepage',
            name='article_subheading_en_gb',
            field=models.CharField(blank=True, help_text='This is a subheading that displays below the main title on the article page', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='internationalarticlepage',
            name='article_subheading_es',
            field=models.CharField(blank=True, help_text='This is a subheading that displays below the main title on the article page', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='internationalarticlepage',
            name='article_subheading_fr',
            field=models.CharField(blank=True, help_text='This is a subheading that displays below the main title on the article page', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='internationalarticlepage',
            name='article_subheading_ja',
            field=models.CharField(blank=True, help_text='This is a subheading that displays below the main title on the article page', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='internationalarticlepage',
            name='article_subheading_pt',
            field=models.CharField(blank=True, help_text='This is a subheading that displays below the main title on the article page', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='internationalarticlepage',
            name='article_subheading_pt_br',
            field=models.CharField(blank=True, help_text='This is a subheading that displays below the main title on the article page', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='internationalarticlepage',
            name='article_subheading_ru',
            field=models.CharField(blank=True, help_text='This is a subheading that displays below the main title on the article page', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='internationalarticlepage',
            name='article_subheading_zh_hans',
            field=models.CharField(blank=True, help_text='This is a subheading that displays below the main title on the article page', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='internationalarticlepage',
            name='article_teaser',
            field=models.CharField(help_text='This is a subheading that displays when the article is featured on another page', max_length=255),
        ),
        migrations.AlterField(
            model_name='internationalarticlepage',
            name='article_teaser_ar',
            field=models.CharField(help_text='This is a subheading that displays when the article is featured on another page', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='internationalarticlepage',
            name='article_teaser_de',
            field=models.CharField(help_text='This is a subheading that displays when the article is featured on another page', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='internationalarticlepage',
            name='article_teaser_en_gb',
            field=models.CharField(help_text='This is a subheading that displays when the article is featured on another page', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='internationalarticlepage',
            name='article_teaser_es',
            field=models.CharField(help_text='This is a subheading that displays when the article is featured on another page', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='internationalarticlepage',
            name='article_teaser_fr',
            field=models.CharField(help_text='This is a subheading that displays when the article is featured on another page', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='internationalarticlepage',
            name='article_teaser_ja',
            field=models.CharField(help_text='This is a subheading that displays when the article is featured on another page', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='internationalarticlepage',
            name='article_teaser_pt',
            field=models.CharField(help_text='This is a subheading that displays when the article is featured on another page', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='internationalarticlepage',
            name='article_teaser_pt_br',
            field=models.CharField(help_text='This is a subheading that displays when the article is featured on another page', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='internationalarticlepage',
            name='article_teaser_ru',
            field=models.CharField(help_text='This is a subheading that displays when the article is featured on another page', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='internationalarticlepage',
            name='article_teaser_zh_hans',
            field=models.CharField(help_text='This is a subheading that displays when the article is featured on another page', max_length=255, null=True),
        ),
    ]
