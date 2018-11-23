import pytest

import find_a_supplier.models
from export_readiness import models
from export_readiness.tests import factories


def test_app_models():
    assert models.ExportReadinessApp.allowed_subpage_models() == [
        models.ExportReadinessApp,
        models.TermsAndConditionsPage,
        models.PrivacyAndCookiesPage,
        models.GetFinancePage,
        models.PerformanceDashboardPage,
        models.PerformanceDashboardNotesPage,
        models.TopicLandingPage,
        models.ArticleListingPage,
        models.ArticlePage,
        models.HomePage,
        models.InternationalLandingPage,
        models.EUExitInternationalFormPage,
        models.EUExitDomesticFormPage,
        models.EUExitFormSuccessPage,
        models.ContactUsGuidancePage,
        models.ContactSuccessPage,
        models.MarketingPages,
        models.CampaignPage,
    ]


@pytest.mark.parametrize('model', [
    models.ExportReadinessApp,
    find_a_supplier.models.FindASupplierApp,
])
def test_app_required_translatable_fields(model):
    assert model.get_required_translatable_fields() == []


@pytest.mark.django_db
def test_set_slug():
    instance = models.ExportReadinessApp.objects.create(
        title_en_gb='the app',
        depth=2,
        path='/thing',
    )

    assert instance.slug == models.ExportReadinessApp.slug_identity


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
def test_tag_slug_created_on_save():
    tag = factories.TagFactory(
        name='Hello test'
    )
    assert tag.slug == 'hello-test'


@pytest.mark.django_db
def test_international_landing_page_articles_count(root_page):
    landing_page = factories.InternationaLandingPageFactory.create(
        parent=root_page
    )
    article_listing_page = factories.ArticleListingPageFactory.create(
        parent=landing_page,
        live=True
    )
    factories.ArticlePageFactory.create(
        parent=article_listing_page,
        live=True
    )
    factories.ArticlePageFactory.create(
        parent=article_listing_page,
        live=True
    )
    article_listing_page_two = factories.ArticleListingPageFactory.create(
        parent=landing_page,
        live=False
    )
    factories.ArticlePageFactory.create(
        live=True,
        parent=article_listing_page_two
    )
    assert landing_page.articles_count == 2


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
    assert page.view_path == values['view_path']


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
    assert page.view_path == values['view_path']
