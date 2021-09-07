# Blocks for the main Great International site, not specific to any sub-section (eg investment_atlas)
from django import forms

from wagtail.core import blocks

from core import blocks as core_blocks
from core.helpers import render_markdown
from core.widgets import MarkdownTextarea


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

class FeaturedImageBlock(core_blocks.BaseAltTextImageBlock):
    pass


class InternationalHomepagePanelBlock(blocks.StructBlock):
    title = blocks.CharBlock(
        max_length=255,
        required=True,
    )
    supporting_text = blocks.TextBlock(
        max_length=1000,
        required=False,
    )

    link = core_blocks.InternalOrExternalLinkBlock(
        required=True,
    )

    class Meta:
        icon = 'fa-globe'


sector_page_block_spec_list = [
    (
        'header',
        blocks.CharBlock(
            max_length=255,
            required=False,
        ),
    ),
    (
        'nested_content',
        blocks.StreamBlock(
            [
                (
                    'text',
                    MarkdownBlock(
                        help_text="Use H3 headers or lower, not H2 or H1",
                    ),
                ),
                (
                    'image',
                    FeaturedImageBlock(),
                ),
                (
                    'columns',
                    blocks.StreamBlock(
                        [
                            ('text', MarkdownBlock()),
                        ],
                        help_text="Smaller snippets of content"
                    ),
                ),
            ],
            min_num=1,
            max_num=2,
            help_text="Smaller snippets of content"
        ),
    ),
]


class InternationalInvestmentSectorPageBlock(blocks.StructBlock):

    content = blocks.StreamBlock(
        sector_page_block_spec_list,
        required=False,
    )

    block_slug = blocks.CharBlock(
        max_length=255,
        required=False,
        help_text="Only needed if special styling is involved: check with a developer. If in doubt, it's not needed"
    )


class InternationalInvestmentSectorPageEarlyOpportunityBlock(blocks.StructBlock):
    image = FeaturedImageBlock(
        blank=False,
    )
    text = MarkdownBlock(
        blank=False,
    )
