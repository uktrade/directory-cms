from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock


class HeadingContentBaseBlock(blocks.StructBlock):
    heading = blocks.CharBlock()
    content = blocks.RichTextBlock()


class ColumnWithTitleIconTextBlock(HeadingContentBaseBlock):
    icon = ImageChooserBlock(required=False)


class DetailsSummaryBlock(HeadingContentBaseBlock):
    pass
