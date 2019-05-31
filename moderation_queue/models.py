from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import ugettext_lazy as _


class Moderation(models.Model):
    revision = models.ForeignKey('wagtailcore.PageRevision', verbose_name=_('revision'), on_delete=models.CASCADE)
    publish_at = models.DateTimeField(null=True)

    # TODO: confirm this is still a string after security/comments work has been confirmed.
    business_approver = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.revision.user} requested moderation of "{self.revision.page}" at {self.created_at}'

    def is_2i_moderated(self):
        return self.reviews.filter(is_accepted=True).exists()


class ModeratorReview(models.Model):
    moderation = models.ForeignKey('Moderation', verbose_name=_('moderation'), on_delete=models.CASCADE, related_name="reviews")
    user = models.ForeignKey(get_user_model(), verbose_name=_('user'), on_delete=models.SET_NULL, null=True)
    is_accepted = models.BooleanField(verbose_name=_('accept page'), default=False)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        state = 'accepted' if self.is_accepted else 'rejected'
        return f'{self.user} {state} "{self.moderation.revision.page}" at {self.created_at}'
