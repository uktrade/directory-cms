import pytest

import find_a_supplier.models
from export_readiness import models
from export_readiness.tests import factories


def test_app_models():
    assert models.ExportReadinessApp.allowed_subpage_models() == [
        models.ExportReadinessApp,
        models.TermsAndConditionsPage,
        models.PrivacyAndCookiesPage,
        models.DeprecatedGetFinancePage,
        models.NewGetFinancePage,
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
def test_get_finance_breadcrumbs():
    page = factories.DeprecatedGetFinancePageFactory.create()
    assert page.breadcrumb.first().label == page.breadcrumbs_label


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
