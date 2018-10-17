from core.api_serializers import APIChildrenSerializer


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
