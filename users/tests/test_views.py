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

USER_DETAILS = {
    'username': 'test',
    'email': 'test@test.com',
    'first_name': 'Foo',
    'last_name': 'Bar',
}

USER_DETAILS_CREATE = USER_DETAILS.copy()
USER_DETAILS_CREATE.update(password1='pass', password2='pass')

USER_DETAILS_CHANGING = {
    'username': 'johnsmith',
    'email': 'john@smiths.com',
    'first_name': 'John',
    'last_name': 'Smith',
}


def test_create_user_view_get(admin_client):
    url = reverse('wagtailusers_users:add')
    response = admin_client.get(url)
    assert response.status_code == status.HTTP_200_OK


@pytest.mark.django_db
def test_create_user_view(admin_client):
    url = reverse('wagtailusers_users:add')

    response = admin_client.post(url, data=USER_DETAILS_CREATE)

    assert response.context['message'] == 'User test created.'
    assert response.status_code == status.HTTP_302_FOUND
    assert response.url == reverse('wagtailusers_users:index')


@pytest.mark.django_db
def test_create_user_view_invalid_form(admin_client):
    url = reverse('wagtailusers_users:add')

    post_data = USER_DETAILS.copy()
    post_data.update(email='This is not an email address')
    response = admin_client.post(url, post_data)

    message = response.context['message']
    assert message == 'The user could not be created due to errors.'
    assert response.status_code == status.HTTP_200_OK


@pytest.mark.django_db
def test_get_edit_user_view(admin_client):
    user = UserFactory(**USER_DETAILS)
    url = reverse('wagtailusers_users:edit', kwargs={'pk': user.pk})
    response = admin_client.get(url)
    assert response.status_code == status.HTTP_200_OK
    assert response.context['can_delete'] is True


@pytest.mark.django_db
def test_edit_user_view(admin_client):
    user = UserFactory(**USER_DETAILS)
    url = reverse('wagtailusers_users:edit', kwargs={'pk': user.pk})

    # We'll add the user to a group, as well as changing their details
    post_data = USER_DETAILS_CHANGING.copy()
    post_data['groups'] = ['1']
    response = admin_client.post(url, data=post_data)

    assert response.context['message'] == 'User johnsmith updated.'
    assert response.status_code == status.HTTP_302_FOUND
    assert response.url == reverse('wagtailusers_users:index')

    user.refresh_from_db()
    # The user's details should have changed to reflect the posted values
    user.refresh_from_db()
    for field_name, changed_value in USER_DETAILS_CHANGING.items():
        assert getattr(user, field_name) == changed_value
    # And they should have been added to a group
    group_ids = set(user.groups.values_list('id', flat=True))
    assert group_ids == {1}


@pytest.mark.django_db
def test_edit_user_view_invalid_form(admin_client, approved_user):
    url = reverse('wagtailusers_users:edit', kwargs={'pk': approved_user.pk})

    post_data = USER_DETAILS.copy()
    post_data.update(email='This is not an email address')

    response = admin_client.post(url, post_data)

    message = response.context['message']
    assert message == 'The user could not be saved due to errors.'
    assert response.status_code == status.HTTP_200_OK


def test_edit_user_view_cannot_change_personal_details_when_sso_enforced(
    admin_client
):
    # Set this flag to True and actions if previous test
    settings.FEATURE_FLAGS['ENFORCE_STAFF_SSO_ON'] = True

    user = UserFactory(**USER_DETAILS)

    # Post changes to the view
    url = reverse('wagtailusers_users:edit', kwargs={'pk': user.pk})
    admin_client.post(url, data=USER_DETAILS_CHANGING)

    # The users details should remain unchanged, because the
    # personal detail fields should all be disabled
    user.refresh_from_db()
    for field_name, original_value in USER_DETAILS.items():
        assert getattr(user, field_name) == original_value

    # Change this back to avoid cross-test pollution
    settings.FEATURE_FLAGS['ENFORCE_STAFF_SSO_ON'] = False


@pytest.mark.django_db
def test_edit_user_view_preserves_ability_to_update_is_active(admin_client):
    # Set this flag to True and actions if previous test
    settings.FEATURE_FLAGS['ENFORCE_STAFF_SSO_ON'] = True

    # Create an 'inactive' user to test with
    user = UserFactory(**USER_DETAILS)
    user.is_active = False
    user.save()

    # Post using the same details + 'is_active=on'
    post_data = USER_DETAILS.copy()
    post_data.update(is_active='on')
    url = reverse('wagtailusers_users:edit', kwargs={'pk': user.pk})
    admin_client.post(url, data=post_data)

    # The change to 'is_active' should have been applied, because that field
    # is not disabled along with the personal detail ones
    user.refresh_from_db()
    assert user.is_active is True

    # Change this back to avoid cross-test pollution
    settings.FEATURE_FLAGS['ENFORCE_STAFF_SSO_ON'] = False


@pytest.mark.django_db
def test_edit_user_view_warns_administrator_if_user_is_awaiting_approval(
    admin_client, user_awaiting_approval
):
    user = user_awaiting_approval
    url = reverse('wagtailusers_users:edit', kwargs={'pk': user.pk})
    response = admin_client.get(url)

    message = response.context['message']
    assert "This user is awaiting approval" in message
    assert "requested to be added to the 'Moderators' group" in message


@pytest.mark.django_db
def test_edit_user_view_marks_user_as_approved_if_added_to_group(
    admin_client, admin_user, user_awaiting_approval
):
    user = user_awaiting_approval
    profile = user_awaiting_approval.userprofile
    url = reverse('wagtailusers_users:edit', kwargs={'pk': user.pk})

    with patch(
        'users.views.notify_user_of_access_request_approval',
        autospec=True
    ) as mocked_method:
        response = admin_client.post(url, {
            'username': user.username,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'email': user.email,
            'is_active': True,
            'groups': [profile.self_assigned_group_id],
        })

    # Ensure the post was successful
    assert response.context['message'] == 'User %s updated.' % user.username
    assert response.status_code == status.HTTP_302_FOUND
    assert response.url == reverse('wagtailusers_users:index')

    # The UserProfile should have been updated
    profile.refresh_from_db()
    assert profile.assignment_status == UserProfile.STATUS_APPROVED
    assert profile.approved_by_id == admin_user.id
    assert profile.approved_at is not None
    # A notification should have been triggered for the user
    expected_call_args = dict(
        request=response.wsgi_request,
        user_email=user.email,
        user_name=user.get_full_name(),
        reviewer_name=admin_user.get_full_name(),
    )
    mocked_method.assert_called_with(**expected_call_args)


@pytest.mark.django_db
def test_edit_user_view_does_not_mark_user_as_approved_if_not_added_to_a_group(
    admin_client, admin_user, user_awaiting_approval
):
    user = user_awaiting_approval
    profile = user_awaiting_approval.userprofile
    url = reverse('wagtailusers_users:edit', kwargs={'pk': user.pk})

    with patch(
        'users.views.notify_user_of_access_request_approval'
    ) as mocked_method:
        response = admin_client.post(url, {
            'username': user.username,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'email': user.email,
            'is_active': True,
        })

    # Ensure the post was successful
    assert response.context['message'] == 'User %s updated.' % user.username
    assert response.status_code == status.HTTP_302_FOUND
    assert response.url == reverse('wagtailusers_users:index')

    # The UserProfile should NOT have been updated
    profile.refresh_from_db()
    assert profile.assignment_status == UserProfile.STATUS_AWAITING_APPROVAL
    assert profile.approved_by_id is None
    assert profile.approved_at is None
    # no notification should have been triggered
    mocked_method.assert_not_called()


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

    with patch(
        'users.views.notify_team_leader_of_pending_access_request',
        autospec=True
    ) as mocked_method:
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
    assert profile.assignment_status == UserProfile.STATUS_AWAITING_APPROVAL # noqa

    # A notification should have been triggered for the user
    expected_call_args = dict(
        request=response.wsgi_request,
        team_leader_email=team_leader.email,
        team_leader_name=team_leader.get_full_name(),
        user_id=admin_user.id,
        user_name=admin_user.get_full_name(),
        user_email=admin_user.email,
        user_role=group.info.name_singular,
    )
    mocked_method.assert_called_with(**expected_call_args)


@pytest.mark.django_db
@pytest.mark.parametrize('url', (
    reverse('wagtailusers_users:sso_request_access'),
    reverse('wagtailusers_users:sso_request_access_success'),
))
def test_ssorequestaccess_views_only_available_to_authenticated_users(
    client, admin_client, url
):
    # When not authenticated, the user is redirected to the login page
    response = client.get(url)
    assert response.status_code == 302
    assert response.url.startswith(settings.LOGIN_URL)

    # When authenticated, things work fine
    response = admin_client.get(url)
    assert response.status_code == 200
