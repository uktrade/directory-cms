from django.db import models

from directory_constants import slugs

from core.models import ExclusivePageMixin, BreadcrumbMixin
from core.model_fields import MarkdownField

from .base import BaseInternationalPage
import great_international.panels.find_a_supplier as panels


class InternationalTradeHomePage(
    panels.InternationalTradeHomePagePanels, ExclusivePageMixin,
    BreadcrumbMixin, BaseInternationalPage,
):
    slug_identity = slugs.FAS_INTERNATIONAL_HOME_PAGE
    parent_page_types = ['great_international.InternationalHomePage']
    subpage_types = ['InternationalTradeIndustryContactPage', 'great_international.AboutDitServicesPage']

    hero_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    mobile_hero_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    hero_image_caption = models.CharField(
        max_length=255,
        blank=True
    )
    breadcrumbs_label = models.CharField(max_length=50)
    hero_text = MarkdownField(blank=False)
    search_field_placeholder = models.CharField(max_length=500)
    search_button_text = models.CharField(max_length=500)
    proposition_text = MarkdownField(blank=False)
    call_to_action_text = models.CharField(max_length=500)
    industries_list_text = MarkdownField(blank=False)
    industries_list_call_to_action_text = models.CharField(max_length=500)
    services_list_text = MarkdownField(blank=False)
    services_column_one = MarkdownField(blank=False)
    services_column_two = MarkdownField(blank=False)
    services_column_three = MarkdownField(blank=False)
    services_column_four = MarkdownField(
        blank=False,
    )
    services_column_one_icon = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    services_column_two_icon = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    services_column_three_icon = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    services_column_four_icon = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )


class InternationalTradeIndustryContactPage(
    panels.InternationalTradeIndustryContactPagePanels, ExclusivePageMixin, BreadcrumbMixin,
    BaseInternationalPage,
):
    parent_page_types = ['InternationalTradeHomePage']
    slug_identity = slugs.CONTACT_FORM_SLUG

    breadcrumbs_label = models.CharField(max_length=50)
    introduction_text = MarkdownField(blank=True)
    submit_button_text = models.CharField(max_length=100)
    success_message_text = MarkdownField(blank=True)
    success_back_link_text = models.CharField(max_length=100)
