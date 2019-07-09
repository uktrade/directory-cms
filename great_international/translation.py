from modeltranslation.decorators import register

from core.translation import BaseTranslationOptions
from great_international import models


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
        'related_page_three',
        'project_opportunities_title',
        'related_opportunities_cta_text',
        'related_opportunities_cta_link'
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
@register(models.InternationalHomePageOld)
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
        'section_three_title',
        'section_three_text',
        'section_three_cta_text',
        'section_three_cta_link',
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

        'contact_title',
        'contact_text',

    )


@register(models.CapitalInvestOpportunityListingPage)
class CapitalInvestOpportunityListingPageTranslationOptions(
        BaseTranslationOptions):
    fields = (
        'breadcrumbs_label',
        'search_results_title'
    )


@register(models.CapitalInvestOpportunityPage)
class CapitalInvestOpportunityPageTranslationOptions(
    BaseTranslationOptions
):
    fields = (
        'breadcrumbs_label',
        'hero_image',
        'hero_title',
        'related_region',

        'opportunity_summary_intro',
        'opportunity_summary_content',
        'opportunity_summary_image',

        'location_icon',
        'location',
        'location_heading',
        'project_promoter_icon',
        'project_promoter',
        'project_promoter_heading',
        'scale_icon',
        'scale',
        'scale_value',
        'scale_heading',
        'sector_icon',
        'sector',
        'sector_heading',
        'investment_type_icon',
        'investment_type',
        'investment_type_heading',
        'planning_status_icon',
        'planning_status',
        'planning_status_heading',

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

        'contact_title',
        'contact_text',

    )


@register(models.CapitalInvestRelatedRegions)
class RelatedRegionsSerializer(
        BaseTranslationOptions):
    fields = (
        'page',
    )


@register(models.CapitalInvestRelatedSectors)
class RelatedSectorsSerializer(
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


@register(models.InvestInternationalHomePage)
class InvestHomePageTranslation(BaseTranslationOptions):
    fields = (
        'breadcrumbs_label',
        'heading',
        'sub_heading',
        'hero_call_to_action_text',
        'hero_call_to_action_url',

        'benefits_section_title',
        'benefits_section_intro',
        'benefits_section_content',
        'benefits_section_img',

        'capital_invest_section_title',
        'capital_invest_section_content',
        'capital_invest_section_image',

        'eu_exit_section_title',
        'eu_exit_section_content',
        'eu_exit_section_call_to_action_text',
        'eu_exit_section_call_to_action_url',
        'eu_exit_section_img',

        # subsections
        'subsection_title_one',
        'subsection_content_one',

        'subsection_title_two',
        'subsection_content_two',

        'subsection_title_three',
        'subsection_content_three',

        'subsection_title_four',
        'subsection_content_four',

        'subsection_title_five',
        'subsection_content_five',

        'subsection_title_six',
        'subsection_content_six',

        'subsection_title_seven',
        'subsection_content_seven',

        'sector_title',
        'sector_intro',
        'hpo_title',
        'hpo_intro',
        'setup_guide_title',
        'setup_guide_content',
        'setup_guide_img',
        'setup_guide_call_to_action_url',
        'setup_guide_lead_in',
        'isd_section_image',
        'isd_section_title',
        'isd_section_text',
        'how_we_help_title',
        'how_we_help_lead_in',
        # how we help
        'how_we_help_text_one',
        'how_we_help_icon_one',

        'how_we_help_text_two',
        'how_we_help_icon_two',

        'how_we_help_text_three',
        'how_we_help_icon_three',

        'how_we_help_text_four',
        'how_we_help_icon_four',

        'how_we_help_text_five',
        'how_we_help_icon_five',

        'how_we_help_text_six',
        'sector_button_text',
        'sector_button_url',
        'contact_section_title',
        'contact_section_content',
        'contact_section_call_to_action_text',
        'contact_section_call_to_action_url'
    )


@register(models.InvestHighPotentialOpportunityFormPage)
class HighPotentialOpportunityFormPageTranslationOptions(
    BaseTranslationOptions
):
    fields = []


@register(models.InvestHighPotentialOpportunityDetailPage)
class HighPotentialOpportunityDetailPageTranslationOptions(
    BaseTranslationOptions
):
    fields = (
        'breadcrumbs_label',
        'heading',
        'hero_image',
        'description',
        'featured',
        'contact_proposition',
        'contact_button',
        'proposition_one',
        'proposition_one_image',
        'proposition_one_video',
        'opportunity_list_title',
        'opportunity_list_item_one',
        'opportunity_list_item_two',
        'opportunity_list_item_three',
        'opportunity_list_image',
        'proposition_two',
        'proposition_two_list_item_one',
        'proposition_two_list_item_two',
        'proposition_two_list_item_three',
        'proposition_two_image',
        'proposition_two_video',
        'competitive_advantages_title',
        'competitive_advantages_list_item_one',
        'competitive_advantages_list_item_one_icon',
        'competitive_advantages_list_item_two',
        'competitive_advantages_list_item_two_icon',
        'competitive_advantages_list_item_three',
        'competitive_advantages_list_item_three_icon',
        'testimonial',
        'testimonial_background',
        'companies_list_text',
        'companies_list_item_image_one',
        'companies_list_item_image_two',
        'companies_list_item_image_three',
        'companies_list_item_image_four',
        'companies_list_item_image_five',
        'companies_list_item_image_six',
        'companies_list_item_image_seven',
        'companies_list_item_image_eight',
        'case_study_list_title',
        'case_study_one_text',
        'case_study_one_image',
        'case_study_two_text',
        'case_study_two_image',
        'case_study_three_text',
        'case_study_three_image',
        'case_study_four_text',
        'case_study_four_image',
        'other_opportunities_title',
        'summary_image',
    )


@register(models.InvestHighPotentialOpportunityFormSuccessPage)
class HighPotentialOpportunityFormSuccessPageTranslationOptions(
    BaseTranslationOptions
):
    fields = []


@register(models.InvestSectorPage)
class InvestSectorPageTranslationOptions(BaseTranslationOptions):
    fields = (
        'description',
        'heading',
        'pullout_text',
        'pullout_stat',
        'pullout_stat_text',
        # subsections
        'subsection_title_one',
        'subsection_content_one',
        'subsection_map_one',

        'subsection_title_two',
        'subsection_content_two',
        'subsection_map_two',

        'subsection_title_three',
        'subsection_content_three',
        'subsection_map_three',

        'subsection_title_four',
        'subsection_content_four',
        'subsection_map_four',

        'subsection_title_five',
        'subsection_content_five',
        'subsection_map_five',

        'subsection_title_six',
        'subsection_content_six',
        'subsection_map_six',

        'subsection_title_seven',
        'subsection_content_seven',
        'subsection_map_seven'
    )


@register(models.InvestRegionLandingPage)
class RegionLandingPageTranslationOptions(BaseTranslationOptions):
    fields = (
        'heading',
    )


@register(models.InternationalTradeHomePage)
class InternationalTradeHomePageTranslationOptions(BaseTranslationOptions):
    fields = (
        'breadcrumbs_label',
        'hero_text',
        'hero_image_caption',
        'search_field_placeholder',
        'search_button_text',
        'proposition_text',
        'call_to_action_text',
        'industries_list_text',
        'industries_list_call_to_action_text',
        'services_list_text',
        'services_column_one',
        'services_column_two',
        'services_column_three',
        'services_column_four',
        'services_column_one_icon',
        'services_column_two_icon',
        'services_column_three_icon',
        'services_column_four_icon',
    )


@register(models.InternationalTradeIndustryContactPage)
class InternationalTradeIndustryContactPageTranslationOptions(
    BaseTranslationOptions
):
    fields = (
        'breadcrumbs_label',
        'introduction_text',
        'submit_button_text',
        'success_message_text',
        'success_back_link_text',
    )
