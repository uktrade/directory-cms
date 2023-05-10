# Generated by Django 2.2.24 on 2021-09-27 15:34

from django.db import migrations
import wagtail.blocks
import wagtail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('great_international', '0124_increase_length_of_region_case_study_text'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='investmentopportunitypage',
            name='location_coords',
        ),
        migrations.RemoveField(
            model_name='investmentopportunitypage',
            name='related_regions',
        ),
        migrations.AddField(
            model_name='investmentopportunitypage',
            name='regions_with_locations',
            field=wagtail.fields.StreamField([('location', wagtail.blocks.StructBlock([('region', wagtail.blocks.PageChooserBlock(label='Linked Region', page_type=['great_international.AboutUkRegionPage'], required=False)), ('map_coordinate', wagtail.blocks.CharBlock(help_text='Latitude and longitude Coordinates, e.g. 176.0944492, -38.50245621', label='Linked Location Coordinates', max_length=200))]))], blank=True, null=True),
        ),
    ]
