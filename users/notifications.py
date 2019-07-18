from notifications_python_client.notifications import NotificationsAPIClient
from django.conf import settings
from django.urls import reverse

notifications_client = NotificationsAPIClient(settings.GOVNOTIFY_API_KEY)


def notify_team_leader_of_pending_access_request(
    request, team_leader_email, team_leader_name, user_id, user_name,
    user_email, user_role
):
    personalisation = {
        'name': team_leader_name,
        'user_name': user_name,
        'user_email': user_email,
        'user_role': user_role,
        'review_url': request.build_absolute_uri(
            reverse('wagtailusers_users:edit', args=(user_id,))
        ),
    }
    return notifications_client.send_email_notification(
        email_address=team_leader_email,
        template_id=settings.GOVNOTIFY_USER_PENDING_APPROVAL_TEMPLATE_ID,
        personalisation=personalisation,
        email_reply_to_id=settings.GOVNOTIFY_REPLY_TO_EMAIL_ID or None,
    )


def notify_user_of_access_request_approval(
    request, user_email, user_name, reviewer_name
):
    personalisation = {
        'name': user_name,
        'reviewer_name': reviewer_name,
        'sign_in_url': request.build_absolute_uri(
            str(settings.LOGIN_URL)  # requires casting because
            # it's not a string
            # it's <class 'django.utils.functional.lazy.<locals>.__proxy__'>
        ),
    }
    return notifications_client.send_email_notification(
        email_address=user_email,
        template_id=settings.GOVNOTIFY_USER_APPROVED_TEMPLATE_ID,
        personalisation=personalisation,
        email_reply_to_id=settings.GOVNOTIFY_REPLY_TO_EMAIL_ID or None,
    )
