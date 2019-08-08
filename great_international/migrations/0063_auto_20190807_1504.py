# Generated by Django 2.2.3 on 2019-08-07 15:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('great_international', '0062_auto_20190731_1236'),
    ]

    operations = [
        migrations.AddField(
            model_name='investinternationalhomepage',
            name='featured_industry_one',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='great_international.InternationalSectorPage'),
        ),
        migrations.AddField(
            model_name='investinternationalhomepage',
            name='featured_industry_three',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='great_international.InternationalSectorPage'),
        ),
        migrations.AddField(
            model_name='investinternationalhomepage',
            name='featured_industry_two',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='great_international.InternationalSectorPage'),
        ),
    ]
