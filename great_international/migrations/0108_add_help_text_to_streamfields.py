# Generated by Django 2.2.24 on 2021-09-09 11:52

from django.db import migrations
import great_international.blocks.great_international
import great_international.blocks.investment_atlas
import great_international.models.investment_atlas
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('great_international', '0107_remove_character_limit_on_opportunity_intro'),
    ]

    operations = [
        migrations.AlterField(
            model_name='investmentatlaslandingpage',
            name='downpage_sections',
            field=wagtail.core.fields.StreamField([('panel', wagtail.core.blocks.StructBlock([('heading', wagtail.core.blocks.CharBlock(max_length=255, required=True)), ('main_text', wagtail.core.blocks.TextBlock(help_text='The first column of the panel')), ('call_to_action', wagtail.core.blocks.StructBlock([('label', wagtail.core.blocks.CharBlock(max_length=255)), ('link', wagtail.core.blocks.StructBlock([('internal_link', wagtail.core.blocks.PageChooserBlock(label='Internal link', required=False)), ('external_link', wagtail.core.blocks.CharBlock(label='External link', max_length=255, required=False))], required=False))], help_text='Set text for the CTA and either an internal or an external URL for its destination', required=False)), ('second_column', wagtail.core.blocks.StreamBlock([('image', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=True)), ('image_alt', wagtail.core.blocks.CharBlock(max_length=255, required=True)), ('caption', wagtail.core.blocks.CharBlock(max_length=255, required=False))])), ('text', wagtail.core.blocks.TextBlock())], help_text='An image OR a text block, but not both.', label='Second column of panel', max_num=1, required=False)), ('block_slug', wagtail.core.blocks.CharBlock(help_text='If a block has special content, this helps us identify it. Consult with a developer when you set it. If in doubt, leave it blank.', max_length=255, required=False))], help_text="If 'Block slug' is set to 'with-regions-map', the panel will show the regions map"))], blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='investmentatlaslandingpage',
            name='downpage_sections_ar',
            field=wagtail.core.fields.StreamField([('panel', wagtail.core.blocks.StructBlock([('heading', wagtail.core.blocks.CharBlock(max_length=255, required=True)), ('main_text', wagtail.core.blocks.TextBlock(help_text='The first column of the panel')), ('call_to_action', wagtail.core.blocks.StructBlock([('label', wagtail.core.blocks.CharBlock(max_length=255)), ('link', wagtail.core.blocks.StructBlock([('internal_link', wagtail.core.blocks.PageChooserBlock(label='Internal link', required=False)), ('external_link', wagtail.core.blocks.CharBlock(label='External link', max_length=255, required=False))], required=False))], help_text='Set text for the CTA and either an internal or an external URL for its destination', required=False)), ('second_column', wagtail.core.blocks.StreamBlock([('image', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=True)), ('image_alt', wagtail.core.blocks.CharBlock(max_length=255, required=True)), ('caption', wagtail.core.blocks.CharBlock(max_length=255, required=False))])), ('text', wagtail.core.blocks.TextBlock())], help_text='An image OR a text block, but not both.', label='Second column of panel', max_num=1, required=False)), ('block_slug', wagtail.core.blocks.CharBlock(help_text='If a block has special content, this helps us identify it. Consult with a developer when you set it. If in doubt, leave it blank.', max_length=255, required=False))], help_text="If 'Block slug' is set to 'with-regions-map', the panel will show the regions map"))], blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='investmentatlaslandingpage',
            name='downpage_sections_de',
            field=wagtail.core.fields.StreamField([('panel', wagtail.core.blocks.StructBlock([('heading', wagtail.core.blocks.CharBlock(max_length=255, required=True)), ('main_text', wagtail.core.blocks.TextBlock(help_text='The first column of the panel')), ('call_to_action', wagtail.core.blocks.StructBlock([('label', wagtail.core.blocks.CharBlock(max_length=255)), ('link', wagtail.core.blocks.StructBlock([('internal_link', wagtail.core.blocks.PageChooserBlock(label='Internal link', required=False)), ('external_link', wagtail.core.blocks.CharBlock(label='External link', max_length=255, required=False))], required=False))], help_text='Set text for the CTA and either an internal or an external URL for its destination', required=False)), ('second_column', wagtail.core.blocks.StreamBlock([('image', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=True)), ('image_alt', wagtail.core.blocks.CharBlock(max_length=255, required=True)), ('caption', wagtail.core.blocks.CharBlock(max_length=255, required=False))])), ('text', wagtail.core.blocks.TextBlock())], help_text='An image OR a text block, but not both.', label='Second column of panel', max_num=1, required=False)), ('block_slug', wagtail.core.blocks.CharBlock(help_text='If a block has special content, this helps us identify it. Consult with a developer when you set it. If in doubt, leave it blank.', max_length=255, required=False))], help_text="If 'Block slug' is set to 'with-regions-map', the panel will show the regions map"))], blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='investmentatlaslandingpage',
            name='downpage_sections_en_gb',
            field=wagtail.core.fields.StreamField([('panel', wagtail.core.blocks.StructBlock([('heading', wagtail.core.blocks.CharBlock(max_length=255, required=True)), ('main_text', wagtail.core.blocks.TextBlock(help_text='The first column of the panel')), ('call_to_action', wagtail.core.blocks.StructBlock([('label', wagtail.core.blocks.CharBlock(max_length=255)), ('link', wagtail.core.blocks.StructBlock([('internal_link', wagtail.core.blocks.PageChooserBlock(label='Internal link', required=False)), ('external_link', wagtail.core.blocks.CharBlock(label='External link', max_length=255, required=False))], required=False))], help_text='Set text for the CTA and either an internal or an external URL for its destination', required=False)), ('second_column', wagtail.core.blocks.StreamBlock([('image', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=True)), ('image_alt', wagtail.core.blocks.CharBlock(max_length=255, required=True)), ('caption', wagtail.core.blocks.CharBlock(max_length=255, required=False))])), ('text', wagtail.core.blocks.TextBlock())], help_text='An image OR a text block, but not both.', label='Second column of panel', max_num=1, required=False)), ('block_slug', wagtail.core.blocks.CharBlock(help_text='If a block has special content, this helps us identify it. Consult with a developer when you set it. If in doubt, leave it blank.', max_length=255, required=False))], help_text="If 'Block slug' is set to 'with-regions-map', the panel will show the regions map"))], blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='investmentatlaslandingpage',
            name='downpage_sections_es',
            field=wagtail.core.fields.StreamField([('panel', wagtail.core.blocks.StructBlock([('heading', wagtail.core.blocks.CharBlock(max_length=255, required=True)), ('main_text', wagtail.core.blocks.TextBlock(help_text='The first column of the panel')), ('call_to_action', wagtail.core.blocks.StructBlock([('label', wagtail.core.blocks.CharBlock(max_length=255)), ('link', wagtail.core.blocks.StructBlock([('internal_link', wagtail.core.blocks.PageChooserBlock(label='Internal link', required=False)), ('external_link', wagtail.core.blocks.CharBlock(label='External link', max_length=255, required=False))], required=False))], help_text='Set text for the CTA and either an internal or an external URL for its destination', required=False)), ('second_column', wagtail.core.blocks.StreamBlock([('image', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=True)), ('image_alt', wagtail.core.blocks.CharBlock(max_length=255, required=True)), ('caption', wagtail.core.blocks.CharBlock(max_length=255, required=False))])), ('text', wagtail.core.blocks.TextBlock())], help_text='An image OR a text block, but not both.', label='Second column of panel', max_num=1, required=False)), ('block_slug', wagtail.core.blocks.CharBlock(help_text='If a block has special content, this helps us identify it. Consult with a developer when you set it. If in doubt, leave it blank.', max_length=255, required=False))], help_text="If 'Block slug' is set to 'with-regions-map', the panel will show the regions map"))], blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='investmentatlaslandingpage',
            name='downpage_sections_fr',
            field=wagtail.core.fields.StreamField([('panel', wagtail.core.blocks.StructBlock([('heading', wagtail.core.blocks.CharBlock(max_length=255, required=True)), ('main_text', wagtail.core.blocks.TextBlock(help_text='The first column of the panel')), ('call_to_action', wagtail.core.blocks.StructBlock([('label', wagtail.core.blocks.CharBlock(max_length=255)), ('link', wagtail.core.blocks.StructBlock([('internal_link', wagtail.core.blocks.PageChooserBlock(label='Internal link', required=False)), ('external_link', wagtail.core.blocks.CharBlock(label='External link', max_length=255, required=False))], required=False))], help_text='Set text for the CTA and either an internal or an external URL for its destination', required=False)), ('second_column', wagtail.core.blocks.StreamBlock([('image', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=True)), ('image_alt', wagtail.core.blocks.CharBlock(max_length=255, required=True)), ('caption', wagtail.core.blocks.CharBlock(max_length=255, required=False))])), ('text', wagtail.core.blocks.TextBlock())], help_text='An image OR a text block, but not both.', label='Second column of panel', max_num=1, required=False)), ('block_slug', wagtail.core.blocks.CharBlock(help_text='If a block has special content, this helps us identify it. Consult with a developer when you set it. If in doubt, leave it blank.', max_length=255, required=False))], help_text="If 'Block slug' is set to 'with-regions-map', the panel will show the regions map"))], blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='investmentatlaslandingpage',
            name='downpage_sections_ja',
            field=wagtail.core.fields.StreamField([('panel', wagtail.core.blocks.StructBlock([('heading', wagtail.core.blocks.CharBlock(max_length=255, required=True)), ('main_text', wagtail.core.blocks.TextBlock(help_text='The first column of the panel')), ('call_to_action', wagtail.core.blocks.StructBlock([('label', wagtail.core.blocks.CharBlock(max_length=255)), ('link', wagtail.core.blocks.StructBlock([('internal_link', wagtail.core.blocks.PageChooserBlock(label='Internal link', required=False)), ('external_link', wagtail.core.blocks.CharBlock(label='External link', max_length=255, required=False))], required=False))], help_text='Set text for the CTA and either an internal or an external URL for its destination', required=False)), ('second_column', wagtail.core.blocks.StreamBlock([('image', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=True)), ('image_alt', wagtail.core.blocks.CharBlock(max_length=255, required=True)), ('caption', wagtail.core.blocks.CharBlock(max_length=255, required=False))])), ('text', wagtail.core.blocks.TextBlock())], help_text='An image OR a text block, but not both.', label='Second column of panel', max_num=1, required=False)), ('block_slug', wagtail.core.blocks.CharBlock(help_text='If a block has special content, this helps us identify it. Consult with a developer when you set it. If in doubt, leave it blank.', max_length=255, required=False))], help_text="If 'Block slug' is set to 'with-regions-map', the panel will show the regions map"))], blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='investmentatlaslandingpage',
            name='downpage_sections_pt',
            field=wagtail.core.fields.StreamField([('panel', wagtail.core.blocks.StructBlock([('heading', wagtail.core.blocks.CharBlock(max_length=255, required=True)), ('main_text', wagtail.core.blocks.TextBlock(help_text='The first column of the panel')), ('call_to_action', wagtail.core.blocks.StructBlock([('label', wagtail.core.blocks.CharBlock(max_length=255)), ('link', wagtail.core.blocks.StructBlock([('internal_link', wagtail.core.blocks.PageChooserBlock(label='Internal link', required=False)), ('external_link', wagtail.core.blocks.CharBlock(label='External link', max_length=255, required=False))], required=False))], help_text='Set text for the CTA and either an internal or an external URL for its destination', required=False)), ('second_column', wagtail.core.blocks.StreamBlock([('image', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=True)), ('image_alt', wagtail.core.blocks.CharBlock(max_length=255, required=True)), ('caption', wagtail.core.blocks.CharBlock(max_length=255, required=False))])), ('text', wagtail.core.blocks.TextBlock())], help_text='An image OR a text block, but not both.', label='Second column of panel', max_num=1, required=False)), ('block_slug', wagtail.core.blocks.CharBlock(help_text='If a block has special content, this helps us identify it. Consult with a developer when you set it. If in doubt, leave it blank.', max_length=255, required=False))], help_text="If 'Block slug' is set to 'with-regions-map', the panel will show the regions map"))], blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='investmentatlaslandingpage',
            name='downpage_sections_zh_hans',
            field=wagtail.core.fields.StreamField([('panel', wagtail.core.blocks.StructBlock([('heading', wagtail.core.blocks.CharBlock(max_length=255, required=True)), ('main_text', wagtail.core.blocks.TextBlock(help_text='The first column of the panel')), ('call_to_action', wagtail.core.blocks.StructBlock([('label', wagtail.core.blocks.CharBlock(max_length=255)), ('link', wagtail.core.blocks.StructBlock([('internal_link', wagtail.core.blocks.PageChooserBlock(label='Internal link', required=False)), ('external_link', wagtail.core.blocks.CharBlock(label='External link', max_length=255, required=False))], required=False))], help_text='Set text for the CTA and either an internal or an external URL for its destination', required=False)), ('second_column', wagtail.core.blocks.StreamBlock([('image', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=True)), ('image_alt', wagtail.core.blocks.CharBlock(max_length=255, required=True)), ('caption', wagtail.core.blocks.CharBlock(max_length=255, required=False))])), ('text', wagtail.core.blocks.TextBlock())], help_text='An image OR a text block, but not both.', label='Second column of panel', max_num=1, required=False)), ('block_slug', wagtail.core.blocks.CharBlock(help_text='If a block has special content, this helps us identify it. Consult with a developer when you set it. If in doubt, leave it blank.', max_length=255, required=False))], help_text="If 'Block slug' is set to 'with-regions-map', the panel will show the regions map"))], blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='investmentopportunitypage',
            name='main_content',
            field=wagtail.core.fields.StreamField([('content_section', wagtail.core.blocks.StructBlock([('content', wagtail.core.blocks.StreamBlock([('text', great_international.blocks.great_international.MarkdownBlock()), ('image', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=True)), ('image_alt', wagtail.core.blocks.CharBlock(max_length=255, required=True)), ('caption', wagtail.core.blocks.CharBlock(max_length=255, required=False)), ('custom_css_class', wagtail.core.blocks.CharBlock(help_text="Only needed if special styling is involved: check with a developer. If in doubt, it's not needed", max_length=255, required=False))])), ('columns', wagtail.core.blocks.StreamBlock([('text', great_international.blocks.great_international.MarkdownBlock())], help_text='Smaller snippets of content'))], required=False)), ('block_slug', wagtail.core.blocks.CharBlock(help_text="Only needed if special styling is involved: check with a developer. If in doubt, it's not needed", max_length=255, required=False))], help_text="If 'Block slug' is set to 'with-key-links', the 'Key links' panel is shown next to the text. If 'Block slug' is set to 'with-region-spotlight', the 'Region spotlight' panel is shown next to the text.")), ('snippet_content', great_international.blocks.investment_atlas.ReusableSnippetChooserBlock(great_international.models.investment_atlas.ReusableContentSection))], blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='investmentopportunitypage',
            name='main_content_ar',
            field=wagtail.core.fields.StreamField([('content_section', wagtail.core.blocks.StructBlock([('content', wagtail.core.blocks.StreamBlock([('text', great_international.blocks.great_international.MarkdownBlock()), ('image', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=True)), ('image_alt', wagtail.core.blocks.CharBlock(max_length=255, required=True)), ('caption', wagtail.core.blocks.CharBlock(max_length=255, required=False)), ('custom_css_class', wagtail.core.blocks.CharBlock(help_text="Only needed if special styling is involved: check with a developer. If in doubt, it's not needed", max_length=255, required=False))])), ('columns', wagtail.core.blocks.StreamBlock([('text', great_international.blocks.great_international.MarkdownBlock())], help_text='Smaller snippets of content'))], required=False)), ('block_slug', wagtail.core.blocks.CharBlock(help_text="Only needed if special styling is involved: check with a developer. If in doubt, it's not needed", max_length=255, required=False))], help_text="If 'Block slug' is set to 'with-key-links', the 'Key links' panel is shown next to the text. If 'Block slug' is set to 'with-region-spotlight', the 'Region spotlight' panel is shown next to the text.")), ('snippet_content', great_international.blocks.investment_atlas.ReusableSnippetChooserBlock(great_international.models.investment_atlas.ReusableContentSection))], blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='investmentopportunitypage',
            name='main_content_de',
            field=wagtail.core.fields.StreamField([('content_section', wagtail.core.blocks.StructBlock([('content', wagtail.core.blocks.StreamBlock([('text', great_international.blocks.great_international.MarkdownBlock()), ('image', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=True)), ('image_alt', wagtail.core.blocks.CharBlock(max_length=255, required=True)), ('caption', wagtail.core.blocks.CharBlock(max_length=255, required=False)), ('custom_css_class', wagtail.core.blocks.CharBlock(help_text="Only needed if special styling is involved: check with a developer. If in doubt, it's not needed", max_length=255, required=False))])), ('columns', wagtail.core.blocks.StreamBlock([('text', great_international.blocks.great_international.MarkdownBlock())], help_text='Smaller snippets of content'))], required=False)), ('block_slug', wagtail.core.blocks.CharBlock(help_text="Only needed if special styling is involved: check with a developer. If in doubt, it's not needed", max_length=255, required=False))], help_text="If 'Block slug' is set to 'with-key-links', the 'Key links' panel is shown next to the text. If 'Block slug' is set to 'with-region-spotlight', the 'Region spotlight' panel is shown next to the text.")), ('snippet_content', great_international.blocks.investment_atlas.ReusableSnippetChooserBlock(great_international.models.investment_atlas.ReusableContentSection))], blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='investmentopportunitypage',
            name='main_content_en_gb',
            field=wagtail.core.fields.StreamField([('content_section', wagtail.core.blocks.StructBlock([('content', wagtail.core.blocks.StreamBlock([('text', great_international.blocks.great_international.MarkdownBlock()), ('image', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=True)), ('image_alt', wagtail.core.blocks.CharBlock(max_length=255, required=True)), ('caption', wagtail.core.blocks.CharBlock(max_length=255, required=False)), ('custom_css_class', wagtail.core.blocks.CharBlock(help_text="Only needed if special styling is involved: check with a developer. If in doubt, it's not needed", max_length=255, required=False))])), ('columns', wagtail.core.blocks.StreamBlock([('text', great_international.blocks.great_international.MarkdownBlock())], help_text='Smaller snippets of content'))], required=False)), ('block_slug', wagtail.core.blocks.CharBlock(help_text="Only needed if special styling is involved: check with a developer. If in doubt, it's not needed", max_length=255, required=False))], help_text="If 'Block slug' is set to 'with-key-links', the 'Key links' panel is shown next to the text. If 'Block slug' is set to 'with-region-spotlight', the 'Region spotlight' panel is shown next to the text.")), ('snippet_content', great_international.blocks.investment_atlas.ReusableSnippetChooserBlock(great_international.models.investment_atlas.ReusableContentSection))], blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='investmentopportunitypage',
            name='main_content_es',
            field=wagtail.core.fields.StreamField([('content_section', wagtail.core.blocks.StructBlock([('content', wagtail.core.blocks.StreamBlock([('text', great_international.blocks.great_international.MarkdownBlock()), ('image', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=True)), ('image_alt', wagtail.core.blocks.CharBlock(max_length=255, required=True)), ('caption', wagtail.core.blocks.CharBlock(max_length=255, required=False)), ('custom_css_class', wagtail.core.blocks.CharBlock(help_text="Only needed if special styling is involved: check with a developer. If in doubt, it's not needed", max_length=255, required=False))])), ('columns', wagtail.core.blocks.StreamBlock([('text', great_international.blocks.great_international.MarkdownBlock())], help_text='Smaller snippets of content'))], required=False)), ('block_slug', wagtail.core.blocks.CharBlock(help_text="Only needed if special styling is involved: check with a developer. If in doubt, it's not needed", max_length=255, required=False))], help_text="If 'Block slug' is set to 'with-key-links', the 'Key links' panel is shown next to the text. If 'Block slug' is set to 'with-region-spotlight', the 'Region spotlight' panel is shown next to the text.")), ('snippet_content', great_international.blocks.investment_atlas.ReusableSnippetChooserBlock(great_international.models.investment_atlas.ReusableContentSection))], blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='investmentopportunitypage',
            name='main_content_fr',
            field=wagtail.core.fields.StreamField([('content_section', wagtail.core.blocks.StructBlock([('content', wagtail.core.blocks.StreamBlock([('text', great_international.blocks.great_international.MarkdownBlock()), ('image', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=True)), ('image_alt', wagtail.core.blocks.CharBlock(max_length=255, required=True)), ('caption', wagtail.core.blocks.CharBlock(max_length=255, required=False)), ('custom_css_class', wagtail.core.blocks.CharBlock(help_text="Only needed if special styling is involved: check with a developer. If in doubt, it's not needed", max_length=255, required=False))])), ('columns', wagtail.core.blocks.StreamBlock([('text', great_international.blocks.great_international.MarkdownBlock())], help_text='Smaller snippets of content'))], required=False)), ('block_slug', wagtail.core.blocks.CharBlock(help_text="Only needed if special styling is involved: check with a developer. If in doubt, it's not needed", max_length=255, required=False))], help_text="If 'Block slug' is set to 'with-key-links', the 'Key links' panel is shown next to the text. If 'Block slug' is set to 'with-region-spotlight', the 'Region spotlight' panel is shown next to the text.")), ('snippet_content', great_international.blocks.investment_atlas.ReusableSnippetChooserBlock(great_international.models.investment_atlas.ReusableContentSection))], blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='investmentopportunitypage',
            name='main_content_ja',
            field=wagtail.core.fields.StreamField([('content_section', wagtail.core.blocks.StructBlock([('content', wagtail.core.blocks.StreamBlock([('text', great_international.blocks.great_international.MarkdownBlock()), ('image', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=True)), ('image_alt', wagtail.core.blocks.CharBlock(max_length=255, required=True)), ('caption', wagtail.core.blocks.CharBlock(max_length=255, required=False)), ('custom_css_class', wagtail.core.blocks.CharBlock(help_text="Only needed if special styling is involved: check with a developer. If in doubt, it's not needed", max_length=255, required=False))])), ('columns', wagtail.core.blocks.StreamBlock([('text', great_international.blocks.great_international.MarkdownBlock())], help_text='Smaller snippets of content'))], required=False)), ('block_slug', wagtail.core.blocks.CharBlock(help_text="Only needed if special styling is involved: check with a developer. If in doubt, it's not needed", max_length=255, required=False))], help_text="If 'Block slug' is set to 'with-key-links', the 'Key links' panel is shown next to the text. If 'Block slug' is set to 'with-region-spotlight', the 'Region spotlight' panel is shown next to the text.")), ('snippet_content', great_international.blocks.investment_atlas.ReusableSnippetChooserBlock(great_international.models.investment_atlas.ReusableContentSection))], blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='investmentopportunitypage',
            name='main_content_pt',
            field=wagtail.core.fields.StreamField([('content_section', wagtail.core.blocks.StructBlock([('content', wagtail.core.blocks.StreamBlock([('text', great_international.blocks.great_international.MarkdownBlock()), ('image', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=True)), ('image_alt', wagtail.core.blocks.CharBlock(max_length=255, required=True)), ('caption', wagtail.core.blocks.CharBlock(max_length=255, required=False)), ('custom_css_class', wagtail.core.blocks.CharBlock(help_text="Only needed if special styling is involved: check with a developer. If in doubt, it's not needed", max_length=255, required=False))])), ('columns', wagtail.core.blocks.StreamBlock([('text', great_international.blocks.great_international.MarkdownBlock())], help_text='Smaller snippets of content'))], required=False)), ('block_slug', wagtail.core.blocks.CharBlock(help_text="Only needed if special styling is involved: check with a developer. If in doubt, it's not needed", max_length=255, required=False))], help_text="If 'Block slug' is set to 'with-key-links', the 'Key links' panel is shown next to the text. If 'Block slug' is set to 'with-region-spotlight', the 'Region spotlight' panel is shown next to the text.")), ('snippet_content', great_international.blocks.investment_atlas.ReusableSnippetChooserBlock(great_international.models.investment_atlas.ReusableContentSection))], blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='investmentopportunitypage',
            name='main_content_zh_hans',
            field=wagtail.core.fields.StreamField([('content_section', wagtail.core.blocks.StructBlock([('content', wagtail.core.blocks.StreamBlock([('text', great_international.blocks.great_international.MarkdownBlock()), ('image', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=True)), ('image_alt', wagtail.core.blocks.CharBlock(max_length=255, required=True)), ('caption', wagtail.core.blocks.CharBlock(max_length=255, required=False)), ('custom_css_class', wagtail.core.blocks.CharBlock(help_text="Only needed if special styling is involved: check with a developer. If in doubt, it's not needed", max_length=255, required=False))])), ('columns', wagtail.core.blocks.StreamBlock([('text', great_international.blocks.great_international.MarkdownBlock())], help_text='Smaller snippets of content'))], required=False)), ('block_slug', wagtail.core.blocks.CharBlock(help_text="Only needed if special styling is involved: check with a developer. If in doubt, it's not needed", max_length=255, required=False))], help_text="If 'Block slug' is set to 'with-key-links', the 'Key links' panel is shown next to the text. If 'Block slug' is set to 'with-region-spotlight', the 'Region spotlight' panel is shown next to the text.")), ('snippet_content', great_international.blocks.investment_atlas.ReusableSnippetChooserBlock(great_international.models.investment_atlas.ReusableContentSection))], blank=True, null=True),
        ),
    ]