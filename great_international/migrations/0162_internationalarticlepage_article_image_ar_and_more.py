# Generated by Django 4.1.9 on 2023-07-03 09:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ('wagtailmedia', '0004_duration_optional_floatfield'),
        ('wagtailimages', '0024_index_image_file_hash'),
        ('great_international', '0161_alter_internationalarticlelistingpage_tags_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='internationalarticlepage',
            name='article_image_ar',
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name='+',
                to='wagtailimages.image',
            ),
        ),
        migrations.AddField(
            model_name='internationalarticlepage',
            name='article_image_de',
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name='+',
                to='wagtailimages.image',
            ),
        ),
        migrations.AddField(
            model_name='internationalarticlepage',
            name='article_image_en_gb',
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name='+',
                to='wagtailimages.image',
            ),
        ),
        migrations.AddField(
            model_name='internationalarticlepage',
            name='article_image_es',
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name='+',
                to='wagtailimages.image',
            ),
        ),
        migrations.AddField(
            model_name='internationalarticlepage',
            name='article_image_fr',
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name='+',
                to='wagtailimages.image',
            ),
        ),
        migrations.AddField(
            model_name='internationalarticlepage',
            name='article_image_ja',
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name='+',
                to='wagtailimages.image',
            ),
        ),
        migrations.AddField(
            model_name='internationalarticlepage',
            name='article_image_pt',
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name='+',
                to='wagtailimages.image',
            ),
        ),
        migrations.AddField(
            model_name='internationalarticlepage',
            name='article_image_zh_hans',
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name='+',
                to='wagtailimages.image',
            ),
        ),
        migrations.AddField(
            model_name='internationalarticlepage',
            name='article_video_ar',
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name='+',
                to='wagtailmedia.media',
            ),
        ),
        migrations.AddField(
            model_name='internationalarticlepage',
            name='article_video_de',
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name='+',
                to='wagtailmedia.media',
            ),
        ),
        migrations.AddField(
            model_name='internationalarticlepage',
            name='article_video_en_gb',
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name='+',
                to='wagtailmedia.media',
            ),
        ),
        migrations.AddField(
            model_name='internationalarticlepage',
            name='article_video_es',
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name='+',
                to='wagtailmedia.media',
            ),
        ),
        migrations.AddField(
            model_name='internationalarticlepage',
            name='article_video_fr',
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name='+',
                to='wagtailmedia.media',
            ),
        ),
        migrations.AddField(
            model_name='internationalarticlepage',
            name='article_video_ja',
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name='+',
                to='wagtailmedia.media',
            ),
        ),
        migrations.AddField(
            model_name='internationalarticlepage',
            name='article_video_pt',
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name='+',
                to='wagtailmedia.media',
            ),
        ),
        migrations.AddField(
            model_name='internationalarticlepage',
            name='article_video_zh_hans',
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name='+',
                to='wagtailmedia.media',
            ),
        ),
    ]