from django.conf import settings
from django.db import models


class UserProfile(models.Model):
    CREATED = 'CREATED'
    AWAITING_APPROVAL = 'AWAITING_APPROVAL'
    APPROVED = 'APPROVED'

    STATUSES = (
        (CREATED, CREATED),
        (AWAITING_APPROVAL, AWAITING_APPROVAL),
        (APPROVED, APPROVED)
    )

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )

    assignment_status = models.CharField(
        choices=STATUSES,
        default=CREATED,
        max_length=30
    )

    self_assigned_group = models.ForeignKey(
        'auth.Group',
        null=True,
        on_delete=models.SET_NULL,
    )

    team_leader = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='team_leader_for',
        null=True,
        on_delete=models.SET_NULL,
    )
