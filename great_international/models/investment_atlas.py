from django.db import models

from wagtail.core.fields import StreamField

from .base import BaseInternationalPage

from core.fields import single_struct_block_stream_field_factory

from modelcluster.fields import ParentalManyToManyField
import great_international.panels.investment_atlas as investment_atlas_panels
import great_international.models.great_international as gi_models

import great_international.blocks.investment_atlas as investment_atlas_blocks


class InvestmentOpportunityPage(
    BaseInternationalPage,
    investment_atlas_panels.InvestmentOpportunityPagePanels,
):
    # `title` comes from the base class
    breadcrumbs_label = models.CharField(max_length=50)

    priority_weighting = models.DecimalField(
        default='0.0',
        max_digits=5,
        decimal_places=2,
        help_text=(
            'For use when auto-ordering results or automatically choosing which to show '
            '- an Opportunity with a higher priority weighting will be shown earlier. '
            'Max val: 999.99'
        )
    )

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

    featured_images = single_struct_block_stream_field_factory(
        field_name='images',
        block_class_instance=investment_atlas_blocks.FeaturedImageBlock(),
        max_num=5,
        null=True,
        blank=True,
    )

    opportunity_summary = models.TextField(
        max_length=1000,
        blank=False,
        help_text=(
            'Simple summary of the Opportunity, for display on pages (eg listin pages) '
            'which link TO a full page about this opportunity.'
        )
    )

    main_content = StreamField(
        [
            ('copy', investment_atlas_blocks.CopyBlock()),
            ('contact_details', investment_atlas_blocks.ContactDetailsBlock()),
        ],
        null=True,
        blank=True,
    )

    # TO COME/TBC
    # location / geo pointfield
    # dit_how_we_help_summary -> see AboutUKLandingPage for set of fields
    # case_studies
    # uk_specialist_support - from ISD
