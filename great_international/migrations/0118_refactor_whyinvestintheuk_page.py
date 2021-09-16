# Generated by Django 2.2.24 on 2021-09-16 14:53

import core.model_fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0022_uploadedimage'),
        ('great_international', '0117_refactor_atlas_general_content_text_block'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='whyinvestintheukpage',
            name='featured_description',
        ),
        migrations.RemoveField(
            model_name='whyinvestintheukpage',
            name='featured_description_ar',
        ),
        migrations.RemoveField(
            model_name='whyinvestintheukpage',
            name='featured_description_de',
        ),
        migrations.RemoveField(
            model_name='whyinvestintheukpage',
            name='featured_description_en_gb',
        ),
        migrations.RemoveField(
            model_name='whyinvestintheukpage',
            name='featured_description_es',
        ),
        migrations.RemoveField(
            model_name='whyinvestintheukpage',
            name='featured_description_fr',
        ),
        migrations.RemoveField(
            model_name='whyinvestintheukpage',
            name='featured_description_ja',
        ),
        migrations.RemoveField(
            model_name='whyinvestintheukpage',
            name='featured_description_pt',
        ),
        migrations.RemoveField(
            model_name='whyinvestintheukpage',
            name='featured_description_zh_hans',
        ),
        migrations.RemoveField(
            model_name='whyinvestintheukpage',
            name='featured_summary',
        ),
        migrations.RemoveField(
            model_name='whyinvestintheukpage',
            name='featured_summary_ar',
        ),
        migrations.RemoveField(
            model_name='whyinvestintheukpage',
            name='featured_summary_de',
        ),
        migrations.RemoveField(
            model_name='whyinvestintheukpage',
            name='featured_summary_en_gb',
        ),
        migrations.RemoveField(
            model_name='whyinvestintheukpage',
            name='featured_summary_es',
        ),
        migrations.RemoveField(
            model_name='whyinvestintheukpage',
            name='featured_summary_fr',
        ),
        migrations.RemoveField(
            model_name='whyinvestintheukpage',
            name='featured_summary_ja',
        ),
        migrations.RemoveField(
            model_name='whyinvestintheukpage',
            name='featured_summary_pt',
        ),
        migrations.RemoveField(
            model_name='whyinvestintheukpage',
            name='featured_summary_zh_hans',
        ),
        migrations.RemoveField(
            model_name='whyinvestintheukpage',
            name='hero_title',
        ),
        migrations.RemoveField(
            model_name='whyinvestintheukpage',
            name='hero_title_ar',
        ),
        migrations.RemoveField(
            model_name='whyinvestintheukpage',
            name='hero_title_de',
        ),
        migrations.RemoveField(
            model_name='whyinvestintheukpage',
            name='hero_title_en_gb',
        ),
        migrations.RemoveField(
            model_name='whyinvestintheukpage',
            name='hero_title_es',
        ),
        migrations.RemoveField(
            model_name='whyinvestintheukpage',
            name='hero_title_fr',
        ),
        migrations.RemoveField(
            model_name='whyinvestintheukpage',
            name='hero_title_ja',
        ),
        migrations.RemoveField(
            model_name='whyinvestintheukpage',
            name='hero_title_pt',
        ),
        migrations.RemoveField(
            model_name='whyinvestintheukpage',
            name='hero_title_zh_hans',
        ),
        migrations.AddField(
            model_name='whyinvestintheukpage',
            name='intro_image',
            field=models.ForeignKey(blank=True, help_text='Goes beside the intro text', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image'),
        ),
        migrations.AddField(
            model_name='whyinvestintheukpage',
            name='intro_image_ar',
            field=models.ForeignKey(blank=True, help_text='Goes beside the intro text', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image'),
        ),
        migrations.AddField(
            model_name='whyinvestintheukpage',
            name='intro_image_de',
            field=models.ForeignKey(blank=True, help_text='Goes beside the intro text', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image'),
        ),
        migrations.AddField(
            model_name='whyinvestintheukpage',
            name='intro_image_en_gb',
            field=models.ForeignKey(blank=True, help_text='Goes beside the intro text', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image'),
        ),
        migrations.AddField(
            model_name='whyinvestintheukpage',
            name='intro_image_es',
            field=models.ForeignKey(blank=True, help_text='Goes beside the intro text', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image'),
        ),
        migrations.AddField(
            model_name='whyinvestintheukpage',
            name='intro_image_fr',
            field=models.ForeignKey(blank=True, help_text='Goes beside the intro text', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image'),
        ),
        migrations.AddField(
            model_name='whyinvestintheukpage',
            name='intro_image_ja',
            field=models.ForeignKey(blank=True, help_text='Goes beside the intro text', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image'),
        ),
        migrations.AddField(
            model_name='whyinvestintheukpage',
            name='intro_image_pt',
            field=models.ForeignKey(blank=True, help_text='Goes beside the intro text', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image'),
        ),
        migrations.AddField(
            model_name='whyinvestintheukpage',
            name='intro_image_zh_hans',
            field=models.ForeignKey(blank=True, help_text='Goes beside the intro text', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image'),
        ),
        migrations.AddField(
            model_name='whyinvestintheukpage',
            name='introduction',
            field=core.model_fields.MarkdownField(default=None),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='whyinvestintheukpage',
            name='introduction_ar',
            field=core.model_fields.MarkdownField(null=True),
        ),
        migrations.AddField(
            model_name='whyinvestintheukpage',
            name='introduction_de',
            field=core.model_fields.MarkdownField(null=True),
        ),
        migrations.AddField(
            model_name='whyinvestintheukpage',
            name='introduction_en_gb',
            field=core.model_fields.MarkdownField(null=True),
        ),
        migrations.AddField(
            model_name='whyinvestintheukpage',
            name='introduction_es',
            field=core.model_fields.MarkdownField(null=True),
        ),
        migrations.AddField(
            model_name='whyinvestintheukpage',
            name='introduction_fr',
            field=core.model_fields.MarkdownField(null=True),
        ),
        migrations.AddField(
            model_name='whyinvestintheukpage',
            name='introduction_ja',
            field=core.model_fields.MarkdownField(null=True),
        ),
        migrations.AddField(
            model_name='whyinvestintheukpage',
            name='introduction_pt',
            field=core.model_fields.MarkdownField(null=True),
        ),
        migrations.AddField(
            model_name='whyinvestintheukpage',
            name='introduction_zh_hans',
            field=core.model_fields.MarkdownField(null=True),
        ),
        migrations.AddField(
            model_name='whyinvestintheukpage',
            name='strapline',
            field=models.CharField(default=None, help_text='A single sentence which goes beneath the page title', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='whyinvestintheukpage',
            name='strapline_ar',
            field=models.CharField(help_text='A single sentence which goes beneath the page title', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='whyinvestintheukpage',
            name='strapline_de',
            field=models.CharField(help_text='A single sentence which goes beneath the page title', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='whyinvestintheukpage',
            name='strapline_en_gb',
            field=models.CharField(help_text='A single sentence which goes beneath the page title', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='whyinvestintheukpage',
            name='strapline_es',
            field=models.CharField(help_text='A single sentence which goes beneath the page title', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='whyinvestintheukpage',
            name='strapline_fr',
            field=models.CharField(help_text='A single sentence which goes beneath the page title', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='whyinvestintheukpage',
            name='strapline_ja',
            field=models.CharField(help_text='A single sentence which goes beneath the page title', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='whyinvestintheukpage',
            name='strapline_pt',
            field=models.CharField(help_text='A single sentence which goes beneath the page title', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='whyinvestintheukpage',
            name='strapline_zh_hans',
            field=models.CharField(help_text='A single sentence which goes beneath the page title', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='whyinvestintheukpage',
            name='hero_image',
            field=models.ForeignKey(blank=True, help_text='Main page hero image, above the title', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image'),
        ),
        migrations.AlterField(
            model_name='whyinvestintheukpage',
            name='hero_image_ar',
            field=models.ForeignKey(blank=True, help_text='Main page hero image, above the title', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image'),
        ),
        migrations.AlterField(
            model_name='whyinvestintheukpage',
            name='hero_image_de',
            field=models.ForeignKey(blank=True, help_text='Main page hero image, above the title', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image'),
        ),
        migrations.AlterField(
            model_name='whyinvestintheukpage',
            name='hero_image_en_gb',
            field=models.ForeignKey(blank=True, help_text='Main page hero image, above the title', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image'),
        ),
        migrations.AlterField(
            model_name='whyinvestintheukpage',
            name='hero_image_es',
            field=models.ForeignKey(blank=True, help_text='Main page hero image, above the title', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image'),
        ),
        migrations.AlterField(
            model_name='whyinvestintheukpage',
            name='hero_image_fr',
            field=models.ForeignKey(blank=True, help_text='Main page hero image, above the title', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image'),
        ),
        migrations.AlterField(
            model_name='whyinvestintheukpage',
            name='hero_image_ja',
            field=models.ForeignKey(blank=True, help_text='Main page hero image, above the title', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image'),
        ),
        migrations.AlterField(
            model_name='whyinvestintheukpage',
            name='hero_image_pt',
            field=models.ForeignKey(blank=True, help_text='Main page hero image, above the title', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image'),
        ),
        migrations.AlterField(
            model_name='whyinvestintheukpage',
            name='hero_image_zh_hans',
            field=models.ForeignKey(blank=True, help_text='Main page hero image, above the title', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image'),
        ),
    ]
