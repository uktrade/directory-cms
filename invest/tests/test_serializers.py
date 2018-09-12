from invest import models, serializers


def test_api_children_sector_serializer():
    model_class = serializers.APIChildrenSectorSerializer.get_model()
    assert model_class is models.SectorPage


def test_api_children_setup_guide_serializer():
    model_class = serializers.APIChildrenSetupGuideSerializer.get_model()
    assert model_class is models.SetupGuidePage
