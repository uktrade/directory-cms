from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock


class ColumnWithTitleIconTextBlock(blocks.StructBlock):
    icon = ImageChooserBlock(required=False)
    title = blocks.CharBlock()
    body = blocks.RichTextBlock()


class DetailsSummaryBlock(blocks.StructBlock):
    title = blocks.CharBlock()
    body = blocks.RichTextBlock()
