# Generated by Django 4.1.9 on 2023-06-14 13:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('great_international', '0160_auto_20230505_1933'),
        ('export_readiness', '0081_auto_20211124_1053'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='country',
            name='region',
        ),
        migrations.RemoveField(
            model_name='industrytag',
            name='icon',
        ),
        migrations.DeleteModel(
            name='Tag',
        ),
        migrations.DeleteModel(
            name='Country',
        ),
        migrations.DeleteModel(
            name='IndustryTag',
        ),
        migrations.DeleteModel(
            name='Region',
        ),
    ]
