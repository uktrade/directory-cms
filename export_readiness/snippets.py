from django.db import models
from django.utils.text import slugify

from wagtail.search import index
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.snippets.models import register_snippet


@register_snippet
class Tag(index.Indexed, models.Model):
    name = models.CharField(max_length=100)
    slug = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.name

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        self.slug = slugify(self.name)
        return super().save(force_insert, force_update, using, update_fields)

    panels = [
        FieldPanel('name')
    ]

    search_fields = [
        index.SearchField('name', partial_match=True),
    ]
