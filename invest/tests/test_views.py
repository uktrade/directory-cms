import pytest
from rest_framework.reverse import reverse

from . import factories


@pytest.mark.django_db
def test_invest_home_page(admin_client):
    factories.InvestHomePageFactory(live=True)

    url = reverse(
        'lookup-by-page-type',
        kwargs={'page_type': 'invest.InvestHomePage'}
    )

    response = admin_client.get(url)
    assert response.status_code == 200
    meta = response.json()['meta']
    assert meta['url'] == 'http://invest.trade.great:8011/invest/'
    assert meta['slug'] == 'invest-home-page'


@pytest.mark.django_db
def test_invest_info_page(admin_client):
    page = factories.InfoPageFactory(live=True)

    url = reverse('api:pages:detail', kwargs={'pk': page.pk})

    response = admin_client.get(url)
    assert response.status_code == 200
