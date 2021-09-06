"""Streamfield blocks for Investment Atlas pages"""

from django import forms

from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock
from wagtail.snippets.blocks import SnippetChooserBlock

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


# This is separate because it's used in both PageSectionBlock, below, and
# the ReusableContentSection snippet model
page_section_block_spec_list = [
    ('text', MarkdownBlock()),
    ('image', InlineOpportunityImageBlock()),
    (
        'columns',
        blocks.StreamBlock(
            [
                ('text', MarkdownBlock()),
            ],
            help_text="Smaller snippets of content"
        ),
    ),

]


class PageSectionBlock(blocks.StructBlock):
    "Each PageSectionBlock is a new section/panel in the rendered page"

    content = blocks.StreamBlock(
        page_section_block_spec_list,
        required=False,
    )

    block_slug = blocks.CharBlock(
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


def _get_block_for_block_name(
    # Takes the spec of a StreamField's block config to allow us
    # to look up the relevant block class by its key/name from the config
    block_type_name,
    block_spec_list=page_section_block_spec_list
):
    for block_name, block_class in block_spec_list:
        if block_name == block_type_name:
            return block_class


class ReusableSnippetChooserBlock(SnippetChooserBlock):
    # Subclassing SnippetChooserBlock to get full control over the rendering of the snippet
    # so that it's StreamField like. There may be more idiomatic ways to do this, but it works

    def get_api_representation(self, value, context=None):
        retval_dict = {}
        if value:
            retval_dict.update({
                'block_slug': value.block_slug
            })
            rendered_content = []
            for child_block in value.content:  # Value.content is a StreamField
                block_type_name = child_block.block_type
                block_class = _get_block_for_block_name(block_type_name)
                if block_class:
                    api_ready_val = block_class.get_api_representation(child_block.value)
                    rendered_content.append({
                        # Make the structure match what Wagtail would naturally do
                        "type": block_type_name,
                        "value": api_ready_val,
                        "id": child_block.id,
                    })
            retval_dict.update({'content': rendered_content})
        return retval_dict
