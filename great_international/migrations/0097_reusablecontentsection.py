# Generated by Django 2.2.24 on 2021-08-31 14:16

from django.db import migrations, models
import great_international.blocks.investment_atlas
import wagtail.blocks
import wagtail.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('great_international', '0096_auto_20210820_1509'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReusableContentSection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('content', wagtail.fields.StreamField([('text', great_international.blocks.investment_atlas.MarkdownBlock()), ('image', wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=True)), ('image_alt', wagtail.blocks.CharBlock(max_length=255, required=True)), ('caption', wagtail.blocks.CharBlock(max_length=255, required=False)), ('custom_css_class', wagtail.blocks.CharBlock(help_text="Only needed if special styling is involved: check with a developer. If in doubt, it's not needed", max_length=255, required=False))])), ('columns', wagtail.blocks.StreamBlock([('text', great_international.blocks.investment_atlas.MarkdownBlock())], help_text='Smaller snippets of content'))])),
                ('block_slug', models.CharField(blank=True, help_text="Only needed if special styling is involved: check with a developer. If in doubt, it's not needed", max_length=255)),
            ],
        ),
    ]
