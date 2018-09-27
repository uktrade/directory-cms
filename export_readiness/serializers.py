from core.serializers import APIChildrenSerializer


class APIChildrenTopicLandingPageListSerializer(APIChildrenSerializer):
    sorting_key = 'last_published_at'

    @staticmethod
    def get_model():
        from .models import ArticleListingPage
        return ArticleListingPage


class APIChildrenArticleListingPageListSerializer(APIChildrenSerializer):
    sorting_key = 'last_published_at'

    @staticmethod
    def get_model():
        from .models import ArticlePage
        return ArticlePage


class APIChildrenArticleNewsPageListSerializer(APIChildrenSerializer):
    sorting_key = 'last_published_at'

    def to_representation(self, instance):
        """We are using this serializer instead of APIQuerysetSerializer
        because get() is not a lazy queryset object and if it's in the __init__
        method of a serializer it's evaluated before the models are ready.
        By having it here we defer its evaluation until the models are ready.

        Happy days :)
        """
        from .models import ArticleListingPage, ArticlePage
        if not ArticleListingPage.objects.filter(slug='news').exists():
            return []
        queryset = ArticleListingPage.objects.get(
            slug='news'
        ).get_descendants().type(
            ArticlePage
        ).live().specific()
        serializer_class = self.context['view']._get_serializer_class(
            router=self.context['router'],
            model=ArticlePage,
            fields_config=self.fields_config,
        )
        serializer = serializer_class(
            queryset, many=True, context=self.context
        )
        data = serializer.data
        # When ordering at the database level, the lookup seems to happens on
        # the superclass `Page` table level, so it is not aware of the fields
        # the subclass has. We are ordering on the application level
        sorted_data = sorted(
            data,
            key=lambda x: x[self.sorting_key]
        )
        return sorted_data
