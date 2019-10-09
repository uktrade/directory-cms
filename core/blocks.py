from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock
from wagtailmedia.blocks import AbstractMediaChooserBlock


class VideoChooserBlock(AbstractMediaChooserBlock):
    def render_basic(self, value, context=None):
        """We don't need any HTML rendering"""
        if not value:
            return ''
        return value.file.url


class HeadingContentBaseBlock(blocks.StructBlock):
    heading = blocks.CharBlock()
    content = blocks.RichTextBlock()


class ColumnWithTitleIconTextBlock(HeadingContentBaseBlock):
    icon = ImageChooserBlock(required=False)
    image_alt = blocks.CharBlock(required=False)


class DetailsSummaryBlock(HeadingContentBaseBlock):
    pass


class LinkBlock(blocks.StructBlock):
    source = blocks.CharBlock(help_text='The source of the link, eg GOV.UK')
    text = blocks.CharBlock()
    url = blocks.CharBlock()  # not a URL block to allow relative links


class LinkWithImageAndContentBlock(LinkBlock):
    image = ImageChooserBlock(required=False)
    image_alt = blocks.CharBlock(required=False)
    content = blocks.RichTextBlock()
