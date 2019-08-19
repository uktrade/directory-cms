from django.db import models

from core.models import (WagtailAdminExclusivePageMixin)
from core.model_fields import MarkdownField

import great_international.panels.expand as panels

from .base import BaseInternationalPage


class ExpandInternationalLandingPage(
    WagtailAdminExclusivePageMixin,
    BaseInternationalPage,
    panels.ExpandInternationalLandingPagePanels,
):
    slug_identity = 'expand'
    parent_page_types = ['great_international.InternationalHomePage']

    breadcrumbs_label = models.CharField(max_length=50)
    hero_title = models.CharField(max_length=255)
    sub_heading = models.CharField(max_length=255, blank=True)
    hero_cta_text = models.CharField(max_length=255, blank=True)
    hero_cta_link = models.CharField(max_length=255, blank=True)
    hero_image = models.ForeignKey(
        'wagtailimages.Image',
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    # Benefits section
    benefits_section_title = models.CharField(max_length=255, blank=True)
    benefits_section_intro = models.TextField(max_length=255, blank=True)
    benefits_section_text = MarkdownField(blank=True)
    benefits_section_cta_text = models.CharField(max_length=255, blank=True)
    benefits_section_cta_link = models.CharField(max_length=255, blank=True)
    benefits_section_img = models.ForeignKey(
        'wagtailimages.Image',
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name='+',
        verbose_name="Benefits section image"
    )

    # How to expand section
    how_to_expand_title = models.CharField(max_length=255, blank=True)
    how_to_expand_image = models.ForeignKey(
        'wagtailimages.Image',
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name='+',
        verbose_name="Benefits section image"
    )

    how_to_expand_intro = models.TextField(blank=True)

    how_to_expand_title_one = models.CharField(max_length=255, blank=True)
    how_to_expand_text_one = MarkdownField(blank=True)

    how_to_expand_title_two = models.CharField(max_length=255, blank=True)
    how_to_expand_text_two = MarkdownField(blank=True)

    how_to_expand_title_three = models.CharField(max_length=255, blank=True)
    how_to_expand_text_three = MarkdownField(blank=True)

    how_to_expand_title_four = models.CharField(max_length=255, blank=True)
    how_to_expand_text_four = MarkdownField(blank=True)

    # How we help section
    how_we_help_title = models.CharField(
        max_length=255,
        blank=True
    )
    how_we_help_intro = MarkdownField(blank=True)
    how_we_help_text_one = models.CharField(max_length=255, blank=True)
    how_we_help_icon_one = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    how_we_help_text_two = models.CharField(max_length=255, blank=True)
    how_we_help_icon_two = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    how_we_help_text_three = models.CharField(max_length=255, blank=True)
    how_we_help_icon_three = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    how_we_help_text_four = models.CharField(max_length=255, blank=True)
    how_we_help_icon_four = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    how_we_help_text_five = models.CharField(max_length=255, blank=True)
    how_we_help_icon_five = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    # Contact section
    contact_section_title = models.CharField(max_length=255, blank=True)
    contact_section_content = models.TextField(max_length=255, blank=True)
    contact_section_cta_text = models.CharField(max_length=255, blank=True)
    contact_section_cta_link = models.CharField(max_length=255, blank=True)

    # ISD section
    isd_section_title = models.CharField(
        max_length=255,
        blank=True,
        verbose_name="Investment Support Directory section title"
    )
    isd_section_text = MarkdownField(
        blank=True,
        verbose_name="Investment Support Directory section text"
    )
    isd_section_cta_text = models.CharField(
        max_length=255,
        blank=True,
        verbose_name="Investment Support Directory section cta text"
    )
    isd_section_cta_link = models.CharField(
        max_length=255,
        blank=True,
        verbose_name="Investment Support Directory section cta link"
    )

    # HPO section
    hpo_title = models.CharField(
        max_length=255,
        verbose_name="High potential opportunity section title",
        blank=True
    )
    hpo_intro = MarkdownField(
        blank=True,
        verbose_name="High potential opportunity section intro"
    )

    # Industries section
    industries_title = models.CharField(
        max_length=255,
        blank=True
    )
    industries_intro = MarkdownField(blank=True)

    featured_industry_one = models.ForeignKey(
        'great_international.InternationalSectorPage',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    featured_industry_two = models.ForeignKey(
        'great_international.InternationalSectorPage',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    featured_industry_three = models.ForeignKey(
        'great_international.InternationalSectorPage',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    industries_cta_text = models.CharField(
        max_length=255,
        blank=True
    )
    industries_cta_link = models.CharField(
        max_length=255,
        blank=True
    )
