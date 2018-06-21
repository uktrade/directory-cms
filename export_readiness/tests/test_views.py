from rest_framework.reverse import reverse

from . import factories


def test_performance_dashboard(admin_client, root_page):
    page = factories.PerformanceDashboardPageFactory(
        live=True,
        parent=root_page
    )

    url = reverse('api:pages:detail', kwargs={'pk': page.pk})

    response = admin_client.get(url)
    assert response.status_code == 200


def test_performance_dashboard_notes(admin_client, root_page):
    page = factories.PerformanceDashboardNotesPageFactory(
        live=True,
        parent=root_page
    )

    url = reverse('api:pages:detail', kwargs={'pk': page.pk})

    response = admin_client.get(url)
    assert response.status_code == 200
