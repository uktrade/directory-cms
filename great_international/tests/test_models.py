import pytest

from great_international import models


def test_app_models():
    assert models.GreatInternationalApp.allowed_subpage_models() == [
        models.GreatInternationalApp,
        models.InternationalHomePage,
        models.InternationalMarketingPages,
        models.InternationalUKHQPages,
        models.InternationalArticlePage,
        models.InternationalArticleListingPage,
        models.InternationalCampaignPage
    ]


@pytest.mark.parametrize('model', [
    models.GreatInternationalApp,
])
def test_app_required_translatable_fields(model):
    assert model.get_required_translatable_fields() == []


@pytest.mark.django_db
def test_set_slug():
    instance = models.GreatInternationalApp.objects.create(
        title_en_gb='the app',
        depth=2,
        path='/thing',
    )

    assert instance.slug == models.GreatInternationalApp.slug_identity


@pytest.mark.parametrize('folder_page_class', [
    models.InternationalMarketingPages,
])
@pytest.mark.django_db
def test_folders_set_title(folder_page_class):
    instance = folder_page_class.objects.create(
        depth=2,
        path='/thing',
    )

    assert instance.title_en_gb == instance.get_verbose_name()
