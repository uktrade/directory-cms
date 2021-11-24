import pytest

from export_readiness import models
from . import factories


@pytest.mark.django_db
def test_app_models():
    # using sets here because order shouldn't matter
    assert set(models.HomePage.allowed_subpage_models()) == {
        models.TermsAndConditionsPage,
        models.PrivacyAndCookiesPage,
        models.SitePolicyPages,
        models.PerformanceDashboardNotesPage,
        models.TopicLandingPage,
        models.SuperregionPage,
        models.ArticleListingPage,
        models.MarketingPages,
        models.CampaignPage,
        models.ArticlePage,
        models.EUExitDomesticFormPage,
        models.EUExitFormSuccessPage,
        models.EUExitFormPages,
        models.ContactUsGuidancePages,
        models.ContactSuccessPages,
        models.ContactUsGuidancePage,
        models.ContactSuccessPage,
        models.AllContactPagesPage,
    }


@pytest.mark.django_db
def test_set_slug():
    instance = models.HomePage.objects.create(
        title_en_gb='the app',
        depth=2,
        path='/thing',
    )

    assert instance.slug == models.HomePage.slug_identity


@pytest.mark.parametrize('folder_page_class', [
    models.MarketingPages,
    models.EUExitFormPages,
    models.ContactUsGuidancePages,
    models.ContactSuccessPages,
    models.SitePolicyPages,
    models.AllContactPagesPage,
])
@pytest.mark.django_db
def test_folders_set_title(folder_page_class):
    instance = folder_page_class.objects.create(
        depth=2,
        path='/thing',
    )

    assert instance.title_en_gb == instance.get_verbose_name()


@pytest.mark.django_db
def test_article_listing_page_articles_count(root_page):
    article_listing_page = factories.ArticleListingPageFactory.create(
        parent=root_page
    )
    factories.ArticlePageFactory.create(
        parent=article_listing_page,
        live=True
    )
    factories.ArticlePageFactory.create(
        parent=article_listing_page,
        live=True
    )
    factories.ArticlePageFactory.create(
        parent=article_listing_page,
        live=False
    )
    factories.ArticlePageFactory.create(
        live=True,
        parent=root_page
    )

    assert article_listing_page.articles_count == 2


@pytest.mark.django_db
def test_superregion_page_articles_count(root_page):
    superregion_page = factories.SuperregionPageFactory.create(
        parent=root_page
    )
    factories.ArticlePageFactory.create(
        parent=superregion_page,
        live=True
    )
    factories.ArticlePageFactory.create(
        parent=superregion_page,
        live=True
    )
    factories.ArticlePageFactory.create(
        parent=superregion_page,
        live=False
    )
    factories.ArticlePageFactory.create(
        live=True,
        parent=root_page
    )

    assert superregion_page.articles_count == 2


@pytest.mark.django_db
def test_tag_str():
    tag = factories.TagFactory(
        name='Hello test'
    )
    assert str(tag) == tag.name


@pytest.mark.django_db
@pytest.mark.parametrize(
    'topic,values', models.ContactUsGuidancePage.topic_mapping.items()
)
def test_contact_us_guidance_infers_field_values(topic, values):
    page = factories.ContactUsGuidancePageFactory.create(
        topic=topic
    )

    assert page.slug == topic
    assert page.title == values['title']
    assert page.full_path == values['full_path_override']


@pytest.mark.django_db
@pytest.mark.parametrize(
    'topic,values', models.ContactSuccessPage.topic_mapping.items()
)
def test_contact_us_success_infers_field_values(topic, values):
    page = factories.ContactSuccessPageFactory.create(
        topic=topic
    )

    assert page.slug == topic
    assert page.title == values['title']
    assert page.full_path == values['full_path_override']
