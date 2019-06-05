from django.conf import settings
from django.core.exceptions import ValidationError
from django.db import models
from django.template.loader import render_to_string
from django.utils.translation import ugettext_lazy as _

from wagtail.admin.utils import send_mail


class Reviewer(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.CASCADE, related_name='+')
    email = models.EmailField(blank=True)

    def clean(self):
        if self.user is None and not self.email:
            raise ValidationError("A reviewer must have either an email address or a user account")

    def get_email_address(self):
        return self.email or self.user.email

    def get_name(self):
        return self.user.get_full_name() if self.user else self.email

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
