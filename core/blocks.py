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


class LinkBlock(blocks.StructBlock):
    source = blocks.CharBlock(help_text='The source or the type of the link, e.g. GOV.UK/Advice')
    text = blocks.CharBlock()
    url = blocks.CharBlock()  # not a URL block to allow relative links


class LinkWithImageAndContentBlock(LinkBlock):
    image = ImageChooserBlock(required=False)
    image_alt = blocks.CharBlock(required=False)
    content = blocks.RichTextBlock()


class LinkStructValue(blocks.StructValue):
    """
    Generates a URL for blocks with multiple link choices.
    """

    @property
    def url(self):
        page = self.get('internal_link')
        ext = self.get('external_link')
        if page:
            return page.url_path
        else:
            return ext


class InternalOrExternalLinkBlock(blocks.StructBlock):
    internal_link = blocks.PageChooserBlock(
        required=False,
        label='Internal link',
    )
    external_link = blocks.CharBlock(
        required=False,
        max_length=255,
        label='External link',
    )

    class Meta:
        value_class = LinkStructValue
        icon = 'redirect'


class ButtonBlock(blocks.StructBlock):
    label = blocks.CharBlock(max_length=255)
    link = InternalOrExternalLinkBlock(required=False)

    class Meta:
        icon = 'radio-full'
