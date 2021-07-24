"""Streamfield blocks for Investment Atlas pages"""

from django import forms

from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock

from core.widgets import MarkdownTextarea


IMAGE_RENDITION_SPEC = "fill-960x540"


class FeaturedImageBlock(blocks.StructBlock):
    image = ImageChooserBlock(required=True)
    image_alt = blocks.CharBlock(
        max_length=255,
        required=True,
    )
    caption = blocks.CharBlock(
        max_length=255,
        required=False,
    )

    def get_api_representation(self, value, context=None):
        """Expand the default serialization to show the image rendition URL"""
        retval = {}

        img = value.get("image")

        if img:
            retval.update(
                {
                    'image': img.get_rendition(IMAGE_RENDITION_SPEC).url,
                    'image_alt': value.get('image_alt', ''),
                    'caption': value.get('caption'),
                }
            )

        return retval


class MarkdownBlock(blocks.FieldBlock):
    def __init__(self, required=True, help_text=None, **kwargs):
        self.field = forms.CharField(
            required=required,
            help_text=help_text,
            widget=MarkdownTextarea(),
        )
        super().__init__(**kwargs)


class CopyBlock(blocks.StructBlock):
    "Generic copy block"

    text_content = MarkdownBlock(
        required=True,
    )
    custom_css_class = blocks.CharBlock(
        max_length=255,
        required=False,
        help_text="Only needed if special styling is involved: check with a developer. If in doubt, it's not needed"
    )


class ContactDetailsBlock(blocks.StructBlock):
    name = blocks.CharBlock(
        max_length=255,
        required=True,
    )
    job_title = blocks.CharBlock(
        max_length=255,
        required=True,
    )
    contact_link = blocks.CharBlock(
        blank=True,
        null=True,
        help_text="Can be a URL or an email link in the format mailto:user@example.com"
    )
