import pytest
from rest_framework.reverse import reverse

from . import factories


@pytest.mark.django_db
def test_invest_home_page(admin_client):
    page = factories.InvestHomePageFactory(live=True)
    factories.SetupGuidePageFactory(live=True)
    factories.SetupGuidePageFactory(live=False)
    factories.SectorPageFactory(live=True, featured=True)
    factories.SectorPageFactory(live=True, featured=False)

    url = reverse(
        'lookup-by-slug',
        kwargs={'slug': page.slug}
    )

    response = admin_client.get(url)
    assert response.status_code == 200
    meta = response.json()['meta']
    assert meta['url'] == 'http://invest.trade.great:8011/invest/'
    assert meta['slug'] == 'invest-home-page'
    assert len(response.json()['guides']) == 1
    assert len(response.json()['sectors']) == 1


@pytest.mark.django_db
def test_invest_info_page(admin_client):
    page = factories.InfoPageFactory(live=True)

    url = reverse('api:pages:detail', kwargs={'pk': page.pk})

    response = admin_client.get(url)
    assert response.status_code == 200
