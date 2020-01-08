from unittest.mock import ANY

import pytest
from rest_framework.reverse import reverse

from tests.export_readiness import factories
from directory_constants import urls


@pytest.mark.django_db
def test_performance_dashboard(admin_client, root_page):
    page = factories.PerformanceDashboardPageFactory(
        live=True,
        parent=root_page,
        product_link=urls.SERVICES_GREAT_DOMESTIC
    )

    url = reverse('api:api:pages:detail', kwargs={'pk': page.pk})

    response = admin_client.get(url)
    assert response.status_code == 200
    assert response.json()['page_type'] == 'PerformanceDashboardPage'


@pytest.mark.django_db
def test_performance_dashboard_notes(admin_client, root_page):
    page = factories.PerformanceDashboardNotesPageFactory(
        live=True,
        parent=root_page
    )

    url = reverse('api:api:pages:detail', kwargs={'pk': page.pk})

    response = admin_client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_topic_landing_page_view(admin_client, root_page):
    topic_landing_page = factories.TopicLandingPageFactory.create(
        parent=root_page,
        live=True
    )
    article_listing_page = factories.ArticleListingPageFactory.create(
        parent=topic_landing_page,
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

    url = reverse('api:api:pages:detail', kwargs={'pk': topic_landing_page.pk})
    response = admin_client.get(url)
    assert response.status_code == 200
    assert 'child_pages' in response.json()


@pytest.mark.django_db
def test_article_listing_page_view(admin_client, root_page):
    article_listing_page = factories.ArticleListingPageFactory.create(
        parent=root_page,
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

    url = reverse(
        'api:api:pages:detail', kwargs={'pk': article_listing_page.pk}
    )
    response = admin_client.get(url)
    assert response.status_code == 200
    assert 'articles' in response.json()
    assert 'meta' in response.json()['articles'][0]


@pytest.mark.django_db
def test_article_page_view(admin_client, root_page):
    topic_landing_page = factories.TopicLandingPageFactory.create(
        parent=root_page,
        live=True
    )
    article_listing_page = factories.ArticleListingPageFactory.create(
        parent=topic_landing_page,
        live=True
    )
    tag = factories.TagFactory()
    tag2 = factories.TagFactory()
    article = factories.ArticlePageFactory.create(
        parent=article_listing_page,
        live=True,
    )
    article.tags = [tag, tag2]
    article.save()

    url = reverse('api:api:pages:detail', kwargs={'pk': article.pk})
    response = admin_client.get(url)
    assert response.status_code == 200
    assert 'tags' in response.json()
    assert 'name' in response.json()['tags'][0]


@pytest.mark.django_db
def test_domestic_homepage(admin_client, root_page):
    home_page = factories.HomePageFactory.create(
        parent=root_page,
        hero_cta_url='/foo/bar'
    )

    url = reverse('api:api:pages:detail', kwargs={'pk': home_page.pk})
    response = admin_client.get(url)
    assert response.json()['hero_cta_url'] == '/foo/bar'
    assert response.status_code == 200


@pytest.mark.django_db
def test_country_page_view(admin_client, root_page):
    page = factories.CountryGuidePageFactory(
        parent=root_page,
        live=True
    )
    tag = factories.IndustryTagFactory(name='test')
    page.tags = [tag]
    page.save()
    url = reverse('api:api:pages:detail', kwargs={'pk': page.pk})
    response = admin_client.get(url)
    assert response.status_code == 200
    assert 'accordions' in response.json()
    assert 'statistics' in response.json()
    assert 'fact_sheet' in response.json()
    assert 'intro_ctas' in response.json()
    assert 'subsections' in response.json()['accordions'][0]
    assert 'statistics' in response.json()['accordions'][0]
    assert 'case_study' in response.json()['accordions'][0]
    assert 'tags' in response.json()
    assert response.json()['tags'][0]['name'] == tag.name
    assert response.json()['tags'][0]['id'] == tag.id


@pytest.mark.django_db
def test_topic_landing_page_view_country_guides_alph_order(
        admin_client,
        root_page):
    topic_landing_page = factories.TopicLandingPageFactory.create(
        parent=root_page,
        live=True
    )
    country_guide_page1 = factories.CountryGuidePageFactory.create(
        parent=topic_landing_page,
        live=True,
        heading='acme'
    )
    country_guide_page2 = factories.CountryGuidePageFactory.create(
        parent=topic_landing_page,
        live=True,
        heading='foo'
    )

    url = reverse('api:api:pages:detail', kwargs={'pk': topic_landing_page.pk})
    response = admin_client.get(url)
    assert response.status_code == 200
    assert [page['id'] for page in response.json()['child_pages']] == [
        country_guide_page1.pk, country_guide_page2.pk
    ]


@pytest.mark.django_db
def test_industry_tags_list_endpoint(client):
    tag1 = factories.IndustryTagFactory()
    tag2 = factories.IndustryTagFactory()
    page = factories.CountryGuidePageFactory()
    page2 = factories.CountryGuidePageFactory()
    page3 = factories.CountryGuidePageFactory(live=False)
    page.tags = [tag1, tag2]
    page.save()
    page2.tags = [tag1]
    page2.save()
    page3.tags = [tag1]
    page3.save()
    url = reverse('api:industry-tags-list')
    response = client.get(url)
    assert response.status_code == 200
    assert response.json() == [
        {
            'id': tag1.pk,
            'name': tag1.name,
            'icon': {'url': ANY, 'width': 100, 'height': 100},
            'pages_count': 2
        },
        {
            'id': tag2.pk,
            'name': tag2.name,
            'icon': {'url': ANY, 'width': 100, 'height': 100},
            'pages_count': 1
        }
    ]


@pytest.mark.django_db
def test_lookup_countries_by_tag_list_endpoint(client):
    tag = factories.IndustryTagFactory()
    market1 = factories.CountryGuidePageFactory()
    market1.tags = [tag]
    market1.save()
    market2 = factories.CountryGuidePageFactory()
    market2.tags = [tag]
    market2.save()
    url = reverse('api:lookup-countries-by-tag-list', kwargs={'pk': tag.pk})
    response = client.get(url)
    assert response.status_code == 200
    assert len(response.json()['countries']) == 2


@pytest.mark.django_db
def test_lookup_market_guides_missing_filters(client):
    tag = factories.IndustryTagFactory()
    tag2 = factories.IndustryTagFactory()
    market1 = factories.CountryGuidePageFactory()
    market1.tags = [tag, tag2]
    market1.save()
    market2 = factories.CountryGuidePageFactory()
    market2.tags = [tag]
    market2.save()

    url = reverse('api:lookup-country-guides-list-view')

    response = client.get(url)
    assert response.status_code == 200
    assert len(response.json()) == 2


@pytest.mark.django_db
def test_lookup_market_guides_missing_region(client):
    tag = factories.IndustryTagFactory()
    tag2 = factories.IndustryTagFactory()
    market1 = factories.CountryGuidePageFactory()
    market1.tags = [tag2]
    market1.save()
    market2 = factories.CountryGuidePageFactory()
    market2.tags = [tag]
    market2.save()

    url = reverse('api:lookup-country-guides-list-view')

    response = client.get(f'{url}?industry={tag.name},{tag2.name}')
    assert response.status_code == 200
    assert len(response.json()) == 2
    assert response.json()[0]['id'] == market1.pk


@pytest.mark.django_db
def test_lookup_market_guides_missing_region_markets_have_region(client):
    tag = factories.IndustryTagFactory()
    tag2 = factories.IndustryTagFactory()
    region = factories.RegionFactory()
    country = factories.CountryFactory(region=region)
    market1 = factories.CountryGuidePageFactory(country=country)
    market1.tags = [tag, tag2]
    market1.save()
    market2 = factories.CountryGuidePageFactory()
    market2.tags = [tag]
    market2.save()
    factories.CountryGuidePageFactory()

    url = reverse('api:lookup-country-guides-list-view')

    response = client.get(f'{url}?industry={tag.name},{tag2.name}')
    assert response.status_code == 200
    assert len(response.json()) == 2
    assert response.json()[0]['id'] == market1.pk


@pytest.mark.django_db
def test_lookup_market_guides_all_filters(client):
    tag = factories.IndustryTagFactory()
    region = factories.RegionFactory()
    country = factories.CountryFactory(region=region)
    market1 = factories.CountryGuidePageFactory(country=country)
    market1.tags = [tag]
    market1.save()
    factories.CountryGuidePageFactory(country=country)
    url = reverse('api:lookup-country-guides-list-view')

    response = client.get(f'{url}?industry={tag.name}&region={region.name}')
    assert response.status_code == 200
    assert len(response.json()) == 1
    assert response.json()[0]['id'] == market1.pk


@pytest.mark.django_db
def test_regions_list_view(client):

    url = reverse('api:regions-list-view')

    response = client.get(url)
    assert response.status_code == 200
