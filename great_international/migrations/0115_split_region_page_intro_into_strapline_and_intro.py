# Generated by Django 2.2.24 on 2021-09-14 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('great_international', '0114_auto_20210914_1328'),
    ]

    operations = [
        migrations.AddField(
            model_name='aboutukregionpage',
            name='region_summary_section_strapline',
            field=models.TextField(blank=True, help_text='Displayd above Region Section Summary Intro', max_length=255),
        ),
        migrations.AddField(
            model_name='aboutukregionpage',
            name='region_summary_section_strapline_ar',
            field=models.TextField(blank=True, help_text='Displayd above Region Section Summary Intro', max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='aboutukregionpage',
            name='region_summary_section_strapline_de',
            field=models.TextField(blank=True, help_text='Displayd above Region Section Summary Intro', max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='aboutukregionpage',
            name='region_summary_section_strapline_en_gb',
            field=models.TextField(blank=True, help_text='Displayd above Region Section Summary Intro', max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='aboutukregionpage',
            name='region_summary_section_strapline_es',
            field=models.TextField(blank=True, help_text='Displayd above Region Section Summary Intro', max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='aboutukregionpage',
            name='region_summary_section_strapline_fr',
            field=models.TextField(blank=True, help_text='Displayd above Region Section Summary Intro', max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='aboutukregionpage',
            name='region_summary_section_strapline_ja',
            field=models.TextField(blank=True, help_text='Displayd above Region Section Summary Intro', max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='aboutukregionpage',
            name='region_summary_section_strapline_pt',
            field=models.TextField(blank=True, help_text='Displayd above Region Section Summary Intro', max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='aboutukregionpage',
            name='region_summary_section_strapline_zh_hans',
            field=models.TextField(blank=True, help_text='Displayd above Region Section Summary Intro', max_length=255, null=True),
        ),
    ]
