from django.db import models

from wagtail.admin.panels import FieldPanel
from wagtail.snippets.models import register_snippet


@register_snippet
class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

    panels = [
        FieldPanel('name')
    ]


@register_snippet
class IndustryTag(models.Model):
    name = models.CharField(max_length=100, unique=True)
    icon = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    def __str__(self):
        return self.name

    panels = [
        FieldPanel('name'),
        FieldPanel('icon')
    ]


@register_snippet
class Region(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

    panels = [
        FieldPanel('name')
    ]


@register_snippet
class Country(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.CharField(max_length=100, unique=True)
    region = models.ForeignKey(Region, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name

    panels = [
        FieldPanel('name'),
        FieldPanel('slug'),
        FieldPanel('region')
    ]
