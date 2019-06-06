import pytest
from wagtail.core.models import Page

from great_international import models
from . import factories
from export_readiness.tests import factories as exread_factories


def test_models_hierarchy():
    # homepage / app root
    assert models.InternationalHomePage.allowed_subpage_models() == [
        models.InternationalArticleListingPage,
        models.InternationalTopicLandingPage,
        models.InternationalCuratedTopicLandingPage,
        models.InternationalGuideLandingPage,
        models.InternationalRegionPage,
        models.InternationalEUExitFormPage,
        models.InternationalEUExitFormSuccessPage,
        models.InternationalCapitalInvestLandingPage,
        models.CapitalInvestOpportunityListingPage,
        models.CapitalInvestRegionPage,
        models.InvestInternationalHomePage,
        models.InvestHighPotentialOpportunityDetailPage,
        models.InvestHighPotentialOpportunityFormPage,
        models.InvestHighPotentialOpportunityFormSuccessPage
    ]
    assert models.InternationalHomePage.allowed_parent_page_models() == [
        Page,
    ]
    # region page
    assert models.InternationalRegionPage.allowed_subpage_models() == [
        models.InternationalLocalisedFolderPage
    ]
    # regional folder page
    assert models.InternationalLocalisedFolderPage.allowed_subpage_models(
    ) == [
        models.InternationalArticlePage,
        models.InternationalCampaignPage
    ]
    # topic landing
    assert models.InternationalTopicLandingPage.allowed_subpage_models() == [
        models.InternationalArticleListingPage,
        models.InternationalCampaignPage,
        models.InternationalSectorPage,
    ]
    # curated topic landing
    assert models.InternationalCuratedTopicLandingPage \
        .allowed_subpage_models() == []
    # guide landing
    assert models.InternationalGuideLandingPage.allowed_subpage_models() == [
        models.InternationalArticlePage,
    ]
    # article listing
    assert models.InternationalArticleListingPage.allowed_subpage_models() == [
        models.InternationalArticlePage,
        models.InternationalCampaignPage
    ]
    # campaign
    assert models.InternationalCampaignPage.allowed_subpage_models() == [
        models.InternationalArticlePage,
    ]
    # EU Exit forms
    assert models.InternationalEUExitFormPage.allowed_subpage_models() == [
        models.InternationalEUExitFormSuccessPage,
    ]
    assert models.InternationalEUExitFormSuccessPage.allowed_parent_page_models() == [  # NOQA
        models.InternationalEUExitFormPage,
    ]
    assert models.CapitalInvestRegionPage.allowed_subpage_models() == [
        models.CapitalInvestRegionalSectorPage,
    ]
    assert models.CapitalInvestOpportunityListingPage.allowed_subpage_models() == [  # NOQA
        models.CapitalInvestOpportunityPage,
    ]


@pytest.mark.parametrize('model', [
    models.CapitalInvestOpportunityListingPage,
])
def test_opp_listing_required_translatable_fields(model):
    assert model.get_required_translatable_fields() == []


@pytest.mark.django_db
def test_set_slug():
    instance = models.InternationalHomePage.objects.create(
        title_en_gb='the app',
        depth=2,
        path='/thing',
        hero_title='blah',
        hero_title_en_gb='blah',
        invest_title='blah',
        invest_title_en_gb='blah',
        trade_title='blah',
        trade_title_en_gb='blah',
        tariffs_title='blah',
        tariffs_title_en_gb='blah',
        tariffs_description='blah',
        tariffs_description_en_gb='blah',
        tariffs_link='http://blah.com/',
        tariffs_link_en_gb='http://blah.com/',
        tariffs_call_to_action_text='blah',
        tariffs_call_to_action_text_en_gb='blah',
        news_title='blah',
        news_title_en_gb='blah',
        study_in_uk_cta_text='blah',
        study_in_uk_cta_text_en_gb='blah',
        visit_uk_cta_text='blah',
        visit_uk_cta_text_en_gb='blah',
    )

    assert instance.slug == models.InternationalHomePage.slug_identity


@pytest.mark.django_db
def test_article_inherit_tags_from_parent(root_page):
    tag1 = exread_factories.TagFactory(name='foo')
    tag2 = exread_factories.TagFactory(name='bar')
    tag3 = exread_factories.TagFactory(name='xyz')
    article_listing_page = factories.InternationalArticleListingPageFactory(
        parent=root_page
    )
    article_listing_page.tags = [tag1, tag2]
    article_listing_page.save()

    article = factories.InternationalArticlePageFactory(
        parent=article_listing_page
    )
    article.tags = [tag3, ]
    article.save()

    assert list(
        article.tags.values_list('pk', flat=True)
    ) == [tag1.pk, tag2.pk, tag3.pk]


@pytest.mark.django_db
def test_campaign_inherit_tags_from_parent(root_page):
    tag1 = exread_factories.TagFactory(name='foo')
    tag2 = exread_factories.TagFactory(name='bar')
    tag3 = exread_factories.TagFactory(name='xyz')
    marketing_page = factories.InternationalArticleListingPageFactory(
        parent=root_page
    )
    marketing_page.tags = [tag1, tag2]
    marketing_page.save()

    campaign = factories.InternationalArticlePageFactory(
        parent=marketing_page
    )
    campaign.tags = [tag3, ]
    campaign.save()

    assert list(
        campaign.tags.values_list('pk', flat=True)
    ) == [tag1.pk, tag2.pk, tag3.pk]


@pytest.mark.django_db
def test_adding_new_tag_to_parent_propagate_to_descendants(root_page):
    tag1 = exread_factories.TagFactory(name='foo')
    tag2 = exread_factories.TagFactory(name='bar')
    article_listing_page = factories.InternationalArticleListingPageFactory(
        parent=root_page
    )
    article_listing_page.tags.add(tag1)
    article_listing_page.save()

    article1 = factories.InternationalArticlePageFactory(
        parent=article_listing_page
    )
    article2 = factories.InternationalArticlePageFactory(
        parent=article_listing_page
    )

    assert list(
        article1.tags.values_list('pk', flat=True)
    ) == [tag1.pk]
    assert list(
        article2.tags.values_list('pk', flat=True)
    ) == [tag1.pk]

    article_listing_page.tags.add(tag2)
    article_listing_page.save()

    assert list(
        article1.tags.values_list('pk', flat=True)
    ) == [tag1.pk, tag2.pk]
    assert list(
        article2.tags.values_list('pk', flat=True)
    ) == [tag1.pk, tag2.pk]


@pytest.mark.django_db
def test_international_folder_page_append_parent_slug():
    region = factories.InternationalRegionPageFactory(
        slug='canada'
    )
    folder_page = factories.InternationalLocalisedFolderPageFactory(
        parent=region,
        slug='test'
    )
    assert folder_page.slug == 'test-canada'


@pytest.mark.django_db
def test_international_folder_page_append_parent_slug_only_on_creation():
    region = factories.InternationalRegionPageFactory(
        slug='canada'
    )
    folder_page = factories.InternationalLocalisedFolderPageFactory(
        parent=region,
        slug='test'
    )
    assert folder_page.slug == 'test-canada'

    folder_page.save()
    assert folder_page.slug == 'test-canada'
