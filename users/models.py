from django.conf import settings
from django.db import models

CREATED = 'CREATED'
AWAITING_APPROVAL = 'AWAITING_APPROVAL'
APPROVED = 'APPROVED'

class UserProfile(models.Model):
    # for convienience
    STATUS_CREATED = CREATED
    STATUS_AWAITING_APPROVAL = AWAITING_APPROVAL
    STATUS_APPROVED = APPROVED

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

    approved_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='approved_users',
        null=True,
        on_delete=models.SET_NULL,
    )

    approved_at = models.DateTimeField(null=True)
