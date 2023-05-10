from wagtail.models import Page

from django.core.exceptions import ValidationError
from django.db import transaction

from core import constants


class ServiceNameUniqueSlugMixin:

    @staticmethod
    def _slug_is_available(slug, parent, page=None):
        from core import filters  # circular dependencies
        queryset = filters.ServiceNameFilter().filter_service_name(
            queryset=Page.objects.filter(slug=slug).exclude(pk=page.pk),
            name=None,
            value=page.service_name,
        )
        return not queryset.exists()

    @transaction.atomic
    def save(self, *args, **kwargs):
        self.service_name = self.service_name_value
        if not self._slug_is_available(
            slug=self.slug,
            parent=self.get_parent(),
            page=self
        ):
            raise ValidationError({'slug': 'This slug is already in use'})
        return super().save(*args, **kwargs)


class ServiceHomepageMixin:
    full_path = '/'

    @property
    def full_url(self):
        return dict(constants.APP_URLS)[self.service_name_value]
