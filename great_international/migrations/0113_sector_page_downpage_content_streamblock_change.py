# Generated by Django 2.2.24 on 2021-09-13 14:14

from django.db import migrations
import great_international.blocks.great_international
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('great_international', '0112_whyinvestintheukpage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='internationalinvestmentsectorpage',
            name='downpage_content',
            field=wagtail.core.fields.StreamField([('content_section', wagtail.core.blocks.StructBlock([('content', wagtail.core.blocks.StreamBlock([('header', wagtail.core.blocks.CharBlock(max_length=255, required=False)), ('nested_content', wagtail.core.blocks.StreamBlock([('text', wagtail.core.blocks.StructBlock([('text', great_international.blocks.great_international.MarkdownBlock(required=False)), ('image', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('image_alt', wagtail.core.blocks.CharBlock(max_length=255, required=False)), ('caption', wagtail.core.blocks.CharBlock(max_length=255, required=False))], required=False))], help_text='Use H3 headers or lower, not H2 or H1')), ('columns', wagtail.core.blocks.StreamBlock([('text', great_international.blocks.great_international.MarkdownBlock())]))], min_num=1))], required=False)), ('block_slug', wagtail.core.blocks.CharBlock(help_text="Only needed if special styling is involved: check with a developer. If in doubt, it's not needed", max_length=255, required=False))]))], blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='internationalinvestmentsectorpage',
            name='downpage_content_ar',
            field=wagtail.core.fields.StreamField([('content_section', wagtail.core.blocks.StructBlock([('content', wagtail.core.blocks.StreamBlock([('header', wagtail.core.blocks.CharBlock(max_length=255, required=False)), ('nested_content', wagtail.core.blocks.StreamBlock([('text', wagtail.core.blocks.StructBlock([('text', great_international.blocks.great_international.MarkdownBlock(required=False)), ('image', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('image_alt', wagtail.core.blocks.CharBlock(max_length=255, required=False)), ('caption', wagtail.core.blocks.CharBlock(max_length=255, required=False))], required=False))], help_text='Use H3 headers or lower, not H2 or H1')), ('columns', wagtail.core.blocks.StreamBlock([('text', great_international.blocks.great_international.MarkdownBlock())]))], min_num=1))], required=False)), ('block_slug', wagtail.core.blocks.CharBlock(help_text="Only needed if special styling is involved: check with a developer. If in doubt, it's not needed", max_length=255, required=False))]))], blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='internationalinvestmentsectorpage',
            name='downpage_content_de',
            field=wagtail.core.fields.StreamField([('content_section', wagtail.core.blocks.StructBlock([('content', wagtail.core.blocks.StreamBlock([('header', wagtail.core.blocks.CharBlock(max_length=255, required=False)), ('nested_content', wagtail.core.blocks.StreamBlock([('text', wagtail.core.blocks.StructBlock([('text', great_international.blocks.great_international.MarkdownBlock(required=False)), ('image', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('image_alt', wagtail.core.blocks.CharBlock(max_length=255, required=False)), ('caption', wagtail.core.blocks.CharBlock(max_length=255, required=False))], required=False))], help_text='Use H3 headers or lower, not H2 or H1')), ('columns', wagtail.core.blocks.StreamBlock([('text', great_international.blocks.great_international.MarkdownBlock())]))], min_num=1))], required=False)), ('block_slug', wagtail.core.blocks.CharBlock(help_text="Only needed if special styling is involved: check with a developer. If in doubt, it's not needed", max_length=255, required=False))]))], blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='internationalinvestmentsectorpage',
            name='downpage_content_en_gb',
            field=wagtail.core.fields.StreamField([('content_section', wagtail.core.blocks.StructBlock([('content', wagtail.core.blocks.StreamBlock([('header', wagtail.core.blocks.CharBlock(max_length=255, required=False)), ('nested_content', wagtail.core.blocks.StreamBlock([('text', wagtail.core.blocks.StructBlock([('text', great_international.blocks.great_international.MarkdownBlock(required=False)), ('image', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('image_alt', wagtail.core.blocks.CharBlock(max_length=255, required=False)), ('caption', wagtail.core.blocks.CharBlock(max_length=255, required=False))], required=False))], help_text='Use H3 headers or lower, not H2 or H1')), ('columns', wagtail.core.blocks.StreamBlock([('text', great_international.blocks.great_international.MarkdownBlock())]))], min_num=1))], required=False)), ('block_slug', wagtail.core.blocks.CharBlock(help_text="Only needed if special styling is involved: check with a developer. If in doubt, it's not needed", max_length=255, required=False))]))], blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='internationalinvestmentsectorpage',
            name='downpage_content_es',
            field=wagtail.core.fields.StreamField([('content_section', wagtail.core.blocks.StructBlock([('content', wagtail.core.blocks.StreamBlock([('header', wagtail.core.blocks.CharBlock(max_length=255, required=False)), ('nested_content', wagtail.core.blocks.StreamBlock([('text', wagtail.core.blocks.StructBlock([('text', great_international.blocks.great_international.MarkdownBlock(required=False)), ('image', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('image_alt', wagtail.core.blocks.CharBlock(max_length=255, required=False)), ('caption', wagtail.core.blocks.CharBlock(max_length=255, required=False))], required=False))], help_text='Use H3 headers or lower, not H2 or H1')), ('columns', wagtail.core.blocks.StreamBlock([('text', great_international.blocks.great_international.MarkdownBlock())]))], min_num=1))], required=False)), ('block_slug', wagtail.core.blocks.CharBlock(help_text="Only needed if special styling is involved: check with a developer. If in doubt, it's not needed", max_length=255, required=False))]))], blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='internationalinvestmentsectorpage',
            name='downpage_content_fr',
            field=wagtail.core.fields.StreamField([('content_section', wagtail.core.blocks.StructBlock([('content', wagtail.core.blocks.StreamBlock([('header', wagtail.core.blocks.CharBlock(max_length=255, required=False)), ('nested_content', wagtail.core.blocks.StreamBlock([('text', wagtail.core.blocks.StructBlock([('text', great_international.blocks.great_international.MarkdownBlock(required=False)), ('image', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('image_alt', wagtail.core.blocks.CharBlock(max_length=255, required=False)), ('caption', wagtail.core.blocks.CharBlock(max_length=255, required=False))], required=False))], help_text='Use H3 headers or lower, not H2 or H1')), ('columns', wagtail.core.blocks.StreamBlock([('text', great_international.blocks.great_international.MarkdownBlock())]))], min_num=1))], required=False)), ('block_slug', wagtail.core.blocks.CharBlock(help_text="Only needed if special styling is involved: check with a developer. If in doubt, it's not needed", max_length=255, required=False))]))], blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='internationalinvestmentsectorpage',
            name='downpage_content_ja',
            field=wagtail.core.fields.StreamField([('content_section', wagtail.core.blocks.StructBlock([('content', wagtail.core.blocks.StreamBlock([('header', wagtail.core.blocks.CharBlock(max_length=255, required=False)), ('nested_content', wagtail.core.blocks.StreamBlock([('text', wagtail.core.blocks.StructBlock([('text', great_international.blocks.great_international.MarkdownBlock(required=False)), ('image', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('image_alt', wagtail.core.blocks.CharBlock(max_length=255, required=False)), ('caption', wagtail.core.blocks.CharBlock(max_length=255, required=False))], required=False))], help_text='Use H3 headers or lower, not H2 or H1')), ('columns', wagtail.core.blocks.StreamBlock([('text', great_international.blocks.great_international.MarkdownBlock())]))], min_num=1))], required=False)), ('block_slug', wagtail.core.blocks.CharBlock(help_text="Only needed if special styling is involved: check with a developer. If in doubt, it's not needed", max_length=255, required=False))]))], blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='internationalinvestmentsectorpage',
            name='downpage_content_pt',
            field=wagtail.core.fields.StreamField([('content_section', wagtail.core.blocks.StructBlock([('content', wagtail.core.blocks.StreamBlock([('header', wagtail.core.blocks.CharBlock(max_length=255, required=False)), ('nested_content', wagtail.core.blocks.StreamBlock([('text', wagtail.core.blocks.StructBlock([('text', great_international.blocks.great_international.MarkdownBlock(required=False)), ('image', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('image_alt', wagtail.core.blocks.CharBlock(max_length=255, required=False)), ('caption', wagtail.core.blocks.CharBlock(max_length=255, required=False))], required=False))], help_text='Use H3 headers or lower, not H2 or H1')), ('columns', wagtail.core.blocks.StreamBlock([('text', great_international.blocks.great_international.MarkdownBlock())]))], min_num=1))], required=False)), ('block_slug', wagtail.core.blocks.CharBlock(help_text="Only needed if special styling is involved: check with a developer. If in doubt, it's not needed", max_length=255, required=False))]))], blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='internationalinvestmentsectorpage',
            name='downpage_content_zh_hans',
            field=wagtail.core.fields.StreamField([('content_section', wagtail.core.blocks.StructBlock([('content', wagtail.core.blocks.StreamBlock([('header', wagtail.core.blocks.CharBlock(max_length=255, required=False)), ('nested_content', wagtail.core.blocks.StreamBlock([('text', wagtail.core.blocks.StructBlock([('text', great_international.blocks.great_international.MarkdownBlock(required=False)), ('image', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('image_alt', wagtail.core.blocks.CharBlock(max_length=255, required=False)), ('caption', wagtail.core.blocks.CharBlock(max_length=255, required=False))], required=False))], help_text='Use H3 headers or lower, not H2 or H1')), ('columns', wagtail.core.blocks.StreamBlock([('text', great_international.blocks.great_international.MarkdownBlock())]))], min_num=1))], required=False)), ('block_slug', wagtail.core.blocks.CharBlock(help_text="Only needed if special styling is involved: check with a developer. If in doubt, it's not needed", max_length=255, required=False))]))], blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='internationalinvestmentsectorpage',
            name='early_opportunities',
            field=wagtail.core.fields.StreamField([('early_opportunity', wagtail.core.blocks.StructBlock([('text', great_international.blocks.great_international.MarkdownBlock(required=False)), ('image', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('image_alt', wagtail.core.blocks.CharBlock(max_length=255, required=False)), ('caption', wagtail.core.blocks.CharBlock(max_length=255, required=False))], required=False))]))], blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='internationalinvestmentsectorpage',
            name='early_opportunities_ar',
            field=wagtail.core.fields.StreamField([('early_opportunity', wagtail.core.blocks.StructBlock([('text', great_international.blocks.great_international.MarkdownBlock(required=False)), ('image', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('image_alt', wagtail.core.blocks.CharBlock(max_length=255, required=False)), ('caption', wagtail.core.blocks.CharBlock(max_length=255, required=False))], required=False))]))], blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='internationalinvestmentsectorpage',
            name='early_opportunities_de',
            field=wagtail.core.fields.StreamField([('early_opportunity', wagtail.core.blocks.StructBlock([('text', great_international.blocks.great_international.MarkdownBlock(required=False)), ('image', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('image_alt', wagtail.core.blocks.CharBlock(max_length=255, required=False)), ('caption', wagtail.core.blocks.CharBlock(max_length=255, required=False))], required=False))]))], blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='internationalinvestmentsectorpage',
            name='early_opportunities_en_gb',
            field=wagtail.core.fields.StreamField([('early_opportunity', wagtail.core.blocks.StructBlock([('text', great_international.blocks.great_international.MarkdownBlock(required=False)), ('image', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('image_alt', wagtail.core.blocks.CharBlock(max_length=255, required=False)), ('caption', wagtail.core.blocks.CharBlock(max_length=255, required=False))], required=False))]))], blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='internationalinvestmentsectorpage',
            name='early_opportunities_es',
            field=wagtail.core.fields.StreamField([('early_opportunity', wagtail.core.blocks.StructBlock([('text', great_international.blocks.great_international.MarkdownBlock(required=False)), ('image', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('image_alt', wagtail.core.blocks.CharBlock(max_length=255, required=False)), ('caption', wagtail.core.blocks.CharBlock(max_length=255, required=False))], required=False))]))], blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='internationalinvestmentsectorpage',
            name='early_opportunities_fr',
            field=wagtail.core.fields.StreamField([('early_opportunity', wagtail.core.blocks.StructBlock([('text', great_international.blocks.great_international.MarkdownBlock(required=False)), ('image', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('image_alt', wagtail.core.blocks.CharBlock(max_length=255, required=False)), ('caption', wagtail.core.blocks.CharBlock(max_length=255, required=False))], required=False))]))], blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='internationalinvestmentsectorpage',
            name='early_opportunities_ja',
            field=wagtail.core.fields.StreamField([('early_opportunity', wagtail.core.blocks.StructBlock([('text', great_international.blocks.great_international.MarkdownBlock(required=False)), ('image', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('image_alt', wagtail.core.blocks.CharBlock(max_length=255, required=False)), ('caption', wagtail.core.blocks.CharBlock(max_length=255, required=False))], required=False))]))], blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='internationalinvestmentsectorpage',
            name='early_opportunities_pt',
            field=wagtail.core.fields.StreamField([('early_opportunity', wagtail.core.blocks.StructBlock([('text', great_international.blocks.great_international.MarkdownBlock(required=False)), ('image', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('image_alt', wagtail.core.blocks.CharBlock(max_length=255, required=False)), ('caption', wagtail.core.blocks.CharBlock(max_length=255, required=False))], required=False))]))], blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='internationalinvestmentsectorpage',
            name='early_opportunities_zh_hans',
            field=wagtail.core.fields.StreamField([('early_opportunity', wagtail.core.blocks.StructBlock([('text', great_international.blocks.great_international.MarkdownBlock(required=False)), ('image', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('image_alt', wagtail.core.blocks.CharBlock(max_length=255, required=False)), ('caption', wagtail.core.blocks.CharBlock(max_length=255, required=False))], required=False))]))], blank=True, null=True),
        ),
    ]
