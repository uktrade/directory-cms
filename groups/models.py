from django.db import models


class GroupInfo(models.Model):
    """
    Store additional information about groups used for role assignment
    within Wagtail (without affecting the workings of the underlying
    groups or permissions in any way).

    A ``GroupInfo`` object should be created for each group automatically
    when a new group is saved.
    """

    VISIBILITY_UNRESTRICTED = 0
    VISIBILITY_MANAGERS_ONLY = 1
    VISIBILITY_SUPERUSERS_ONLY = 2
    VISIBILITY_CHOICES = [
        (VISIBILITY_UNRESTRICTED, 'Visible to anyone'),
        (VISIBILITY_MANAGERS_ONLY, 'Visible only to managers and superusers'),
        (VISIBILITY_SUPERUSERS_ONLY, 'Visible only to superusers'),
    ]

    SENIORITY_LEVEL_CHOICES = [
        (1, '1 (lowest)'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5 (highest)'),
    ]

    group = models.OneToOneField('auth.Group')
    name_singular = models.CharField(
        max_length=100,
        verbose_name='name (singular)',
        help_text='e.g. Content writer',
    )
    permission_summary = models.TextField(
        blank=True,
        help_text=(
            'A simple summary of what belonging to the group allows a '
            'user to do. Used to help managers decide what groups users '
            'should belong to. For example: Can only create drafts.'
        )
    )
    role_match_description = models.TextField(
        blank=True,
        help_text=(
            'A simple description to help non-technical users understand '
            'which group is most suitable for them based on their real-life '
            'role. For example: If your role requires you to produce content '
            'for your department and you are located in POST or in the UK, '
            'you should select this as your role.'
        )
    )
    visibility = models.PositiveSmallIntegerField(
        choices=VISIBILITY_CHOICES,
        default=VISIBILITY_SUPERUSERS_ONLY,
        db_index=True,
    )
    seniority_level = models.PositiveSmallIntegerField(
        choices=SENIORITY_LEVEL_CHOICES,
        default=5,
        help_text=(
            "Used to order groups in a more natural way. For example, a "
            "'Content editors' group might have the lowest value, and so "
            "should be displayed first."
        )
    )

    class Meta:
        verbose_name = 'group info'
        verbose_name_plural = 'group info'
        ordering = ('visibility', 'seniority_level', 'name_singular')

    @property
    def name(self):
        return self.group.name

    def __str__(self):
        return self.name_singular
