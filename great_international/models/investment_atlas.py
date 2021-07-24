from django.db import models

from .base import BaseInternationalPage
from core.model_fields import MarkdownField

from modelcluster.fields import ParentalManyToManyField
import great_international.panels.investment_atlas as investment_atlas_panels
import great_international.models.great_international as gi_models


class InvestmentOpportunityPage(
    BaseInternationalPage,
    investment_atlas_panels.InvestmentOpportunityPagePanels,
):
    # Due to the fact that wagtail-modeltranslation seems to not
    # support StreamFields, we cannot use StreamFields in this model
    # if we want to make it translateable (which we do)

    # `title` comes from the base class
    breadcrumbs_label = models.CharField(max_length=50)

    relevant_regions = ParentalManyToManyField(
        gi_models.AboutUkRegionPage,
        blank=True,
    )
    relevant_sectors = ParentalManyToManyField(
        gi_models.InternationalSectorPage,
        blank=True,
    )
    related_opportunities = ParentalManyToManyField(
        'InvestmentOpportunityPage',
        blank=True,
    )

    featured_image_1 = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    featured_image_1_alt = models.CharField(
        max_length=250,
        blank=True,
    )
    featured_image_1_caption = models.CharField(
        max_length=250,
        blank=True,
    )

    featured_image_2 = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    featured_image_2_alt = models.CharField(
        max_length=250,
        blank=True,
    )
    featured_image_2_caption = models.CharField(
        max_length=250,
        blank=True,
    )

    featured_image_3 = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    featured_image_3_alt = models.CharField(
        max_length=250,
        blank=True,
    )
    featured_image_3_caption = models.CharField(
        max_length=250,
        blank=True,
    )

    featured_image_4 = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    featured_image_4_alt = models.CharField(
        max_length=250,
        blank=True,
    )
    featured_image_4_caption = models.CharField(
        max_length=250,
        blank=True,
    )

    featured_image_5 = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    featured_image_5_alt = models.CharField(
        max_length=250,
        blank=True,
    )
    featured_image_5_caption = models.CharField(
        max_length=250,
        blank=True,
    )
    executive_summary = MarkdownField(
        blank=True,
    )
    data_snapshot = MarkdownField(
        blank=True,
    )
    contact_name = models.CharField(
        max_length=250,
        blank=True,
    )
    contact_job_title = models.CharField(
        max_length=250,
        blank=True,
    )
    contact_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    contact_cta_email = models.EmailField(
        blank=True,
        null=True,
    )
    opportunity_details = MarkdownField(
        blank=True,
    )
    location_details = MarkdownField(
        blank=True,
    )
    financial_details = MarkdownField(
        blank=True,
    )
    local_or_national_support = MarkdownField(
        blank=True,
    )

    # TO COME/TBC
    # location / geo pointfield
    # dit_how_we_help_summary -> see AboutUKLandingPage for set of fields
    # case_studies
    # uk_specialist_support - from ISD
