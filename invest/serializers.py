from core.serializers import APIChildrenSerializer


class APIChildrenSectorSerializer(APIChildrenSerializer):
    sorting_key = 'heading'

    @staticmethod
    def get_model():
        from invest.models import SectorPage
        return SectorPage


class APIChildrenSetupGuideSerializer(APIChildrenSerializer):
    sorting_key = 'heading'

    @staticmethod
    def get_model():
        from invest.models import SetupGuidePage
        return SetupGuidePage
