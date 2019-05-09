import sys
import pytest
from unittest.mock import patch
from importlib import import_module, reload
from django.conf import settings
from django.core.urlresolvers import clear_url_caches
from django.urls import reverse
from rest_framework import status

from .factories import UserFactory
from groups.models import GroupInfo
from users.models import UserProfile

BLANK_CHOICE = ('', '---------')


def test_create_user_view_get(admin_client):
    url = reverse('wagtailusers_users:add')
    response = admin_client.get(url)
    assert response.status_code == status.HTTP_200_OK


@pytest.mark.django_db
def test_create_user_view(admin_client):
    url = reverse('wagtailusers_users:add')
    response = admin_client.post(
        url,
        data={
            'username': 'test',
            'email': 'test@test.com',
            'first_name': 'Test',
            'last_name': 'User',
            'password1': 'password',
            'password2': 'password',
            'groups': ['1']
        }
    )
    assert response.context['message'] == 'User test created.'
    assert response.status_code == status.HTTP_302_FOUND
    assert response.url == reverse('wagtailusers_users:index')


@pytest.mark.django_db
def test_create_user_view_invalid_form(admin_client):
    url = reverse('wagtailusers_users:add')
    response = admin_client.post(
        url,
        data={
            'username': 'test',
            'email': 'test@test.com',
            'first_name': 'Test',
            'last_name': 'User',
            'password1': 'password',
            'password2': 'passwords',
            'groups': ['1']
        }
    )
    message = response.context['message']
    assert message == 'The user could not be created due to errors.'
    assert response.status_code == status.HTTP_200_OK


@pytest.mark.django_db
def test_edit_user_view(admin_client):
    user = UserFactory(username='test')
    url = reverse('wagtailusers_users:edit', kwargs={'pk': user.pk})
    response = admin_client.post(
        url,
        data={
            'username': 'foobar',
            'email': 'test@test.com',
            'first_name': 'Test',
            'last_name': 'User',
            'groups': ['1']
        }
    )
    assert response.context['message'] == 'User foobar updated.'
    assert response.status_code == status.HTTP_302_FOUND
    assert response.url == reverse('wagtailusers_users:index')
    user.refresh_from_db()
    assert user.username == 'foobar'


@pytest.mark.django_db
def test_edit_user_view_invalid(admin_client):
    user = UserFactory(username='test')
    url = reverse('wagtailusers_users:edit', kwargs={'pk': user.pk})
    response = admin_client.post(
        url,
        data={
            'username': 'foobar',
            'email': 'test@test.com',
            'last_name': 'User',
            'groups': ['1']
        }
    )
    message = response.context['message']
    assert message == 'The user could not be saved due to errors.'
    assert response.status_code == status.HTTP_200_OK


def reload_urlconf(urlconf=None):
    clear_url_caches()
    if urlconf is None:
        urlconf = settings.ROOT_URLCONF
    if urlconf in sys.modules:
        reload(sys.modules[urlconf])
    else:
        import_module(urlconf)


def test_force_staff_sso(client):
    """Test that URLs and redirects are in place."""
    settings.FEATURE_FLAGS['ENFORCE_STAFF_SSO_ON'] = True
    settings.AUTHBROKER_CLIENT_ID = 'debug'
    settings.AUTHBROKER_CLIENT_SECRET = 'debug'
    settings.AUTHBROKER_URL = 'https://test.com'
    reload_urlconf()

    assert reverse('authbroker:login') == '/auth/login/'
    assert reverse('authbroker:callback') == '/auth/callback/'
    response = client.get('/admin/login/')
    assert response.status_code == 302
    assert response.url == '/auth/login/'

    settings.FEATURE_FLAGS['ENFORCE_STAFF_SSO_ON'] = False
    reload_urlconf()


@pytest.mark.parametrize('assignment_status, expected_status_code', (
    (UserProfile.STATUS_CREATED, 200),
    (UserProfile.STATUS_AWAITING_APPROVAL, 302),
    (UserProfile.STATUS_APPROVED, 302)
))
@pytest.mark.django_db
def test_ssorequestaccessview_responds_based_on_assignment_status(
    admin_client, admin_user, assignment_status, expected_status_code
):
    url = reverse('wagtailusers_users:sso_request_access')
    profile = admin_user.userprofile
    profile.assignment_status = assignment_status
    profile.save()
    response = admin_client.get(url)
    assert response.status_code == expected_status_code


@pytest.mark.django_db
def test_ssorequestaccessview_shows_unlimited_visibilty_groups_only(
    admin_client, groups_with_info
):
    url = reverse('wagtailusers_users:sso_request_access')

    # Visbility is set to 'unrestricted' for all groups in `groups_with_info`,
    # so choices should reflect that by default
    expected_choices = tuple(
        (g.id, g.info.name_singular) for g in groups_with_info
    )

    # Confirm the choices in the form are as expected
    response = admin_client.get(url)
    group_field = response.context['form']['self_assigned_group'].field
    actual_choices = tuple(group_field.choices)
    assert actual_choices == expected_choices

    # Change the visibility of groups and try again
    GroupInfo.objects.all().update(
        visibility=GroupInfo.VISIBILITY_MANAGERS_ONLY)

    # Choices should be empty now
    response = admin_client.get(url)
    group_field = response.context['form']['self_assigned_group'].field
    assert tuple(group_field.choices) == ()


@pytest.mark.django_db
def test_ssorequestaccessview_with_no_team_leaders_group(admin_client):
    # If no 'team leaders group' has been designated, the 'team_leaders'
    # field should only have a 'blank' option
    url = reverse('wagtailusers_users:sso_request_access')
    response = admin_client.get(url)
    team_leader_field = response.context['form']['team_leader'].field
    assert tuple(team_leader_field.choices) == (BLANK_CHOICE,)


@pytest.mark.django_db
def test_ssorequestaccessview_with_team_leaders_group_but_no_members(
    admin_client, team_leaders_group
):
    # If the designated 'team leaders group' has no members, the 'team_leaders'
    # field should only have a 'blank' option
    url = reverse('wagtailusers_users:sso_request_access')
    response = admin_client.get(url)
    team_leader_field = response.context['form']['team_leader'].field
    assert team_leaders_group.user_set.all().exists() is False
    assert tuple(team_leader_field.choices) == (BLANK_CHOICE,)


@pytest.mark.django_db
def test_ssorequestaccessview_with_team_leaders(
    admin_client, team_leaders_group, team_leaders
):
    url = reverse('wagtailusers_users:sso_request_access')

    # When team leaders are defined, they will appear as choices
    # for the 'team_leaders' field
    expected_choices = [BLANK_CHOICE]
    expected_choices.extend(list(
        (tl.id, "{} <{}>".format(tl.get_full_name(), tl.email))
        for tl in team_leaders
    ))

    # Confirm the choices in the form are as expected
    response = admin_client.get(url)
    team_leader_field = response.context['form']['team_leader'].field
    actual_choices = list(team_leader_field.choices)
    assert actual_choices == expected_choices


@pytest.mark.django_db
def test_ssorequestaccessview_fails_validation_if_form_incomplete(
    admin_client, groups_with_info, team_leaders
):
    url = reverse('wagtailusers_users:sso_request_access')
    response = admin_client.post(url, data={})

    # Should still be on the same view
    assert response.status_code == 200

    # Both form fields should have errors
    assert 'self_assigned_group' in response.context['form'].errors
    assert 'team_leader' in response.context['form'].errors


@pytest.mark.django_db
def test_ssorequestaccessview_post_with_complete_data(
    admin_client, admin_user, groups_with_info, team_leaders
):
    group = groups_with_info[0]
    team_leader = team_leaders[0]

    with patch('users.views.SSORequestAccessView.notify_team_leader_of_pending_approval') as mock_method: # noqa
        response = admin_client.post(
            reverse('wagtailusers_users:sso_request_access'),
            data={
                'self_assigned_group': group.id,
                'team_leader': team_leader.id,
            }
        )

    # Should be redirected to the success url
    success_url = reverse('wagtailusers_users:sso_request_access_success')
    assert response.url == success_url

    # The UserProfile for `admin_user` should have been updated
    profile = admin_user.userprofile
    assert profile.self_assigned_group_id == group.id
    assert profile.team_leader_id == team_leader.id
    assert profile.assignment_status == UserProfile.STATUS_AWAITING_APPROVAL

    # notify_team_leader_of_pending_approval() should have been called too!
    assert mock_method.called
