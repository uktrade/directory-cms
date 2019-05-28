from modeltranslation.decorators import register

from core.translation import BaseTranslationOptions
from great_international import models


@register(models.GreatInternationalApp)
class GreatInternationalAppTranslationOptions(BaseTranslationOptions):
    fields = []


@register(models.InternationalSectorPage)
class InternationalSectorPageTranslationOptions(BaseTranslationOptions):
    fields = (
        'heading',
        'sub_heading',
        'hero_image',
        'heading_teaser',
        'section_one_body',
        'section_one_image',
        'section_one_image_caption',
        'section_one_image_caption_company',
        'statistic_1_number',
        'statistic_1_heading',
        'statistic_1_smallprint',
        'statistic_2_number',
        'statistic_2_heading',
        'statistic_2_smallprint',
        'statistic_3_number',
        'statistic_3_heading',
        'statistic_3_smallprint',
        'statistic_4_number',
        'statistic_4_heading',
        'statistic_4_smallprint',
        'statistic_5_number',
        'statistic_5_heading',
        'statistic_5_smallprint',
        'statistic_6_number',
        'statistic_6_heading',
        'statistic_6_smallprint',
        'section_two_heading',
        'section_two_teaser',
        'section_two_subsection_one_icon',
        'section_two_subsection_one_heading',
        'section_two_subsection_one_body',
        'section_two_subsection_two_icon',
        'section_two_subsection_two_heading',
        'section_two_subsection_two_body',
        'section_two_subsection_three_icon',
        'section_two_subsection_three_heading',
        'section_two_subsection_three_body',
        'case_study_title',
        'case_study_description',
        'case_study_cta_text',
        'case_study_cta_page',
        'case_study_image',
        'section_three_heading',
        'section_three_teaser',
        'section_three_subsection_one_heading',
        'section_three_subsection_one_teaser',
        'section_three_subsection_one_body',
        'section_three_subsection_two_heading',
        'section_three_subsection_two_teaser',
        'section_three_subsection_two_body',
        'related_page_one',
        'related_page_two',
        'related_page_three'
    )


@register(models.InternationalArticlePage)
class InternationalArticlePageTranslationOptions(BaseTranslationOptions):
    fields = (
        'article_title',
        'article_subheading',
        'article_teaser',
        'article_image',
        'article_body_text',
        'related_page_one',
        'related_page_two',
        'related_page_three',
    )


@register(models.InternationalCampaignPage)
class InternationalCampaignPageTranslationOptions(BaseTranslationOptions):
    fields = (
        'campaign_subheading',
        'campaign_teaser',
        'campaign_heading',
        'campaign_hero_image',
        'section_one_heading',
        'section_one_intro',
        'section_one_image',
        'selling_point_one_icon',
        'selling_point_one_heading',
        'selling_point_one_content',
        'selling_point_two_icon',
        'selling_point_two_heading',
        'selling_point_two_content',
        'selling_point_three_icon',
        'selling_point_three_heading',
        'selling_point_three_content',
        'section_one_contact_button_url',
        'section_one_contact_button_text',
        'section_two_heading',
        'section_two_intro',
        'section_two_image',
        'section_two_contact_button_url',
        'section_two_contact_button_text',
        'related_content_heading',
        'related_content_intro',
        'related_page_one',
        'related_page_two',
        'related_page_three',
        'cta_box_message',
        'cta_box_button_url',
        'cta_box_button_text',
    )


@register(models.InternationalHomePage)
class InternationalHomePageTranslationOptions(BaseTranslationOptions):
    fields = (
        'hero_title',
        'hero_subtitle',
        'hero_cta_text',
        'hero_cta_link',
        'hero_image',
        'invest_title',
        'invest_content',
        'invest_image',
        'trade_title',
        'trade_content',
        'trade_image',
        'tariffs_title',
        'tariffs_description',
        'tariffs_link',
        'tariffs_image',
        'section_two_heading',
        'section_two_teaser',
        'section_two_subsection_one_icon',
        'section_two_subsection_one_heading',
        'section_two_subsection_one_body',
        'section_two_subsection_two_icon',
        'section_two_subsection_two_heading',
        'section_two_subsection_two_body',
        'section_two_subsection_three_icon',
        'section_two_subsection_three_heading',
        'section_two_subsection_three_body',
        'section_two_subsection_four_icon',
        'section_two_subsection_four_heading',
        'section_two_subsection_four_body',
        'section_two_subsection_five_icon',
        'section_two_subsection_five_heading',
        'section_two_subsection_five_body',
        'section_two_subsection_six_icon',
        'section_two_subsection_six_heading',
        'section_two_subsection_six_body',
        'tariffs_call_to_action_text',
        'featured_links_title',
        'featured_links_summary',
        'featured_link_one_heading',
        'featured_link_one_image',
        'featured_link_two_heading',
        'featured_link_two_image',
        'featured_link_three_heading',
        'featured_link_three_image',
        'news_title',
        'study_in_uk_cta_text',
        'visit_uk_cta_text',
        'related_page_one',
        'related_page_two',
        'related_page_three',
    )


@register(models.InternationalArticleListingPage)
class InternationalArticleListingPage(BaseTranslationOptions):
    fields = (
        'landing_page_title',
        'hero_image',
        'hero_teaser',
        'list_teaser',
    )


@register(models.InternationalRegionPage)
class InternationalRegionPageTranslationOptions(BaseTranslationOptions):
    fields = []


@register(models.InternationalTopicLandingPage)
class InternationalTopicLandingPageTranslationOptions(BaseTranslationOptions):
    fields = (
        'landing_page_title',
        'hero_image',
        'hero_teaser',
    )


@register(models.InternationalCuratedTopicLandingPage)
class InternationalCuratedTopicLandingPageTranslationOptions(
    BaseTranslationOptions
):
    fields = (
        'display_title',
        'hero_image',
        'teaser',
        'feature_section_heading',
        'feature_one_heading',
        'feature_one_image',
        'feature_one_content',
        'feature_two_heading',
        'feature_two_image',
        'feature_two_content',
        'feature_three_heading',
        'feature_three_image',
        'feature_three_url',
        'feature_four_heading',
        'feature_four_image',
        'feature_four_url',
        'feature_five_heading',
        'feature_five_image',
        'feature_five_url',
    )


@register(models.InternationalGuideLandingPage)
class InternationalGuideLandingPageTranslationOptions(
    BaseTranslationOptions
):
    fields = (
        'display_title',
        'hero_image',
        'teaser',
        'section_one_content',
        'section_one_image',
        'section_one_image_caption',
        'section_two_heading',
        'section_two_teaser',
        'section_two_button_text',
        'section_two_button_url',
        'section_two_image',
        'guides_section_heading',
    )


@register(models.InternationalLocalisedFolderPage)
class InternationalRegionalFolderPageTranslationOptions(
    BaseTranslationOptions
):
    fields = []


@register(models.InternationalEUExitFormPage)
class InternationalEUExitFormPageTranslationOptions(BaseTranslationOptions):
    fields = []


@register(models.InternationalEUExitFormSuccessPage)
class InternationalEUExitFormSuccessPageTranslationOptions(
    BaseTranslationOptions
):
    fields = []


@register(models.InternationalCapitalInvestLandingPage)
class InternationalCapitalInvestLandingPageTranslationOptions(
    BaseTranslationOptions
):
    fields = (
        'hero_title',
        'hero_image',
        'hero_subheading',
        'hero_subtitle',
        'hero_cta_text',

        'reason_to_invest_section_title',
        'reason_to_invest_section_intro',
        'reason_to_invest_section_content',
        'reason_to_invest_section_image',

        'region_ops_section_title',
        'region_ops_section_intro',

        'banner_information',

        'energy_sector_title',
        'energy_sector_content',
        'energy_sector_image',
        'energy_sector_cta_text',
        'energy_sector_pdf_document',

        'homes_in_england_section_title',

        'how_we_help_title',
        'how_we_help_intro',
        'how_we_help_one_icon',
        'how_we_help_one_text',
        'how_we_help_two_icon',
        'how_we_help_two_text',
        'how_we_help_three_icon',
        'how_we_help_three_text',
        'how_we_help_four_icon',
        'how_we_help_four_text',

        'contact_section_title',
        'contact_section_text',
        'contact_section_cta_text',
    )


@register(models.CapitalInvestRegionPage)
class CapitalInvestRegionPageTranslationOptions(
    BaseTranslationOptions
):
    fields = (
        'hero_title',
        'breadcrumbs_label',
        'hero_image',

        'featured_description',

        'region_summary_section_image',
        'region_summary_section_intro',
        'region_summary_section_content',

        'investment_opps_title',
        'investment_opps_intro',

        'economics_data_title',
        'economics_stat_1_number',
        'economics_stat_1_heading',
        'economics_stat_1_smallprint',

        'economics_stat_2_number',
        'economics_stat_2_heading',
        'economics_stat_2_smallprint',

        'economics_stat_3_number',
        'economics_stat_3_heading',
        'economics_stat_3_smallprint',

        'economics_stat_4_number',
        'economics_stat_4_heading',
        'economics_stat_4_smallprint',

        'location_data_title',
        'location_stat_1_number',
        'location_stat_1_heading',
        'location_stat_1_smallprint',

        'location_stat_2_number',
        'location_stat_2_heading',
        'location_stat_2_smallprint',

        'location_stat_3_number',
        'location_stat_3_heading',
        'location_stat_3_smallprint',

        'location_stat_4_number',
        'location_stat_4_heading',
        'location_stat_4_smallprint',

        'property_and_infrastructure_section_title',
        'property_and_infrastructure_section_image',
        'property_and_infrastructure_section_content',

        'case_study_image',
        'case_study_title',
        'case_study_text',
        'case_study_cta_text',
        'case_study_cta_link',

        'next_steps_title',
        'next_steps_intro',
        'invest_cta_text',
        'buy_cta_text',
    )


@register(models.CapitalInvestRegionalSectorPage)
class CapitalInvestRegionalSectorPageTranslationOptions(
    BaseTranslationOptions
):
    fields = (
        'breadcrumbs_label',
        'hero_image',
        'hero_title',
        'featured_description',

        'sector_summary_intro',
        'sector_summary_content',
        'sector_summary_image',

        'investment_opportunities_title',

        'next_steps_title',
        'next_steps_intro',

        'invest_cta_text',
        'buy_cta_text',

    )


@register(models.CapitalInvestOpportunityListingPage)
class CapitalInvestOpportunityListingPageTranslationOptions(
        BaseTranslationOptions):
    fields = []


@register(models.CapitalInvestOpportunityPage)
class CapitalInvestOpportunityPageTranslationOptions(
    BaseTranslationOptions
):
    fields = (
        'breadcrumbs_label',
        'hero_image',
        'hero_title',

        'opportunity_summary_intro',
        'opportunity_summary_content',
        'opportunity_summary_image',

        'location_icon',
        'location',
        'project_promoter_icon',
        'project_promoter',
        'scale_icon',
        'scale',
        'sector_icon',
        'sector',
        'investment_type_icon',
        'investment_type',
        'planning_status_icon',
        'planning_status',

        'project_background_title',
        'project_background_intro',
        'project_description_title',
        'project_description_content',
        'project_promoter_title',
        'project_promoter_content',
        'project_image',

        'case_study_image',
        'case_study_title',
        'case_study_text',
        'case_study_cta_text',
        'case_study_cta_link',

        'similar_projects_title',
        'related_page_one',
        'related_page_two',
        'related_page_three',
        'similar_projects_cta_text',
        'similar_projects_cta_link',

        'next_steps_title',
        'next_steps_intro',

        'invest_cta_text',
        'buy_cta_text',
    )


@register(models.SectorRelatedOpportunities)
class SectorRelatedOpportunitiesSerializer(
        BaseTranslationOptions):
    fields = (
        'page',
    )


@register(models.CapitalInvestRelatedRegions)
class RelatedRegionsSerializer(
        BaseTranslationOptions):
    fields = (
        'page',
    )


@register(models.CapitalInvestRegionCardFieldsSummary)
class CapitalInvestRegionCardFieldSerializer(
        BaseTranslationOptions):
    fields = (
        'page',
    )


@register(models.CapitalInvestHomesInEnglandCardFieldsSummary)
class CapitalInvestHomesInEnglandCardFieldsSummarySerializer(
        BaseTranslationOptions):
    fields = (
        'page',
    )
