from wagtail import blocks
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
        icon = 'redirect'

    def get_api_representation(self, value, context=None):
        """Standardise the API output so the consumer doesn't have to worry about whether
        a link is internal or external"""
        original_retval_dict = super().get_api_representation(value, context=context)
        retval = None

        # If there's both an internal link and an exernal link configured, the internal
        # one takes priority. Also, we only want to return flat URL, not dictionary with
        # 'internal_link' or 'external_link' keys, or even a 'url' key
        if (
            'internal_link' in original_retval_dict and
            isinstance(original_retval_dict['internal_link'], int)
        ):
            # Correct this to be a full URL, not a page ID
            retval = value['internal_link'].specific.get_url()  # Note, this lacks the port number when used locally
        elif 'external_link' in original_retval_dict:
            retval = value['external_link']

        return retval


class ButtonBlock(blocks.StructBlock):
    label = blocks.CharBlock(
        max_length=255,
        required=False,
    )
    link = InternalOrExternalLinkBlock(
        required=False,
    )

    class Meta:
        icon = 'radio-full'


DEFAULT_IMAGE_RENDITION_SPEC = "fill-960x540"


class BaseAltTextImageBlock(blocks.StructBlock):
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


class GreatMediaBlock(AbstractMediaChooserBlock):

    def get_api_representation(self, value, context=None):
        from great_international.serializers import GreatMediaSerializer

        """Expand the default serialization to show the GreatMediaSerializer"""
        retval_dict = {}

        if not value:
            return retval_dict

        serializer = GreatMediaSerializer(instance=value)
        retval_dict = serializer.data
        return retval_dict
