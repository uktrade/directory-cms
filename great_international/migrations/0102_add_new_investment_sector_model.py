# Generated by Django 2.2.24 on 2021-09-07 10:07

import core.model_fields
from django.db import migrations, models
import django.db.models.deletion
import great_international.blocks.great_international
import great_international.panels.great_international
import modelcluster.fields
import wagtail.blocks
import wagtail.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0022_uploadedimage'),
        ('wagtailcore', '0059_apply_collection_ordering'),
        ('great_international', '0101_remove_limit_on_atlas_landing_page_block_main_content'),
    ]

    operations = [
        migrations.CreateModel(
            name='InternationalInvestmentSectorPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('service_name', models.CharField(choices=[('FIND_A_SUPPLIER', 'Find a Supplier'), ('EXPORT_READINESS', 'Export Readiness'), ('INVEST', 'Invest'), ('COMPONENTS', 'Components'), ('GREAT_INTERNATIONAL', 'Great International')], db_index=True, max_length=100, null=True)),
                ('uses_tree_based_routing', models.BooleanField(default=False, help_text="Allow this page's URL to be determined by its slug, and the slugs of its ancestors in the page tree.", verbose_name='tree-based routing enabled')),
                ('heading', models.CharField(max_length=255, verbose_name='Sector name')),
                ('heading_en_gb', models.CharField(max_length=255, null=True, verbose_name='Sector name')),
                ('heading_de', models.CharField(max_length=255, null=True, verbose_name='Sector name')),
                ('heading_ja', models.CharField(max_length=255, null=True, verbose_name='Sector name')),
                ('heading_zh_hans', models.CharField(max_length=255, null=True, verbose_name='Sector name')),
                ('heading_fr', models.CharField(max_length=255, null=True, verbose_name='Sector name')),
                ('heading_es', models.CharField(max_length=255, null=True, verbose_name='Sector name')),
                ('heading_pt', models.CharField(max_length=255, null=True, verbose_name='Sector name')),
                ('heading_ar', models.CharField(max_length=255, null=True, verbose_name='Sector name')),
                ('standfirst', models.TextField(blank=True, help_text='Displayed below the sector name')),
                ('standfirst_en_gb', models.TextField(blank=True, help_text='Displayed below the sector name', null=True)),
                ('standfirst_de', models.TextField(blank=True, help_text='Displayed below the sector name', null=True)),
                ('standfirst_ja', models.TextField(blank=True, help_text='Displayed below the sector name', null=True)),
                ('standfirst_zh_hans', models.TextField(blank=True, help_text='Displayed below the sector name', null=True)),
                ('standfirst_fr', models.TextField(blank=True, help_text='Displayed below the sector name', null=True)),
                ('standfirst_es', models.TextField(blank=True, help_text='Displayed below the sector name', null=True)),
                ('standfirst_pt', models.TextField(blank=True, help_text='Displayed below the sector name', null=True)),
                ('standfirst_ar', models.TextField(blank=True, help_text='Displayed below the sector name', null=True)),
                ('featured_description', models.TextField(blank=True, help_text='This is the description shown when the sector is featured on another page')),
                ('featured_description_en_gb', models.TextField(blank=True, help_text='This is the description shown when the sector is featured on another page', null=True)),
                ('featured_description_de', models.TextField(blank=True, help_text='This is the description shown when the sector is featured on another page', null=True)),
                ('featured_description_ja', models.TextField(blank=True, help_text='This is the description shown when the sector is featured on another page', null=True)),
                ('featured_description_zh_hans', models.TextField(blank=True, help_text='This is the description shown when the sector is featured on another page', null=True)),
                ('featured_description_fr', models.TextField(blank=True, help_text='This is the description shown when the sector is featured on another page', null=True)),
                ('featured_description_es', models.TextField(blank=True, help_text='This is the description shown when the sector is featured on another page', null=True)),
                ('featured_description_pt', models.TextField(blank=True, help_text='This is the description shown when the sector is featured on another page', null=True)),
                ('featured_description_ar', models.TextField(blank=True, help_text='This is the description shown when the sector is featured on another page', null=True)),
                ('intro_text', core.model_fields.MarkdownField(blank=True, null=True)),
                ('intro_text_en_gb', core.model_fields.MarkdownField(blank=True, null=True)),
                ('intro_text_de', core.model_fields.MarkdownField(blank=True, null=True)),
                ('intro_text_ja', core.model_fields.MarkdownField(blank=True, null=True)),
                ('intro_text_zh_hans', core.model_fields.MarkdownField(blank=True, null=True)),
                ('intro_text_fr', core.model_fields.MarkdownField(blank=True, null=True)),
                ('intro_text_es', core.model_fields.MarkdownField(blank=True, null=True)),
                ('intro_text_pt', core.model_fields.MarkdownField(blank=True, null=True)),
                ('intro_text_ar', core.model_fields.MarkdownField(blank=True, null=True)),
                ('contact_name', models.CharField(blank=True, max_length=255)),
                ('contact_name_en_gb', models.CharField(blank=True, max_length=255, null=True)),
                ('contact_name_de', models.CharField(blank=True, max_length=255, null=True)),
                ('contact_name_ja', models.CharField(blank=True, max_length=255, null=True)),
                ('contact_name_zh_hans', models.CharField(blank=True, max_length=255, null=True)),
                ('contact_name_fr', models.CharField(blank=True, max_length=255, null=True)),
                ('contact_name_es', models.CharField(blank=True, max_length=255, null=True)),
                ('contact_name_pt', models.CharField(blank=True, max_length=255, null=True)),
                ('contact_name_ar', models.CharField(blank=True, max_length=255, null=True)),
                ('contact_job_title', models.CharField(blank=True, max_length=255)),
                ('contact_job_title_en_gb', models.CharField(blank=True, max_length=255, null=True)),
                ('contact_job_title_de', models.CharField(blank=True, max_length=255, null=True)),
                ('contact_job_title_ja', models.CharField(blank=True, max_length=255, null=True)),
                ('contact_job_title_zh_hans', models.CharField(blank=True, max_length=255, null=True)),
                ('contact_job_title_fr', models.CharField(blank=True, max_length=255, null=True)),
                ('contact_job_title_es', models.CharField(blank=True, max_length=255, null=True)),
                ('contact_job_title_pt', models.CharField(blank=True, max_length=255, null=True)),
                ('contact_job_title_ar', models.CharField(blank=True, max_length=255, null=True)),
                ('contact_link', models.URLField(blank=True, max_length=1500, null=True)),
                ('contact_link_en_gb', models.URLField(blank=True, max_length=1500, null=True)),
                ('contact_link_de', models.URLField(blank=True, max_length=1500, null=True)),
                ('contact_link_ja', models.URLField(blank=True, max_length=1500, null=True)),
                ('contact_link_zh_hans', models.URLField(blank=True, max_length=1500, null=True)),
                ('contact_link_fr', models.URLField(blank=True, max_length=1500, null=True)),
                ('contact_link_es', models.URLField(blank=True, max_length=1500, null=True)),
                ('contact_link_pt', models.URLField(blank=True, max_length=1500, null=True)),
                ('contact_link_ar', models.URLField(blank=True, max_length=1500, null=True)),
                ('contact_link_button_preamble', models.CharField(blank=True, help_text='eg: "Contact the sector lead"', max_length=255)),
                ('contact_link_button_preamble_en_gb', models.CharField(blank=True, help_text='eg: "Contact the sector lead"', max_length=255, null=True)),
                ('contact_link_button_preamble_de', models.CharField(blank=True, help_text='eg: "Contact the sector lead"', max_length=255, null=True)),
                ('contact_link_button_preamble_ja', models.CharField(blank=True, help_text='eg: "Contact the sector lead"', max_length=255, null=True)),
                ('contact_link_button_preamble_zh_hans', models.CharField(blank=True, help_text='eg: "Contact the sector lead"', max_length=255, null=True)),
                ('contact_link_button_preamble_fr', models.CharField(blank=True, help_text='eg: "Contact the sector lead"', max_length=255, null=True)),
                ('contact_link_button_preamble_es', models.CharField(blank=True, help_text='eg: "Contact the sector lead"', max_length=255, null=True)),
                ('contact_link_button_preamble_pt', models.CharField(blank=True, help_text='eg: "Contact the sector lead"', max_length=255, null=True)),
                ('contact_link_button_preamble_ar', models.CharField(blank=True, help_text='eg: "Contact the sector lead"', max_length=255, null=True)),
                ('contact_link_button_label', models.CharField(blank=True, max_length=255)),
                ('contact_link_button_label_en_gb', models.CharField(blank=True, max_length=255, null=True)),
                ('contact_link_button_label_de', models.CharField(blank=True, max_length=255, null=True)),
                ('contact_link_button_label_ja', models.CharField(blank=True, max_length=255, null=True)),
                ('contact_link_button_label_zh_hans', models.CharField(blank=True, max_length=255, null=True)),
                ('contact_link_button_label_fr', models.CharField(blank=True, max_length=255, null=True)),
                ('contact_link_button_label_es', models.CharField(blank=True, max_length=255, null=True)),
                ('contact_link_button_label_pt', models.CharField(blank=True, max_length=255, null=True)),
                ('contact_link_button_label_ar', models.CharField(blank=True, max_length=255, null=True)),
                ('related_opportunities_header', models.CharField(blank=True, help_text='You may want to phrase this to suit the kind of opportunities being featured, if not automatic', max_length=255)),
                ('related_opportunities_header_en_gb', models.CharField(blank=True, help_text='You may want to phrase this to suit the kind of opportunities being featured, if not automatic', max_length=255, null=True)),
                ('related_opportunities_header_de', models.CharField(blank=True, help_text='You may want to phrase this to suit the kind of opportunities being featured, if not automatic', max_length=255, null=True)),
                ('related_opportunities_header_ja', models.CharField(blank=True, help_text='You may want to phrase this to suit the kind of opportunities being featured, if not automatic', max_length=255, null=True)),
                ('related_opportunities_header_zh_hans', models.CharField(blank=True, help_text='You may want to phrase this to suit the kind of opportunities being featured, if not automatic', max_length=255, null=True)),
                ('related_opportunities_header_fr', models.CharField(blank=True, help_text='You may want to phrase this to suit the kind of opportunities being featured, if not automatic', max_length=255, null=True)),
                ('related_opportunities_header_es', models.CharField(blank=True, help_text='You may want to phrase this to suit the kind of opportunities being featured, if not automatic', max_length=255, null=True)),
                ('related_opportunities_header_pt', models.CharField(blank=True, help_text='You may want to phrase this to suit the kind of opportunities being featured, if not automatic', max_length=255, null=True)),
                ('related_opportunities_header_ar', models.CharField(blank=True, help_text='You may want to phrase this to suit the kind of opportunities being featured, if not automatic', max_length=255, null=True)),
                ('downpage_content', wagtail.fields.StreamField([('content_section', wagtail.blocks.StructBlock([('content', wagtail.blocks.StreamBlock([('header', wagtail.blocks.CharBlock(max_length=255, required=False)), ('nested_content', wagtail.blocks.StreamBlock([('text', great_international.blocks.great_international.MarkdownBlock(help_text='Use H3 headers or lower, not H2 or H1')), ('image', wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=True)), ('image_alt', wagtail.blocks.CharBlock(max_length=255, required=True)), ('caption', wagtail.blocks.CharBlock(max_length=255, required=False))])), ('columns', wagtail.blocks.StreamBlock([('text', great_international.blocks.great_international.MarkdownBlock())], help_text='Smaller snippets of content'))], help_text='Smaller snippets of content', max_num=2, min_num=1))], required=False)), ('block_slug', wagtail.blocks.CharBlock(help_text="Only needed if special styling is involved: check with a developer. If in doubt, it's not needed", max_length=255, required=False))]))], blank=True, null=True)),
                ('downpage_content_en_gb', wagtail.fields.StreamField([('content_section', wagtail.blocks.StructBlock([('content', wagtail.blocks.StreamBlock([('header', wagtail.blocks.CharBlock(max_length=255, required=False)), ('nested_content', wagtail.blocks.StreamBlock([('text', great_international.blocks.great_international.MarkdownBlock(help_text='Use H3 headers or lower, not H2 or H1')), ('image', wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=True)), ('image_alt', wagtail.blocks.CharBlock(max_length=255, required=True)), ('caption', wagtail.blocks.CharBlock(max_length=255, required=False))])), ('columns', wagtail.blocks.StreamBlock([('text', great_international.blocks.great_international.MarkdownBlock())], help_text='Smaller snippets of content'))], help_text='Smaller snippets of content', max_num=2, min_num=1))], required=False)), ('block_slug', wagtail.blocks.CharBlock(help_text="Only needed if special styling is involved: check with a developer. If in doubt, it's not needed", max_length=255, required=False))]))], blank=True, null=True)),
                ('downpage_content_de', wagtail.fields.StreamField([('content_section', wagtail.blocks.StructBlock([('content', wagtail.blocks.StreamBlock([('header', wagtail.blocks.CharBlock(max_length=255, required=False)), ('nested_content', wagtail.blocks.StreamBlock([('text', great_international.blocks.great_international.MarkdownBlock(help_text='Use H3 headers or lower, not H2 or H1')), ('image', wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=True)), ('image_alt', wagtail.blocks.CharBlock(max_length=255, required=True)), ('caption', wagtail.blocks.CharBlock(max_length=255, required=False))])), ('columns', wagtail.blocks.StreamBlock([('text', great_international.blocks.great_international.MarkdownBlock())], help_text='Smaller snippets of content'))], help_text='Smaller snippets of content', max_num=2, min_num=1))], required=False)), ('block_slug', wagtail.blocks.CharBlock(help_text="Only needed if special styling is involved: check with a developer. If in doubt, it's not needed", max_length=255, required=False))]))], blank=True, null=True)),
                ('downpage_content_ja', wagtail.fields.StreamField([('content_section', wagtail.blocks.StructBlock([('content', wagtail.blocks.StreamBlock([('header', wagtail.blocks.CharBlock(max_length=255, required=False)), ('nested_content', wagtail.blocks.StreamBlock([('text', great_international.blocks.great_international.MarkdownBlock(help_text='Use H3 headers or lower, not H2 or H1')), ('image', wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=True)), ('image_alt', wagtail.blocks.CharBlock(max_length=255, required=True)), ('caption', wagtail.blocks.CharBlock(max_length=255, required=False))])), ('columns', wagtail.blocks.StreamBlock([('text', great_international.blocks.great_international.MarkdownBlock())], help_text='Smaller snippets of content'))], help_text='Smaller snippets of content', max_num=2, min_num=1))], required=False)), ('block_slug', wagtail.blocks.CharBlock(help_text="Only needed if special styling is involved: check with a developer. If in doubt, it's not needed", max_length=255, required=False))]))], blank=True, null=True)),
                ('downpage_content_zh_hans', wagtail.fields.StreamField([('content_section', wagtail.blocks.StructBlock([('content', wagtail.blocks.StreamBlock([('header', wagtail.blocks.CharBlock(max_length=255, required=False)), ('nested_content', wagtail.blocks.StreamBlock([('text', great_international.blocks.great_international.MarkdownBlock(help_text='Use H3 headers or lower, not H2 or H1')), ('image', wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=True)), ('image_alt', wagtail.blocks.CharBlock(max_length=255, required=True)), ('caption', wagtail.blocks.CharBlock(max_length=255, required=False))])), ('columns', wagtail.blocks.StreamBlock([('text', great_international.blocks.great_international.MarkdownBlock())], help_text='Smaller snippets of content'))], help_text='Smaller snippets of content', max_num=2, min_num=1))], required=False)), ('block_slug', wagtail.blocks.CharBlock(help_text="Only needed if special styling is involved: check with a developer. If in doubt, it's not needed", max_length=255, required=False))]))], blank=True, null=True)),
                ('downpage_content_fr', wagtail.fields.StreamField([('content_section', wagtail.blocks.StructBlock([('content', wagtail.blocks.StreamBlock([('header', wagtail.blocks.CharBlock(max_length=255, required=False)), ('nested_content', wagtail.blocks.StreamBlock([('text', great_international.blocks.great_international.MarkdownBlock(help_text='Use H3 headers or lower, not H2 or H1')), ('image', wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=True)), ('image_alt', wagtail.blocks.CharBlock(max_length=255, required=True)), ('caption', wagtail.blocks.CharBlock(max_length=255, required=False))])), ('columns', wagtail.blocks.StreamBlock([('text', great_international.blocks.great_international.MarkdownBlock())], help_text='Smaller snippets of content'))], help_text='Smaller snippets of content', max_num=2, min_num=1))], required=False)), ('block_slug', wagtail.blocks.CharBlock(help_text="Only needed if special styling is involved: check with a developer. If in doubt, it's not needed", max_length=255, required=False))]))], blank=True, null=True)),
                ('downpage_content_es', wagtail.fields.StreamField([('content_section', wagtail.blocks.StructBlock([('content', wagtail.blocks.StreamBlock([('header', wagtail.blocks.CharBlock(max_length=255, required=False)), ('nested_content', wagtail.blocks.StreamBlock([('text', great_international.blocks.great_international.MarkdownBlock(help_text='Use H3 headers or lower, not H2 or H1')), ('image', wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=True)), ('image_alt', wagtail.blocks.CharBlock(max_length=255, required=True)), ('caption', wagtail.blocks.CharBlock(max_length=255, required=False))])), ('columns', wagtail.blocks.StreamBlock([('text', great_international.blocks.great_international.MarkdownBlock())], help_text='Smaller snippets of content'))], help_text='Smaller snippets of content', max_num=2, min_num=1))], required=False)), ('block_slug', wagtail.blocks.CharBlock(help_text="Only needed if special styling is involved: check with a developer. If in doubt, it's not needed", max_length=255, required=False))]))], blank=True, null=True)),
                ('downpage_content_pt', wagtail.fields.StreamField([('content_section', wagtail.blocks.StructBlock([('content', wagtail.blocks.StreamBlock([('header', wagtail.blocks.CharBlock(max_length=255, required=False)), ('nested_content', wagtail.blocks.StreamBlock([('text', great_international.blocks.great_international.MarkdownBlock(help_text='Use H3 headers or lower, not H2 or H1')), ('image', wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=True)), ('image_alt', wagtail.blocks.CharBlock(max_length=255, required=True)), ('caption', wagtail.blocks.CharBlock(max_length=255, required=False))])), ('columns', wagtail.blocks.StreamBlock([('text', great_international.blocks.great_international.MarkdownBlock())], help_text='Smaller snippets of content'))], help_text='Smaller snippets of content', max_num=2, min_num=1))], required=False)), ('block_slug', wagtail.blocks.CharBlock(help_text="Only needed if special styling is involved: check with a developer. If in doubt, it's not needed", max_length=255, required=False))]))], blank=True, null=True)),
                ('downpage_content_ar', wagtail.fields.StreamField([('content_section', wagtail.blocks.StructBlock([('content', wagtail.blocks.StreamBlock([('header', wagtail.blocks.CharBlock(max_length=255, required=False)), ('nested_content', wagtail.blocks.StreamBlock([('text', great_international.blocks.great_international.MarkdownBlock(help_text='Use H3 headers or lower, not H2 or H1')), ('image', wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=True)), ('image_alt', wagtail.blocks.CharBlock(max_length=255, required=True)), ('caption', wagtail.blocks.CharBlock(max_length=255, required=False))])), ('columns', wagtail.blocks.StreamBlock([('text', great_international.blocks.great_international.MarkdownBlock())], help_text='Smaller snippets of content'))], help_text='Smaller snippets of content', max_num=2, min_num=1))], required=False)), ('block_slug', wagtail.blocks.CharBlock(help_text="Only needed if special styling is involved: check with a developer. If in doubt, it's not needed", max_length=255, required=False))]))], blank=True, null=True)),
                ('early_opportunities', wagtail.fields.StreamField([('early_opportunity', wagtail.blocks.StructBlock([('image', wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=True)), ('image_alt', wagtail.blocks.CharBlock(max_length=255, required=True)), ('caption', wagtail.blocks.CharBlock(max_length=255, required=False))], blank=False)), ('text', great_international.blocks.great_international.MarkdownBlock(blank=False))]))], blank=True, null=True)),
                ('early_opportunities_en_gb', wagtail.fields.StreamField([('early_opportunity', wagtail.blocks.StructBlock([('image', wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=True)), ('image_alt', wagtail.blocks.CharBlock(max_length=255, required=True)), ('caption', wagtail.blocks.CharBlock(max_length=255, required=False))], blank=False)), ('text', great_international.blocks.great_international.MarkdownBlock(blank=False))]))], blank=True, null=True)),
                ('early_opportunities_de', wagtail.fields.StreamField([('early_opportunity', wagtail.blocks.StructBlock([('image', wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=True)), ('image_alt', wagtail.blocks.CharBlock(max_length=255, required=True)), ('caption', wagtail.blocks.CharBlock(max_length=255, required=False))], blank=False)), ('text', great_international.blocks.great_international.MarkdownBlock(blank=False))]))], blank=True, null=True)),
                ('early_opportunities_ja', wagtail.fields.StreamField([('early_opportunity', wagtail.blocks.StructBlock([('image', wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=True)), ('image_alt', wagtail.blocks.CharBlock(max_length=255, required=True)), ('caption', wagtail.blocks.CharBlock(max_length=255, required=False))], blank=False)), ('text', great_international.blocks.great_international.MarkdownBlock(blank=False))]))], blank=True, null=True)),
                ('early_opportunities_zh_hans', wagtail.fields.StreamField([('early_opportunity', wagtail.blocks.StructBlock([('image', wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=True)), ('image_alt', wagtail.blocks.CharBlock(max_length=255, required=True)), ('caption', wagtail.blocks.CharBlock(max_length=255, required=False))], blank=False)), ('text', great_international.blocks.great_international.MarkdownBlock(blank=False))]))], blank=True, null=True)),
                ('early_opportunities_fr', wagtail.fields.StreamField([('early_opportunity', wagtail.blocks.StructBlock([('image', wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=True)), ('image_alt', wagtail.blocks.CharBlock(max_length=255, required=True)), ('caption', wagtail.blocks.CharBlock(max_length=255, required=False))], blank=False)), ('text', great_international.blocks.great_international.MarkdownBlock(blank=False))]))], blank=True, null=True)),
                ('early_opportunities_es', wagtail.fields.StreamField([('early_opportunity', wagtail.blocks.StructBlock([('image', wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=True)), ('image_alt', wagtail.blocks.CharBlock(max_length=255, required=True)), ('caption', wagtail.blocks.CharBlock(max_length=255, required=False))], blank=False)), ('text', great_international.blocks.great_international.MarkdownBlock(blank=False))]))], blank=True, null=True)),
                ('early_opportunities_pt', wagtail.fields.StreamField([('early_opportunity', wagtail.blocks.StructBlock([('image', wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=True)), ('image_alt', wagtail.blocks.CharBlock(max_length=255, required=True)), ('caption', wagtail.blocks.CharBlock(max_length=255, required=False))], blank=False)), ('text', great_international.blocks.great_international.MarkdownBlock(blank=False))]))], blank=True, null=True)),
                ('early_opportunities_ar', wagtail.fields.StreamField([('early_opportunity', wagtail.blocks.StructBlock([('image', wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=True)), ('image_alt', wagtail.blocks.CharBlock(max_length=255, required=True)), ('caption', wagtail.blocks.CharBlock(max_length=255, required=False))], blank=False)), ('text', great_international.blocks.great_international.MarkdownBlock(blank=False))]))], blank=True, null=True)),
                ('contact_avatar', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image')),
                ('contact_avatar_ar', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image')),
                ('contact_avatar_de', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image')),
                ('contact_avatar_en_gb', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image')),
                ('contact_avatar_es', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image')),
                ('contact_avatar_fr', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image')),
                ('contact_avatar_ja', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image')),
                ('contact_avatar_pt', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image')),
                ('contact_avatar_zh_hans', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image')),
                ('hero_image', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image')),
                ('hero_image_ar', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image')),
                ('hero_image_de', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image')),
                ('hero_image_en_gb', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image')),
                ('hero_image_es', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image')),
                ('hero_image_fr', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image')),
                ('hero_image_ja', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image')),
                ('hero_image_pt', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image')),
                ('hero_image_zh_hans', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image')),
                ('intro_image', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image')),
                ('intro_image_ar', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image')),
                ('intro_image_de', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image')),
                ('intro_image_en_gb', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image')),
                ('intro_image_es', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image')),
                ('intro_image_fr', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image')),
                ('intro_image_ja', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image')),
                ('intro_image_pt', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image')),
                ('intro_image_zh_hans', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image')),
                ('manually_selected_related_opportunities', modelcluster.fields.ParentalManyToManyField(blank=True, help_text='Max 3 will be shown. If none is selected, three will be automatically chosen based on priority and/or most recently created', to='great_international.InvestmentOpportunityPage')),
                ('tags', modelcluster.fields.ParentalManyToManyField(blank=True, to='export_readiness.Tag')),
            ],
            options={
                'abstract': False,
            },
            bases=(great_international.panels.great_international.InternationalInvestmentSectorPagePanels, 'wagtailcore.page'),
        ),
    ]