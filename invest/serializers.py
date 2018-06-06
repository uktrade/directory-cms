from core.serializers import APIChildrenSerializer


class APIChildrenSectorSerializer(APIChildrenSerializer):
    @staticmethod
    def get_model():
        from invest.models import SectorPage
        return SectorPage


class APIChildrenSetupGuideSerializer(APIChildrenSerializer):
    @staticmethod
    def get_model():
        from invest.models import SetupGuidePage
        return SetupGuidePage
