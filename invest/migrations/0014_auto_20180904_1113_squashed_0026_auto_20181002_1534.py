# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-10-09 13:51
from __future__ import unicode_literals

import core.fields
import core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    replaces = [('invest', '0014_auto_20180904_1113'), ('invest', '0015_auto_20180911_1049'), ('invest', '0016_auto_20180911_1506'), ('invest', '0017_auto_20180911_1513'), ('invest', '0018_auto_20180913_1445'), ('invest', '0019_auto_20180917_0838'), ('invest', '0020_auto_20180917_1326'), ('invest', '0021_auto_20180917_1404'), ('invest', '0022_auto_20180917_1622'), ('invest', '0023_auto_20180918_0805'), ('invest', '0024_highpotentialopportunitydetailpage_testimonial_background'), ('invest', '0025_auto_20180920_0941'), ('invest', '0026_auto_20181002_1534')]

    dependencies = [
        ('wagtaildocs', '0008_document_file_size'),
        ('wagtailmedia', '0003_copy_media_permissions_to_collections'),
        ('wagtailcore', '0040_page_draft_title'),
        ('invest', '0010_merge_20180829_0939_squashed_0013_auto_20180830_0632'),
        ('wagtailimages', '0021_image_file_hash'),
    ]

    operations = [
        migrations.CreateModel(
            name='HighPotentialOpportunityDetailPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('service_name', models.CharField(choices=[('FIND_A_SUPPLIER', 'Find a Supplier'), ('EXPORT_READINESS', 'Export Readiness'), ('INVEST', 'Invest')], db_index=True, max_length=100, null=True)),
                ('breadcrumbs_label', models.CharField(max_length=50)),
                ('heading', models.CharField(max_length=255)),
                ('contact_proposition', core.fields.MarkdownField(validators=[core.validators.slug_hyperlinks], verbose_name='Body text')),
                ('contact_button', models.CharField(max_length=500)),
                ('proposition_one', core.fields.MarkdownField(validators=[core.validators.slug_hyperlinks])),
                ('opportunity_list_title', models.CharField(max_length=300)),
                ('opportunity_list_item_one', core.fields.MarkdownField(validators=[core.validators.slug_hyperlinks])),
                ('opportunity_list_item_two', core.fields.MarkdownField(validators=[core.validators.slug_hyperlinks])),
                ('opportunity_list_item_three', core.fields.MarkdownField(blank=True, validators=[core.validators.slug_hyperlinks])),
                ('proposition_two', core.fields.MarkdownField(validators=[core.validators.slug_hyperlinks])),
                ('proposition_two_list_item_one', core.fields.MarkdownField(validators=[core.validators.slug_hyperlinks])),
                ('proposition_two_list_item_two', core.fields.MarkdownField(validators=[core.validators.slug_hyperlinks])),
                ('proposition_two_list_item_three', core.fields.MarkdownField(validators=[core.validators.slug_hyperlinks])),
                ('competitive_advantages_title', models.CharField(max_length=300, verbose_name='Body text')),
                ('competitive_advantages_list_item_one', core.fields.MarkdownField(validators=[core.validators.slug_hyperlinks])),
                ('competitive_advantages_list_item_two', core.fields.MarkdownField(validators=[core.validators.slug_hyperlinks])),
                ('competitive_advantages_list_item_three', core.fields.MarkdownField(validators=[core.validators.slug_hyperlinks])),
                ('testimonial', core.fields.MarkdownField(blank=True, validators=[core.validators.slug_hyperlinks])),
                ('companies_list_text', core.fields.MarkdownField(validators=[core.validators.slug_hyperlinks])),
                ('case_study_list_title', models.CharField(max_length=300)),
                ('case_study_one_text', core.fields.MarkdownField(blank=True, validators=[core.validators.slug_hyperlinks])),
                ('case_study_two_text', core.fields.MarkdownField(blank=True, validators=[core.validators.slug_hyperlinks])),
                ('case_study_three_text', core.fields.MarkdownField(blank=True, validators=[core.validators.slug_hyperlinks])),
                ('case_study_four_text', core.fields.MarkdownField(blank=True, validators=[core.validators.slug_hyperlinks])),
                ('case_study_four_image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image')),
                ('case_study_one_image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image')),
                ('case_study_three_image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image')),
                ('case_study_two_image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image')),
                ('companies_list_item_image_eight', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image')),
                ('companies_list_item_image_five', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image')),
                ('companies_list_item_image_four', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image')),
                ('companies_list_item_image_one', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image')),
                ('companies_list_item_image_seven', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image')),
                ('companies_list_item_image_six', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image')),
                ('companies_list_item_image_three', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image')),
                ('companies_list_item_image_two', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image')),
                ('hero_image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image')),
                ('opportunity_list_image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image')),
                ('proposition_one_image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image')),
                ('proposition_one_video', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailmedia.Media')),
                ('proposition_two_image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image')),
                ('proposition_two_video', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailmedia.Media')),
                ('competitive_advantages_list_item_one_icon', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image')),
                ('competitive_advantages_list_item_three_icon', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image')),
                ('competitive_advantages_list_item_two_icon', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image')),
                ('other_opportunities_title', models.CharField(default='', max_length=300, verbose_name='Title')),
                ('summary_image', models.ForeignKey(blank=True, help_text='Image used on the opportunity listing page for this opportunity', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image', verbose_name='Image')),
                ('pdf_document', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtaildocs.Document')),
                ('testimonial_background', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image', verbose_name='Background image')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.RenameModel(
            old_name='HighPotentialOfferFormPage',
            new_name='HighPotentialOpportunityFormPage',
        ),
        migrations.AddField(
            model_name='highpotentialopportunityformpage',
            name='heading',
            field=models.CharField(default='Your business details', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='highpotentialopportunityformpage',
            name='sub_heading',
            field=models.CharField(default='The questions below will help us provide the best support for you', max_length=255),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='HighPotentialOpportunityFormSuccessPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('service_name', models.CharField(choices=[('FIND_A_SUPPLIER', 'Find a Supplier'), ('EXPORT_READINESS', 'Export Readiness'), ('INVEST', 'Invest')], db_index=True, max_length=100, null=True)),
                ('breadcrumbs_label', models.CharField(max_length=50)),
                ('heading', models.CharField(max_length=255, verbose_name='section title')),
                ('sub_heading', models.CharField(max_length=255, verbose_name='section body')),
                ('next_steps_title', models.CharField(max_length=255, verbose_name='section title')),
                ('next_steps_body', models.CharField(max_length=255, verbose_name='section body')),
                ('documents_title', models.CharField(max_length=255, verbose_name='section title')),
                ('documents_body', models.CharField(max_length=255, verbose_name='section body')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.AddField(
            model_name='highpotentialopportunityformpage',
            name='breadcrumbs_label',
            field=models.CharField(default='Contact us', max_length=50),
            preserve_default=False,
        ),
        migrations.RemoveField(
            model_name='highpotentialopportunityformpage',
            name='terms_agreed_help_text',
        ),
        migrations.RemoveField(
            model_name='highpotentialopportunityformpage',
            name='terms_agreed_label',
        ),
    ]
