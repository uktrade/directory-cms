import pytest
from rest_framework.reverse import reverse

from tests.great_international import factories

from core import cache


@pytest.mark.django_db
def test_international_homepage(admin_client, root_page):
    home_page = factories.InternationalHomePageFactory.create(
        parent=root_page
    )
    home_page.homepage_link_panels = [
        (
            'link_panel',
            {
                'title': 'panel one',
                'supporting_text': 'panel one supporting text',
                'link': {
                    'external_link': 'http://example.com/one/',
                }
            }
        ),
        (
            'link_panel',
            {
                'title': 'panel two',
                'supporting_text': 'panel two supporting text',
                'link': {
                    'external_link': 'http://example.com/two/',
                }
            }
        ),
    ]
    home_page.save()

    cache.rebuild_all_cache()

    url = reverse('api:api:pages:detail', kwargs={'pk': home_page.pk})
    response = admin_client.get(url)
    assert response.status_code == 200
    json_response = response.json()

    assert 'hero_title' in json_response

    homepage_link_panels = response.json()['homepage_link_panels']
    assert homepage_link_panels[0]['type'] == 'link_panel'
    assert homepage_link_panels[0]['value'] == {
        'title': 'panel one',
        'supporting_text': 'panel one supporting text',
        'link': 'http://example.com/one/',
    }
    assert homepage_link_panels[1]['type'] == 'link_panel'
    assert homepage_link_panels[1]['value'] == {
        'title': 'panel two',
        'supporting_text': 'panel two supporting text',
        'link': 'http://example.com/two/',
    }


@pytest.mark.django_db
def test_international_campaign_page(admin_client, international_root_page):
    campaign_page = factories.InternationalCampaignPageFactory(
        parent=international_root_page
    )
    cache.rebuild_all_cache()

    url = reverse('api:api:pages:detail', kwargs={'pk': campaign_page.pk})
    response = admin_client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_international_article_listing_page_view(admin_client, international_root_page):
    article_listing_page = factories.InternationalArticleListingPageFactory.create(  # NOQA
        parent=international_root_page,
        live=True
    )
    article = factories.InternationalArticlePageFactory.create(
        parent=article_listing_page,
        live=True
    )
    campaign = factories.InternationalCampaignPageFactory.create(
        parent=article_listing_page,
        live=True
    )
    cache.rebuild_all_cache()

    url = reverse(
        'api:api:pages:detail', kwargs={'pk': article_listing_page.pk}
    )
    response = admin_client.get(url)
    assert response.status_code == 200
    assert 'child_pages' in response.json()
    assert sorted(
        [page['id'] for page in response.json()['child_pages']],
        reverse=True
    ) == [campaign.pk, article.pk]
    assert 'meta' in response.json()['child_pages'][0]


@pytest.mark.django_db
def test_international_topic_landing_page_view(admin_client, international_root_page):
    topic_landing_page = factories.InternationalTopicLandingPageFactory.create(
        parent=international_root_page,
        live=True
    )
    campaign_page = factories.InternationalCampaignPageFactory(
        parent=topic_landing_page,
        live=True
    )
    article_listing_page = factories.InternationalArticleListingPageFactory.create(
        parent=topic_landing_page,
        live=True
    )
    cache.rebuild_all_cache()

    url = reverse('api:api:pages:detail', kwargs={'pk': topic_landing_page.pk})
    response = admin_client.get(url)
    assert response.status_code == 200
    assert 'child_pages' in response.json()
    assert sorted(
        [page['id'] for page in response.json()['child_pages']],
        reverse=True
    ) == [article_listing_page.pk, campaign_page.pk]


@pytest.mark.django_db
def test_international_topic_landing_page_view_sectors_alphabetical_order(
        admin_client, international_root_page):
    landing_page = factories.InternationalTopicLandingPageFactory.create(
        parent=international_root_page
    )
    sector_page1 = factories.InternationalInvestmentSectorPageFactory.create(
        parent=landing_page,
        live=True,
        heading='acme'
    )
    sector_page2 = factories.InternationalInvestmentSectorPageFactory.create(
        parent=landing_page,
        live=True,
        heading='foo'
    )
    cache.rebuild_all_cache()

    url = reverse('api:api:pages:detail', kwargs={'pk': landing_page.pk})
    response = admin_client.get(url)
    assert response.status_code == 200
    assert [page['id'] for page in response.json()['child_pages']] == [
        sector_page1.pk, sector_page2.pk
    ]


@pytest.mark.django_db
def test_international_trade_home_page_exposes_industries(
    admin_client, international_root_page
):
    industry = factories.InternationalInvestmentSectorPageFactory(
        parent=international_root_page,
        live=True,
    )
    factories.InternationalInvestmentSectorPageFactory(
        parent=international_root_page,
        live=False,
    )
    homepage = factories.InternationalTradeHomePageFactory(
        live=True,
        parent=international_root_page
    )
    cache.rebuild_all_cache()

    url = reverse('api:api:pages:detail', kwargs={'pk': homepage.pk})
    response = admin_client.get(url)

    assert response.status_code == 200
    assert len(response.json()['industries']) == 1
    assert response.json()['industries'][0]['meta']['pk'] == industry.pk
