# Generated by Django 4.1.9 on 2023-06-14 14:57

from django.db import migrations
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0032_auto_20230614_0954'),
        ('great_international', '0160_auto_20230505_1933'),
    ]

    operations = [
        migrations.AlterField(
            model_name='internationalarticlelistingpage',
            name='tags',
            field=modelcluster.fields.ParentalManyToManyField(blank=True, to='core.tag'),
        ),
        migrations.AlterField(
            model_name='internationalarticlepage',
            name='tags',
            field=modelcluster.fields.ParentalManyToManyField(blank=True, to='core.tag'),
        ),
        migrations.AlterField(
            model_name='internationalcampaignpage',
            name='tags',
            field=modelcluster.fields.ParentalManyToManyField(blank=True, to='core.tag'),
        ),
        migrations.AlterField(
            model_name='internationalinvestmentsectorpage',
            name='tags',
            field=modelcluster.fields.ParentalManyToManyField(blank=True, to='core.tag'),
        ),
        migrations.AlterField(
            model_name='internationaltopiclandingpage',
            name='tags',
            field=modelcluster.fields.ParentalManyToManyField(blank=True, to='core.tag'),
        ),
    ]
