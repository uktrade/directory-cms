# Generated by Django 2.2.4 on 2019-09-17 13:15

import core.blocks
from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('export_readiness', '0059_auto_20190912_1349'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='campaign',
            field=wagtail.core.fields.StreamField([('campaign', wagtail.core.blocks.StructBlock([('heading', wagtail.core.blocks.CharBlock()), ('subheading', wagtail.core.blocks.CharBlock()), ('related_link', wagtail.core.blocks.RichTextBlock()), ('image', wagtail.images.blocks.ImageChooserBlock()), ('video', core.blocks.VideoChooserBlock()), ('video_transcript', wagtail.core.blocks.RichTextBlock())]))], blank=True, null=True),
        ),
    ]