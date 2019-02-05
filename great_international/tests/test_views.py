from directory_constants.constants import cms
from rest_framework.reverse import reverse

from great_international.tests import factories


def test_international_homepage(admin_client, root_page):
    home_page = factories.InternationalHomePageFactory.create(
        parent=root_page
    )
    # news
    marketing_folder = factories.InternationalMarketingPagesFactory(
        slug=cms.GREAT_INTERNATIONAL_MARKETING_PAGES_SLUG,
        live=True
    )
    for _ in range(5):
        factories.InternationalArticlePageFactory.create(
            parent=marketing_folder
        )
    factories.InternationalArticlePageFactory.create(
        parent=root_page
    )

    url = reverse('api:api:pages:detail', kwargs={'pk': home_page.pk})
    response = admin_client.get(url)
    assert response.status_code == 200
    assert 'articles' in response.json()
    assert len(response.json()['articles']) == 5


def test_international_homepage_no_news(admin_client, root_page):

    home_page = factories.InternationalHomePageFactory.create(
        parent=root_page
    )

    url = reverse('api:api:pages:detail', kwargs={'pk': home_page.pk})
    response = admin_client.get(url)
    assert response.status_code == 200
    assert 'articles' in response.json()
    assert len(response.json()['articles']) == 0
