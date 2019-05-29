from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import ugettext_lazy as _


class PagePendingModeration(models.Model):
    revision = models.ForeignKey('wagtailcore.PageRevision', verbose_name=_('revision'), on_delete=models.CASCADE)
    user = models.ForeignKey(get_user_model(), verbose_name=_('user'), on_delete=models.SET_NULL, null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user} requested moderation of "{self.revision.page}" at {self.created_at}'
