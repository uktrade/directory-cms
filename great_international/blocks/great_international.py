# Blocks for the main Great International site, not specific to any sub-section (eg investment_atlas)
from django import forms
from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock

from core import blocks as core_blocks
from core.helpers import render_markdown
from django.utils.safestring import mark_safe


class MarkdownBlock(blocks.FieldBlock):
    def __init__(self, required=True, help_text=mark_safe(
            'Enter content in Markdown format - <a href=https://stackedit.io/app# target=\'_blank\'> Guide </a>'),
            **kwargs):
        self.field = forms.CharField(
            required=required,
            help_text=help_text,
            widget=forms.Textarea(),
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


class OptionalImageBlock(core_blocks.BaseAltTextImageBlock):

    # redefine a couple of fields as optional
    image = ImageChooserBlock(required=False)
    image_alt = blocks.CharBlock(
        max_length=255,
        required=False,
    )


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


class InternationalInvestmentPageCopyBlockBase(blocks.StructBlock):
    text = MarkdownBlock(
        required=False,
    )
    image = OptionalImageBlock(
        required=False,
    )


class InternationalInvestmentSectorPageCopyBlock(
    InternationalInvestmentPageCopyBlockBase
):
    pass


class InternationalInvestmentSectorPageEarlyOpportunityBlock(
    InternationalInvestmentPageCopyBlockBase
):
    pass


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
                    InternationalInvestmentSectorPageCopyBlock(
                        help_text=(
                            "Use H3 headers or lower, not H2 or H1. "
                            "To add an expandable/folding marker to the text, "
                            "add a horizontal rule (--- with a blank line before "
                            "and after it) where the 'More' button should be."
                        )
                    ),
                ),
                (
                    'columns',
                    blocks.StreamBlock(
                        [
                            ('text', MarkdownBlock()),
                        ],
                    ),
                ),
            ],
            min_num=1,
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


class InternationalUKStrengthPanelBlock(
    blocks.StructBlock
):
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
    image = core_blocks.BaseAltTextImageBlock(required=True)

    class Meta:
        icon = 'fa-globe'
