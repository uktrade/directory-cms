from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock

from core import blocks as core_blocks


class CampaignBlock(blocks.StructBlock):
    heading = blocks.CharBlock()
    subheading = blocks.CharBlock()
    related_link_text = blocks.CharBlock()
    related_link_url = blocks.CharBlock()
    image = ImageChooserBlock()
    video = core_blocks.VideoChooserBlock()
    video_transcript = blocks.RichTextBlock()

    class Meta:
        icon = 'media'
