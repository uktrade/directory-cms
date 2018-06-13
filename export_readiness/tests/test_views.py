from rest_framework.reverse import reverse

from . import factories


class test_performance_dashboard(admin_client):
    page = factories.PerformanceDashboardPageFactory()

    url = reverse('api:pages:detail', kwargs={'pk': page.pk})

    response = admin_client.get(url)
    assert response.status_code == 200
