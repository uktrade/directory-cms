"""Streamfield blocks for Investment Atlas pages"""

from django import forms

from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock

from core.blocks import ButtonBlock
from core.helpers import render_markdown
from core.widgets import MarkdownTextarea


DEFAULT_IMAGE_RENDITION_SPEC = "fill-960x540"


class BaseAtlasImageBlock(blocks.StructBlock):
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
        if not context:
            context = {}

        retval_dict = {}

        img = value.get("image")

        if img:
            _rendition_spec = context.get('rendition_spec', DEFAULT_IMAGE_RENDITION_SPEC)
            retval_dict.update(
                {
                    'image': img.get_rendition(_rendition_spec).url,
                    'image_alt': value.get('image_alt'),
                    'caption': value.get('caption'),
                }
            )

        return retval_dict


class FeaturedImageBlock(BaseAtlasImageBlock):
    pass


class InlineOpportunityImageBlock(BaseAtlasImageBlock):
    custom_css_class = blocks.CharBlock(
        max_length=255,
        required=False,
        help_text="Only needed if special styling is involved: check with a developer. If in doubt, it's not needed"
    )

    def get_api_representation(self, value, context=None):
        retval_dict = super().get_api_representation(value, context)
        if retval_dict:
            retval_dict.update({'custom_css_class': value.get('custom_css_class')})
        return retval_dict


class MarkdownBlock(blocks.FieldBlock):
    def __init__(self, required=True, help_text=None, **kwargs):
        self.field = forms.CharField(
            required=required,
            help_text=help_text,
            widget=MarkdownTextarea(),
        )
        super().__init__(**kwargs)

    def get_api_representation(self, value, context=None):
        """Expand the default serialization to turn the Markdown into HTML"""
        raw_markdown = super().get_api_representation(value, context)
        if raw_markdown:
            return render_markdown(raw_markdown)
        else:
            return ''


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


class AtlasLandingPagePanelImageBlock(BaseAtlasImageBlock):
    pass


class AtlasLandingPagePanelBlock(blocks.StructBlock):

    heading = blocks.CharBlock(
        max_length=255,
        required=True,
    )
    main_text = blocks.TextBlock(
        max_length=255,
        help_text="The first column of the panel"
    )
    call_to_action = ButtonBlock(
        required=False,
        help_text="Set text for the CTA and either an internal or an external URL for its destination"
    )
    second_column = blocks.StreamBlock(
        [
            ('image', AtlasLandingPagePanelImageBlock()),
            ('text', blocks.TextBlock()),
        ],
        label='Second column of panel',
        max_num=1,
        required=False,
        help_text=(
            "An image OR a text block, but not both."
        )
    )
    block_slug = blocks.CharBlock(
        max_length=255,
        required=False,
        help_text=(
            "If a block has special content, this helps us identify it. "
            "Consult with a developer when you set it. If in doubt, leave it blank."
        )
    )
