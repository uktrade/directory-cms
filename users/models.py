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

    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                                on_delete=models.CASCADE)
    assignment_status = models.CharField(
        choices=STATUSES,
        default=CREATED,
        max_length=30
    )
