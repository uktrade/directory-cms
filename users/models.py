from django.conf import settings
from django.db import models

CREATED = 'CREATED'
AWAITING_APPROVAL = 'AWAITING_APPROVAL'
APPROVED = 'APPROVED'


ASSIGNMENT_CHOICES = (
    (CREATED, 'created'),
    (AWAITING_APPROVAL, 'awaiting_approval'),
    (APPROVED, 'approved')
)


class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                                 on_delete=models.CASCADE)
    assignment_status = models.CharField(
        choices=ASSIGNMENT_CHOICES,
        default=CREATED,
        max_length=30
    )
