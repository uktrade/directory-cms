from django.db import models

from core.models import (
    ExclusivePageMixin, WagtailAdminExclusivePageMixin, FormPageMetaClass)
from core.model_fields import MarkdownField

import great_international.panels.invest as panels

from .base import BaseInternationalPage


class InvestInternationalHomePage(
    WagtailAdminExclusivePageMixin,
    BaseInternationalPage,
    panels.InvestInternationalHomePagePanels,
):
    slug_identity = 'invest'
    parent_page_types = ['great_international.InternationalHomePage']
    subpage_types = [
        'InvestHighPotentialOpportunitiesPage',
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

    sector_button_text = models.TextField(
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


class InvestHighPotentialOpportunitiesPage(
    ExclusivePageMixin, BaseInternationalPage,
    panels.InvestHighPotentialOpportunitiesPagePanels,
):
    """
    An empty page in lieu of a landing page so we don't break the
    tree based routing pattern.
    This page's url will redirect to an existing page on the frontend.
    """

    slug_identity = 'high-potential-opportunities'

    parent_page_types = ['InvestInternationalHomePage']
    subpage_types = [
        'InvestHighPotentialOpportunityDetailPage',
        'InvestHighPotentialOpportunityFormPage',
    ]

    def save(self, *args, **kwargs):
        # title is used for tree_based_breadcrumbs that are displayed in the UI
        self.title = 'High potential opportunities'
        return super().save(*args, **kwargs)


class InvestHighPotentialOpportunityFormPage(
    ExclusivePageMixin,
    BaseInternationalPage,
    metaclass=FormPageMetaClass,
):
    # metaclass creates <field_name>_label and <field_name>_help_text
    form_field_names = [
        'full_name',
        'role_in_company',
        'email_address',
        'phone_number',
        'company_name',
        'website_url',
        'country',
        'company_size',
        'opportunities',
        'comment',
    ]

    slug_identity = 'contact'
    subpage_types = ['InvestHighPotentialOpportunityFormSuccessPage']
    parent_page_types = ['InvestHighPotentialOpportunitiesPage']

    heading = models.CharField(max_length=255)
    sub_heading = models.CharField(max_length=255)
    breadcrumbs_label = models.CharField(max_length=50)

    content_panels_before_form = \
        panels.InvestHighPotentialOpportunityFormPagePanels.content_panels_before_form  # noqa
    content_panels_after_form = \
        panels.InvestHighPotentialOpportunityFormPagePanels.content_panels_after_form  # noqa
    settings_panels = \
        panels.InvestHighPotentialOpportunityFormPagePanels.settings_panels


class InvestHighPotentialOpportunityDetailPage(
    BaseInternationalPage,
    panels.InvestHighPotentialOpportunityDetailPagePanels,
):
    parent_page_types = ['InvestHighPotentialOpportunitiesPage']
    breadcrumbs_label = models.CharField(max_length=50)
    heading = models.CharField(max_length=255)
    hero_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    featured = models.BooleanField(default=True)
    description = models.TextField(
        blank=True,
        help_text="This is the description shown when the HPO "
                  "is featured on another page i.e. the Invest Home Page"
    )

    contact_proposition = MarkdownField(
        blank=False,
        verbose_name='Body text',
    )
    contact_button = models.CharField(max_length=500)
    proposition_one = MarkdownField(blank=False)
    proposition_one_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    proposition_one_video = models.ForeignKey(
        'wagtailmedia.Media',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    opportunity_list_title = models.CharField(max_length=300)
    opportunity_list_item_one = MarkdownField()
    opportunity_list_item_two = MarkdownField()
    opportunity_list_item_three = MarkdownField(blank=True)
    opportunity_list_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    proposition_two = MarkdownField(blank=False)
    proposition_two_list_item_one = MarkdownField()
    proposition_two_list_item_two = MarkdownField()
    proposition_two_list_item_three = MarkdownField()
    proposition_two_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    proposition_two_video = models.ForeignKey(
        'wagtailmedia.Media',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    competitive_advantages_title = models.CharField(
        max_length=300,
        verbose_name='Body text',
    )
    competitive_advantages_list_item_one = MarkdownField()
    competitive_advantages_list_item_one_icon = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    competitive_advantages_list_item_two = MarkdownField()
    competitive_advantages_list_item_two_icon = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    competitive_advantages_list_item_three = MarkdownField()
    competitive_advantages_list_item_three_icon = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    testimonial = MarkdownField(blank=True)
    testimonial_background = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        verbose_name='Background image',
    )
    companies_list_text = MarkdownField()
    companies_list_item_image_one = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    companies_list_item_image_two = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    companies_list_item_image_three = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    companies_list_item_image_four = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    companies_list_item_image_five = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    companies_list_item_image_six = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    companies_list_item_image_seven = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    companies_list_item_image_eight = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    case_study_list_title = models.CharField(max_length=300)
    case_study_one_text = MarkdownField(blank=True)
    case_study_one_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    case_study_two_text = MarkdownField(blank=True)
    case_study_two_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    case_study_three_text = MarkdownField(blank=True)
    case_study_three_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    case_study_four_text = MarkdownField(blank=True)
    case_study_four_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    other_opportunities_title = models.CharField(
        max_length=300,
        verbose_name='Title'
    )
    pdf_document = models.ForeignKey(
        'wagtaildocs.Document',
        null=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    summary_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text=(
            'Image used on the opportunity listing page for this opportunity'
        ),
        verbose_name='Image',
    )


class InvestHighPotentialOpportunityFormSuccessPage(
    panels.InvestHighPotentialOpportunityFormSuccessPagePanels,
    ExclusivePageMixin,
    BaseInternationalPage,
):
    slug_identity = 'success'
    parent_page_types = ['InvestHighPotentialOpportunityFormPage']

    breadcrumbs_label = models.CharField(max_length=50)
    heading = models.CharField(
        max_length=255,
        verbose_name='section title'
    )
    sub_heading = models.CharField(
        max_length=255,
        verbose_name='section body',
    )
    next_steps_title = models.CharField(
        max_length=255,
        verbose_name='section title'
    )
    next_steps_body = models.CharField(
        max_length=255,
        verbose_name='section body',
    )
    documents_title = models.CharField(
        max_length=255,
        verbose_name='section title'
    )
    documents_body = models.CharField(
        max_length=255,
        verbose_name='section body',
    )


class InvestRegionLandingPage(
    ExclusivePageMixin,
    BaseInternationalPage,
    panels.InvestRegionLandingPagePanels,
):

    parent_page_types = ['InvestInternationalHomePage']
    subpage_types = ['InvestRegionPage']
    slug_override = 'invest-uk-regions'

    # page fields
    heading = models.CharField(max_length=255)

    hero_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )


class InvestRegionPage(
    BaseInternationalPage,
    panels.InvestRegionPagePanels,
):

    parent_page_types = ['InvestRegionLandingPage']

    featured = models.BooleanField(default=False)
    description = models.TextField(
        help_text="This is the description shown when the "
                  "sector is featured on another page i.e. "
                  "the Invest Home Page"
    )  # appears in card on external pages

    # page fields
    heading = models.CharField(max_length=255)

    hero_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    pullout_text = MarkdownField(blank=True, null=True)
    pullout_stat = models.CharField(max_length=255, blank=True, null=True)
    pullout_stat_text = models.CharField(max_length=255, blank=True, null=True)

    subsection_title_one = models.CharField(max_length=200)
    subsection_content_one = MarkdownField()
    subsection_map_one = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    subsection_title_two = models.CharField(max_length=200)
    subsection_content_two = MarkdownField()
    subsection_map_two = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    subsection_title_three = models.CharField(max_length=200, blank=True)
    subsection_content_three = MarkdownField(blank=True)
    subsection_map_three = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    subsection_title_four = models.CharField(max_length=200, blank=True)
    subsection_content_four = MarkdownField(blank=True)
    subsection_map_four = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    subsection_title_five = models.CharField(max_length=200, blank=True)
    subsection_content_five = MarkdownField(blank=True)
    subsection_map_five = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    subsection_title_six = models.CharField(max_length=200, blank=True)
    subsection_content_six = MarkdownField(blank=True)
    subsection_map_six = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    subsection_title_seven = models.CharField(max_length=200, blank=True)
    subsection_content_seven = MarkdownField(blank=True)
    subsection_map_seven = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
