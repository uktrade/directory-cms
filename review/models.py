from django.conf import settings
from django.contrib.auth import get_user_model

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

    def send_request_email(self):
        # FIXME
        email_address = self.get_email_address()

        context = {
            'email': email_address,
            'user': self.user,
            'review': self.review,
            'page': self.review.revision_as_page,
            'submitter': self.review.submitter,
            'respond_url': self.get_respond_url(absolute=True),
            'view_url': self.get_view_url(absolute=True),
        }

        email_subject = render_to_string('wagtail_review/email/request_review_subject.txt', context).strip()
        email_content = render_to_string('wagtail_review/email/request_review.txt', context).strip()

        send_mail(email_subject, email_content, [email_address])


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
        return self.filter(responses__is_accepted=True)

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

    created_at = models.DateTimeField(auto_now_add=True)

    objects = ModerationRequestQuerySet.as_manager()

    def __str__(self):
        return f'{self.revision.user} requested moderation of "{self.revision.page}" at {self.created_at}'  # noqa: E501

    def is_2i_moderated(self):
        return self.reviews.filter(is_accepted=True).exists()

    def get_review_url(self, user):
        reviewer, created = Reviewer.objects.get_or_create(user=user)
        review_token = get_review_token(reviewer, self.revision, enable_moderation=True)
        return self.revision.page.specific.get_url(is_draft=True) + '&review_token=' + review_token.decode('utf-8')

    @property
    def is_locked(self):
        return self.locked_until > timezone.now()

    @property
    def latest_response(self):
        return self.responses.latest('created_at')


class ModerationResponse(models.Model):
    request = models.ForeignKey(
        'ModerationRequest',
        verbose_name=_('request'),
        on_delete=models.CASCADE,
        related_name='responses',
    )
    reviewer = models.ForeignKey(Reviewer, on_delete=models.CASCADE, related_name='moderation_responses')
    is_accepted = models.BooleanField(
        verbose_name=_('accept page'),
        default=False,
    )
    comment = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        state = 'accepted' if self.is_accepted else 'rejected'
        return f'{self.user} {state} "{self.request.revision.page}" at {self.created_at}'  # noqa: E501
