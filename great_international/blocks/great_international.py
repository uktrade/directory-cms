# Blocks for the main Great International site, not specific to any sub-section (eg investment_atlas)
from wagtail.core import blocks

from core import blocks as core_blocks


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
