from wagtail.api import APIField

from . import api_serializers


class APIChildrenTopicLandingPageListField(APIField):
    def __init__(self, name):
        field_names = [
            'landing_page_title',
            'hero_image',
            'articles_count',
            'last_published_at',
            'full_url',
            'full_path'
        ]
        # see explanation of the `fields_config` syntax here:
        # https://github.com/wagtail/wagtail/blob/
        # db6d36845f3f2c5d7009a22421c2efab9968aa24/wagtail/api/v2/utils.py#L68
        serializer = api_serializers.APIChildrenTopicLandingPageListSerializer(
            name,
            fields_config=[(name, False, None) for name in field_names],
        )
        super().__init__(name=name, serializer=serializer)


class APIChildrenArticleListingPageListField(APIField):
    def __init__(self, name):
        field_names = [
            'article_title',
            'last_published_at',
            'full_url',
            'full_path'
        ]
        # see explanation of the `fields_config` syntax here:
        # https://github.com/wagtail/wagtail/blob/
        # db6d36845f3f2c5d7009a22421c2efab9968aa24/wagtail/api/v2/utils.py#L68
        serializer = api_serializers.APIChildrenArticleListingPageListSerializer(  # NOQA
            name,
            fields_config=[(name, False, None) for name in field_names],
        )
        super().__init__(name=name, serializer=serializer)
