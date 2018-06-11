from invest import models, serializers


def test_api_children_sector_serializer():
    serializer_class = serializers.APIChildrenSectorSerializer.get_model()
    assert serializer_class == models.SectorPage


def test_api_children_setup_guide_serializer():
    serializer_class = serializers.APIChildrenSetupGuideSerializer.get_model()
    assert serializer_class == models.SetupGuidePage
