import pytest
from django.conf import settings
from django.urls import reverse

from groups.models import GroupInfo


@pytest.mark.django_db
def test_group_info_modal_only_available_to_authenticated_users(client):
    response = client.get(reverse('group-info'))
    assert response.status_code == 302
    assert response.url.startswith(settings.LOGIN_URL)


@pytest.mark.django_db
def test_group_info_modal_shows_unlimited_visibility_groups_only(
    admin_client, groups_with_info
):
    url = reverse('group-info')
    response = admin_client.get(url)
    assert response.status_code == 200

    # Visbility is set to 'unrestricted' for all groups in `groups_with_info`,
    # so the same groups should be diplayed
    expected_items = tuple(group.info for group in groups_with_info)
    actual_items = tuple(response.context['queryset'])
    assert actual_items == expected_items

    # Check that expected groups are actually rendered
    modal_html = response.json()['html']
    for item in expected_items:
        assert '<dt>' + item.name_singular + '</dt>' in modal_html
        assert '<dd>' + item.role_match_description + '</dd>' in modal_html

    # Change the visibility of groups and try again
    GroupInfo.objects.all().update(
        visibility=GroupInfo.VISIBILITY_MANAGERS_ONLY)
    response = admin_client.get(url)
    assert response.context['queryset'].exists() is False
