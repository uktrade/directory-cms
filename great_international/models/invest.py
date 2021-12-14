from django.db import models

from directory_constants import slugs

from core.models import (
    WagtailAdminExclusivePageMixin,
)
from core.model_fields import MarkdownField

import great_international.panels.invest as panels

from .base import BaseInternationalPage


VIDEO_TRANSCRIPT_HELP_TEXT = (
    "If the video is present, a transcript must be provided."
)

IMAGE_DESCRIPTION_HELP_TEXT = (
    "If this image adds extra information to the page that is not already provided by the text "
    "(e.g. if the image is a diagram, chart, or has text on it) then an image description must be provided."
)


class InvestInternationalHomePage(
    WagtailAdminExclusivePageMixin,
    BaseInternationalPage,
    panels.InvestInternationalHomePagePanels,
):
    slug_identity = slugs.INVEST_INTERNATIONAL_HOME_PAGE
    parent_page_types = ['great_international.InternationalHomePage']
    subpage_types = [
        'great_international.AboutDitServicesPage',
    ]

    breadcrumbs_label = models.CharField(max_length=50)
    heading = models.CharField(max_length=255)
    sub_heading = models.CharField(max_length=255)
    hero_call_to_action_text = models.CharField(max_length=255, blank=True)
    hero_call_to_action_url = models.CharField(max_length=255, blank=True)
    hero_image = models.ForeignKey(
        'wagtailimages.Image',
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    teaser = models.TextField(blank=True)

    benefits_section_title = models.CharField(max_length=255, blank=True)
    benefits_section_intro = models.TextField(max_length=255, blank=True)
    benefits_section_content = MarkdownField(blank=True)
    benefits_section_cta_text = models.CharField(max_length=255, blank=True)
    benefits_section_cta_url = models.CharField(max_length=255, blank=True)
    benefits_section_img = models.ForeignKey(
        'wagtailimages.Image',
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name='+',
        verbose_name="Benefits section image"
    )

    eu_exit_section_title = models.CharField(
        max_length=255,
        blank=True,
        verbose_name="EU exit section title"
    )

    eu_exit_section_content = MarkdownField(
        blank=True,
        verbose_name="EU exit section content"
    )

    eu_exit_section_call_to_action_text = models.CharField(
        max_length=255,
        blank=True,
        verbose_name="EU exit section button text"
    )

    eu_exit_section_call_to_action_url = models.CharField(
        max_length=255,
        blank=True,
        verbose_name="EU exit section button url"
    )

    eu_exit_section_img = models.ForeignKey(
        'wagtailimages.Image',
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name='+',
        verbose_name="EU exit section image"
    )

    sector_title = models.TextField(
        default="Discover UK Industries",
        max_length=255,
        blank=True
    )

    sector_button_text = models.CharField(
        default="See more industries",
        max_length=255,
        blank=True
    )

    sector_button_url = models.CharField(
        max_length=255,
        blank=True
    )

    sector_intro = models.TextField(max_length=255, blank=True)

    hpo_title = models.CharField(
        max_length=255,
        verbose_name="High potential opportunity section title",
        blank=True
    )
    hpo_intro = models.TextField(
        max_length=255,
        blank=True,
        verbose_name="High potential opportunity section intro"
    )

    featured_card_one_image = models.ForeignKey(
        'wagtailimages.Image',
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name='+',
    )
    featured_card_one_title = models.CharField(blank=True, max_length=255)
    featured_card_one_summary = MarkdownField(blank=True)
    featured_card_one_cta_link = models.CharField(max_length=255, blank=True)

    featured_card_two_image = models.ForeignKey(
        'wagtailimages.Image',
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name='+',
    )
    featured_card_two_title = models.CharField(
        max_length=255,
        blank=True,
    )
    featured_card_two_summary = MarkdownField(
        max_length=255,
        blank=True,
    )
    featured_card_two_cta_link = models.CharField(max_length=255, blank=True)

    featured_card_three_image = models.ForeignKey(
        'wagtailimages.Image',
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    featured_card_three_title = models.CharField(
        max_length=255, blank=True
    )
    featured_card_three_summary = MarkdownField(blank=True)
    featured_card_three_cta_link = models.CharField(max_length=255, blank=True)

    # how we help
    how_we_help_title = models.CharField(
        default='How we help',
        max_length=255,
        blank=True
    )
    how_we_help_lead_in = models.TextField(blank=True, null=True)
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
    how_we_help_text_six = models.CharField(max_length=255, blank=True)
    how_we_help_icon_six = models.ForeignKey(
        'wagtailimages.Image',
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name='+',
    )

    how_we_help_cta_text = models.CharField(max_length=255, blank=True)
    how_we_help_cta_link = models.CharField(max_length=255, blank=True)

    contact_section_title = models.CharField(max_length=255, blank=True)
    contact_section_content = models.TextField(max_length=255, blank=True)
    contact_section_call_to_action_text = models.CharField(
        max_length=255,
        blank=True
    )
    contact_section_call_to_action_url = models.CharField(
        max_length=255,
        blank=True
    )

    # How to expand section
    how_to_expand_title = models.CharField(max_length=255, blank=True)
    how_to_expand_image = models.ForeignKey(
        'wagtailimages.Image',
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    how_to_expand_intro = MarkdownField(blank=True)

    how_to_expand_title_one = models.CharField(max_length=255, blank=True)
    how_to_expand_text_one = MarkdownField(blank=True)

    how_to_expand_title_two = models.CharField(max_length=255, blank=True)
    how_to_expand_text_two = MarkdownField(blank=True)

    how_to_expand_title_three = models.CharField(max_length=255, blank=True)
    how_to_expand_text_three = MarkdownField(blank=True)

    how_to_expand_title_four = models.CharField(max_length=255, blank=True)
    how_to_expand_text_four = MarkdownField(blank=True)

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
