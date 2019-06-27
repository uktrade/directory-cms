from datetime import timedelta

from django.conf import settings

from django.core.exceptions import ValidationError
from django.db import models
from django.template.loader import render_to_string
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _

from wagtail.admin.utils import send_mail

from review.api.token import get_review_token


class Reviewer(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.CASCADE, related_name='+')
    email = models.EmailField(blank=True)

    def clean(self):
        if self.user is None and not self.email:
            raise ValidationError("A reviewer must have either an email address or a user account")

    def get_email_address(self):
        return self.email or self.user.email

    def get_name(self):
        if self.user:
            return self.user.get_full_name() or self.user.username
        else:
            return self.email


class Share(models.Model):
    page_revision = models.ForeignKey('wagtailcore.PageRevision', on_delete=models.CASCADE, related_name='shares')
    reviewer = models.ForeignKey(Reviewer, on_delete=models.CASCADE, related_name='shares')
    shared_by = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.SET_NULL, related_name='+')
    shared_at = models.DateTimeField(auto_now_add=True)
    first_accessed_at = models.DateTimeField(null=True)
    last_accessed_at = models.DateTimeField(null=True)

    def get_review_url(self):
        review_token = get_review_token(self.reviewer, self.page_revision, share_id=self.id)
        return self.page_revision.page.specific.get_url(is_draft=True) + '&review_token=' + review_token.decode('utf-8')

    def send_share_email(self):
        review_url = self.get_review_url()
        email_address = self.reviewer.get_email_address()

        email_body = render_to_string('review/emails/share.txt', {
            'page': self.page_revision.page,
            'review_url': review_url,
        })

        send_mail("A page has been shared with you", email_body, [email_address])

    def get_expires_at(self):
        return self.shared_at + timedelta(days=1)

    def has_expired(self):
        return timezone.now() > self.get_expires_at()


class Comment(models.Model):
    page_revision = models.ForeignKey('wagtailcore.PageRevision', on_delete=models.CASCADE, related_name='comments')
    reviewer = models.ForeignKey(Reviewer, on_delete=models.CASCADE, related_name='comments')
    quote = models.TextField(blank=True)
    text = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_resolved = models.BooleanField(default=False)

    content_path = models.TextField()
    start_xpath = models.TextField(blank=True)
    start_offset = models.IntegerField()
    end_xpath = models.TextField(blank=True)
    end_offset = models.IntegerField()


class CommentReply(models.Model):
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name='replies')
    reviewer = models.ForeignKey(Reviewer, on_delete=models.CASCADE, related_name='comment_replies')
    text = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class ModerationRequestQuerySet(models.QuerySet):
    def accepted(self):
        return self.filter(responses__status=ModerationResponse.STATUS_APPROVED)

    def pending(self):
        return (self.filter(responses__isnull=True)
                    .order_by('-created_at')
                    .select_related('revision', 'revision__user'))


class ModerationRequest(models.Model):
    revision = models.ForeignKey(
        'wagtailcore.PageRevision',
        verbose_name=_('revision'),
        on_delete=models.CASCADE,
    )
    publish_at = models.DateTimeField(null=True)
    comment = models.TextField(max_length=100, blank=True)

    # When the lock of this ModerationRequest ends. A user opening this ModerationRequest
    # for review will set this field and update it while their browser is open
    # on that page.
    locked_until = models.DateTimeField(null=True)
    locked_by = models.ForeignKey(Reviewer, null=True, on_delete=models.SET_NULL, related_name='+')

    created_at = models.DateTimeField(auto_now_add=True)

    objects = ModerationRequestQuerySet.as_manager()

    def __str__(self):
        return f'{self.revision.user} requested moderation of "{self.revision.page}" at {self.created_at}'  # noqa: E501

    def is_2i_moderated(self):
        return self.responses.filter(status=ModerationResponse.STATUS_APPROVED).exists()

    def get_review_url(self, user):
        reviewer, created = Reviewer.objects.get_or_create(user=user)
        review_token = get_review_token(reviewer, self.revision, enable_moderation=True)
        return self.revision.page.specific.get_url(is_draft=True) + '&review_token=' + review_token.decode('utf-8')

    @property
    def is_locked(self):
        return self.locked_until is not None and self.locked_until > timezone.now()

    @property
    def latest_response(self):
        return self.responses.latest('created_at')


class ModerationResponse(models.Model):
    STATUS_APPROVED = 'approved'
    STATUS_NEEDS_CHANGES = 'needs-changes'
    STATUS_CHOICES = [
        (STATUS_APPROVED, _("approved")),
        (STATUS_NEEDS_CHANGES, _("needs changes")),
    ]

    request = models.ForeignKey(
        'ModerationRequest',
        verbose_name=_('request'),
        on_delete=models.CASCADE,
        related_name='responses',
    )
    reviewer = models.ForeignKey(Reviewer, on_delete=models.CASCADE, related_name='moderation_responses')
    status = models.CharField(max_length=255, choices=STATUS_CHOICES)
    comment = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user} {self.get_status_display()} "{self.request.revision.page}" at {self.created_at}'  # noqa: E501
