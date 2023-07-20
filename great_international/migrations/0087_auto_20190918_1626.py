# Generated by Django 2.2.4 on 2019-09-18 16:26

import wagtailmarkdown.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('great_international', '0086_auto_20190917_0752'),
    ]

    operations = [
        migrations.AddField(
            model_name='aboutukwhychoosetheukpage',
            name='how_dit_help_title',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='aboutukwhychoosetheukpage',
            name='how_dit_help_title_ar',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='aboutukwhychoosetheukpage',
            name='how_dit_help_title_de',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='aboutukwhychoosetheukpage',
            name='how_dit_help_title_en_gb',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='aboutukwhychoosetheukpage',
            name='how_dit_help_title_es',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='aboutukwhychoosetheukpage',
            name='how_dit_help_title_fr',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='aboutukwhychoosetheukpage',
            name='how_dit_help_title_ja',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='aboutukwhychoosetheukpage',
            name='how_dit_help_title_pt',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='aboutukwhychoosetheukpage',
            name='how_dit_help_title_zh_hans',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='aboutukwhychoosetheukpage',
            name='primary_contact_cta_link',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='aboutukwhychoosetheukpage',
            name='primary_contact_cta_link_ar',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='aboutukwhychoosetheukpage',
            name='primary_contact_cta_link_de',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='aboutukwhychoosetheukpage',
            name='primary_contact_cta_link_en_gb',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='aboutukwhychoosetheukpage',
            name='primary_contact_cta_link_es',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='aboutukwhychoosetheukpage',
            name='primary_contact_cta_link_fr',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='aboutukwhychoosetheukpage',
            name='primary_contact_cta_link_ja',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='aboutukwhychoosetheukpage',
            name='primary_contact_cta_link_pt',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='aboutukwhychoosetheukpage',
            name='primary_contact_cta_link_zh_hans',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='aboutukwhychoosetheukpage',
            name='primary_contact_cta_text',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='aboutukwhychoosetheukpage',
            name='primary_contact_cta_text_ar',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='aboutukwhychoosetheukpage',
            name='primary_contact_cta_text_de',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='aboutukwhychoosetheukpage',
            name='primary_contact_cta_text_en_gb',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='aboutukwhychoosetheukpage',
            name='primary_contact_cta_text_es',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='aboutukwhychoosetheukpage',
            name='primary_contact_cta_text_fr',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='aboutukwhychoosetheukpage',
            name='primary_contact_cta_text_ja',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='aboutukwhychoosetheukpage',
            name='primary_contact_cta_text_pt',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='aboutukwhychoosetheukpage',
            name='primary_contact_cta_text_zh_hans',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='aboutukwhychoosetheukpage',
            name='related_page_one',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='great_international.AboutDitServicesPage'),
        ),
        migrations.AddField(
            model_name='aboutukwhychoosetheukpage',
            name='related_page_one_ar',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='great_international.AboutDitServicesPage'),
        ),
        migrations.AddField(
            model_name='aboutukwhychoosetheukpage',
            name='related_page_one_de',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='great_international.AboutDitServicesPage'),
        ),
        migrations.AddField(
            model_name='aboutukwhychoosetheukpage',
            name='related_page_one_en_gb',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='great_international.AboutDitServicesPage'),
        ),
        migrations.AddField(
            model_name='aboutukwhychoosetheukpage',
            name='related_page_one_es',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='great_international.AboutDitServicesPage'),
        ),
        migrations.AddField(
            model_name='aboutukwhychoosetheukpage',
            name='related_page_one_fr',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='great_international.AboutDitServicesPage'),
        ),
        migrations.AddField(
            model_name='aboutukwhychoosetheukpage',
            name='related_page_one_ja',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='great_international.AboutDitServicesPage'),
        ),
        migrations.AddField(
            model_name='aboutukwhychoosetheukpage',
            name='related_page_one_pt',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='great_international.AboutDitServicesPage'),
        ),
        migrations.AddField(
            model_name='aboutukwhychoosetheukpage',
            name='related_page_one_zh_hans',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='great_international.AboutDitServicesPage'),
        ),
        migrations.AddField(
            model_name='aboutukwhychoosetheukpage',
            name='related_page_three',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='great_international.AboutDitServicesPage'),
        ),
        migrations.AddField(
            model_name='aboutukwhychoosetheukpage',
            name='related_page_three_ar',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='great_international.AboutDitServicesPage'),
        ),
        migrations.AddField(
            model_name='aboutukwhychoosetheukpage',
            name='related_page_three_de',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='great_international.AboutDitServicesPage'),
        ),
        migrations.AddField(
            model_name='aboutukwhychoosetheukpage',
            name='related_page_three_en_gb',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='great_international.AboutDitServicesPage'),
        ),
        migrations.AddField(
            model_name='aboutukwhychoosetheukpage',
            name='related_page_three_es',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='great_international.AboutDitServicesPage'),
        ),
        migrations.AddField(
            model_name='aboutukwhychoosetheukpage',
            name='related_page_three_fr',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='great_international.AboutDitServicesPage'),
        ),
        migrations.AddField(
            model_name='aboutukwhychoosetheukpage',
            name='related_page_three_ja',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='great_international.AboutDitServicesPage'),
        ),
        migrations.AddField(
            model_name='aboutukwhychoosetheukpage',
            name='related_page_three_pt',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='great_international.AboutDitServicesPage'),
        ),
        migrations.AddField(
            model_name='aboutukwhychoosetheukpage',
            name='related_page_three_zh_hans',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='great_international.AboutDitServicesPage'),
        ),
        migrations.AddField(
            model_name='aboutukwhychoosetheukpage',
            name='related_page_two',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='great_international.AboutDitServicesPage'),
        ),
        migrations.AddField(
            model_name='aboutukwhychoosetheukpage',
            name='related_page_two_ar',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='great_international.AboutDitServicesPage'),
        ),
        migrations.AddField(
            model_name='aboutukwhychoosetheukpage',
            name='related_page_two_de',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='great_international.AboutDitServicesPage'),
        ),
        migrations.AddField(
            model_name='aboutukwhychoosetheukpage',
            name='related_page_two_en_gb',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='great_international.AboutDitServicesPage'),
        ),
        migrations.AddField(
            model_name='aboutukwhychoosetheukpage',
            name='related_page_two_es',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='great_international.AboutDitServicesPage'),
        ),
        migrations.AddField(
            model_name='aboutukwhychoosetheukpage',
            name='related_page_two_fr',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='great_international.AboutDitServicesPage'),
        ),
        migrations.AddField(
            model_name='aboutukwhychoosetheukpage',
            name='related_page_two_ja',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='great_international.AboutDitServicesPage'),
        ),
        migrations.AddField(
            model_name='aboutukwhychoosetheukpage',
            name='related_page_two_pt',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='great_international.AboutDitServicesPage'),
        ),
        migrations.AddField(
            model_name='aboutukwhychoosetheukpage',
            name='related_page_two_zh_hans',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='great_international.AboutDitServicesPage'),
        ),
        migrations.AlterField(
            model_name='aboutukarticlesfields',
            name='summary',
            field=wagtailmarkdown.fields.MarkdownField(blank=True),
        ),
    ]
