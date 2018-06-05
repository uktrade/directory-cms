from core.serializers import APIChildrenSerializer


class APIChildrenSectorSerializer(APIChildrenSerializer):
    def get_model(self):
        from invest.models import SectorPage
        return SectorPage

    def get_order_by_attribute(self):
        return 'sectorpage__heading'


class APIChildrenSetupGuideSerializer(APIChildrenSerializer):
    def get_model(self):
        from invest.models import SetupGuidePage
        return SetupGuidePage

    def get_order_by_attribute(self):
        return 'heading'
